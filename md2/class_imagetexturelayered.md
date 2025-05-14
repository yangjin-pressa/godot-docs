# ImageTextureLayered

**Inherits:** TextureLayered < Texture < Resource < RefCounted < Object

**Inherited By:** Cubemap, CubemapArray, Texture2DArray

Base class for texture types containing multiple ImageTexture instances. All images must have the same size and format.

## Description

Base class for Texture2DArray, Cubemap, and CubemapArray. Cannot be used directly. See Texture3D for related classes.

## Methods

- **create_from_images(images: Array[Image])**: Creates ImageTextureLayered from array of images. First image determines size/format. Other images must match.
  
  Example:
  ```gdscript
  var images = []
  const LAYERS = 6
  for i in LAYERS:
      var image = Image.create_empty(128, 128, false, Image.FORMAT_RGB8)
      if i % 3 == 0:
          image.fill(Color.RED)
      elif i % 3 == 1:
          image.fill(Color.GREEN)
      else:
          image.fill(Color.BLUE)
      images.push_back(image)
  
  var texture_2d_array = Texture2DArray.new()
  texture_2d_array.create_from_images(images)
  ResourceSaver.save(texture_2d_array, "res://texture_2d_array.res", ResourceSaver.FLAG_COMPRESS)
  ```

- **update_layer(image: Image, layer: int)**: Replaces existing image data at specified layer. Image must match other images' format and dimensions.

## Key Notes

- All images must have same width, height, format, and mipmapping setting
- The first image determines the base dimensions and format
- Updates are immediately synchronized with drawing
- unsupported formats are converted to supported ones automatically