# InputEventMouse

**Inherits**: InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object

**Inherited By**: InputEventMouseButton, InputEventMouseMotion

## Description
Stores general information about mouse events.

## Tutorials
- [Using InputEvent](../tutorials/inputs/inputevent)

## Properties
- **button_mask**: BitField of MouseButtonMask, default 0  
- **global_position**: Vector2, default (0, 0)  
- **position**: Vector2, default (0, 0)  

## Property Descriptions
### button_mask
- **set_button_mask**: void (value: BitField of MouseButtonMask)  
- **get_button_mask**: BitField of MouseButtonMask  
- **Description**: Mouse button mask identifier, one of or a bitwise combination of the MouseButton button masks.

### global_position
- **set_global_position**: void (value: Vector2)  
- **get_global_position**: Vector2  
- **Description**: When received in Node._input() or Node._unhandled_input(), returns the mouse's position in the root Viewport. When received in Control._gui_input(), returns the mouse's position in the CanvasLayer.

### position
- **set_position**: void (value: Vector2)  
- **get_position**: Vector2  
- **Description**: When received in Node._input() or Node._unhandled_input(), returns the mouse's position in the Viewport. When received in Control._gui_input(), returns the mouse's position in the Control using the local coordinate system.

## Notes
- Methods like `set_global_position` and `get_global_position` are used to manipulate the mouse position data.  
- The `button_mask` property uses a bitmask to represent mouse button states.