# Dart VM Service

A CLI tool for interacting with the Dart VM Service API, allowing for debugging and introspection of Dart applications.

## Features

- Connect to a running Dart/Flutter application via VM service protocol
- Enable debug painting, performance overlay, and repaint rainbow
- Interact with widgets (tap, enter text)
- Get a list of widgets on the current screen
- Supports both direct usage and gRPC server mode

## Installation

### From Source

Clone this repository and install the package globally:

```bash
dart pub get
dart pub global activate --source path .
```

### Dependencies

Make sure you have protobuf installed for gRPC functionality:

```bash
brew install protobuf  # macOS
# OR
apt-get install protobuf  # Ubuntu/Debian
```

## Usage

After installation, you can use the tool directly from the command line:

### Direct Mode

Connect directly to a Dart/Flutter application:

```bash
dart_vm_service connect http://127.0.0.1:50000/abcdef/
```

### gRPC Server Mode

Start the gRPC server to expose functionality:

```bash
dart_vm_service --grpc --port=50051
```

or

```bash
dart_vm_service grpc-server --port=50051
```

## Development

### Generating gRPC Code

Before using gRPC mode, you need to generate the Dart code from the protobuf definitions:

```bash
make generate
```

This requires the `protoc` compiler to be installed on your system.

### Dependencies

- `vm_service`: For connecting to the Dart VM Service
- `grpc`: For gRPC server implementation
- `protobuf`: For protocol buffer support
- `args`: For command-line argument parsing

## API Documentation

### gRPC Service Methods

- `Connect`: Connect to a Dart application via VM service
- `ToggleDebugPaint`: Toggle debug painting on/off
- `TogglePerformanceOverlay`: Toggle performance overlay on/off
- `ToggleRepaintRainbow`: Toggle repaint rainbow on/off
- `TapWidgetByKey`: Tap a widget by its key
- `TapWidgetByText`: Tap a widget by its displayed text
- `EnterText`: Enter text into a widget
- `TapBackButton`: Tap the back button
- `GetCurrentScreenItems`: Get a list of widgets on the current screen

## License

MIT
