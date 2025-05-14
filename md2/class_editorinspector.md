**EditorInspector**  
A class for editing properties of objects in the Godot engine.  

---

### **Description**  
The `EditorInspector` is used to display and modify properties of an object. To get the `EditorInspector` used in the editor's Inspector dock, use `EditorInterface.get_inspector()`.  

**Key Methods**  
- `edit(object: Object)`: Shows the properties of the given object in this inspector for editing. To clear the inspector, call this method with `null`.  
- `get_edited_object()`: Returns the object currently selected in this inspector.  
- `get_selected_path()`: Gets the path of the currently selected property.  
- `instantiate_property_editor(...)`: Creates a property editor for a specified property of an object.  

---

### **Properties**  
- **override_scroll**: `bool` (Default: `true`)  
- **override_zoom**: `bool` (Default: `true`)  
- **scroll_speed**: `float` (Default: `1.0`)  
- **zoom_speed**: `float` (Default: `1.0`)  

---

### **Methods**  
- **edit(object: Object)**:  
  Shows the properties of the given `object` in this inspector for editing.  
  **Note**: Use `EditorInterface.edit_*` methods for main inspector edits.  

- **get_edited_object()**:  
  Returns the object currently selected in this inspector.  

- **get_selected_path()**:  
  Gets the path of the currently selected property.  

- **instantiate_property_editor(object: Object, type: Variant.Type, path: String, hint: PropertyHint, hint_text: String, usage: int, wide: bool = false)**:  
  Creates a property editor for a specified property of an `object`.  

---

### **Signals**  
- **restart_requested()**:  
  Emitted when a property requiring a restart is edited. Used in Project Settings and Editor Settings.  

- **resource_selected(resource: Object)**:  
  Emitted when a resource is selected in the inspector.  

- **property_changed(property: String, value: Variant)**:  
  Emitted when a property changes.  

- **restart_requested()**:  
  Emitted when a restart is needed after editing a property.  

---

### **Notes**  
- **Property Editors**: The `instantiate_property_editor` method is static and allows plugins to create custom property editors.  
- **Override Behavior**: Properties like `override_scroll` and `override_zoom` control inspector behavior.  
- **Signal Usage**: Signals like `restart_requested` are critical for post-edits actions (e.g., restarting a game).  

This class is central to interactive property editing in Godot, with methods for dynamic object manipulation and event handling.