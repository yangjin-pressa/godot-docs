**Class Name**: VisualShaderNodeInput  
**Inherits**: VisualShaderNode → Resource → RefCounted → Object  

---

### **Description**  
Represents input shader parameters in the visual shader graph. Accesses built-in variables for the shader. Refer to the Shading Reference for available built-ins (see Tutorials section for link).  

---

### **Tutorials**  
- [Shading reference index](https://godotengine.org/tutorials/shaders/shader_reference/index)  

---

### **Properties**  
- **input_name**: String = "[None]"  

---

### **Methods**  
- **get_input_real_name() → String**  
  Returns the Godot Shader Language translation of the current constant (e.g., "ALBEDO" for "albedo").  

---

### **Signals**  
- **input_type_changed()**  
  Emitted when input is modified via `input_name`.  

---

### **Property Descriptions**  
- **input_name**: String = "[None]"  
  Specifies an input constant (e.g., "vertex", "point_size").  

---

### **Method Descriptions**  
- **get_input_real_name() → String**  
  Returns the translated name of the constant in Godot Shader Language.  

---

### **Key Notes**  
- Input names are case-sensitive (e.g., "albedo" vs. "ALBEDO").  
- The property and method are used to manage and retrieve input constants for shader graphs.