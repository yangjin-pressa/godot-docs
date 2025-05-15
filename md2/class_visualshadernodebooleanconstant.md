**Class:** VisualShaderNodeBooleanConstant  
**Inherits:** VisualShaderNodeConstant → VisualShaderNode → Resource → RefCounted → Object  

---

### **Description**  
- Has one output port and no inputs.  
- Translates to `bool` in shader language.  

---

### **Properties**  
- **constant**: `bool` (default: `false`)  
  - Boolean value of the node.  

---

### **Methods**  
- **set_constant(value: `bool`)**  
  - Sets the boolean value of the node.  

- **get_constant()**: `bool`  
  - Retrieves the boolean value of the node.  

---

### **References**  
- Inherits from: `VisualShaderNodeConstant` [class_VisualShaderNodeConstant](https://github.com/godotengine/godot/tree/master/doc/classes/VisualShaderNodeConstant.xml)  
- Inheritance chain: `VisualShaderNodeBooleanConstant` → `VisualShaderNodeConstant` → `VisualShaderNode` → `Resource` → `RefCounted` → `Object`  

---

### **Key Attributes**  
- **Type:** Boolean constant node.  
- **Output:** Single `bool` value.  
- **Usage:** Used in visual shader graphs to represent boolean states.