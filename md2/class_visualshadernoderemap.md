**Class:** VisualShaderNodeRemap  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  

---

### Description  
Remap transforms input ranges to output ranges. Example: convert `0..1` to `-2..2`. Refer to `GlobalScope.remap()` for details.  

---

### Properties  
- **op_type**: `OpType` (default: `0`)  
  - Defines the data type for remapping operations.  

---

### Enumerations  
**OpType**  
- **OP_TYPE_SCALAR** = `0`  
  - Floating-point scalar type.  
- **OP_TYPE_VECTOR_2D** = `1`  
  - 2D vector type.  
- **OP_TYPE_VECTOR_2D_SCALAR** = `2`  
  - `value` uses 2D vector; others use scalar.  
- **OP_TYPE_VECTOR_3D** = `3`  
  - 3D vector type.  
- **OP_TYPE_VECTOR_3D_SCALAR** = `4`  
  - `value` uses 3D vector; others use scalar.  
- **OP_TYPE_VECTOR_4D** = `5`  
  - 4D vector type.  
- **OP_TYPE_VECTOR_4D_SCALAR** = `6`  
  - `value` uses 4D vector; others use scalar.  
- **OP_TYPE_MAX** = `7`  
  - Enum size (7 entries).  

---

### Property Descriptions  
**op_type**  
- **set_op_type**(value: `OpType`)  
- **get_op_type**()  
  - Currently no description. Contribute one via the documentation process.  

---

### Notes  
- The `op_type` property controls the data type for remapping (scalar, vector, etc.).  
- Refer to `GlobalScope.remap()` for implementation details.