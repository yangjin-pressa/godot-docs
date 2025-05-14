# InputEvent Class Documentation

## Overview

The `InputEvent` class serves as the base for all input events in the Godot engine. It provides a common interface for handling user interactions such as keyboard inputs, mouse movements, touch events, and joystick actions. This class is essential for processing input in games and applications, enabling developers to respond to user actions in a structured manner.

Key features of the `InputEvent` class include:
- **Event Type Identification**: Determines the type of input event (keyboard, mouse, joystick, etc.).
- **State Management**: Tracks whether an event is pressed, released, or canceled.
- **Transformation Support**: Allows for coordinate transformations when handling events in different coordinate systems.
- **Echo and Cancellation**: Handles repeated events (echo) and events that are canceled by the system.

---

## Properties

### `device_type`
- **Type**: `int`
- **Description**: Indicates the type of input device that generated the event. Valid values are:
  - `DEVICE_TYPE_KEYBOARD`: Key press or release.
  - `DEVICE_TYPE_JOY`: Joystick input.
  - `DEVICE_TYPE_MOUSE`: Mouse movement or button press.
  - `DEVICE_TYPE_SCREEN`: Touchscreen input.
  - `DEVICE_TYPE_ANY`: A generic device type (e.g., gamepad).

### `is_pressed`
- **Type**: `bool`
- **Description**: Returns `true` if the event is a press (not a release or echo). Not relevant for motion events like `InputEventMouseMotion`.

### `is_released`
- **Type**: `bool`
- **Description**: Returns `true` if the event is a release. Not relevant for motion events.

### `is_canceled`
- **Type**: `bool`
- **Description**: Returns `true` if the event was canceled by the system (e.g., due to user settings or system restrictions).

### `is_echo`
- **Type**: `bool`
- **Description**: Returns `true` if the event is an echo (repeated key press). Relevant only for keyboard events.

---

## Methods

### `is_action_type()`
- **Description**: Returns `true` if this input event's type is compatible with being assigned to an input action (e.g., key, button, or axis events).
- **Use Case**: Used to determine if an event can be mapped to an action in the Godot editor.

### `is_action_pressed(action, allow_echo=false, exact_match=false)`
- **Description**: Returns `true` if the specified action is currently pressed. It considers the action's configuration (e.g., key, button, or axis) rather than the event's state.
- **Parameters**:
  - `action`: The action to check (e.g., `ACTION_MOVE_LEFT`).
  - `allow_echo`: Whether to include echo events (repeated key presses).
  - `exact_match`: Whether to match the action's configuration exactly.
- **Note**: Due to keyboard ghosting, this method may return `false` even if one of the action's keys is pressed.

### `is_action_released(action, exact_match=false)`
- **Description**: Returns `true` if the specified action is released. Not relevant for motion events.
- **Parameters**:
  - `action`: The action to check.
  - `exact_match`: Whether to match the action's configuration exactly.

### `is_action_match(event, exact_match=true)`
- **Description**: Returns `true` if the specified `event` matches this event in terms of configuration (e.g., key, button, or axis) rather than state.
- **Parameters**:
  - `event`: The event to compare against.
  - `exact_match`: Whether to match the event's configuration exactly.
- **Use Case**: Used to check if two events are equivalent in terms of their input source and type.

### `is_match(event, exact_match=true)`
- **Description**: Returns `true` if the specified `event` matches this event in terms of configuration (e.g., key, button, or axis) rather than state.
- **Parameters**:
  - `event`: The event to compare against.
  - `exact_match`: Whether to match the event's configuration exactly.
- **Note**: This method is specific to action events (key, button, axis).

### `xformed_by(xform, local_ofs=Vector2(0, 0))`
- **Description**: Returns a transformed copy of the event, adjusted by the given `xform` (Transform2D) and `local_ofs` (Vector2). Useful for events that require coordinate transformations (e.g., UI events).
- **Parameters**:
  - `xform`: The 2D transformation matrix.
  - `local_ofs`: An offset to apply to the event's position.
- **Use Case**: Transform mouse or touch events to match a different coordinate system.

---

## Constants

### `DEVICE_TYPE_KEYBOARD`
- **Value**: `0`
- **Description**: Indicates the event is from a keyboard.

### `DEVICE_TYPE_JOY`
- **Value**: `1`
- **Description**: Indicates the event is from a joystick.

### `DEVICE_TYPE_MOUSE`
- **Value**: `2`
- **Description**: Indicates the event is from a mouse.

### `DEVICE_TYPE_SCREEN`
- **Value**: `3`
- **Description**: Indicates the event is from a touchscreen.

### `DEVICE_TYPE_ANY`
- **Value**: `4`
- **Description**: Indicates the event is from any device type.

---

## Notes and Considerations

1. **Ghosting**: Keyboard events may generate multiple key presses even when a single key is held down. Use `is_action_pressed` with `allow_echo=false` to avoid unintended triggers.
2. **Cancellation**: Events canceled by the system (e.g., due to user settings) should be ignored to prevent unexpected behavior.
3. **Transformation**: Use `xformed_by` when handling events that need to be adjusted for different coordinate systems (e.g., UI elements).
4. **Echo Events**: Echo events are repeated key presses. Use `is_echo` to distinguish them from single presses.
5. **Action Matching**: `is_action_match` is crucial for determining if two events are equivalent for action mapping purposes.

---

## Example Usage

```gdscript
# Check if a key is pressed
if input_event.is_action_pressed(ACTION_MOVE_LEFT, allow_echo=False):
    print("Left action is pressed.")

# Transform a mouse event
var transformed_event = input_event.xformed_by(Transform2D.IDENTITY, Vector2(100, 100))
```

---

## See Also

- [InputEventMouse](https://docs.godotengine.org/en/stable/classes/class_inputeventmouse.html)
- [InputEventKeyboard](https://docs.godotengine.org/en/stable/classes/class_inputeventkeyboard.html)
- [InputEventJoystick](https://docs.godotengine.org/en/stable/classes/class_inputeventjoystick.html)
- [InputEventScreen](https://docs.godotengine.org/en/stable/classes/class_inputeventscreen.html)