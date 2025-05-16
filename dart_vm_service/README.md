# Dart VM Service

A tool for controlling and testing Flutter applications via VM Service protocol, with gRPC support.

## Features

- Connect to a running Flutter application via VM service
- Enable debug painting, performance overlay, and repaint rainbow
- Interact with widgets (tap, enter text)
- Get a list of widgets on the current screen
- Supports both direct usage and gRPC server mode

## Installation

```bash
dart pub get
brew install protobuf
dart pub global activate protoc_plugin
```

## Usage

### Direct Mode

Connect directly to a Flutter application:

```bash
dart bin/flutter_browser_tool.dart connect http://127.0.0.1:50000/abcdef/
```

### gRPC Server Mode

Start the gRPC server to expose functionality:

```bash
dart bin/flutter_browser_tool.dart --grpc --port=50051
```

or

```bash
dart bin/flutter_browser_tool.dart grpc-server --port=50051
```

## Development

### Generating gRPC Code

Before using gRPC mode, you need to generate the Dart code from the protobuf definitions:

```bash
make generate
```

This requires the `protoc` compiler to be installed on your system.

### Dependencies

- `vm_service`: For connecting to the Flutter VM Service
- `grpc`: For gRPC server implementation
- `protobuf`: For protocol buffer support
- `args`: For command-line argument parsing

## API Documentation

### gRPC Service Methods

- `Connect`: Connect to a Flutter application via VM service
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
