# InputEventWithModifiers

**Inherits:** `InputEventFromWindow` < `InputEvent` < `Resource` < `RefCounted` < `Object`  
**Inherited By:** `InputEventGesture`, `InputEventKey`, `InputEventMouse`  

Abstract base class for input events affected by modifier keys like Shift and Alt.

## Description
Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such as Shift or Alt. See `Node._input()`.

**Note:** Modifier keys are considered modifiers only when used in combination with another key. As a result, their corresponding member variables, such as `ctrl_pressed`, will return `false` if the key is pressed on its own.

## Tutorials
- [Using InputEvent](../tutorials/inputs/inputevent)

## Properties
- `alt_pressed` = `false`  
  State of the Alt modifier.  
- `command_or_control_autoremap` = `false`  
  Automatically use Meta (Cmd) on macOS and Ctrl on other platforms. If `true`, `ctrl_pressed` and `meta_pressed` cannot be set.  
- `ctrl_pressed` = `false`  
  State of the Ctrl modifier.  
- `meta_pressed` = `false`  
  State of the Meta modifier. On Windows/Linux, this represents the Windows key. On macOS, this represents the Command key.  
- `shift_pressed` = `false`  
  State of the Shift modifier.  

## Methods
- `get_modifiers_mask()`  
  Returns the keycode combination of modifier keys.  
- `is_command_or_control_pressed()`  
  On macOS, returns `true` if Meta (Cmd) is pressed. On other platforms, returns `true` if Ctrl is pressed.  

## Notes
- Modifier keys (Shift, Ctrl, Alt) are only effective when combined with other keys.  
- `command_or_control_autoremap` determines whether Meta/Ctrl is used based on the platform.