# Texture2D Class Documentation

The `Texture2D` class in Godot is a fundamental resource for handling 2D textures. It provides methods to draw textures, retrieve their dimensions, and check for alpha channels. This class is used extensively in 2D graphics and is the base for many derived texture types.

---

## Overview

The `Texture2D` class represents a 2D texture that can be used for rendering in 2D games. It supports operations such as drawing textures, querying dimensions, and checking for alpha channels. This class is typically used in conjunction with the `CanvasItem` class for rendering.

---

## Key Methods

### Public Methods

#### `draw(canvas_item: RID, position: Vector2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false) -> void`
Draws the texture using the `CanvasItem` API with the `RenderingServer`.

**Parameters:**
- `canvas_item`: The `CanvasItem` to draw the texture onto.
- `position`: The position on the screen where the texture is drawn.
- `modulate`: A color multiplier for the texture (default is fully opaque white).
- `transpose`: Whether to transpose the texture (default is false).

**Note:** This method is used for rendering and should be called via the `RenderingServer` API.

---

#### `draw_rect(canvas_item: RID, rect: Rect2, tile: bool = false, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false) -> void`
Draws a rectangular portion of the texture onto a `CanvasItem`.

**Parameters:**
- `canvas_item`: The `CanvasItem` to draw the texture onto.
- `rect`: The rectangle on the screen where the texture is drawn.
- `tile`: Whether to tile the texture (default is false).
- `modulate`: A color multiplier for the texture (default is fully opaque white).
- `transpose`: Whether to transpose the texture (default is false).

**Note:** This method is used for rendering and should be called via the `RenderingServer` API.

---

#### `draw_rect_region(canvas_item: RID, rect: Rect2, src_rect: Rect2, modulate: Color = Color(1, 1, 1, 1), transpose: bool = false, clip_uv: bool = true) -> void`
Draws a specific region of the texture onto a `CanvasItem`.

**Parameters:**
- `canvas_item`: The `CanvasItem` to draw the texture onto.
- `rect`: The rectangle on the screen where the texture is drawn.
- `src_rect`: The region of the texture to draw.
- `modulate`: A color multiplier for the texture (default is fully opaque white).
- `transpose`: Whether to transpose the texture (default is false).
- `clip_uv`: Whether to clip the UV coordinates (default is true).

**Note:** This method is used for rendering and should be called via the `RenderingServer` API.

---

#### `get_height() -> int`
Returns the height of the texture in pixels.

**Note:** This method is used to query the dimensions of the texture.

---

#### `get_image() -> Image`
Returns an `Image` that is a copy of the texture data. A new `Image` is created each time this method is called.

**Note:** This method fetches texture data from the GPU, which can be performance-intensive. Avoid calling this frequently on large textures.

---

#### `get_size() -> Vector2`
Returns the dimensions of the texture as a `Vector2` (width and height).

---

#### `get_width() -> int`
Returns the width of the texture in pixels.

---

#### `has_alpha() -> bool`
Returns `true` if the texture has an alpha channel.

**Note:** This method delegates to the private `_has_alpha()` method.

---

### Private Methods

#### `_get_height() -> int`
Called when the height of the texture is queried.

**Note:** This method is intended for internal use by subclasses.

---

#### `_get_width() -> int`
Called when the width of the texture is queried.

**Note:** This method is intended for internal use by subclasses.

---

#### `_has_alpha() -> bool`
Called when checking if the texture has an alpha channel.

**Note:** This method is intended for internal use by subclasses.

---

#### `_is_pixel_opaque(x: int, y: int) -> bool`
Called when checking if a specific pixel is opaque.

**Note:** This method is intended for internal use by subclasses.

---

## Creating a Placeholder

#### `create_placeholder() -> Resource`
Creates a placeholder version of this texture, typically a `PlaceholderTexture2D`.

**Use Case:** Useful for UI or during texture loading when a real texture is not yet available.

---

## Notes

- **Performance:** The `get_image()` method can be slow due to GPU data fetching. Avoid using it in performance-critical sections.
- **Transposing:** The `transpose` parameter is used for rotating the texture, which is useful for certain visual effects.
- **Alpha Channel:** The presence of an alpha channel affects how the texture is rendered, especially in transparent or semi-transparent effects.

---

## Inheritance

The `Texture2D` class is the base for many derived texture types, including `PlaceholderTexture2D`, `Texture2DArray`, and `TextureRectangle`.

---

## Example Usage

```gdscript
var texture = Texture2D.new()
texture.create_placeholder() # Creates a placeholder texture

var image = texture.get_image() # Fetches texture data as an Image

texture.draw_rect(canvas_item, Rect2(0, 0, 100, 100), modulate=Color(1, 0, 0, 0.5)) # Draws a red semi-transparent rectangle
```

---

This documentation provides a comprehensive overview of the `Texture2D` class, its methods, and usage patterns. Developers should refer to this guide when working with texture rendering and manipulation in Godot.