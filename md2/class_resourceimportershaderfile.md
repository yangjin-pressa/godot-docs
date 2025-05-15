# ResourceImporterShaderFile

**Inherits:** ResourceImporter < RefCounted < Object

## Description
Imports native GLSL shaders as RDShaderFile resources, for use with low-level RenderingDevice operations. This importer does *not* handle `.gdshader` files.

## Key Features
- Targets: RDShaderFile resources
- Scope: Low-level RenderingDevice operations
- File type: Native GLSL shaders
- Excludes: .gdshader files

## Related References
- RDShaderFile
- RenderingDevice

## Notes
- This class is designed for low-level graphics pipeline integration.