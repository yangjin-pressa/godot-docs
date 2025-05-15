The `TabBar` class in Godot is a container for managing multiple tabs, allowing users to navigate between them. Below is a detailed breakdown of its core functionality, methods, properties, and key considerations:

---

### **Core Functionality**
- **Tabs as Items**: Each tab is a visual element that can be interacted with (e.g., clicked, focused, or closed). 
- **Navigation**: Supports keyboard/controller input for tab switching and scrollable arrow buttons when tabs exceed the container width.
- **Customization**: Highly customizable via themes, icons, and styles for different states (hovered, selected, disabled, etc.).

---

### **Key Methods**
1. **`_notification`**  
   - **Purpose**: Handles internal notifications (e.g., when the node is added/removed from the scene).  
   - **Use Case**: Not typically overridden by users but essential for internal logic.

2. **`_draw`**  
   - **Purpose**: Renders the tab bar and its elements (tabs, arrows, close buttons).  
   - **Use Case**: Internal rendering logic; users typically do not modify this.

3. **`_input`**  
   - **Purpose**: Processes input events (e.g., mouse clicks, keyboard navigation).  
   - **Use Case**: Manages tab selection, closing, and scroll navigation.

4. **`_update`**  
   - **Purpose**: Updates the tab bar's state (e.g., recalculates tab positions).  
   - **Use Case**: Ensures tabs are correctly positioned and visible.

5. **`_add_tab`**  
   - **Purpose**: Adds a new tab to the tab bar.  
   - **Parameters**: The tab node (e.g., a `Label` or custom node).  
   - **Note**: The tab is automatically added to the UI, but its content is managed externally.

6. **`_remove_tab`**  
   - **Purpose**: Removes a tab from the tab bar.  
   - **Parameters**: The tab node or its index.  
   - **Note**: Ensures the tab is no longer displayed or interacted with.

7. **`_move_tab`**  
   - **Purpose**: Rearranges tabs in the tab bar.  
   - **Parameters**: The tab node or index, and the new position.  
   - **Use Case**: Useful for reordering tabs via drag-and-drop or keyboard navigation.

8. **`_on_tab_close`**  
   - **Purpose**: Handles the action when a tab is closed.  
   - **Use Case**: Triggers a callback or removes the tab from the container.

9. **`_on_tab_selected`**  
   - **Purpose**: Handles the action when a tab is selected.  
   - **Use Case**: Updates the UI or triggers a callback for the selected tab.

---

### **Key Properties**
1. **`tab_close_display_policy`**  
   - **Purpose**: Controls when close buttons are displayed (e.g., always, only on hover, etc.).  
   - **Common Values**:  
     - `TAB_CLOSE_DISPLAY_ALWAYS`: Show close buttons on all tabs.  
     - `TAB_CLOSE_DISPLAY_ON_HOVER`: Only show when the tab is hovered.  
     - `TAB_CLOSE_DISPLAY_NEVER`: Hide close buttons entirely.

2. **`drag_to_rearrange_enabled`**  
   - **Purpose**: Enables drag-and-drop reordering of tabs.  
   - **Use Case**: Allows users to rearrange tabs visually.

3. **`tab_separation`**  
   - **Purpose**: Defines the space between tabs.  
   - **Note**: Affects layout and spacing when tabs are displayed.

4. **`h_separation`**  
   - **Purpose**: Horizontal separation between elements inside tabs (e.g., labels, icons).  
   - **Use Case**: Customizes tab content spacing.

5. **`outline_size`**  
   - **Purpose**: Controls the size of text outlines for tabs.  
   - **Note**: Relevant for stylized text (e.g., outlines or shadows).

6. **`font` and `font_size`**  
   - **Purpose**: Define the font and size used for tab labels.  
   - **Use Case**: Customize the appearance of tab text.

7. **`tab_close`**  
   - **Purpose**: The icon for the close button.  
   - **Use Case**: Replace the default close icon with a custom texture.

8. **`decrement` / `increment`**  
   - **Purpose**: Icons for scroll buttons (left/right arrows) when tabs overflow.  
   - **Use Case**: Customize scroll navigation visuals.

---

### **Theming and Styles**
- **StyleBox Properties**:  
  - **`tab_hovered`**: Style for hovered tabs (e.g., highlight color).  
  - **`tab_selected`**: Style for the currently selected tab.  
  - **`tab_unselected`**: Style for non-selected tabs.  
  - **`tab_disabled`**: Style for disabled tabs (e.g., grayed-out appearance).  
  - **`button_highlight` / `button_pressed`**: Styles for tab and close buttons when hovered/pressed.  

- **Icons**:  
  - **`drop_mark`**: Icon for drag-and-drop indicators.  
  - **`decrement_highlight` / `increment_highlight`**: Hover states for scroll buttons.  

- **Focus Style**:  
  - **`tab_focus`**: Visual effect when the tab bar is focused (e.g., a border or underline).  
  - **Note**: Use `StyleBoxEmpty` to disable focus visuals, but this may impair keyboard navigation.

---

### **Best Practices**
- **Keyboard Navigation**: Ensure `tab_focus` is properly configured for accessibility.  
- **Tab Overflow**: Use `decrement` and `increment` buttons when tabs exceed the container width.  
- **Close Buttons**: Avoid using `tab_close_display_policy = TAB_CLOSE_DISPLAY_NEVER` if users might want to close tabs.  
- **Themes**: Override `font`, `outline_size`, and `tab_separation` to unify tab appearance across the UI.  
- **Drag-and-Drop**: Enable `drag_to_rearrange_enabled` for flexible tab ordering.  

---

### **Example Use Case**
```gdscript
# Create a tab bar
var tab_bar = TabBar.new()
tab_bar.add_tab(Label.new("Tab 1"))
tab_bar.add_tab(Label.new("Tab 2"))
tab_bar.tab_close_display_policy = TAB_CLOSE_DISPLAY_ALWAYS
tab_bar.drag_to_rearrange_enabled = true
```

This example creates a tab bar with two tabs, enables close buttons, and allows reordering via dragging.

---

### **Common Pitfalls**
- **Incorrect Tab Spacing**: Misconfigured `tab_separation` or `h_separation` can cause tabs to overlap or leave too much empty space.  
- **Overriding Render Methods**: Modifying `_draw` or `_input` without understanding their internal logic can break the tab bar's functionality.  
- **Focus Visuals**: Disabling `tab_focus` may make the tab bar inaccessible via keyboard.  

By understanding these components, you can effectively design a tab bar that is both functional and visually cohesive.