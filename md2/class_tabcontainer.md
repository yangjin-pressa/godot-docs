# TabContainer Help File

## Overview
The `TabContainer` class in Godot is a container that manages multiple tabs, each of which can be a node. It provides a way to dynamically add, remove, and navigate between tabs, with customizable appearance through themes and properties. This class is particularly useful for UI interfaces that require a tab-based layout.

---

## Properties

### `tab_alignment`
- **Description:** Determines the horizontal alignment of the tabs within the container.
- **Options:** `TabBar.ALIGNMENT_LEFT`, `TabBar.ALIGNMENT_CENTER`, `TabBar.ALIGNMENT_RIGHT`.
- **Note:** The alignment affects the side margin and the positioning of the tabs.

### `clip_tabs`
- **Description:** Controls whether tabs are clipped when the container's width is insufficient to display all tabs.
- **Type:** `bool`
- **Default:** `false`

### `drag_to_rearrange_enabled`
- **Description:** Enables or disables the ability to rearrange tabs by dragging them.
- **Type:** `bool`
- **Default:** `true`

### `side_margin`
- **Description:** The space at the left or right edges of the tab bar, depending on the alignment.
- **Type:** `int`
- **Default:** `8`

### `tab_separation`
- **Description:** The space between individual tabs in the tab bar.
- **Type:** `int`
- **Default:** `0`

---

## Methods

### `add_tab(name: String, content: Node) -> int`
- **Description:** Adds a new tab to the container.
- **Parameters:**
  - `name`: The name of the tab (used for identification).
  - `content`: The node to be displayed in the tab.
- **Returns:** The index of the newly added tab.

### `remove_tab(index: int) -> void`
- **Description:** Removes a tab by its index.
- **Parameters:**
  - `index`: The index of the tab to be removed.

### `select_tab(index: int) -> void`
- **Description:** Selects a specific tab to bring it to the front.
- **Parameters:**
  - `index`: The index of the tab to be selected.

### `get_tab_count() -> int`
- **Description:** Returns the total number of tabs currently in the container.

### `get_tab(index: int) -> Node`
- **Description:** Returns the node associated with the specified tab index.

### `get_tab_name(index: int) -> String`
- **Description:** Returns the name of the tab at the specified index.

---

## Themes

The `TabContainer` supports various themes to customize its appearance:

### Icon Themes
- **`decrement`**: Icon for the left arrow button when there are too many tabs.
- **`decrement_highlight`**: Icon for the left arrow button when hovered.
- **`increment`**: Icon for the right arrow button when there are too many tabs.
- **`increment_highlight`**: Icon for the right arrow button when hovered.
- **`drop_mark`**: Icon indicating where a dragged tab will be dropped.
- **`menu`**: Icon for the menu button (when a popup is set).
- **`menu_highlight`**: Icon for the menu button when hovered.

### Style Themes
- **`panel`**: Background style for the entire container.
- **`tab_disabled`**: Style for disabled tabs.
- **`tab_focus`**: Style for the focused tab (overrides the base style).
- **`tab_hovered`**: Style for tabs when hovered.
- **`tab_selected`**: Style for the currently selected tab.
- **`tab_unselected`**: Style for unselected tabs.
- **`tabbar_background`**: Background style for the tab bar area.

### Font and Size
- **`font`**: Font used for tab labels.
- **`font_size`**: Font size for tab labels.

---

## Important Notes

1. **Focus Style:** The `tab_focus` style is displayed over the base style of the selected tab. Use a partially transparent style (e.g., an outline or underline) to ensure the base style remains visible. Avoid using `StyleBoxEmpty` for focus if keyboard/controller navigation is required.

2. **Margin Considerations:** The `side_margin` is ignored if the tabs are clipped (`clip_tabs = true`) or a popup is set (`set_popup()`). It is always ignored if the alignment is `TabBar.ALIGNMENT_CENTER`.

3. **Outline Rendering:** If using a font with MSDF support, set the `msdf_pixel_range` to at least twice the `outline_size` for correct outline rendering.

4. **Drag Rearrangement:** The `drag_to_rearrange_enabled` property controls whether tabs can be reordered by dragging. This is useful for dynamic UIs requiring tab reordering.

---

## Example Usage
```gdscript
# Create a new TabContainer
var tab_container = TabContainer.new()

# Add a tab
var tab1 = TabContainer.new()
tab1.add_child(Panel.new())
tab_container.add_tab("Tab 1", tab1)

# Add another tab
var tab2 = TabContainer.new()
tab2.add_child(Label.new("Second Tab"))
tab_container.add_tab("Tab 2", tab2)

# Select the second tab
tab_container.select_tab(1)
```

This example demonstrates creating a `TabContainer`, adding two tabs, and selecting the second one. Adjust the `tab_alignment`, `clip_tabs`, or other properties as needed for your UI layout.