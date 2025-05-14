# CompressedCubemapArray

## Inheritance
- `CompressedTextureLayered`  
- `TextureLayered`  
- `Texture`  
- `Resource`  
- `RefCounted`  
- `Object`  

## Description
A cubemap array loaded from a `.ccubearray` file (internal to Godot). It supports 4 compression methods:

- **Lossless** (WebP or PNG, uncompressed on GPU)  
- **Lossy** (WebP, uncompressed on GPU)  
- **VRAM Compressed** (compressed on GPU; reduces GPU memory usage)  
- **VRAM Uncompressed** (uncompressed on GPU)  
- **Basis Universal** (compressed on GPU; smaller file size than VRAM Compressed, but slower to compress and lower quality)  

**Key Notes**:  
- VRAM Compressed reduces GPU memory usage but may introduce artifacts.  
- Lossless/Lossy methods reduce disk storage but not GPU memory.  
- VRAM Compressed textures load faster but may not be suitable for 2D rendering.  

## Related Resources  
See [CubemapArray](class_CubemapArray) for general cubemap array information.