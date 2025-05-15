# VisualShaderNodeDerivativeFunc

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

Calculates a derivative within the visual shader graph.  
**Available in:** Fragment and Light shaders.

## Properties

- **function**: `Function` (0)  
  Derivative function type. Options: FUNC_SUM, FUNC_X, FUNC_Y.  
- **op_type**: `OpType` (0)  
  Operand type. Options: SCALAR, VECTOR_2D, VECTOR_3D, VECTOR_4D.  
- **precision**: `Precision` (0)  
  Derivative precision. Options: NONE, COARSE, FINE.

## Enumerations

### OpType
- **OP_TYPE_SCALAR** = 0  
  Floating-point scalar.  
- **OP_TYPE_VECTOR_2D** = 1  
  2D vector.  
- **OP_TYPE_VECTOR_3D** = 2  
  3D vector.  
- **OP_TYPE_VECTOR_4D** = 3  
  4D vector.  
- **OP_TYPE_MAX** = 4  
  Enum size.

### Function
- **FUNC_SUM** = 0  
  Sum of inputs.  
- **FUNC_X** = 1  
  X component.  
- **FUNC_Y** = 2  
  Y component.  
- **FUNC_Z** = 3  
  Z component.  
- **FUNC_W** = 4  
  W component.  
- **FUNC_MAX** = 5  
  Enum size.

### Precision
- **PRECISION_NONE** = 0  
  No effect.  
- **PRECISION_COARSE** = 1  
  Lower precision.  
- **PRECISION_FINE** = 2  
  Higher precision.  
- **PRECISION_MAX** = 3  
  Enum size.

## Property Descriptions

- **function**  
  Sets the type of derivative calculation (e.g., sum, component).  
- **op_type**  
  Defines operand and output type (scalar, vector).  
- **precision**  
  Controls derivative calculation precision. Unused in Compatibility renderer.