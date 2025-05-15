# Sprite3D Class Overview

## Inheritance Hierarchy
- `Sprite3D`  
  ← `SpriteBase3D`  
  ← `GeometryInstance3D`  
  ← `VisualInstance3D`  
  ← `Node3D`  
  ← `Node`  
  ← `Object`

## Description
A 3D node that displays 2D textures. Supports atlas textures or sprite sheet animations. See `SpriteBase3D` for shared properties like billboard mode.

## Properties
- **frame**: `int` (default: 0)  
- **frame_coords**: `Vector2i` (default: (0,0))  
- **hframes**: `int` (default: 1)  
- **region_enabled**: `bool` (default: false)  
- **region_rect**: `Rect2` (default: (0,0,0,0))  
- **texture**: `Texture2D`  
- **vframes**: `int` (default: 1)

## Signals
- **frame_changed()**: Emitted when `frame` changes.  
- **texture_changed()**: Emitted when `texture` changes.

## Property Details
- **frame**  
  - Set/Get: `set_frame(value: int)`, `get_frame()`  
  - Displays a frame from a sprite sheet. Adjusts automatically when `hframes`/`vframes` change. Defaults to 0 if adjustment fails.

- **frame_coords**  
  - Set/Get: `set_frame_coords(value: Vector2i)`, `get_frame_coords()`  
  - Coordinates for the frame. `hframes`/`vframes` must be > 1.

- **hframes**  
  - Set/Get: `set_hframes(value: int)`, `get_hframes()`  
  - Number of columns in the sprite sheet. Adjusts `frame` to maintain visual alignment.

- **region_enabled**  
  - Set/Get: `set_region_enabled(value: bool)`, `is_region_enabled()`  
  - Enables use of `region_rect` for texture clipping.

- **region_rect**  
  - Set/Get: `set_region_rect(value: Rect2)`, `get_region_rect()`  
  - Texture region to display. Requires `region_enabled` to be true.

- **texture**  
  - Set/Get: `set_texture(value: Texture2D)`, `get_texture()`  
  - Texture to draw. Overrides if `GeometryInstance3D.material_override` is set.

- **vframes**  
  - Set/Get: `set_vframes(value: int)`, `get_vframes()`  
  - Number of rows in the sprite sheet. Adjusts `frame` to maintain visual alignment.