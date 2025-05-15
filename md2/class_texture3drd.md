# Texture3DRD

## Inheritance
- **Texture3DRD**  
  Inherits: Texture3D < Texture < Resource < RefCounted < Object

## Description
This texture class allows use of a 3D texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

## Properties
- **texture_rd_rid**: RID of the texture object created on the RenderingDevice.

## Property Descriptions
- **set_texture_rd_rid**(value: RID): void  
  Sets the RID of the texture object.

- **get_texture_rd_rid**(): RID  
  Retrieves the RID of the texture object.

## References
- [RenderingDevice](class_RenderingDevice)  
- [Texture3D](class_Texture3D)  
- [Texture](class_Texture)  
- [Resource](class_Resource)  
- [RefCounted](class_RefCounted)  
- [Object](class_Object)