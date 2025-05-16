import os
import subprocess

def generate_proto():
    """Generate Python code from proto file using grpcio-tools."""
    print("Generating Python code from proto file...")
    
    
    cmd = [
        "python", "-m", "grpc_tools.protoc",
        "-I.", 
        "--python_out=.", 
        "--grpc_python_out=.",
        "dart_vm_service.proto"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Successfully generated Python code from proto file.")
        print("Generated files:")
        print("  - dart_vm_service_pb2.py")
        print("  - dart_vm_service_pb2_grpc.py")
    else:
        print("Failed to generate Python code from proto file.")
        print(f"Error: {result.stderr}")

if __name__ == "__main__":
    generate_proto() 