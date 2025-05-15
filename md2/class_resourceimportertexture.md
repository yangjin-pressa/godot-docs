# ResourceImporterTexture Documentation

## Properties

### `compress/allow_alpha`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the texture will have an alpha channel, which is useful for transparency.

---

### `compress/autodetect`
**Type**: `bool`  
**Default**: `true`  
**Description**: If enabled, the format will be automatically detected based on the file extension.

---

### `compress/enable`
**Type**: `bool`  
**Default**: `true`  
**Description**: If enabled, the texture will be compressed, which reduces file size but may affect quality.

---

### `compress/format`
**Type**: `String`  
**Default**: `"auto"`  
**Description**: The format to use for compression. Options include `"auto"`, `"png"`, `"jpg"`, `"jpeg"`, `"webp"`, etc.

---

### `compress/max_size`
**Type**: `int`  
**Default**: `0`  
**Description**: Sets the maximum size for the compressed texture. If set to `0`, the original size is used.

---

### `compress/quality`
**Type**: `float`  
**Default**: `0.0`  
**Description**: Controls the quality of the compressed texture. For JPEG, it's a value between `0` and `1`. For others, it's ignored.

---

### `compress/quality_limit`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the quality is limited to the maximum for the chosen format.

---

### `compress/texture`
**Type**: `String`  
**Default**: `""`  
**Description**: The path to the texture file to compress. If empty, the current texture is used.

---

### `compress/texture_size`
**Type**: `Vector2`  
**Default**: `Vector2()`  
**Description**: The size of the texture to compress. If empty, the original size is used.

---

### `compress/texture_use_alpha`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the alpha channel is used in the compressed texture.

---

### `compress/texture_use_mipmap`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, mipmaps are used in the compressed texture.

---

### `compress/width`
**Type**: `int`  
**Default**: `0`  
**Description**: Sets the width of the compressed texture. If set to `0`, the original width is used.

---

### `compress/height`
**Type**: `int`  
**Default**: `0`  
**Description**: Sets the height of the compressed texture. If set to `0`, the original height is used.

---

### `detect`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the texture is automatically detected from the file.

---

### `detect/enable`
**Type**: `bool`  
**Default**: `true`  
**Description**: If enabled, the texture is automatically detected from the file.

---

### `detect/texture`
**Type**: `String`  
**Default**: `""`  
**Description**: The path to the texture to detect. If empty, the current texture is used.

---

### `detect/texture_size`
**Type**: `Vector2`  
**Default**: `Vector2()`  
**Description**: The size of the texture to detect. If empty, the original size is used.

---

### `detect/texture_use_alpha`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the alpha channel is used in the detected texture.

---

### `detect/texture_use_mipmap`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, mipmaps are used in the detected texture.

---

### `process/fix_alpha_border`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the texture will have an alpha channel, which is useful for transparency.

---

### `process/hdr_as_srgb`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the texture will have an alpha channel, which is useful for transparency.

---

### `process/hdr_clamp_exposure`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the texture will have an alpha channel, which is useful for transparency.

---

### `process/normal_map_invert_y`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the texture will have an alpha channel, which is useful for transparency.

---

### `process/premult_alpha`
**Type**: `bool`  
**Default**: `false`  
**Description**: If enabled, the texture will have an alpha channel, which is useful for transparency.

---

### `process/size_limit`
**Type**: `int`  
**Default**: `0`  
**Description**: If set to a non-zero value, the texture will be scaled to fit within the specified size, preserving aspect ratio.

---

### `roughness/mode`
**Type**: `int`  
**Default**: `0`  
**Description**: The mode for determining the roughness of the texture. This may affect how the texture is applied in rendering.

---

### `roughness/src_normal`
**Type**: `String`  
**Default**: `""`  
**Description**: The path to the normal map file used for determining the roughness. If empty, the default normal map is used.

---

### `svg/scale`
**Type**: `float`  
**Default**: `1.0`  
**Description**: The scale factor for SVG textures. This controls how the SVG is resized when imported.