# VisualShaderNodeMix

**Inherits:** VisualShaderNode → Resource → RefCounted → Object

## Description
Translates to `mix(a, b, weight)` in the shader language.

## Properties
- **op_type**: `OpType` (default: 0)

## Enumerations
- **OP_TYPE_SCALAR** = 0  
  A floating-point scalar.

- **OP_TYPE_VECTOR_2D** = 1  
  A 2D vector type.

- **OP_TYPE_VECTOR_2D_SCALAR** = 2  
  `a` and `b` ports use 2D vector type; `weight` uses scalar.

- **OP_TYPE_VECTOR_3D** = 3  
  A 3D vector type.

- **OP_TYPE_VECTOR_3D_SCALAR** = 4  
  `a` and `b` ports use 3D vector type; `weight` uses scalar.

- **OP_TYPE_VECTOR_4D** = 5  
  A 4D vector type.

- **OP_TYPE_VECTOR_4D_SCALAR** = 6  
  `a` and `b` ports use 4D vector type; `weight` uses scalar.

- **OP_TYPE_MAX** = 7  
  Represents the size of the `OpType` enum.

## Property Descriptions
- **op_type**:  
  A type of operands and returned value.  
  - `set_op_type(value: OpType)`  
  - `get_op_type()`