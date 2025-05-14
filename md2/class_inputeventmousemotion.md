# InputEventMouseMotion

**Inherits:** InputEventMouse → InputEventWithModifiers → InputEventFromWindow → InputEvent → Resource → RefCounted → Object

Represents mouse or pen movement events.

---

## Description

Tracks mouse/pen motion data including relative/absolute positions and velocity. Use `Node._input()` for handling.

- **Note:** Events are typically emitted once per frame. Set `Input.use_accumulated_input` to false for more frequent updates.
- **Note:** Check `relative.is_zero_approx()` to determine if movement occurred, as events may fire even when no movement happens.

---

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent)
- [Mouse and Coordinates](../tutorials/inputs/mouse_and_input_coordinates)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

---

## Properties

- **pen_inverted** (bool): Default `false`. Indicates stylus eraser use. Available on Linux, macOS, Windows.
- **pressure** (float): Default `0.0`. Pressure applied to pen (0.0–1.0).
- **relative** (Vector2): Default (0, 0). Mouse position relative to previous frame.
- **screen_relative** (Vector2): Default (0, 0). Unscaled relative position in screen coordinates.
- **screen_velocity** (Vector2): Default (0, 0). Unscaled velocity in pixels per second (screen coords).
- **tilt** (Vector2): Default (0, 0). Pen tilt angles (X: right, Y: toward user, -1.0–1.0).
- **velocity** (Vector2): Default (0, 0). Mouse velocity in pixels per second (scaled by content scale).

---

## Notes

- **relative** and **velocity** are scaled by content scale. Use **screen_relative**/**screen_velocity** for unscaled data.
- **screen_relative** and **screen_velocity** are preferred for mouse aiming in `Input.MOUSE_MODE_CAPTURED` mode.
- Check `relative.is_zero_approx()` to confirm actual movement.
- Events may fire without movement. Use timers to detect stop conditions.