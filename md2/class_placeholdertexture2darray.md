# PlaceholderTexture2DArray

**Inherits:**  
- PlaceholderTextureLayered  
  - TextureLayered  
    - Texture  
      - Resource  
        - RefCounted  
          - Object  

## Description  
- Used for:  
  - Exported projects in dedicated server mode (only texture dimensions are retained)  
  - When Texture2D subclass is missing due to engine version/mode differences  

**Important Notes:**  
- Not intended for rendering  
- May not function correctly in shaders/materials (e.g. UV calculations)  
- Provides no visual output or interactive behavior  

## Key Characteristics  
- Serves as a fallback implementation  
- Reduces PCK file size when used in dedicated server mode  
- Acts as a placeholder for texture array functionality  
- Does not support actual rendering operations  

## Usage Context  
- Required when:  
  - Project uses Texture2D subclass but engine version differs  
  - Dedicated server build requires reduced file size  
  - Modules/dependencies are missing from the engine version  

## Important Constraints  
- Should not be used as a replacement for actual textures  
- May produce unexpected results in material/shader contexts  
- Only provides dimensional data when used in dedicated server mode