**EditorResourcePicker**  
- **Inherits**: `Control`  

---

### **Description**  
A `Control` node used in the editor's Inspector dock to select Resource type properties. Provides options for creating, loading, saving, and converting Resources. Used in conjunction with `EditorInspectorPlugin`. Note: This class does not include an editor for the Resource itself; editing is controlled by the Inspector dock or its sub-components.  

---

### **Properties**  
- **base_type**: `String` = `""`  
  - Description: Default value for the base type.  
- **editable**: `bool` = `true`  
  - Description: Whether the property is editable.  
- **edited_resource**: `Resource`  
  - Description: The currently selected Resource.  
- **toggle_mode**: `bool` = `false`  
  - Description: Whether the main button operates in toggle mode.  

---

### **Methods**  
- **set_toggle_pressed(pressed: bool)**  
  - Description: Sets the toggle mode state for the main button. Works only if `toggle_mode` is `true`.  

- **set_toggle_pressed(pressed: bool)**  
  - Description: Sets the toggle mode state for the main button. Works only if `toggle_mode` is `true`.  

---

### **Signals**  
- **resource_changed(resource: Resource)**  
  - Description: Emitted when the selected Resource changes.  

- **resource_selected(resource: Resource, inspect: bool)**  
  - Description: Emitted when a Resource is selected for inspection.  

---

### **Property Descriptions**  
- **base_type**:  
  - **Set**: `set_base_type(value: String)`  
  - **Get**: `get_base_type() -> String`  

- **editable**:  
  - **Set**: `set_editable(value: bool)`  
  - **Get**: `get_editable() -> bool`  

- **edited_resource**:  
  - **Set**: `set_edited_resource(value: Resource)`  
  - **Get**: `get_edited_resource() -> Resource`  

- **toggle_mode**:  
  - **Set**: `set_toggle_mode(value: bool)`  
  - **Get**: `get_toggle_mode() -> bool`  

---

### **Method Descriptions**  
- **set_toggle_pressed(pressed: bool)**:  
  - Sets the toggle mode state for the main button. Works only if `toggle_mode` is `true`.  

--- 

This summary captures the class's key attributes, behaviors, and interactions.