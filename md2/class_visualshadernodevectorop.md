**Class: VisualShaderNodeVectorOp**  
**Inherits:** VisualShaderNodeVectorBase → VisualShaderNode → Resource → RefCounted → Object  

**Description**  
A visual shader node for vector operations, taking two vectors (a and b) as input.  

---

**Properties**  
- **operator**: `Operator` (0)  
  - The vector operation to apply.  

---

**Enumerations**  
**Operator** (enum):  
- **OP_ADD** = 0  
  - Adds two vectors.  
- **OP_SUB** = 1  
  - Subtracts a vector from another.  
- **OP_MUL** = 2  
  - Multiplies two vectors.  
- **OP_DIV** = 3  
  - Divides one vector by another.  
- **OP_MOD** = 4  
  - Returns the remainder of vector components.  
- **OP_POW** = 5  
  - Raises first vector to the power of the second.  
- **OP_MAX** = 6  
  - Returns the greater of two vector components.  
- **OP_MIN** = 7  
  - Returns the lesser of two vector components.  
- **OP_CROSS** = 8  
  - Calculates the cross product of two vectors.  
- **OP_ATAN2** = 9  
  - Returns the arc-tangent of the parameters.  
- **OP_REFLECT** = 10  
  - Computes reflection vector (a: incident, b: normal).  
- **OP_STEP** = 11  
  - Returns 0.0 if a < b, else 1.0.  
- **OP_ENUM_SIZE** = 12  
  - Enum size (13 entries).  

---

**Property Descriptions**  
- **operator**:  
  - **Setter**: set_operator(value: Operator)  
  - **Getter**: get_operator()  
  - Defines the operation to perform on vectors a and b.  

--- 

**Notes**  
- The node operates on two input vectors (a and b).  
- Operators are defined as constants in the enum.