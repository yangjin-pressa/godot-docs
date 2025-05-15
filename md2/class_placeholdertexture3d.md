# PlaceholderTexture3D

**Inherits:** Texture3D < Texture < Resource < RefCounted < Object

## Description

This class is used when loading a project that uses a Texture3D subclass in two conditions:

1. When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

2. When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

**Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

## Properties

- **size**: Vector3i (default: Vector3i(1, 1, 1))

## Property Descriptions

**size** = Vector3i(1, 1, 1)

The texture's size (in pixels).

## Method Descriptions

- `set_size(value: Vector3i)`  
- `get_size()`  

## Class Inheritance Hierarchy

Texture3D  
├── Texture  
│   └── Resource  
│       └── RefCounted  
│           └── Object

## Related Classes

- [Texture3D](class_Texture3D)  
- [Texture](class_Texture)  
- [Resource](class_Resource)  
- [RefCounted](class_RefCounted)  
- [Object](class_Object)