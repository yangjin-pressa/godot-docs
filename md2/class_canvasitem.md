Here's a structured summary of the Godot Engine's `CanvasItem` class methods, highlighting key functionality and important notes:

---

### **Core Drawing and Redraw Functions**
- **`draw()`**  
  Virtual method to implement custom drawing logic for the canvas item. Subclasses must override this to define visual output.

- **`queue_redraw()`**  
  Schedules the canvas item for redrawing. Triggers the `NOTIFICATION_DRAW` signal once per frame if the item is visible.

---

### **Visibility and Tree State**
- **`hide()` / `show()`**  
  Toggles the visibility of the canvas item by setting the `visible` property to `false`/`true`.

- **`is_visible_in_tree()`**  
  Checks if the item is visible in the scene tree, considering its own visibility and all ancestors.  
  **Note**: Does **not** account for `visibility_layer` settings, which might override visibility.

- **`set_visibility_layer_bit()`**  
  Sets/clears individual bits in the `visibility_layer` to control rendering layers.  
  **Use Case**: Simplifies managing visibility across multiple layers (e.g., background, foreground).

---

### **Transform and Notifications**
- **`set_notify_local_transform()` / `set_notify_transform()`**  
  Enables/disables notifications for local/global transform changes:  
  - `NOTIFICATION_LOCAL_TRANSFORM_CHANGED` (local transform)  
  - `NOTIFICATION_TRANSFORM_CHANGED` (global transform)  
  **Use Case**: Essential for nodes that depend on transform updates (e.g., cameras, lights).

- **`is_local_transform_notification_enabled()` / `is_transform_notification_enabled()`**  
  Checks if notifications for transform changes are enabled.

---

### **Position and Input Handling**
- **`make_canvas_position_local()`**  
  Converts a viewport coordinate to the canvas item's local coordinate system.  
  **Opposite**: Use `get_global_transform_with_canvas()` for the reverse.

- **`make_input_local()`**  
  Converts an input event (e.g., mouse movement) to local coordinates relative to the canvas item.  
  **Use Case**: For handling user input within specific canvas regions.

---

### **Canvas Positioning and Z-Order**
- **`move_to_front()`**  
  Moves the canvas item to the front of its siblings, ensuring it draws on top of others.

- **`make_canvas_position_local()`**  
  Transforms a viewport point to local coordinates (used for positioning within the canvas).

---

### **Shader Parameters (Per-Instance Uniforms)**
- **`set_instance_shader_parameter()` / `get_instance_shader_parameter()`**  
  Sets/clears shader uniforms specific to this instance.  
  **Important**: Uniforms must be declared as `instance uniform` in the shader for this to work.  
  **Note**: Use `ShaderMaterial.set_shader_parameter()` for shared uniforms across instances.

---

### **Key Concepts**
- **Local vs. Global Transforms**:  
  - Local transform is relative to the parent.  
  - Global transform is absolute (relative to the root of the scene).

- **Canvas Layers**:  
  - `visibility_layer` controls rendering order via bitmasking.  
  - Nodes with lower layer values draw behind higher ones.

- **Performance Considerations**:  
  - `queue_redraw()` is efficient as it only triggers once per frame.  
  - Avoid unnecessary redraws by leveraging `is_visible_in_tree()`.

---

### **Useful Notes**
- **CanvasItem vs. SceneTree**:  
  Canvas items are rendered in the order they appear in the scene tree. `move_to_front()` adjusts this order.

- **Shader Uniforms**:  
  Per-instance uniforms are critical for custom visual effects that differ per canvas item.

- **Notifications**:  
  Nodes that require transform updates (e.g., cameras, lights) should enable notifications to react dynamically.

This summary covers the primary methods and their interrelations, emphasizing how to control rendering, visibility, and interaction in Godot's 2D canvas system.