# ParallaxBackground

**Deprecated:** Use the `Parallax2D` node instead.

**Inherits:** CanvasLayer → Node → Object

A node used to create a parallax scrolling background.

## Description
Uses `ParallaxLayer` child nodes to create a parallax effect. Each layer moves at a different speed, creating depth. Requires a `Camera2D` for automatic scrolling, or manual calculation of `scroll_offset`.

**Note:** Each ParallaxBackground is tied to a specific Viewport. For split-screen games, create a separate instance per Viewport.

## Properties

- **scroll_base_offset** (Vector2): Base position offset for all layers. Default: Vector2(0, 0)
- **scroll_base_scale** (Vector2): Base motion scale. Default: Vector2(1, 1)
- **scroll_ignore_camera_zoom** (bool): If true, layers aren't affected by camera zoom. Default: false
- **scroll_limit_begin** (Vector2): Top-left scroll limit. Default: Vector2(0, 0)
- **scroll_limit_end** (Vector2): Bottom-right scroll limit. Default: Vector2(0, 0)
- **scroll_offset** (Vector2): Scroll value. Default: Vector2(0, 0)

## Property Descriptions

**scroll_base_offset**  
The base position offset for all ParallaxLayer children.

**scroll_base_scale**  
The base motion scale for all ParallaxLayer children.

**scroll_ignore_camera_zoom**  
If true, elements in ParallaxLayer child aren't affected by the zoom level of the camera.

**scroll_limit_begin**  
Top-left limits for scrolling to begin. If the camera is outside of this limit, the background will stop scrolling. Must be lower than scroll_limit_end.

**scroll_limit_end**  
Bottom-right limits for scrolling to end. If the camera is outside of this limit, the background will stop scrolling. Must be higher than scroll_limit_begin.

**scroll_offset**  
The ParallaxBackground's scroll value. Calculated automatically when using a Camera2D, but can be used to manually manage scrolling when no camera is present.

## Methods

- `set_scroll_base_offset(value: Vector2)`  
- `get_scroll_base_offset()`  

- `set_scroll_base_scale(value: Vector2)`  
- `get_scroll_base_scale()`  

- `set_ignore_camera_zoom(value: bool)`  
- `is_ignore_camera_zoom()`  

- `set_limit_begin(value: Vector2)`  
- `get_limit_begin()`  

- `set_limit_end(value: Vector2)`  
- `get_limit_end()`  

- `set_scroll_offset(value: Vector2)`  
- `get_scroll_offset()`