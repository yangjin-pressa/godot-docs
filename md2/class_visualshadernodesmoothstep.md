**VisualShaderNodeSmoothStep**

**Description**  
This node translates to the shader function `smoothstep(edge0, edge1, x)`. It returns `0` if `x < edge0`, `1` if `x > edge1`, and an interpolated value otherwise.

**Inherits From**  
VisualShaderNode < Resource < RefCounted < Object

**Properties**  
- **OpType**: A value of `0` indicating the type of operation.

**Enumerations**  
- **OP_TYPE_SCALAR** = 0: Represents a floating-point scalar type.  
- **OP_TYPE_VECTOR_2D** = 1: Denotes a 2D vector type.  
- **OP_TYPE_VECTOR_3D** = 2: Refers to a 3D vector type.  
- **OP_TYPE_VECTOR_4D** = 3: Represents a 4D vector type.  
- **OP_TYPE_MATRIX** = 4: Indicates a matrix type.  

**Property Description**  
The `op_type` property defines the type of operation. It can be set or retrieved using the following methods:  

- **set_op_type(value)**: Sets the `op_type` to the specified value.  
- **get_op_type()**: Retrieves the current `op_type`.  

**Shader Function Reference**  
Translates to the shader function `smoothstep(edge0, edge1, x)` in the shader language.