# MeshTexture

**Inherits:** Texture2D < Texture < Resource < RefCounted < Object

## Description
A texture that uses a mesh to draw itself. Limited features include inability to change flags and lack of region drawing support.

## Properties
- **base_texture**: Texture2D (sets the base texture for mesh drawing)
- **image_size**: Vector2 (defines image size; default: Vector2(0, 0))
- **mesh**: Mesh (defines the mesh used for drawing; must be 2D)

## Property Descriptions
### base_texture
- **set_base_texture**(value: Texture2D): Assigns the base texture for mesh drawing
- **get_base_texture**(): Retrieves the current base texture

### image_size
- **set_image_size**(value: Vector2): Sets the image size for reference
- **get_image_size**(): Returns the current image size

### mesh
- **set_mesh**(value: Mesh): Assigns the mesh for drawing (must be 2D)
- **get_mesh**(): Retrieves the current mesh

## Notes
- Resource-local-to-scene flag is overridden to false by default.