**Class:** VisualShaderNodeTransformVecMult  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  

---

### Description  
Performs a multiplication operation between a Transform3D (4×4 matrix) and a Vector3, supporting various operators.  

---

### Properties  
- **operator**: `Operator` (default: 0)  
  - Controls the multiplication type.  

---

### Enumerations  
**Operator**  
- **OP_AxB** = 0  
  - Multiply transform `a` by vector `b`.  
- **OP_BxA** = 1  
  - Multiply vector `b` by transform `a`.  
- **OP_3x3_AxB** = 2  
  - Multiply transform `a` by vector `b`, ignoring the last row/column of the transform.  
- **OP_3x3_BxA** = 3  
  - Multiply vector `b` by transform `a`, ignoring the last row/column of the transform.  
- **OP_MAX** = 4  
  - Enum size marker.  

---

### Property Descriptions  
**operator**  
- **Type:** `Operator`  
- **Default:** 0  
- **Set/Get:**  
  - `set_operator(value: Operator)`  
  - `get_operator()`  
- **Description:** Defines the multiplication mode.  

--- 

### Notes  
- The node connects to a Transform3D and a Vector3 input.  
- Operators determine whether the transform is applied to the vector or vice versa, with options for 4×4 matrix or 3×3 matrix operations.