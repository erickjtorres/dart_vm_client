// Example of using dart_vm_service programmatically

import 'dart:io';

import 'package:dart_vm_service/dart_vm_service_tool.dart';
import 'package:dart_vm_service/dart_vm_service_grcp_server.dart';

void main() async {
  // Example 1: Connect to a VM service directly
  print('Example 1: Connecting to a VM service (not run in this example)');
  print('var tool = DartVmServiceTool();');
  print('await tool.start("http://127.0.0.1:50000/abcdef/");\n');

  // Example 2: Start a gRPC server
  print('Example 2: Starting a gRPC server');
  final server = DartVmServiceGrpcServer(port: 50051);
  print('Starting gRPC server on port 50051...');
  await server.start();

  print('gRPC server running on port 50051. Press Ctrl+C to stop.');
  print('Press any key to stop the server in this example...');

  // Wait for a key press (simulating Ctrl+C)
  await stdin.first;
  await server.stop();
  print('Server stopped.');
}

// For CLI usage, install the package globally:
// dart pub global activate dart_vm_service
//
// Then run:
// dart_vm_service connect http://127.0.0.1:50000/abcdef/
// 
// Or start the gRPC server:
// dart_vm_service --grpc --port=50051 