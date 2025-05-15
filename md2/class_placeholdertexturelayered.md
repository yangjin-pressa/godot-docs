# PlaceholderTextureLayered

**Inherits:** TextureLayered < Texture < Resource < RefCounted < Object  
**Inherited By:** PlaceholderCubemap, PlaceholderCubemapArray, PlaceholderTexture2DArray  

## Description  
This class is used when loading a project that uses a TextureLayered subclass in 2 conditions:  

1. When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.  
2. When this subclass is missing due to using a different engine version or build (e.g. modules disabled).  

**Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).  

## Properties  
- **layers**: int = 1  
- **size**: Vector2i = Vector2i(1, 1)  

## Property Descriptions  
### layers  
- **Type**: int  
- **Default**: 1  
- **Description**: The number of layers in the texture array.  
- **Methods**:  
  - `set_layers(value: int)`  
  - `get_layers()`  

### size  
- **Type**: Vector2i  
- **Default**: Vector2i(1, 1)  
- **Description**: The size of each texture layer (in pixels).  
- **Methods**:  
  - `set_size(value: Vector2i)`  
  - `get_size()`