The `NativeMenu` class in Godot is used to create and manage native-style menus for different platforms (such as macOS, Windows, etc.). Below is a structured guide on how to use it effectively, including key methods and their purposes:

---

### **1. Basic Structure and Initialization**
- **Create a NativeMenu instance**:
  ```gdscript
  var menu = NativeMenu.new()
  ```

- **Set the minimum width** (platform-specific for macOS):
  ```gdscript
  menu.set_minimum_width(200)
  ```

---

### **2. Adding Items and Submenus**
- **Add a basic item**:
  ```gdscript
  menu.add_item("File")
  ```

- **Add a multistate item** (e.g., for dropdowns with multiple states):
  ```gdscript
  menu.add_multistate_item("State 1", "State 2", "State 3")
  ```

- **Add a submenu**:
  ```gdscript
  var submenu = NativeMenu.new()
  submenu.add_item("Submenu Item")
  menu.set_item_submenu(menu.get_item_index("File"), submenu.rid)
  ```

- **Add an item with a tooltip** (macOS only):
  ```gdscript
  menu.set_item_tooltip(menu.get_item_index("File"), "Click to open")
  ```

- **Add an item with an icon**:
  ```gdscript
  var icon = Texture2D.new()
  icon.load_file("res://icon.png")
  menu.set_item_icon(menu.get_item_index("File"), icon)
  ```

---

### **3. Setting Item Properties**
- **Set item text**:
  ```gdscript
  menu.set_item_text(menu.get_item_index("File"), "New File")
  ```

- **Set item tag** (for metadata):
  ```gdscript
  menu.set_item_tag(menu.get_item_index("File"), "file_action")
  ```

- **Set item indentation level** (macOS only):
  ```gdscript
  menu.set_item_indentation_level(menu.get_item_index("File"), 1)
  ```

- **Set item state** (for multistate items):
  ```gdscript
  menu.set_item_state(menu.get_item_index("State 1"), 1)
  ```

- **Set item max states** (for multistate items):
  ```gdscript
  menu.set_item_max_states(menu.get_item_index("State 1"), 3)
  ```

---

### **4. Handling Callbacks**
- **Set callback for item clicks**:
  ```gdscript
  menu.set_item_callback(menu.get_item_index("File"), func() -> {
      print("File menu clicked!")
  })
  ```

- **Set callback for accelerator activation** (macOS only):
  ```gdscript
  menu.set_item_key_callback(menu.get_item_index("File"), func() -> {
      print("Accelerator triggered!")
  })
  ```

- **Set callback for hover events** (macOS only):
  ```gdscript
  menu.set_item_hover_callback(menu.get_item_index("File"), func() -> {
      print("Item hovered!")
  })
  ```

- **Set menu open/close callbacks**:
  ```gdscript
  menu.set_popup_open_callback(func() -> {
      print("Menu opened!")
  })
  menu.set_popup_close_callback(func() -> {
      print("Menu closed!")
  })
  ```

---

### **5. Managing Menu State**
- **Check if the menu is opened**:
  ```gdscript
  if menu.is_opened():
      print("Menu is currently open.")
  ```

- **Check if an item is a submenu**:
  ```gdscript
  if menu.is_submenu(menu.get_item_index("File")):
      print("This item has a submenu.")
  ```

---

### **6. Displaying the Menu**
- **Show the menu**:
  ```gdscript
  menu.popup(global_position)
  ```

  - `global_position`: The screen coordinates where the menu should appear.

---

### **7. Platform-Specific Notes**
- **macOS**:
  - Tooltips, indentation, and some callbacks are supported.
  - Dock menu items behave differently and may not support all methods (e.g., `set_item_icon`).

- **Windows/Linux**:
  - Basic functionality is supported, but some methods (like tooltip setting) may not work.

---

### **8. Example Usage**
```gdscript
var menu = NativeMenu.new()
menu.add_item("File")
menu.add_item("Edit")
menu.add_item("Help")

# Set item text
menu.set_item_text(0, "New File")
menu.set_item_text(1, "Cut")
menu.set_item_text(2, "About")

# Set item callbacks
menu.set_item_callback(0, func() -> {
    print("New File clicked!")
})
menu.set_item_callback(1, func() -> {
    print("Cut clicked!")
})

# Set menu open/close callbacks
menu.set_popup_open_callback(func() -> {
    print("Menu opened!")
})
menu.set_popup_close_callback(func() -> {
    print("Menu closed!")
})

# Show the menu
menu.popup(Vector2(100, 100))
```

---

### **Key Considerations**
- **Platform Compatibility**: Use `set_item_tooltip`, `set_item_indentation_level`, and others only where supported.
- **State Management**: Use `is_opened()` to track menu state and avoid redundant operations.
- **Callbacks**: Connect callbacks to handle user interactions (e.g., item clicks, accelerator keys).

By leveraging these methods, you can create rich, platform-specific menus that integrate seamlessly with the native UI of the target OS.