from .dart_vm_service_manager import DartVmServiceManager
from .dart_vm_service_client import DartVmServiceClient

class DartVmClient:
    """Main client for interacting with the Dart VM Service."""
    
    def __init__(self, start_service=True, port=50051, dart_executable=None, use_global_package=True):
        """
        Initialize the client.
        
        Args:
            start_service: Whether to start the bundled Dart VM service
            port: Port for the gRPC service
            dart_executable: Optional path to Dart executable
            use_global_package: Whether to use the globally installed dart_vm_service package
                instead of the bundled one (requires: dart pub global activate dart_vm_service)
        """
        self.port = port
        self.service_manager = None
        
        if start_service:
            self.service_manager = DartVmServiceManager(
                port=port, 
                dart_executable=dart_executable,
                use_global_package=use_global_package
            )
            success = self.service_manager.start()
            if not success:
                raise RuntimeError("Failed to start Dart VM Service")
        
        # Initialize the gRPC client
        self.client = DartVmServiceClient(f"localhost:{port}")
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def close(self):
        """Close the client and stop the service if it was started by this client."""
        if hasattr(self, 'client'):
            self.client.close()
        
        if self.service_manager:
            self.service_manager.stop()
            self.service_manager = None
    
    def __del__(self):
        """Ensure resources are cleaned up when object is garbage collected."""
        self.close()
    
    # Forward all methods to the gRPC client
    def __getattr__(self, name):
        """Forward all attribute access to the client."""
        if hasattr(self.client, name):
            return getattr(self.client, name)
        raise AttributeError(f"'DartVmClient' has no attribute '{name}'")
