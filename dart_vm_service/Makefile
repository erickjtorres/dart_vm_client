.PHONY: generate clean

# Generate Dart files from proto definitions
generate:
	@echo "Generating Dart files from proto definitions..."
	@mkdir -p lib/src/generated
	@protoc --dart_out=grpc:lib/src/generated -Iprotos protos/*.proto
	@echo "Generation complete."

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -rf lib/src/generated
	@echo "Clean complete." 