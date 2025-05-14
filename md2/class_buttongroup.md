# ButtonGroup

**Inherits:** Resource < RefCounted < Object  
A group of buttons that doesn't allow more than one button to be pressed at a time.

## Description
- A group of BaseButton-derived buttons
- Buttons are treated like radio buttons: only one can be pressed at a time
- Buttons with special appearance when in this state
- All members must have toggle_mode set to true

## Properties
- **allow_unpress**: false (bool)  
  If true, allows unpressing all buttons in the group
- **resource_local_to_scene**: true (bool)  
  Overrides Resource's resource_local_to_scene property

## Methods
- **get_buttons()** → Array[BaseButton]  
  Returns array of buttons in this group
- **get_pressed_button()** → BaseButton  
  Returns the currently pressed button

## Signals
- **pressed(button: BaseButton)**  
  Emitted when a button in the group is pressed

## Property Descriptions
- **allow_unpress** (bool)  
  Controls whether all buttons can be unpressed

## Method Descriptions
- **get_buttons()**  
  Returns array of buttons associated with this group
- **get_pressed_button()**  
  Returns the currently pressed button in the group