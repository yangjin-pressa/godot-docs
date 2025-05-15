# VisualShaderNodeTexture3D

## Inheritance
- **VisualShaderNodeTexture3D** < **VisualShaderNodeSample3D** < **VisualShaderNode** < **Resource** < **RefCounted** < **Object**

## Description
Performs a 3D texture lookup within the visual shader graph. Supports multiple texture sources.

## Properties
- **Texture3D** texture: Reference to a texture. Used when `VisualShaderNodeSample3D.source` is set to `VisualShaderNodeSample3D.SOURCE_TEXTURE`.

## Property Descriptions
### texture
- **set_texture**(value: Texture3D): Assigns a texture source.
- **get_texture**(): Retrieves the current texture source.

## References
- [Texture3D class](class_Texture3D)
- [VisualShaderNodeTexture3D_property_texture](class_VisualShaderNodeTexture3D_property_texture)