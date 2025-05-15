# SpriteBase3D Class Description

The `SpriteBase3D` class serves as a 3D sprite node in Godot, allowing for the rendering of 2D images in 3D space. It combines the functionality of a 2D sprite with 3D positioning and rendering properties, making it suitable for UI elements, icons, or other 2D content in 3D scenes.

## Key Properties

### Rendering and Visibility
- **transparent**: `bool` (default: `true`)  
  Determines if the sprite's transparency is used to hide parts of the sprite.  
- **no_depth_test**: `bool` (default: `false`)  
  Disables depth testing, allowing the sprite to be drawn in render order regardless of depth.  
- **shaded**: `bool` (default: `false`)  
  Enables lighting effects from the environment's `Light3D` on the sprite.  
- **render_priority**: `int` (default: `0`)  
  Sets the render priority for sorting transparent objects. Higher values render in front of lower ones.  
  **Note**: Only affects transparent objects; opaque objects are not sorted.

### Texture and Filtering
- **texture_filter**: `int` (default: `3`)  
  Controls texture filtering options (e.g., nearest neighbor, linear).  
  **Note**: Linear filtering may cause artifacts on opaque textures.  
- **alpha_cut**: `int` (default: `ALPHA_CUT_DISABLED`)  
  Determines how the sprite handles transparency. Options include disabling alpha cut, using alpha for cutting, or using a threshold.  
- **pixel_size**: `float` (default: `0.01`)  
  Defines the size of one pixel in 3D space for scaling the sprite.  
- **texture_filter**: `int` (default: `3`)  
  Filter flags for the texture (see `TextureFilter` enum for options).

### Positioning and Offset
- **offset**: `Vector2` (default: `(0, 0)`)  
  Offset for the sprite's texture drawing.  
- **axis**: `int` (default: `0`)  
  Determines the sprite's rotation axis (0 for Z, 1 for Y, 2 for X).  

### Color and Modulation
- **modulate**: `Color` (default: `(1, 1, 1, 1)`)  
  Applies a color multiplier to the sprite. Values above `1` are not supported.  
  **Note**: For material overrides, ensure the material uses vertex colors for albedo.  
- **render_priority**: `int` (default: `0`)  
  Same as above, see note for transparency sorting.

---

## Methods

### `generate_triangle_mesh()`
- **Returns**: `TriangleMesh`  
  Creates a `TriangleMesh` object representing the sprite's current configuration (e.g., axis, pixel size).  
  **Use Case**: For custom mesh generation based on sprite settings.

### `get_draw_flag(flag: DrawFlags) -> bool`
- **Returns**: `bool`  
  Checks the state of a specific render flag (e.g., `NO_DEPTH_TEST`, `SHADOW_CASTING_ENABLE`).  
  **Use Case**: To query if a specific render property is enabled.

### `get_item_rect() -> Rect2`
- **Returns**: `Rect2`  
  Returns the bounding rectangle of the sprite in 2D space.  
  **Use Case**: For determining the sprite's dimensions in 2D coordinates.

### `set_draw_flag(flag: DrawFlags, enabled: bool)`
- **Sets**: A render flag (e.g., `NO_DEPTH_TEST`, `SHADOW_CASTING_ENABLE`) to `true` or `false`.  
  **Use Case**: To enable or disable specific rendering behaviors.

---

## Notes
- **Transparent Handling**: The `transparent` property and `render_priority` work together to control how transparent objects are sorted.  
- **Alpha Cut**: The `alpha_cut` property determines how the sprite interacts with other objects based on transparency.  
- **Modulate Limitations**: Colors with values above `1.0` are not supported in the `modulate` property.  
- **Mesh Generation**: `generate_triangle_mesh()` is useful for creating custom meshes based on the sprite's current parameters.

This class provides a flexible foundation for rendering 2D content in 3D environments, with precise control over rendering properties, texture behavior, and positioning.