# Dart VM Service Example

This directory contains examples demonstrating how to use the Dart VM Service package.

## Running the Example

```bash
dart run dart_vm_service_example.dart
```

This will start a gRPC server on port 50051 that can be used to interact with Dart applications.

## CLI Usage

After installing the package globally:

```bash
dart pub global activate dart_vm_service
```

You can use the CLI tool:

```bash
# Connect to a VM service
dart_vm_service connect http://127.0.0.1:50000/abcdef/

# Start a gRPC server
dart_vm_service --grpc --port=50051
``` 