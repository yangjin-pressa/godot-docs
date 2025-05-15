**Class:** VisualShaderNodeTexture2DArray  
**Inherits:** VisualShaderNodeSample3D < VisualShaderNode < Resource < RefCounted < Object  

**Description**  
Translated to `uniform sampler2DArray` in the shader language.  

**Properties**  
- `TextureLayered` **texture_array**: Reference to a texture array.  

**Property Descriptions**  
- **texture_array**  
  - **set_texture_array**(value: TextureLayered): Sets the texture array.  
  - **get_texture_array**(): Retrieves the texture array.  
  - Used when `VisualShaderNodeSample3D.source` is set to `VisualShaderNodeSample3D.SOURCE_TEXTURE`.  

**References**  
- [TextureLayered](TextureLayered)  
- [VisualShaderNodeSample3D](VisualShaderNodeSample3D)  
- [VisualShaderNodeSample3D.SOURCE_TEXTURE](VisualShaderNodeSample3D_constant_SOURCE_TEXTURE)