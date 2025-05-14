# InputEventMouseButton

**Inherits:** InputEventMouse → InputEventWithModifiers → InputEventFromWindow → InputEvent → Resource → RefCounted → Object

## Description
Represents a mouse button being pressed or released. See Node._input().

**Note:** On Wear OS devices, rotary input is mapped to MOUSE_BUTTON_WHEEL_UP and MOUSE_BUTTON_WHEEL_DOWN. This can be changed via ProjectSettings.input_devices/pointing/android/rotary_input_scroll_axis.

## Tutorials
- Using InputEvent
- Mouse and input coordinates

## Properties
- **button_index**: MouseButton = 0
- **canceled**: bool = false
- **double_click**: bool = false
- **factor**: float = 1.0
- **pressed**: bool = false

## Property Descriptions
**button_index**  
- Type: MouseButton  
- Default: 0  
- Description: Mouse button identifier (one of MouseButton constants).

**canceled**  
- Type: bool  
- Default: false  
- Description: If true, the event is canceled.

**double_click**  
- Type: bool  
- Default: false  
- Description: If true, the event is a double-click.

**factor**  
- Type: float  
- Default: 1.0  
- Description: Event delta (scroll amount). May be 0 if unsupported.

**pressed**  
- Type: bool  
- Default: false  
- Description: If true, the mouse button is pressed. If false, it's released.

## Method Definitions
- **set_button_index(value: MouseButton)**  
- **get_button_index()**  
- **set_canceled(value: bool)**  
- **is_canceled()**  
- **set_double_click(value: bool)**  
- **is_double_click()**  
- **set_factor(value: float)**  
- **get_factor()**  
- **set_pressed(value: bool)**  
- **is_pressed()**