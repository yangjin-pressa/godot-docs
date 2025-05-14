# InputEventFromWindow

## Inheritance Hierarchy
- **InputEventFromWindow**  
  ← [InputEvent](class_InputEvent)  
  ← [Resource](class_Resource)  
  ← [RefCounted](class_RefCounted)  
  ← [Object](class_Object)

## Inherited By
- [InputEventScreenDrag](class_InputEventScreenDrag)  
- [InputEventScreenTouch](class_InputEventScreenTouch)  
- [InputEventWithModifiers](class_InputEventWithModifiers)  

## Description
Abstract base class for input events tied to windows. Represents mouse, keyboard, or touch events received by windows.

## Properties
- **window_id**: `int` (default: 0)  
  - The ID of the [Window](class_Window) that received this event.

## Method Definitions
- `void set_window_id(int value)`  
- `int get_window_id()`  

## Key Notes
- This class serves as a foundation for events related to viewports and windows.  
- The `window_id` property identifies the specific window associated with the event.