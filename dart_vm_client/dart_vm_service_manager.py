# dart_vm_service_manager.py
import os
import subprocess
import time
import signal
import atexit
import logging
import socket
import grpc
from pathlib import Path

logger = logging.getLogger(__name__)

class DartVmServiceManager:
    def __init__(self, port=50051, dart_executable=None, service_ready_timeout=10):
        self.port = port
        self.process = None
        self.service_dir = Path(__file__).parent / "dart_vm_service"
        self.dart_executable = dart_executable or self._find_dart_executable()
        self.service_ready_timeout = service_ready_timeout
        
        # Register cleanup on exit
        atexit.register(self.stop)

    def _find_dart_executable(self):
        """Find the Dart executable in the system PATH or common locations."""
        # Try to find dart in PATH
        dart_cmd = "dart"
        try:
            subprocess.run([dart_cmd, "--version"], 
                          check=True, 
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE)
            return dart_cmd
        except (subprocess.SubprocessError, FileNotFoundError):
            # Check common installation locations
            common_locations = [
                "/usr/bin/dart",
                "/usr/local/bin/dart",
                "C:\\Program Files\\Dart\\dart.exe",
            ]
            
            for location in common_locations:
                if os.path.isfile(location):
                    return location
                    
            raise RuntimeError(
                "Dart executable not found. Please install Dart SDK or provide path to dart executable."
            )

    def start(self):
        """Start the Dart VM Service gRPC server."""
        if self.process and self.process.poll() is None:
            logger.info("Dart VM Service already running")
            return True
            
        logger.info("Starting Dart VM Service gRPC server...")
        
        # Ensure Dart dependencies are installed
        self._ensure_dart_dependencies()
        
        # Check if the port is already in use
        if self._is_port_in_use(self.port):
            logger.error(f"Port {self.port} is already in use")
            return False
        
        # Start the service
        cmd = [
            self.dart_executable,
            str(self.service_dir / "bin" / "dart_vm_service.dart"),
            "--grpc",
            f"--port={self.port}"
        ]
        
        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            # Wait for service to be ready
            if self._wait_for_service():
                logger.info(f"Dart VM Service started on port {self.port}")
                return True
            else:
                return False
        except Exception as e:
            logger.error(f"Error starting Dart VM Service: {e}")
            return False

    def _is_port_in_use(self, port):
        """Check if the specified port is in use."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
            
    def _ensure_dart_dependencies(self):
        """Make sure Dart dependencies are installed."""
        logger.info("Ensuring Dart dependencies...")
        try:
            subprocess.run(
                [self.dart_executable, "pub", "get"],
                cwd=str(self.service_dir),
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            logger.warning(f"Failed to get Dart dependencies: {e}")
            logger.info("Continuing anyway as dependencies might already be installed")

    def _wait_for_service(self):
        """Wait for the gRPC service to be ready."""
        start_time = time.time()
        
        while time.time() - start_time < self.service_ready_timeout:
            # Check if process is still running
            if self.process.poll() is not None:
                stdout, stderr = self.process.communicate()
                logger.error(f"Dart VM Service failed to start: {stderr}")
                return False
            
            # Try to connect to the gRPC server
            try:
                # Create a temporary channel to test connection
                with grpc.insecure_channel(f'localhost:{self.port}') as channel:
                    # Set a short deadline for the connection attempt
                    channel_ready = grpc.channel_ready_future(channel)
                    channel_ready.result(timeout=1)
                    return True
            except grpc.FutureTimeoutError:
                # Not ready yet, wait a bit
                time.sleep(0.5)
                
        # Timeout reached
        logger.error(f"Timed out waiting for Dart VM Service to start after {self.service_ready_timeout} seconds")
        self.stop()
        return False

    def stop(self):
        """Stop the Dart VM Service gRPC server."""
        if self.process and self.process.poll() is None:
            logger.info("Stopping Dart VM Service...")
            
            try:
                # Try graceful shutdown first
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # Force kill if graceful shutdown fails
                    self.process.kill()
                    self.process.wait()
            except Exception as e:
                logger.error(f"Error stopping Dart VM Service: {e}")
            finally:
                self.process = None
            
            logger.info("Dart VM Service stopped")