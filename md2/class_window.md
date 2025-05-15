The `Window` class in Godot provides a way to create and manage windows with custom styling, interactivity, and input handling. Below is a structured guide to using the class, its methods, properties, and theme-related settings:

---

### **Key Concepts**
- **Window Management**: Control window visibility, dragging, resizing, and state.
- **User Interaction**: Handle mouse events for dragging and resizing.
- **Text Input**: Enable and position the system's native IME (Input Method Editor).
- **Styling**: Customize the appearance of the window using theme properties.

---

### **Methods**

#### **Window Management**
1. **`show()`**  
   Makes the window visible.  
   ```gdscript
   window.show()
   ```

2. **`hide()`**  
   Hides the window (not explicitly listed in the docs, but implied by `show()`).

3. **`popup()`**  
   Displays the window, similar to `show()`, but may trigger additional logic (e.g., modal dialogs).

4.**`queue_free()`**  
   Frees the window from memory. Ensure a reference is kept to avoid orphaning.

#### **User Interaction**
1. **`start_drag()`**  
   Initiates a drag operation using the current mouse position. Useful for moving the window.  
   ```gdscript
   window.start_drag()
   ```

2. **`start_resize(edge)`**  
   Starts resizing the window. `edge` is an enum specifying the resize edge (e.g., top-right).  
   ```gdscript
   window.start_resize(WindowResizeEdge.EDGE_TOP_RIGHT)
   ```

3. **`set_ime_active(active)`**  
   Enables/disables the system's native IME for text input.  
   ```gdscript
   window.set_ime_active(true)
   ```

4. **`set_ime_position(position)`**  
   Sets the position of the IME editor.  
   ```gdscript
   window.set_ime_position(Vector2(100, 100))
   ```

---

### **Styling and Theme Properties**

#### **Theme Properties**
These define visual aspects of the window. They are typically configured in the Godot editor's **Theme Editor**.

1. **`title_color`**  
   Color of the title text.  
   ```gdscript
   window.title_color = Color(0.875, 0.875, 0.875, 1)
   ```

2. **`title_font`**  
   Font used for the title.  
   ```gdscript
   window.title_font = Font("path/to/font.ttf")
   ```

3. **`title_font_size`**  
   Size of the title font.  
   ```gdscript
   window.title_font_size = 24
   ```

4. **`close_h_offset`**  
   Horizontal offset of the close button.  
   ```gdscript
   window.close_h_offset = 18
   ```

5. **`close_v_offset`**  
   Vertical offset of the close button.  
   ```gdscript
   window.close_v_offset = 24
   ```

6. **`title_outline_modulate`**  
   Color of the title text outline.  
   ```gdscript
   window.title_outline_modulate = Color(0, 0, 0, 1)
   ```

7. **`title_outline_size`**  
   Size of the title outline.  
   ```gdscript
   window.title_outline_size = 2
   ```

8. **`embedded_border`**  
   Background style for embedded windows.  
   ```gdscript
   window.embedded_border = StyleBoxFlat.new()
   ```

---

### **Advanced Settings**
1. **`set_use_font_oversampling(enable)`**  
   Enables font oversampling for better rendering.  
   ```gdscript
   window.set_use_font_oversampling(true)
   ```

2. **`set_layout_direction(direction)`**  
   Sets text and layout direction (e.g., right-to-left for Arabic).  
   ```gdscript
   window.set_layout_direction(LayoutDirection.RIGHT)
   ```

3. **`set_unparent_when_invisible(unparent)`**  
   Unparents the window when it becomes invisible.  
   ```gdscript
   window.set_unparent_when_invisible(true)
   ```

---

### **Important Notes**
- **Orphaning Nodes**: If `set_unparent_when_invisible` is enabled, ensure the window is referenced elsewhere to avoid being garbage-collected.
- **Theme Constants**: Values like `resize_margin` (4) define margins for resizing, and should be adjusted based on UI design.
- **IME Position**: Use `set_ime_position()` to place the IME editor relative to the window.

---

### **Example Use Case: Custom Window**
```gdscript
# Create a new window
var my_window = Window.new()
my_window.title = "My Window"
my_window.title_color = Color(0.2, 0.5, 0.8, 1)  # Custom title color
my_window.title_font_size = 28
my_window.set_layout_direction(LayoutDirection.RIGHT)
my_window.show()
```

---

This guide covers the essential methods, properties, and settings for working with the `Window` class in Godot. Adjust theme properties and interaction handlers to tailor the window to your application's needs.