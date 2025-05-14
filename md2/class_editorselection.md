**Class:** EditorSelection  
**Inherits:** Object  

---

### **Description**  
Manages SceneTree selection in the editor.  
**Note:** Not meant to be instantiated directly. Use `EditorInterface.get_selection()` to access the singleton.  

---

### **Methods**  
- **add_node(node: Node)**  
  Adds a node to the selection.  
  **Note:** Selected node isn’t automatically edited in the inspector. Use `EditorInterface.edit_node()` to edit.  

- **clear()**  
  Clears all selected nodes.  

- **get_selected_nodes()** → Array[Node]  
  Returns the list of currently selected nodes.  

- **get_top_selected_nodes()** → Array[Node]  
  Returns top-level selected nodes (excluding children). Useful for transform operations.  
  **Example:** Selecting nodes A (with child B) and sibling C returns A and C.  

- **get_transformable_selected_nodes()** → Array[Node]  
  **Deprecated:** Use `get_top_selected_nodes()` instead.  

- **remove_node(node: Node)**  
  Removes a node from the selection.  

---

### **Signals**  
- **selection_changed()**  
  Emits when the selection changes.  

---

### **Key Notes**  
- `get_transformable_selected_nodes` is deprecated.  
- `get_top_selected_nodes` is preferred for transform operations.  
- Selections are managed via `EditorInterface.get_selection()`.