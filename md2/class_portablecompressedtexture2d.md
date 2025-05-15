# PortableCompressedTexture2D

**Inherits:** Texture2D < Texture < Resource < RefCounted < Object

## Description
Stores compressed textures as self-contained resources. Supports lossy/lossless modes for 2D, and various compression formats for 3D. Recommended formats: S3TC/BPTC for desktop, ETC2 for mobile, Basis Universal for cross-platform.

## Properties
- **keep_compressed_buffer**: bool (default: false)  
  Whether to retain compressed data in memory after loading. Must be set before create_from_image().

- **size_override**: Vector2 (default: (0, 0))  
  Overrides texture size for 2D use. 

## Methods
- **create_from_image(image: Image, compression_mode: CompressionMode, normal_map: bool = false, lossy_quality: float = 0.8)**  
  Initializes compressed texture from image. Lossy quality controls compression quality.

- **get_compression_mode() const**  
  Returns current compression mode.

- **get_format() const**  
  Returns image format used.

- **set_basisu_compressor_params(uastc_level: int, rdo_quality_loss: float)**  
  Configures Basis Universal compression parameters. Must be called before create_from_image().

- **set_keep_all_compressed_buffers(keep: bool)**  
  Static method to globally set compressed buffer retention for all instances.

## Enumerations
**CompressionMode**  
- COMPRESSION_MODE_LOSSLESS (0)  
- COMPRESSION_MODE_LOSSY (1)  
- COMPRESSION_MODE_BASIS_UNIVERSAL (2)  
- COMPRESSION_MODE_S3TC (3)  
- COMPRESSION_MODE_ETC2 (4)  
- COMPRESSION_MODE_BPTC (5)  
- COMPRESSION_MODE_ASTC (6)  

*(Descriptions pending contribution)*

## Key Notes
- Use lossy compression for 2D (disk + VRAM) with quality parameter.
- Basis Universal offers cross-platform support but has quality tradeoffs.
- Static method set_keep_all_compressed_buffers controls global buffer retention.