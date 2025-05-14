# Parallax2D

**Inherits:** Node2D < CanvasItem < Node < Object

A node used to create a parallax scrolling background.

## Description
A Parallax2D is used to create a parallax effect. It can move at a different speed relative to the camera movement using scroll_scale. This creates an illusion of depth in a 2D game. If manual scrolling is desired, the Camera2D position can be ignored with ignore_camera_scroll.

## Tutorials
- 2D Parallax (https://godotengine.org/documentation/.../tutorials/2d/2d_parallax)

## Properties
- autoscroll: Vector2(0, 0) - Velocity for automatic offset scrolling
- follow_viewport: true - Offset by camera position
- ignore_camera_scroll: false - Prevent position from being affected by camera
- limit_begin: Vector2(-1e+07, -1e+07) - Scroll start limits
- limit_end: Vector2(1e+07, 1e+07) - Scroll end limits
- physics_interpolation_mode: 2 (overrides Node physics interpolation)
- repeat_size: Vector2(0, 0) - Texture repeat offset
- repeat_times: 1 - Texture repetition count
- screen_offset: Vector2(0, 0) - Scroll offset value
- scroll_offset: Vector2(0, 0) - Node position offset
- scroll_scale: Vector2(1, 1) - Scroll speed multiplier

## Property Descriptions
**scroll_scale**  
Multiplier to the final Parallax2D's offset.  
- 1: Same speed as camera  
- >1: Faster (closer objects)  
- <1: Slower (further objects)  
- 0: No movement

**repeat_size**  
Repeats Texture2D of children and offsets them.  
- Values > screen size create infinite scrolling effect  
- Axis set to 0: no repeat on that axis

**repeat_times**  
Overrides texture repetition count.  
- Each copy spreads evenly from original by repeat_size

**screen_offset**  
Offset used to scroll this Parallax2D.  
- Automatically updated unless ignore_camera_scroll is true

**scroll_offset**  
Parallax2D's offset.  
- Not overridden by other settings  
- Values loop if repeat_size > 0

**ignore_camera_scroll**  
Prevents position from being affected by camera.  
- Values will loop if repeat_size > 0

**follow_viewport**  
Adjusts node position based on camera position.  
- Default: true

**limit_begin/limit_end**  
Defines scroll boundaries.  
- Values determine scroll range

**autoscroll**  
Controls automatic offset scrolling speed.  
- Default: (0, 0)

**physics_interpolation_mode**  
Overrides Node2D's physics interpolation settings.  
- Default: 2 (custom value)

Note: scroll_offset is not overridden by other settings.