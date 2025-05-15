**Class Hierarchy**  
- `VisualShaderNodeParticleRandomness`  
  Inherits from: `VisualShaderNode` → `Resource` → `RefCounted` → `Object`

**Description**  
A node that generates pseudo-random values of a specified type based on minimum and maximum inputs. Outputs can be scalar, vector (2D/3D/4D), or a value indicating enum size.

**Properties**  
- **op_type**: `OpType` (default: `0`)  
  Determines the type of value returned (scalar, vector, etc.).

**Enumerations**  
**OpType**  
- `OP_TYPE_SCALAR` = `0`  
  Floating-point scalar.  
- `OP_TYPE_VECTOR_2D` = `1`  
  2D vector.  
- `OP_TYPE_VECTOR_3D` = `2`  
  3D vector.  
- `OP_TYPE_VECTOR_4D` = `3`  
  4D vector.  
- `OP_TYPE_MAX` = `4`  
  Enum size (4 entries).  

**Property Descriptions**  
- **op_type**  
  - **set_op_type(value: OpType)**: Sets the operand type.  
  - **get_op_type()**: Retrieves the operand type.  
  Defines the data type of the output (scalar, vector, etc.).