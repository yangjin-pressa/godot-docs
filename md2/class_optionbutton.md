# OptionButton Class Documentation

## Signals

### `item_pressed`
Triggered when an item is pressed (clicked) in the dropdown menu.
- **Parameters**: `idx` (int) - The index of the pressed item.

### `item_selected`
Triggered when an item is selected (focused) in the dropdown menu.
- **Parameters**: `idx` (int) - The index of the selected item.

---

## Properties

### `allow_modulation`
- **Type**: `bool`  
- **Default**: `true`  
- **Description**: If set to `true`, the button will modulate its color based on the theme's font color.

### `arrow_margin`
- **Type**: `int`  
- **Default**: `4`  
- **Description**: The horizontal space between the arrow icon and the right edge of the button.

### `arrow`
- **Type**: `Texture2D`  
- **Description**: The arrow icon to be drawn on the right end of the button.

### `modulate_arrow`
- **Type**: `int`  
- **Default**: `0`  
- **Description**: If set to a non-zero value, the arrow icon will be modulated to the font color.

---

## Methods

### `get_item_text(idx)`
- **Description**: Retrieves the text of the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item.
- **Returns**: `String` - The text of the item.

### `get_item_tooltip(idx)`
- **Description**: Retrieves the tooltip text of the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item.
- **Returns**: `String` - The tooltip text of the item.

### `get_selected_id()`
- **Description**: Retrieves the ID of the currently selected item.
- **Returns**: `int` - The ID of the selected item, or `-1` if none is selected.

### `get_selected_metadata()`
- **Description**: Retrieves the metadata of the currently selected item.
- **Returns**: `Variant` - The metadata of the selected item.

### `get_selected_metadata()`
- **Description**: Retrieves the metadata of the currently selected item.
- **Returns**: `Variant` - The metadata of the selected item.

### `get_item_metadata(idx)`
- **Description**: Retrieves the metadata of the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item.
- **Returns**: `Variant` - The metadata of the item.

### `is_item_disabled(idx)`
- **Description**: Checks if the item at the specified index is disabled.
- **Parameters**: `idx` (int) - Index of the item.
- **Returns**: `bool` - `true` if the item is disabled, `false` otherwise.

### `is_item_separator(idx)`
- **Description**: Checks if the item at the specified index is a separator.
- **Parameters**: `idx` (int) - Index of the item.
- **Returns**: `bool` - `true` if the item is a separator, `false` otherwise.

### `has_selectable_items()`
- **Description**: Checks if the button contains at least one selectable item (not disabled or a separator).
- **Returns**: `bool` - `true` if there are selectable items, `false` otherwise.

### `get_selected_id()`
- **Description**: Retrieves the ID of the currently selected item.
- **Returns**: `int` - The ID of the selected item, or `-1` if none is selected.

### `set_item_disabled(idx, disabled)`
- **Description**: Sets whether the item at the specified index is disabled.
- **Parameters**: `idx` (int) - Index of the item; `disabled` (bool) - Whether to disable the item.
- **Note**: Disabled items are not selectable by the user.

### `set_item_text(idx, text)`
- **Description**: Sets the text of the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item; `text` (String) - New text for the item.

### `set_item_tooltip(idx, tooltip)`
- **Description**: Sets the tooltip text of the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item; `tooltip` (String) - New tooltip text.

### `set_item_metadata(idx, metadata)`
- **Description**: Sets the metadata of the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item; `metadata` (Variant) - New metadata.

### `show_popup()`
- **Description**: Displays the popup menu and adjusts its position and size.
- **Note**: Prefer this method over `get_popup().popup()` for better control.

### `select(idx)`
- **Description**: Selects an item by index. If `-1`, the currently selected item is deselected.
- **Parameters**: `idx` (int) - Index of the item to select.

### `remove_item(idx)`
- **Description**: Removes the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item to remove.

### `set_disable_shortcuts(disabled)`
- **Description**: Disables or enables shortcuts for triggering the button.
- **Parameters**: `disabled` (bool) - Whether to disable shortcuts.

### `set_item_auto_translate_mode(idx, mode)`
- **Description**: Sets the auto-translate mode for the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item; `mode` (AutoTranslateMode) - Auto-translate mode.

### `set_item_icon(idx, texture)`
- **Description**: Sets the icon for the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item; `texture` (Texture2D) - New icon.

### `set_item_id(idx, id)`
- **Description**: Sets the ID of the item at the specified index.
- **Parameters**: `idx` (int) - Index of the item; `id` (int) - New ID.

---

## Theme Properties

### `arrow_margin`
- **Description**: The horizontal space between the arrow icon and the right edge of the button.

### `modulate_arrow`
- **Description**: If non-zero, the arrow icon is modulated to the font color.

### `arrow`
- **Description**: The arrow icon to be drawn on the right end of the button.

---

## Notes

- **Item Pressed vs. Selected**: `item_pressed` is triggered on click, while `item_selected` is for focus.
- **Disabled Items**: Items with `is_item_disabled(true)` are not selectable.
- **Popup Management**: Use `show_popup()` for controlled popup display.