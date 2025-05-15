# ViewportTexture

**Inherits:** Texture2D < Texture < Resource < RefCounted < Object

## Description
A ViewportTexture provides the content of a Viewport as a dynamic Texture2D. It allows combining rendering of Control, Node2D, and Node3D nodes. This can be used to display 3D scenes in TextureRect or 2D overlays in Sprite3D.

Key notes:
- Always local to its scene (Resource property `resource_local_to_scene`)
- High-resolution instances may cause stutter
- HDR textures (when `use_hdr_2d` is true) require conversion to gamma space:
  ```
  img.convert(Image.FORMAT_RGBA8)
  imb.linear_to_srgb()
  ```
- Some nodes (Decal, Light3D, PointLight2D) require conversion to ImageTexture:
  ``` 
  Texture2D.get_image() → ImageTexture.create_from_image()
  ```

## Tutorials
- [GUI in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2807)
- [3D in 2D Viewport Demo](https://godotengine.org/asset-library/asset/2804)
- [2D in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2803)
- [3D Resolution Scaling Demo](https://godotengine.org/asset-library/asset/2805)

## Properties
- **viewport_path**: NodePath = NodePath("")
  - Path to the Viewport node (relative to scene root)

## Method Descriptions
- `set_viewport_path_in_scene(value: NodePath)`: Sets the viewport path
- `get_viewport_path_in_scene()`: Gets the viewport path

Notes:
- Path is automatically updated in the editor but may not update at runtime if scene root is unavailable
- This property is virtual (overrideable) and const (no side effects)

## Additional Notes
- Use `Viewport.get_texture()` to obtain a ViewportTexture
- Texture data is dynamic and updates with viewport changes
- Avoid frequent conversions from ViewportTexture to ImageTexture due to performance cost