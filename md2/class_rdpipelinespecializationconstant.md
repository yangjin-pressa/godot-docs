**Class Name**: RDPipelineSpecializationConstant  
**Inherits**: RefCounted < Object  

---

### Description  
A specialization constant allows creating shader variants without increasing compiled shader versions. This reduces branching and improves performance while maintaining flexibility for different use cases. Used by RenderingDevice.  

---

### Properties  
- **constant_id**: `int` (default: `0`)  
  - Identifier for the specialization constant. Starts at `0` and increments for each unique constant in a shader.  
  - Methods: `set_constant_id(value: int)`, `get_constant_id()`.  

- **value**: `Variant`  
  - Value of the specialization constant. Only `bool`, `int`, or `float` are valid.  
  - Methods: `set_value(value: Variant)`, `get_value()`.  

---

### Key Notes  
- Specialization constants are used to manage shader flexibility without increasing shader versions.  
- `constant_id` uniquely identifies each constant for a shader.  
- `value` must be a scalar type (boolean, integer, or float).