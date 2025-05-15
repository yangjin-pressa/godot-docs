# TextEdit Class Documentation

## Overview
The `TextEdit` class in Godot is a versatile UI component for handling text input and display. It supports various properties for text formatting, editing, and styling, and provides methods for handling input events and text manipulation.

---

## Properties

### `editable` (bool)
**Description:** Determines whether the text can be edited by the user. When set to `false`, the text becomes read-only.

### `placeholder_text` (String)
**Description:** Text displayed in the edit area when no text is present. Useful for hints or instructions.

### `font` (Font)
**Description:** The default font used for rendering text. Can be customized to change the appearance.

### `font_size` (int)
**Description:** Sets the default font size. Adjusts the size of the text displayed in the TextEdit.

### `caret_width` (int)
**Description:** The width of the text cursor (caret) in pixels. A value of `0` or lower will automatically adjust the width based on the display scaling factor.

### `line_spacing` (int)
**Description:** Additional vertical spacing between lines (in pixels). Spacing is added to line descent. Can be negative.

### `outline_size` (int)
**Description:** The size of the text outline. If using a font with MSDF enabled, ensure the pixel range is twice the outline size to avoid rendering issues.

### `highlight_all_occurrences` (bool)
**Description:** When enabled, multiple occurrences of a word or text are highlighted. Requires `word_highlighted_color` to be set.

### `word_highlighted_color` (Color)
**Description:** The color used to highlight multiple occurrences of a word or text. Set to `Color(0, 0, 0, 0)` to disable highlighting.

---

## Methods

### `_process(delta)`
**Description:** A virtual method called every frame. Used for real-time text processing, such as updating the UI or handling animations.

### `_input(event)`
**Description:** A virtual method handling input events (e.g., key presses, mouse movements). Override this to customize behavior for specific input types.

### `_notification(int)`
**Description:** A virtual method called when the node receives a notification (e.g., `NOTIFICATION_ENTER_TREE`). Override this to perform setup or initialization.

### `select_all()`
**Description:** Selects all text in the TextEdit. Useful for copying or editing the entire content.

### `select_range(int start, int end)`
**Description:** Selects a specific range of text. `start` and `end` are indices within the text.

### `insert_text(String text)`
**Description:** Inserts text at the current cursor position. Useful for dynamic content insertion.

### `remove_text(int start, int end)`
**Description:** Removes text between the given indices. Useful for editing or deleting specific parts of the text.

### `get_text()`
**Description:** Returns the current text content of the TextEdit.

### `get_selection_start()`
**Description:** Returns the starting index of the currently selected text.

### `get_selection_end()`
**Description:** Returns the ending index of the currently selected text.

### `set_editable(bool editable)`
**Description:** Sets whether the TextEdit is editable. Overrides the `editable` property.

---

## Themed Constants

### `caret_width` (int)
**Description:** Width of the caret in pixels. Default: `1`.

### `line_spacing` (int)
**Description:** Additional vertical spacing between lines. Default: `4`.

### `outline_size` (int)
**Description:** Size of the text outline. Default: `0`.

### `font` (Font)
**Description:** Default font used for rendering text.

### `font_size` (int)
**Description:** Default font size. Default: `16`.

### `space` (Texture2D)
**Description:** Custom texture for space characters (e.g., " ").

### `tab` (Texture2D)
**Description:** Custom texture for tab characters.

### `focus` (StyleBox)
**Description:** Style box applied when the TextEdit is in focus.

### `normal` (StyleBox)
**Description:** Style box applied when the TextEdit is not focused.

### `read_only` (StyleBox)
**Description:** Style box applied when the text is read-only.

### `background` (Color)
**Description:** Background color of the TextEdit.

### `text_color` (Color)
**Description:** Default text color.

### `selected_text_color` (Color)
**Description:** Color of selected text.

### `search_result_border_color` (Color)
**Description:** Border color for search results.

### `search_result_text_color` (Color)
**Description:** Text color for search results.

### `caret_color` (Color)
**Description:** Color of the caret (cursor).

---

## Important Notes
- **Accessibility:** The `caret_width` and `font_size` properties affect readability. Ensure values are suitable for all users.
- **Performance:** Overriding `_process` or `_input` can impact performance. Use efficiently.
- **MSDF Fonts:** If using MSDF fonts, ensure the `outline_size` is compatible with the `pixel_range` of the font to avoid rendering artifacts.

---

## Signals
The `TextEdit` class emits the following signals:
- `text_changed`: Triggered when the text changes.
- `selection_changed`: Triggered when the selected text range changes.
- `cursor_position_changed`: Triggered when the cursor position changes.

---

This documentation covers the core functionality and properties of the `TextEdit` class, ensuring developers can customize and utilize it effectively for text input and display in Godot projects.