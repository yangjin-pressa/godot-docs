# VisualShaderNodeTexture

**Inherits**: VisualShaderNode → Resource → RefCounted → Object

## Description
Performs a 2D texture lookup within the visual shader graph. Supports multiple texture sources.

## Properties
- **source**: Source (0)  
  Determines the source for the lookup. See Source enum for options.
- **texture**: Texture2D  
  The source texture for the selected source.  
- **texture_type**: TextureType (0)  
  Specifies the texture type if source is SOURCE_TEXTURE. See TextureType enum for options.

## Enumerations

### Source
- **SOURCE_TEXTURE** (0)  
  Use the texture provided as an argument.
- **SOURCE_SCREEN** (1)  
  Use the current viewport's texture.
- **SOURCE_2D_TEXTURE** (2)  
  Use the texture from this shader's texture built-in (e.g. Sprite2D).
- **SOURCE_2D_NORMAL** (3)  
  Use the texture from this shader's normal map built-in.
- **SOURCE_DEPTH** (4)  
  Use the depth texture from the depth prepass. Available in spatial shaders.
- **SOURCE_PORT** (5)  
  Use the texture provided in the input port.
- **SOURCE_3D_NORMAL** (6)  
  Use the normal buffer from the depth prepass. Available in spatial shaders.
- **SOURCE_ROUGHNESS** (7)  
  Use the roughness buffer from the depth prepass. Available in spatial shaders.
- **SOURCE_MAX** (8)  
  Represents the size of the Source enum.

### TextureType
- **TYPE_DATA** (0)  
  No sRGB to linear conversion hints added.
- **TYPE_COLOR** (1)  
  Adds `source_color` hint for sRGB to linear conversion.
- **TYPE_NORMAL_MAP** (2)  
  Adds `hint_normal` hint for normal map conversion.
- **TYPE_MAX** (3)  
  Represents the size of the TextureType enum.

## Property Descriptions
- **source**  
  Sets/gets the source type.  
  - `set_source(value: Source)`  
  - `get_source() → Source`  
- **texture**  
  Sets/gets the texture.  
  - `set_texture(value: Texture2D)`  
  - `get_texture() → Texture2D`  
- **texture_type**  
  Sets/gets the texture type.  
  - `set_texture_type(value: TextureType)`  
  - `get_texture_type() → TextureType`