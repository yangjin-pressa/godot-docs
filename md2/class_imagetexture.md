# ImageTexture

## Inheritance
- Texture2D
  - Texture
    - Resource
      - RefCounted
        - Object

## Description
- **ImageTexture** is a Texture2D based on an Image.
- Create from image using:  
  ```gdscript
  var image = Image.load_from_file("res://icon.svg")
  var texture = ImageTexture.create_from_image(image)
  $Sprite2D.texture = texture
  ```
- Prefer using `@GDScript.load()` for imported textures over `Image.load()` to ensure compatibility with exported projects.
- `Texture2D.get_image()` returns a copy of the image data.
- ImageTexture is not intended for direct editor use; use `EditorImportPlugin` for procedural image generation in the editor.

## Tutorials
- [Importing images](../tutorials/assets_pipeline/importing_images)

## Properties
- `resource_local_to_scene`: false (overrides Resource property)

## Methods
- **static** `create_from_image(image: Image)`: Creates a new ImageTexture from an Image.
- `get_format()`: Returns the texture format (e.g., Format).
- `set_image(image: Image)`: Replaces texture data with a new Image (re-allocates memory).
- `set_size_override(size: Vector2i)`: Resizes the texture to specified dimensions.
- `update(image: Image)`: Updates texture data without re-allocating memory (requires prior creation or setup).

## Notes
- Max texture size: 16384×16384 pixels (hardware limitation).
- `set_image()` is slower than `update()` for frequent updates.
- `update()` requires matching image dimensions, format, and mipmaps with existing texture.

## References
- [Texture2D.get_image()](class_Texture2D_method_get_image)  
- [@GDScript.load()](class_@GDScript_method_load)  
- [EditorImportPlugin](class_EditorImportPlugin)