**Class:** VisualShaderNodeFrame  
**Inherits:** VisualShaderNodeResizableBase → VisualShaderNode → Resource → RefCounted → Object  
**Inherited By:** VisualShaderNodeComment  

---

### Description  
A rectangular frame for grouping visual shader nodes. Nodes attached to the frame move with it and can auto-resize to enclose attached nodes. Customizable title, description, and color.  

---

### Properties  
- **attached_nodes**: `PackedInt32Array()`  
  List of nodes attached to the frame.  
  - **set_attached_nodes**: Sets the list.  
  - **get_attached_nodes**: Returns a copy of the list.  

- **autoshrink**: `true`  
  If `true`, the frame automatically resizes to enclose all attached nodes.  
  - **set_autoshrink_enabled**: Enables or disables auto-resizing.  

- **tint_color**: `Color(0.3, 0.3, 0.3, 0.75)`  
  Frame color when `tint_color_enabled` is `true`.  
  - **set_tint_color**: Sets the tint color.  
  - **get_tint_color**: Retrieves the tint color.  

- **tint_color_enabled**: `false`  
  If `true`, the frame is tinted with `tint_color`.  
  - **set_tint_color_enabled**: Toggles tint color activation.  

- **title**: `"Title"`  
  The title of the node.  
  - **set_title**: Sets the title.  
  - **get_title**: Retrieves the title.  

---

### Methods  
- **add_attached_node**(node: `int`):  
  Adds a node to the frame. **Not meant to be called directly**; use `VisualShader.attach_node_to_frame()` instead.  

- **remove_attached_node**(node: `int`):  
  Removes a node from the frame. **Not meant to be called directly**; use `VisualShader.detach_node_from_frame()` instead.  

---

### Notes  
- The `attached_nodes` property returns a copied array; changes to the copy do not affect the original.  
- Methods like `add_attached_node` and `remove_attached_node` are internal and should be used via the `VisualShader` API.