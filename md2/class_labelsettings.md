# LabelSettings Class Documentation

A class representing settings for rendering text labels, including font, color, size, and various stacked outlines/shadows.

## Properties

### font
- **Type:** `Font`
- **Description:** The font used for rendering the label text.

### color
- **Type:** `Color`
- **Description:** The base color of the label text.

### size
- **Type:** `int`
- **Description:** The font size for the label text.

### stacked_outline_count
- **Type:** `int`
- **Description:** The number of stacked outlines. This property indicates how many outlines are currently configured.
- **Note:** This is read-only. Use `set_stacked_outline_count` to modify the number of outlines.

### stacked_shadow_count
- **Type:** `int`
- **Description:** The number of stacked shadows. This property indicates how many shadows are currently configured.
- **Note:** This is read-only. Use `set_stacked_shadow_count` to modify the number of shadows.

---

## Methods

### add_stacked_outline(index=-1)
- **Type:** `void`
- **Description:** Adds a new stacked outline to the label. If `index` is -1, the outline is added at the end of the list.
- **Parameters:**
  - `index` (optional): The index at which to insert the new outline. Default is -1 (append to the end).

### add_stacked_shadow(index=-1)
- **Type:** `void`
- **Description:** Adds a new stacked shadow to the label. If `index` is -1, the shadow is added at the end of the list.
- **Parameters:**
  - `index` (optional): The index at which to insert the new shadow. Default is -1 (append to the end).

### get_stacked_outline_color(index)
- **Type:** `Color`
- **Description:** Returns the color of the stacked outline at the specified index.
- **Parameters:**
  - `index`: The index of the outline.
- **Returns:** The color of the outline at the given index.

### get_stacked_outline_size(index)
- **Type:** `int`
- **Description:** Returns the size of the stacked outline at the specified index.
- **Parameters:**
  - `index`: The index of the outline.
- **Returns:** The size of the outline at the given index.

### get_stacked_shadow_color(index)
- **Type:** `Color`
- **Description:** Returns the color of the stacked shadow at the specified index.
- **Parameters:**
  - `index`: The index of the shadow.
- **Returns:** The color of the shadow at the given index.

### get_stacked_shadow_offset(index)
- **Type:** `Vector2`
- **Description:** Returns the offset of the stacked shadow at the specified index.
- **Parameters:**
  - `index`: The index of the shadow.
- **Returns:** The offset vector for the shadow at the given index.

### get_stacked_shadow_outline_size(index)
- **Type:** `int`
- **Description:** Returns the outline size of the stacked shadow at the specified index.
- **Parameters:**
  - `index`: The index of the shadow.
- **Returns:** The outline size of the shadow at the given index.

### move_stacked_outline(from_index, to_position)
- **Type:** `void`
- **Description:** Moves the stacked outline at `from_index` to the position `to_position` in the list.
- **Parameters:**
  - `from_index`: The index of the outline to move.
  - `to_position`: The new position in the list.

### move_stacked_shadow(from_index, to_position)
- **Type:** `void`
- **Description:** Moves the stacked shadow at `from_index` to the position `to_position` in the list.
- **Parameters:**
  - `from_index`: The index of the shadow to move.
  - `to_position`: The new position in the list.

### remove_stacked_outline(index)
- **Type:** `void`
- **Description:** Removes the stacked outline at the specified index.
- **Parameters:**
  - `index`: The index of the outline to remove.

### remove_stacked_shadow(index)
- **Type:** `void`
- **Description:** Removes the stacked shadow at the specified index.
- **Parameters:**
  - `index`: The index of the shadow to remove.

### set_stacked_outline_color(index, color)
- **Type:** `void`
- **Description:** Sets the color of the stacked outline at the specified index.
- **Parameters:**
  - `index`: The index of the outline.
  - `color`: The new color for the outline.

### set_stacked_outline_size(index, size)
- **Type:** `void`
- **Description:** Sets the size of the stacked outline at the specified index.
- **Parameters:**
  - `index`: The index of the outline.
  - `size`: The new size for the outline.

### set_stacked_shadow_color(index, color)
- **Type:** `void`
- **Description:** Sets the color of the stacked shadow at the specified index.
- **Parameters:**
  - `index`: The index of the shadow.
  - `color`: The new color for the shadow.

### set_stacked_shadow_offset(index, offset)
- **Type:** `void`
- **Description:** Sets the offset of the stacked shadow at the specified index.
- **Parameters:**
  - `index`: The index of the shadow.
  - `offset`: The new offset vector for the shadow.

### set_stacked_shadow_outline_size(index, size)
- **Type:** `void`
- **Description:** Sets the outline size of the stacked shadow at the specified index.
- **Parameters:**
  - `index`: The index of the shadow.
  - `size`: The new outline size for the shadow.

---

## Notes

- **Virtual Methods:** Methods like `add_stacked_outline` and `add_stacked_shadow` are virtual, meaning they can be overridden by subclasses to customize behavior.
- **Const Methods:** Methods like `get_stacked_outline_color` are const, indicating they do not modify the object's state.
- **Stacked Outlines/Shadows:** These are layered effects that can be individually configured (color, size, offset) and managed in a list.