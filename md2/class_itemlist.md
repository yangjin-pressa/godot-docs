# ItemList Class Documentation

## Overview
The `ItemList` class is a UI control used to display a list of items. It provides methods for rendering items, handling user input, and customizing visual properties. The class includes theme properties to control the appearance of items, including colors, spacing, fonts, and styles.

---

## Methods

### Base Methods
These methods are part of the base implementation for rendering and input handling. They are typically overridden by subclasses to customize behavior.

- **_base_get_item_rect(index: int) -> Rect2**:  
  Returns the bounding rectangle for the specified item.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: The rectangle coordinates for the item.

- **_base_get_item_text(index: int) -> String**:  
  Returns the text content of the specified item.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: The text string for the item.

- **_base_input(event: InputEvent) -> bool**:  
  Handles user input events (e.g., mouse clicks, keyboard presses).  
  **Parameters**:  
  - `event`: The input event to process.  
  **Return**: `true` if the event was handled, `false` otherwise.

- **_base_item_rect(index: int) -> Rect2**:  
  Returns the rectangle for the specified item, adjusted for UI alignment.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: The adjusted rectangle coordinates.

- **_base_item_text(index: int) -> String**:  
  Returns the text content of the specified item, with possible formatting.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: The formatted text string for the item.

- **_base_item_visible(index: int) -> bool**:  
  Determines if the specified item is currently visible on the screen.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: `true` if the item is visible, `false` otherwise.

- **_base_item_visible_rect(index: int) -> Rect2**:  
  Returns the visible rectangle for the specified item.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: The visible rectangle coordinates.

- **_base_item_visible_rect(index: int) -> Rect2**:  
  (Duplicate method, likely a typo or oversight in the original description.)

---

### Public Methods
These methods are used to interact with the `ItemList` directly.

- **get_item_rect(index: int) -> Rect2**:  
  Returns the rectangle for the specified item.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: The rectangle coordinates.

- **get_item_text(index: int) -> String**:  
  Returns the text content of the specified item.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: The text string for the item.

- **get_item_visible(index: int) -> bool**:  
  Determines if the specified item is currently visible.  
  **Parameters**:  
  - `index`: The index of the item in the list.  
  **Return**: `true` if the item is visible, `false` otherwise.

---

## Theme Properties

### Colors
- **font_color**:  
  The default color of the item's text.  
  **Default**: `Color(0.7, 0.7, 0.7, 1)`

- **font_hovered_color**:  
  The color of the text when the item is hovered but not selected.  
  **Default**: `Color(0.95, 0.95, 0.95, 1)`

- **font_hovered_selected_color**:  
  The color of the text when the item is hovered and selected.  
  **Default**: `Color(1, 1, 1, 1)`

- **font_outline_color**:  
  The color of the text outline.  
  **Default**: `Color(0, 0, 0, 1)`

- **guide_color**:  
  The color of the guideline line between items.  
  **Default**: `Color(0.7, 0.7, 0.7, 0.25)`

---

### Constants
- **h_separation**:  
  Horizontal spacing between items.  
  **Default**: `4`

- **icon_margin**:  
  Spacing between the item's icon and text.  
  **Default**: `4`

- **line_separation**:  
  Vertical spacing between lines of text.  
  **Default**: `2`

- **v_separation**:  
  Vertical spacing between items.  
  **Default**: `4`

---

### Styles
- **cursor**:  
  The style for the cursor when the `ItemList` is being focused.  
  **Default**: Default cursor style.

- **cursor_unfocused**:  
  The style for the cursor when the `ItemList` is not focused.  
  **Default**: Default cursor style.

- **focus**:  
  The style for the focused state of the `ItemList`.  
  **Default**: Default focus style.

- **hovered**:  
  The style for items when hovered but not selected.  
  **Default**: Default hovered style.

- **hovered_selected**:  
  The style for items when hovered and selected (non-focused).  
  **Default**: Default hovered-selected style.

- **hovered_selected_focus**:  
  The style for items when hovered and selected (focused).  
  **Default**: Default hovered-selected focus style.

- **panel**:  
  The background style for the `ItemList`.  
  **Default**: Default panel style.

- **selected**:  
  The style for selected items (non-focused).  
  **Default**: Default selected style.

- **selected_focus**:  
  The style for selected items (focused).  
  **Default**: Default selected focus style.

---

## Notes and Warnings

- **Outline Size and MSDF Settings**:  
  If using a font with `FontFile.multichannel_signed_distance_field` enabled, set `FontFile.msdf_pixel_range` to at least twice the value of `outline_size` to avoid rendering artifacts.

- **Theme Customization**:  
  Modify theme properties (e.g., colors, spacing) to customize the appearance of the `ItemList` for your project.

- **Override Base Methods**:  
  Override base methods like `_base_get_item_rect` and `_base_input` in subclasses to implement custom behavior for item rendering and user interaction.

---

This documentation provides a comprehensive guide to using and customizing the `ItemList` class in Godot, covering both its core functionality and visual properties.