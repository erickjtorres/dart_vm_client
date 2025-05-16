import 'dart:io';

import 'package:args/args.dart';
import 'package:dart_vm_service/dart_vm_service_grpc_server.dart';
import 'package:dart_vm_service/dart_vm_service_tool.dart';

Future<void> main(List<String> args) async {
  final parser = ArgParser()
    ..addFlag('help',
        abbr: 'h', negatable: false, help: 'Show help information')
    ..addFlag('grpc',
        abbr: 'g', negatable: false, help: 'Start in gRPC server mode')
    ..addOption('port',
        abbr: 'p', defaultsTo: '50051', help: 'gRPC server port')
    ..addCommand('connect')
    ..addCommand('grpc-server');

  try {
    final results = parser.parse(args);

    if (results['help'] == true) {
      printUsage(parser);
      exit(0);
    }

    if (results['grpc'] == true) {
      // Run in gRPC server mode
      final port = int.tryParse(results['port']) ?? 50051;
      final server = DartVmServiceGrpcServer(port: port);
      print('Starting gRPC server on port $port');
      await server.start();

      print('gRPC server running on port $port. Press Ctrl+C to stop.');
      await ProcessSignal.sigint.watch().first;
      await server.stop();
      exit(0);
    }
    if (results.command?.name == 'connect') {
      final connectArgs = results.command!.arguments;
      if (connectArgs.isEmpty) {
        print('Error: VM service URI is required');
        printUsage(parser);
        exit(1);
      }

      final String vmServiceUri = connectArgs[0];
      final tool = DartVmServiceTool();
      await tool.start(vmServiceUri);
    } else if (results.command?.name == 'grpc-server') {
      final port = int.tryParse(results['port']) ?? 50051;
      final server = DartVmServiceGrpcServer(port: port);
      await server.start();

      print('gRPC server running on port $port. Press Ctrl+C to stop.');
      await ProcessSignal.sigint.watch().first;
      await server.stop();
      exit(0);
    } else {
      if (args.isEmpty) {
        printUsage(parser);
        exit(1);
      }

      final String vmServiceUri = args[0];
      final tool = DartVmServiceTool();
      await tool.start(vmServiceUri);
    }
  } catch (e) {
    print('Error: $e');
    printUsage(parser);
    exit(1);
  }
}

void printUsage(ArgParser parser) {
  print(
      'Dart VM Service Tool - A tool for interacting with Dart VM applications');
  print('');
  print('Usage:');
  print('  Direct connection:');
  print('    dart_vm_service connect <vm-service-uri>');
  print('');
  print('  Start gRPC server:');
  print('    dart_vm_service --grpc [--port=50051]');
  print('  or');
  print('    dart_vm_service grpc-server [--port=50051]');
  print('');
  print('Examples:');
  print('  dart_vm_service connect http://127.0.0.1:50000/abcdef/');
  print('  dart_vm_service --grpc --port=8080');
  print('');
  print('Options:');
  print(parser.usage);
}
