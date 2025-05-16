from setuptools import setup, find_namespace_packages
import os
import shutil

# Ensure dart_vm_service directory is included in the package
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('dart_vm_client/dart_vm_service')

if __name__ == "__main__":
    setup(
        # Use find_namespace_packages to include dart_vm_service
        packages=find_namespace_packages(include=['dart_vm_client', 'dart_vm_client.*']),
        package_data={
            'dart_vm_client': ['dart_vm_service.proto', 'dart_vm_service_pb2.py', 'dart_vm_service_pb2_grpc.py', 'dart_vm_service/**/*'],
            'dart_vm_client.dart_vm_service': ['**/*'],
            'dart_vm_client.dart_vm_service.bin': ['**/*'],
            'dart_vm_client.dart_vm_service.lib': ['**/*'],
            'dart_vm_client.dart_vm_service.protos': ['**/*'],
        },
        include_package_data=True,
        zip_safe=False,
    ) 