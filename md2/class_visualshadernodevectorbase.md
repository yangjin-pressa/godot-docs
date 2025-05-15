**Class:** VisualShaderNodeVectorBase  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  

**Description:**  
An abstract class for nodes performing vector operations in the visual shader graph. Derived classes define specific operations.  

---

**Properties**  
- `op_type`: `OpType` (default: 1)  
  - Specifies the vector type (2D, 3D, or 4D).  

---

**Enumerations**  
- `OP_TYPE_VECTOR_2D`: 0  
  - 2D vector type.  
- `OP_TYPE_VECTOR_3D`: 1  
  - 3D vector type.  
- `OP_TYPE_VECTOR_4D`: 2  
  - 4D vector type.  
- `OP_TYPE_MAX`: 3  
  - Enum size (3 values).  

---

**Methods**  
- `set_op_type(value: OpType)`: Sets the vector type.  
- `get_op_type()`: Retrieves the current vector type.  

---

**Key Usage**  
- `op_type` determines the dimensionality of vectors handled by the node.  
- Derived classes (e.g., `VisualShaderNodeVectorCompose`) implement specific vector operations.