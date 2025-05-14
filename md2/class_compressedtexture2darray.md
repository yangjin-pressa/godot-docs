**Class**: CompressedTexture2DArray  
**Inherits**: CompressedTextureLayered → TextureLayered → Texture → Resource → RefCounted → Object  

**Description**  
A texture array loaded from a `.ctexarray` file (internal to Godot, created via import). Supports four compression methods:  

- **Lossless** (WebP or PNG, uncompressed on GPU)  
- **Lossy** (WebP, uncompressed on GPU)  
- **VRAM Compressed** (compressed on GPU)  
- **Basis Universal** (compressed on GPU, lower file size but slower and lower quality)  

**Note**  
- **VRAM Compressed** reduces GPU memory usage.  
- Lossless/Lossy methods reduce disk storage but not GPU memory.  
- VRAM Compressed improves loading times but may exhibit artifacts, intended for 3D rendering.  

**Reference**  
See `Texture2DArray` class for general texture array description.