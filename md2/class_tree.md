# TreeTheme Class Documentation

## Overview
The `TreeTheme` class defines the visual theme for a `Tree` node in Godot. It provides properties to customize the appearance of various elements such as icons, styles, spacing, and scroll behavior. This class is typically used in conjunction with the `Tree` class to create custom tree views in Godot projects.

---

## Properties

### General Properties

- **`scroll`**: `Vector2` (const)  
  The scroll offset for the tree. This property is used to determine the position of the scrollbars and is read-only.

---

### Icons

- **`arrow_cur`**: `Texture` (virtual)  
  The arrow icon used for the current node in a tree. Override this to customize the current node arrow appearance.

- **`arrow_first`**: `Texture` (virtual)  
  The arrow icon used for the first node in a tree. Override this to customize the first node arrow appearance.

- **`arrow_last`**: `Texture` (virtual)  
  The arrow icon used for the last node in a tree. Override this to customize the last node arrow appearance.

- **`arrow_parent`**: `Texture` (virtual)  
  The arrow icon used for the parent node in a tree. Override this to customize the parent node arrow appearance.

- **`arrow_right`**: `Texture` (virtual)  
  The arrow icon used for the right node in a tree. Override this to customize the right node arrow appearance.

- **`arrow_updown`**: `Texture` (virtual)  
  The up/down arrow icon used for the range mode cell. Override this to customize the range mode arrow appearance.

- **`checked`**: `Texture` (virtual)  
  The checked icon used for the check mode cell. Override this to customize the checked state appearance.

- **`checkbox`**: `Texture` (virtual)  
  The checkbox icon used for the checkbox mode cell. Override this to customize the checkbox appearance.

- **`custom`**: `Texture` (virtual)  
  The custom icon used for the custom mode cell. Override this to customize the custom mode icon.

- **`unchecked`**: `Texture` (virtual)  
  The unchecked icon used for the check mode cell. Override this to customize the unchecked state appearance.

- **`updown`**: `Texture` (virtual)  
  The up/down arrow icon used for the range mode cell. Override this to customize the range mode arrow appearance.

- **`updown_selected`**: `Texture` (virtual)  
  The up/down arrow icon used for the range mode cell when selected. Override this to customize the selected range mode arrow appearance.

---

### Styles

- **`button_hover`**: `StyleBox` (virtual)  
  The style box used when a button in the tree is hovered. Override this to customize button hover appearance.

- **`button_pressed`**: `StyleBox` (virtual)  
  The style box used when a button in the tree is pressed. Override this to customize button pressed appearance.

- **`button_focus`**: `StyleBox` (virtual)  
  The style box used when a button in the tree is focused. Override this to customize button focus appearance.

- **`cursor`**: `StyleBox` (virtual)  
  The style box used for the cursor when the tree is being focused. Override this to customize cursor appearance.

- **`cursor_unfocused`**: `Style-than` (virtual)  
  The style box used for the cursor when the tree is not being focused. Override this to customize unfocused cursor appearance.

- **`focus`**: `StyleBox` (virtual)  
  The focused style for the tree, drawn on top of everything. Override this to customize the focused tree appearance.

- **`hovered`**: `StyleBox` (virtual)  
  The style box for the item being hovered but not selected. Override this to customize hover appearance.

- **`hovered_dimmed`**: `StyleBox` (virtual)  
  The style box for the item being hovered while a button of the same item is hovered. Override this to customize dimmed hover appearance.

- **`hovered_selected`**: `StyleBox` (virtual)  
  The style box for the hovered and selected items when the tree is not focused. Override this to customize selected hover appearance.

- **`hovered_selected_focus`**: `StyleBox` (virtual)  
  The style box for the hovered and selected items when the tree is focused. Override this to customize focused selected hover appearance.

- **`panel`**: `StyleBox` (virtual)  
  The background style for the tree. Override this to customize the tree panel appearance.

- **`selected`**: `StyleBox` (virtual)  
  The style box for the selected items when the tree is not focused. Override this to customize selected item appearance.

- **`selected_focus`**: `StyleBox` (virtual)  
  The style box for the selected items when the tree is focused. Override this to customize focused selected item appearance.

- **`title_button_hover`**: `StyleBox` (virtual)  
  The style box used when the title button is hovered. Override this to customize title button hover appearance.

- **`title_button_normal`**: `StyleBox` (virtual)  
  The default style box for the title button. Override this to customize title button normal appearance.

- **`title_button_pressed`**: `StyleBox` (virtual)  
  The style box used when the title button is pressed. Override this to customize title button pressed appearance.

- **`custom_button`**: `StyleBox` (virtual)  
  The default style box for a custom mode cell when the button is enabled. Override this to customize custom button appearance.

- **`custom_button_hover`**: `StyleBox` (virtual)  
  The style box for a custom mode button cell when it's hovered. Override this to customize custom button hover appearance.

- **`custom_button_pressed`**: `Style_one` (virtual)  
  The style box for a custom mode button cell when it's pressed. Override this to customize custom button pressed appearance.

---

### Spacing and Layout

- **`border`**: `Vector4` (virtual)  
  The border size for the tree. Override this to customize the tree border.

- **`spacing`**: `Vector2` (virtual)  
  The spacing between tree nodes. Override this to customize the spacing between nodes.

- **`spacing_left`**: `float` (virtual)  
  The left spacing for the tree. Override this to customize the left spacing.

- **`spacing_right`**: `float` (virtual)  
  The right spacing for the tree. Override this to customize the right spacing.

- **`spacing_top`**: `float` (virtual)  
  The top spacing for the tree. Override this to customize the top spacing.

- **`spacing_bottom`**: `float` (virtual)  
  The bottom spacing for the tree. Override this to customize the bottom spacing.

- **`padding`**: `Vector4` (virtual)  
  The padding for the tree. Override this to customize the padding.

---

### Scroll Settings

- **`scroll_offset`**: `Vector2` (const)  
  The scroll offset for the tree. This property is read-only and represents the current scroll position.

- **`scroll_moved`**: `bool` (const)  
  Whether the scroll has been moved. This property is read-only and indicates if the scroll position has changed.

---

### Mode-Specific Properties

- **`arrow_cur`**: `Texture` (virtual)  
  The arrow icon for the current node. Override this to customize the current node arrow.

- **`arrow_first`**: `Texture` (virtual)  
  The arrow icon for the first node. Override this to customize the first node arrow.

- **`arrow_last`**: `Texture` (virtual)  
  The arrow icon for the last node. Override this to customize the last node arrow.

- **`arrow_parent`**: `Texture` (virtual)  
  The arrow icon for the parent node. Override this to customize the parent node arrow.

- **`arrow_right`**: `Texture` (virtual)  
  The arrow icon for the right node. Override this to customize the right node arrow.

- **`arrow_updown`**: `Texture` (virtual)  
  The up/down arrow icon for the range mode. Override this to customize the range mode arrow.

- **`checked`**: `Texture` (virtual)  
  The checked icon for the check mode. Override this to customize the checked state.

- **`checkbox`**: `Texture` (virtual)  
  The checkbox icon for the checkbox mode. Override this to customize the checkbox.

- **`custom`**: `Texture` (virtual)  
  The custom icon for the custom mode. Override this to customize the custom mode icon.

- **`unchecked`**: `Texture` (virtual)  
  The unchecked icon for the check mode. Override this to customize the unchecked state.

- **`updown_selected`**: `Texture` (virtual)  
  The up/down arrow icon for the range mode when selected. Override this to customize the selected range mode arrow.

---

## Notes

- **Virtual Properties**: Properties marked as `virtual` can be overridden in custom themes to change the appearance of the tree.
- **Const Properties**: Properties marked as `const` are read-only and should not be modified after the theme is initialized.
- **Tree Theme Usage**: This class is used in conjunction with the `Tree` class to define the visual theme for tree nodes in Godot projects. Customize these properties to achieve the desired UI appearance.