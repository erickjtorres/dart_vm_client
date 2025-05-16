#!/usr/bin/env python3
"""
Example usage of the Dart VM Service Client.

This example demonstrates how to use the Dart VM Service Client to connect to a Flutter
application and interact with it using various methods provided by the client.

Usage:
    1. Start a Flutter application with VM service enabled
    2. Run this script with the VM service URI as an argument
        python example_usage.py ws://127.0.0.1:50505/ws
"""

import sys
import time
import logging

# Import directly from local files
import os
import sys

# Add the current directory to the path so we can import the local files
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dart_vm_service_client import DartVmServiceClient
from dart_vm_service_manager import DartVmServiceManager

# Import our wrapper class
class DartVmClient:
    """Main client for interacting with the Dart VM Service."""
    
    def __init__(self, start_service=True, port=50051, dart_executable=None):
        """Initialize the client."""
        self.port = port
        self.service_manager = None
        
        if start_service:
            self.service_manager = DartVmServiceManager(
                port=port, 
                dart_executable=dart_executable
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
    
    # Forward all methods to the gRPC client
    def __getattr__(self, name):
        """Forward all attribute access to the client."""
        if hasattr(self.client, name):
            return getattr(self.client, name)
        raise AttributeError(f"'DartVmClient' has no attribute '{name}'")


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def example_with_context_manager(vm_service_uri):
    """Example using the context manager approach (recommended)."""
    logger.info("Starting example with context manager")
    
    # The context manager will automatically start the Dart VM Service and clean up
    with DartVmClient(start_service=True) as client:
        # Connect to the Flutter application
        response = client.connect(vm_service_uri)
        logger.info(f"Connection status: {response.success}, Message: {response.message}")
        
        if not response.success:
            logger.error("Failed to connect to Flutter application")
            return
        
        # Get information about the application
        logger.info("Listing available views...")
        views = client.list_views()
        logger.info(f"Views: {views}")
        
        # Enable some debug visualizations
        logger.info("Enabling debug paint...")
        client.toggle_debug_paint(enable=True)
        time.sleep(1)  # Give it a moment to update
        
        logger.info("Enabling performance overlay...")
        client.toggle_performance_overlay(enable=True)
        time.sleep(1)
        
        # Dump the widget tree for inspection
        logger.info("Dumping widget tree...")
        widget_tree = client.dump_widget_tree()
        logger.info(f"Widget tree: {widget_tree.message[:100]}...")
        
        # Example of interacting with widgets (uncomment if you have these widgets)
        # client.tap_widget_by_text("Counter")
        # client.enter_text("username_field", "example_user")
        
        # Disable debug visualizations before finishing
        logger.info("Disabling debug features...")
        client.toggle_debug_paint(enable=False)
        client.toggle_performance_overlay(enable=False)
        
    logger.info("Context manager example completed")


def example_with_manual_management(vm_service_uri, port=50052):
    """Example using manual service and client management."""
    logger.info("Starting example with manual management")
    
    # Start the Dart VM Service separately
    service_manager = DartVmServiceManager(port=port)
    if not service_manager.start():
        logger.error("Failed to start Dart VM Service")
        return
    
    try:
        # Create the client that connects to the running service
        client = DartVmServiceClient(f"localhost:{port}")
        
        # Connect to the Flutter application
        response = client.connect(vm_service_uri)
        logger.info(f"Connection status: {response.success}, Message: {response.message}")
        
        if response.success:
            # Demonstrate some widget interaction methods
            logger.info("Toggling inspector...")
            client.toggle_inspector(enable=True)
            time.sleep(1)
            
            # Demonstrate another debug feature
            logger.info("Toggling repaint rainbow...")
            client.toggle_repaint_rainbow(enable=True)
            time.sleep(1)
            
            # Get render tree
            logger.info("Dumping render tree...")
            render_tree = client.dump_render_tree()
            logger.info(f"Render tree: {render_tree.message[:100]}...")
            
            # Disable features before finishing
            client.toggle_inspector(enable=False)
            client.toggle_repaint_rainbow(enable=False)
    
    except Exception as e:
        logger.error(f"Error in example: {str(e)}")
    
    finally:
        # Clean up resources
        if 'client' in locals():
            logger.info("Closing client...")
            client.close()
        
        logger.info("Stopping Dart VM Service...")
        service_manager.stop()
    
    logger.info("Manual management example completed")


def advanced_example(vm_service_uri):
    """Demonstrates more advanced features of the client."""
    logger.info("Starting advanced example")
    
    with DartVmClient() as client:
        # Connect to the Flutter application
        response = client.connect(vm_service_uri)
        if not response.success:
            logger.error("Failed to connect to Flutter application")
            return
        
        # Example of scrolling and tapping
        logger.info("Performing some widget interactions...")
        
        # You would replace these with actual widget keys and text from your app
        try:
            # Scroll a list
            client.scroll_down_by_type("ListView")
            time.sleep(0.5)
            
            # Tap a button by tooltip
            client.tap_widget_by_tooltip("Add to cart")
            time.sleep(0.5)
            
            # Enter text
            client.enter_text("search_field", "Flutter is awesome!")
            time.sleep(0.5)
            
            # Scroll widget into view
            client.scroll_into_view_by_text("Settings")
            time.sleep(0.5)
            
            # Extended scroll with specific duration and frequency
            client.scroll_down_by_text_extended(
                text="Details", 
                dy=200,  # Scroll down 200 pixels
                duration_microseconds=500000,  # 0.5 seconds
                frequency=120  # Smoothness of animation
            )
            
        except Exception as e:
            logger.warning(f"Some interactions failed (expected if widgets don't exist): {e}")
    
    logger.info("Advanced example completed")


def main():
    # Get VM service URI from command line or use default
    if len(sys.argv) > 1:
        vm_service_uri = sys.argv[1]
    else:
        vm_service_uri = "ws://127.0.0.1:50505/ws"  # Default Flutter debug VM service URI
        logger.info(f"No VM service URI provided, using default: {vm_service_uri}")
    
    try:
        # Run the examples
        example_with_context_manager(vm_service_uri)
        time.sleep(1)  # Brief pause between examples
        
        example_with_manual_management(vm_service_uri, port=50052)
        time.sleep(1)  # Brief pause between examples
        
        advanced_example(vm_service_uri)
        
    except KeyboardInterrupt:
        logger.info("Example interrupted by user")
    except Exception as e:
        logger.error(f"Error running examples: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
