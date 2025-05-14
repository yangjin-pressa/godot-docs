# LineEdit Class Guide

## Methods

### Basic Text Manipulation
- **`get_text()`** → `String`  
  Returns the current text content of the LineEdit.

- **`set_text(text: String)`**  
  Sets the text content of the LineEdit.  
  *Parameters:*  
  - `text`: The new text to display.

- **`clear()`**  
  Removes all text from the LineEdit.

- **`insert_text(text: String, position: int = -1)`**  
  Inserts text at a specified position. If `position` is -1, the text is appended.  
  *Parameters:*  
  - `text`: The text to insert.  
  - `position`: The index at which to insert the text (default: end of the text).

- **`delete_text(start: int, end: int)`**  
  Deletes text between the specified start and end indices.  
  *Parameters:*  
  - `start`: The starting index of the text to delete.  
  - `end`: The ending index of the text to delete.

### Focus and Navigation
- **`get_caret_position()`** → `int`  
  Returns the current position of the text cursor.

- **`set_caret_position(position: int)`**  
  Sets the position of the text cursor.  
  *Parameters:*  
  - `position`: The index at which to place the cursor.

- **`has_focus()`** → `bool`  
  Returns whether the LineEdit currently has focus.

- **`set_editable(value: bool)`**  
  Enables or disables text editing.  
  *Parameters:*  
  - `value`: `true` to allow editing, `false` to disable.

- **`set_placeholder_text(text: String)`**  
  Sets the placeholder text displayed when the LineEdit is empty.  
  *Parameters:*  
  - `text`: The placeholder text.

- **`get_placeholder_text()`** → `String`  
  Returns the current placeholder text.

### Input Handling
- **`_input(event: InputEvent)`**  
  Handles input events (e.g., keyboard, mouse) for the LineEdit.  
  *Parameters:*  
  - `event`: The input event to process.

### Internal Methods
- **`_get_text()`**  
  Virtual method to retrieve text content (overrides default behavior).  
  *Note:* This should be overridden by subclasses if custom text handling is needed.

- **`_set_text(text: String)`**  
  Virtual method to set text content (overrides default behavior).  
  *Note:* This should be overridden by subclasses if custom text handling is needed.

---

## Theme Properties

### Visual Properties
- **`caret_color`** → `Color`  
  Color of the text cursor. Default: `Color(0.95, 0.95, 0.95, 1)`.  
  *Tip:* Use a transparent color to hide the caret entirely.

- **`font_color`** → `Color`  
  Default font color. Default: `Color(0.875, 0.875, 0.875, 1)`.

- **`font_outline_color`** → `Color`  
  Color of the text outline. Default: `Color(0, 0, 0, 1)`.

- **`font_placeholder_color`** → `Color`  
  Color for placeholder text. Default: `Color(0.875, 0.875, 0.875, 0.6)`.

- **`font_selected_color`** → `Color`  
  Color for selected text. Default: `Color(1, 1, 1, 1)`.

- **`font_uneditable_color`** → `Color`  
  Color when editing is disabled. Default: `Color(0.875, 0.875, 0.875, 0.5)`.

- **`selection_color`** → `Color`  
  Color of the selection rectangle. Default: `Color(0.5, 0.5, 0.5, 1)`.

### Layout and Styling
- **`caret_width`** → `int`  
  Width of the caret in pixels. Default: `1`.  
  *Tip:* Increase this for better visibility with larger fonts.

- **`minimum_character_width`** → `int`  
  Minimum horizontal space for text (in 'M' character counts). Default: `4`.

- **`outline_size`** → `int`  
  Size of the text outline. Default: `0`.  
  *Note:* If using MSDF fonts, ensure `outline_size` is half the MSDF pixel range for correct rendering.

- **`font`** → `Font`  
  Font used for text. Default: system font.

- **`font_size`** → `int`  
  Font size. Default: `16` (depends on theme).

### UI Elements
- **`clear_button_color`** → `Color`  
  Default tint for the clear button. Default: `Color(0.875, 0.875, 0.875, 1)`.

- **`clear_button_color_pressed`** → `Color`  
  Color when the clear button is pressed. Default: `Color(1, 1, 1, 1)`.

- **`clear`** → `Texture2D`  
  Texture for the clear button. Only visible if `clear_button_enabled` is `true`.

### Background and Focus
- **`normal`** → `StyleBox`  
  Default background.  
- **`focus`** → `StyleBox`  
  Background when focused. Use a semi-transparent style for better visibility.  
- **`read_only`** → `StyleBox`  
  Background when in read-only mode.

---

## Remarks

### Accessibility
- **Focus Visuals:** The `focus` style should be visible but not distracting. Use outlines or underlines for better keyboard navigation.
- **Caret Visibility:** Ensure `caret_color` is contrastive with the background. Avoid fully transparent colors for screen readers.

### Performance
- **Text Manipulation:** Frequent insert/delete operations may impact performance. Use batch updates where possible.
- **Outline Rendering:** For MSDF fonts, set `outline_size` and `msdf_pixel_range` appropriately to avoid cutoff artifacts.

### Customization
- **Clear Button:** Disable it via `clear_button_enabled` if not needed. Customize its appearance with `clear` and theme colors.
- **Placeholder Text:** Use `placeholder_text` to indicate empty state, which is hidden when text is entered.

This guide covers all methods, properties, and theme-related settings for the LineEdit class, ensuring flexibility and accessibility in UI design.