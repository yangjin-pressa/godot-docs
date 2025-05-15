# VisualShaderNodeStep

## Inheritance
- **VisualShaderNodeStep** > [VisualShaderNode](class_VisualShaderNode) > [Resource](class_Resource) > [RefCounted](class_RefCounted) > [Object](class_Object)

## Description
Translates to `step(edge, x)` in shader language. Returns `0.0` if `x` is less than `edge`, otherwise `1.0`.

## Properties
- **op_type**: `OpType` (default: `0`)  
  Specifies operand type and return value.

## Enumerations
### OpType
- **OP_TYPE_SCALAR** = `0`  
  Floating-point scalar type.
- **OP_TYPE_VECTOR_2D** = `1`  
  2D vector type.
- **OP_TYPE_VECTOR_2D_SCALAR** = `2`  
  `x` port uses 2D vector, `edge` port uses scalar.
- **OP_TYPE_VECTOR_3D** = `3`  
  3D vector type.
- **OP_TYPE_VECTOR_3D_SCALAR** = `4`  
  `x` port uses 3D vector, `edge` port uses scalar.
- **OP_TYPE_VECTOR_4D** = `5`  
  4D vector type.
- **OP_TYPE_VECTOR_4D_SCALAR** = `6`  
  `x` and `edge` ports use 4D vector and scalar, respectively.
- **OP_TYPE_MAX** = `7`  
  Enum size (7 entries).

## Property Descriptions
### op_type
- **set_op_type** (value: `OpType`)  
  Sets operand type.
- **get_op_type** ()  
  Returns operand type.