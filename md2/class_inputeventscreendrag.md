# InputEventScreenDrag

**Inherits:** InputEventFromWindow → InputEvent → Resource → RefCounted → Object

## Description
Represents a screen drag event. See Node._input() method.

## Tutorials
- Using InputEvent

## Properties
- **index**: int = 0  
  Drag event index in multi-drag events
- **pen_inverted**: bool = false  
  Returns true when using eraser end of stylus pen
- **position**: Vector2(0, 0)  
  Drag position in viewport coordinates
- **pressure**: float = 0.0  
  Pressure on pen (0.0-1.0 range)
- **relative**: Vector2(0, 0)  
  Drag position relative to previous frame
- **screen_relative**: Vector2(0, 0)  
  Unscaled drag position relative to previous frame
- **screen_velocity**: Vector2(0, 0)  
  Unscaled drag velocity in pixels/second
- **tilt**: Vector2(0, 0)  
  Pen tilt angles (-1.0-1.0 range)
- **velocity**: Vector2(0, 0)  
  Drag velocity (scaled by content scale factor)

## Property Methods
- **set_index(value: int)**: void
- **get_index()**: int
- **set_pen_inverted(value: bool)**: void
- **get_pen_inverted()**: bool
- **set_position(value: Vector2)**: void
- **get_position()**: Vector2
- **set_pressure(value: float)**: void
- **get_pressure()**: float
- **set_relative(value: Vector2)**: void
- **get_relative()**: Vector2
- **set_screen_relative(value: Vector2)**: void
- **get_screen_relative()**: Vector2
- **set_screen_velocity(value: Vector2)**: void
- **get_screen_velocity()**: Vector2
- **set_tilt(value: Vector2)**: void
- **get_tilt()**: Vector2
- **set_velocity(value: Vector2)**: void
- **get_velocity()**: Vector2

## Notes
- relative/velocity values are automatically scaled by content scale factor
- Use screen_relative/screen_velocity for consistent touch aiming across resolutions
- tilt values: positive X = right tilt, positive Y = toward user