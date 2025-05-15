# Texture2DArray

**Inherits:**  
- Resource  
- Texture  
- TextureLayered  
- ImageTextureLayered  

---

## Description  
- **Key Difference from Texture3D**: No blending between images (no trilinear interpolation).  
- **Related Classes**:  
  - [Cubemap](class_Cubemap)  
  - [CubemapArray](class_CubemapArray)  
- **Key Difference from AtlasTexture**:  
  - All images are separate with fixed dimensions.  
  - Mipmap chains are handled independently per layer.  
  - No automatic padding or slicing in shaders.  

---

## Methods  
- **create_placeholder**  
  - **Type**: Resource  
  - **Description**: Creates a placeholder version of this resource ([PlaceholderTexture2DArray](class_PlaceholderTexture2DArray)).  
  - **Modifiers**:  
    - `const` (no side effects, no member variable changes)  

---

## Notes  
- **Manual Handling**: Requires manual setup for mipmapping and UV mapping.  
- **Creation**:  
  - Use `ImageTextureLayered.create_from_images()` to generate from images.  
  - Reimport images via Godot Editor import presets for custom files.  

---

## See also  
- [Cubemap](class_Cubemap)  
- [CubemapArray](class_CubemapArray)  
- [AtlasTexture](class_AtlasTexture)  
- [ImageTextureLayered](class_ImageTextureLayered)