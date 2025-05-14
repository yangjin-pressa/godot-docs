# AcceptDialog Class Documentation

## Overview
The `AcceptDialog` class is a specialized `Window` used to display prompts or messages to the user, often with buttons for interaction. It allows for custom button configurations and supports signals for user actions like confirmation or cancellation.

---

## Properties

### `dialog_autowrap` (bool)
- **Description**: Controls whether the text in the dialog wraps to the next line if it exceeds the available width.
- **Default**: `true`
- **Note**: This property is inherited from the `Window` class.

### `dialog_text` (String)
- **Description**: The text displayed in the dialog.
- **Default**: `""`
- **Getter/Setter**: `set_text()` and `get_text()`

### `ok_button_text` (String)
- **Description**: The text displayed on the OK button. If empty, a default text is used.
- **Default**: `""`
- **Getter/Setter**: `set_ok_button_text()` and `get_ok_button_text()`

### `ok_button` (Button)
- **Description**: The OK button instance. This is an internal node and should not be removed or freed directly.
- **Warning**: Use `CanvasItem.visible` to hide the button or its children.

---

## Methods

### `add_button(text: String, right: bool = false, action: String = "")` → Button
- **Description**: Adds a custom button to the dialog. The `action` is passed to the `custom_action` signal when the button is pressed.
- **Parameters**:
  - `text`: The button label.
  - `right`: If `true`, the button is placed to the right of sibling buttons.
  - `action`: The action associated with the button.
- **Returns**: The created `Button` instance.
- **Note**: Use `remove_button()` to remove this button.

### `add_cancel_button(name: String)` → Button
- **Description**: Adds a cancel button with the specified label. The button emits the `canceled` signal when pressed.
- **Parameters**:
  - `name`: The button label.
- **Returns**: The created `Button` instance.
- **Note**: Use `remove_button()` to remove this button.

### `get_label()` → Label
- **Description**: Returns the internal `Label` node used for the dialog's text.
- **Warning**: This is a required internal node. Do not remove or free it directly. Use `CanvasItem.visible` to hide it.

### `get_ok_button()` → Button
- **Description**: Returns the OK button instance.
- **Warning**: This is a required internal node. Do not remove or free it directly. Use `CanvasItem.visible` to hide it.

### `register_text_enter(line_edit: LineEdit)`
- **Description**: Registers a `LineEdit` so that pressing the enter key accepts the dialog.
- **Parameters**:
  - `line_edit`: The `LineEdit` node to register.

### `remove_button(button: Button)`
- **Description**: Removes the specified button from the dialog. The button is not freed.
- **Note**: The button must have been added via `add_button()` or `add_cancel_button()`.
- **Note**: After removal, pressing the button no longer triggers signals.

---

## Theme Properties

### `buttons_min_height` (int)
- **Description**: Minimum height of buttons in the bottom row (e.g., OK/Cancel).
- **Default**: `0`
- **Note**: Increases this value to make buttons easier to click/tap.

### `buttons_min_width` (int)
- **Description**: Minimum width of buttons in the bottom row.
- **Default**: `0`
- **Note**: Increases this value to make buttons easier to click/tap.

### `buttons_separation` (int)
- **Description**: Vertical space between the dialog content and the button row.
- **Default**: `10`

### `panel` (StyleBox)
- **Description**: The background panel style for the dialog window.
- **Note**: This is a required internal node. Do not remove or free it directly.

---

## Signals

- **`confirmed`**: Emitted when the OK button is pressed or when the enter key is pressed in a `LineEdit`.
- **`canceled`**: Emitted when the cancel button is pressed.

---

## Notes

1. **Internal Nodes**: Nodes like `get_label()` and `get_ok_button()` are required internal nodes. Removing or freeing them may cause a crash. Use `CanvasItem.visible` to hide them.
2. **Custom Buttons**: Buttons added via `add_button()` or `add_cancel_button()` are part of the dialog's UI. They emit `custom_action` or `canceled` signals upon interaction.
3. **Text Wrapping**: The `dialog_autowrap` property controls text wrapping, which is useful for long messages.
4. **Enter Key Handling**: The `register_text_enter()` method allows associating a `LineEdit` with accepting the dialog on enter press.

---

This class provides flexibility for custom dialog interactions while maintaining compatibility with Godot's UI system. Use it for prompts, confirmations, or input validation scenarios.