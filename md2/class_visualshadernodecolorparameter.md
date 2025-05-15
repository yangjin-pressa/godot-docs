**Class Name:** VisualShaderNodeColorParameter  
**Inherits:** VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object  

---

### Description  
Translated to `uniform vec4` in the shader language.

---

### Properties  
- **default_value**: `Color` = `Color(1, 1, 1, 1)`  
- **default_value_enabled**: `bool` = `false`  

---

### Property Descriptions  
#### `default_value`  
**Type:** `Color`  
**Default Value:** `Color(1, 1, 1, 1)`  
**Description:** A default value to be assigned within the shader.  
**Methods:**  
- `set_default_value(value: Color)`  
- `get_default_value()`  

#### `default_value_enabled`  
**Type:** `bool`  
**Default Value:** `false`  
**Description:** Enables usage of the `default_value`.  
**Methods:**  
- `set_default_value_enabled(value: bool)`  
- `is_default_value_enabled()`  

---

### Notes  
- `default_value_enabled` determines whether the `default_value` is applied.  
- This class is used to pass a `Color` parameter in a visual shader graph.  

---

### References  
- 🔗[class_VisualShaderNodeColorParameter_property_default_value](#)  
- 🔗[class_VisualShaderNodeColorParameter_property_default_value_enabled](#)  

--- 

**End of Document**