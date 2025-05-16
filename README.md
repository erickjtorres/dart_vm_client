# Dart VM Service Client

A Python client library to communicate with a Dart VM Service gRPC server for controlling Flutter applications.

## Installation

1. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

2. Ensure you have the Dart SDK installed on your system
   - The client can automatically find Dart in your PATH
   - Alternatively, you can specify the path to the Dart executable

3. If needed, generate the Python gRPC code:

```bash
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/dart_vm_service.proto
```

This will create the following files:

- `dart_vm_service_pb2.py`
- `dart_vm_service_pb2_grpc.py`

## Usage

### Basic Usage

```python
from dart_vm_client import DartVmClient

# Create a client and start the Dart VM Service automatically
with DartVmClient() as client:
    # Connect to a Flutter app
    response = client.connect("ws://127.0.0.1:8181/ws")
    print(f"Connection status: {response.success}, Message: {response.message}")
    
    if response.success:
        # Interact with the app
        client.tap_widget_by_text("Login")
        
        # Enable debug features
        client.toggle_debug_paint(enable=True)
        client.toggle_performance_overlay(enable=True)

# Service is automatically stopped when exiting the "with" block
```

### Manual Service Management

```python
from dart_vm_client import DartVmClient, DartVmServiceClient, DartVmServiceManager

# Start the service separately
service_manager = DartVmServiceManager(port=8080)
if service_manager.start():
    # Create a client that connects to the running service
    client = DartVmServiceClient("localhost:8080")
    
    try:
        # Use the client...
        client.connect("ws://127.0.0.1:8181/ws")
        
    finally:
        # Clean up
        client.close()
        service_manager.stop()
```

### Available Methods

The client provides numerous methods for interacting with Flutter apps, including:

#### Connection Management
- `connect(vm_service_uri)`: Connect to a Flutter app VM service
- `close()`: Close the connection

#### Debug Visualization
- `toggle_debug_paint(enable=True)`: Toggle debug painting
- `toggle_repaint_rainbow(enable=True)`: Toggle repaint rainbow
- `toggle_performance_overlay(enable=True)`: Toggle performance overlay
- `toggle_baseline_painting(enable=True)`: Toggle baseline painting
- `toggle_debug_banner(enable=True)`: Toggle debug banner

#### Widget Interaction
- `tap_widget_by_key(key_value)`: Tap a widget by key
- `tap_widget_by_text(text)`: Tap a widget by text
- `enter_text(key_value, text)`: Enter text in a widget by key
- `scroll_into_view_by_key(key_value, alignment=0)`: Scroll a widget into view by key

#### Inspection
- `dump_widget_tree()`: Get the widget tree
- `dump_layer_tree()`: Get the layer tree
- `dump_render_tree()`: Get the render tree
- `toggle_inspector(enable=True)`: Toggle the inspector

And many more. See the `dart_vm_service_client.py` file for a complete list of available methods.

### Example

See `example_usage.py` for a more detailed example of how to use the client.

## Custom Server Address

If your gRPC server is running on a different host or port, specify it when creating the client:

```python
client = DartVmServiceClient(server_address="192.168.1.100:8080")
```

## Error Handling

Use try/except to handle gRPC errors:

```python
import grpc
from dart_vm_service_client import DartVmServiceClient

client = DartVmServiceClient()

try:
    response = client.connect("ws://127.0.0.1:8181/")
    # Your code here
except grpc.RpcError as e:
    print(f"RPC Error: {e.code()}, {e.details()}")
finally:
    client.close()
```
