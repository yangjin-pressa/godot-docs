# ResourceImporterLayeredTexture

Inherits from: ResourceImporter → RefCounted → Object

Imports 3D textures, Texture2DArray, Cubemap, or CubemapArray for use in shaders, fog materials, or particle systems.

## Tutorials
- [Importing images](../tutorials/assets_pipeline/importing_images)

## Properties

- **compress/channel_pack** (int) = 0  
  Controls color channel usage. Options: sRGB friendly, optimized, normal map (RG channels).

- **compress/hdr_compression** (int) = 1  
  HDR compression mode: disabled, opaque only, always. Note: effective for .hdr and .exr files.

- **compress/high_quality** (bool) = true  
  Enables high-quality compression (e.g., Basis Universal) for 3D scenes.

- **compress/rdo_quality_loss** (float) = 0.0  
  Enables Rate-Distortion Optimization (RDO) for file size reduction. Higher values reduce quality.

- **compress/uastc_level** (int) = 0  
  UASTC encoding level. Higher values improve quality but slow encoding.

- **mipmaps/generate** (bool) = true  
  Generates mipmaps for textures. Reduces aliasing but increases memory usage.

- **mipmaps/limit** (int) = -1  
  Unimplemented. Currently has no effect.

- **slices/arrangement** (int) = 1  
  Cubemap layout: 1×6, 6×1, 2×3, or 3×2. 2×3/3×2 better for high-res cubemaps.

## Notes
- Mipmaps recommended for 3D scenes, limited for 2D.
- Basis Universal and UASTC are for 3D use.
- RDO increases encoding time, especially for large images.