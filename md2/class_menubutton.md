# MenuButton

**Inherits:** Button → BaseButton → Control → CanvasItem → Node → Object

## Description
A button that brings up a PopMenu when clicked. To create new items, use `get_popup().add_item("My Item Name")`. See also BaseButton.

## Properties
- **action_mode**: ActionMode (0)  
- **flat**: bool (true)  
- **focus_mode**: FocusMode (3)  
- **item_count**: int (0)  
- **switch_on_hover**: bool (false)  
- **toggle_mode**: bool (true)  

## Methods
- **get_popup()** → PopMenu (Returns the PopMenu contained in this button)  
- **set_disable_shortcuts(disabled: bool)** (Disables shortcuts)  
- **show_popup()** (Shows the PopMenu after adjusting position)  

## Signals
- **about_to_popup()** (Emitted when the PopMenu is about to show)  

## Property Descriptions
### item_count
- **Type**: int (0)  
- **Set**: `set_item_count(value: int)`  
- **Get**: `get_item_count()`  
- **Description**: Number of items in the list.

### switch_on_hover
- **Type**: bool (false)  
- **Set**: `set_switch_on_hover(value: bool)`  
- **Get**: `is_switch_on_hover()`  
- **Description**: Closes current PopMenu when hovering over another MenuButton with this property enabled.

## Notes
- `get_popup()` is an internal node; do not remove or free it. Use `Window.visible` to hide elements.  
- `show_popup()` is preferred over `get_popup().popup()`.