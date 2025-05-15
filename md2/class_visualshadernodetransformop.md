# VisualShaderNodeTransformOp

## Inheritance
- VisualShaderNode
  - Resource
    - RefCounted
      - Object

## Description
Applies an operator to two transform (4×4 matrices) inputs.

## Properties
- **operator**: `0`  
  Type of operation on transforms. See `Operator` enum for options.

## Enumerations
### Operator
- **OP_AxB** = 0  
  Multiplies transform `a` by `b`.
- **OP_BxA** = 1  
  Multiplies transform `b` by `a`.
- **OP_AxB_COMP** = 2  
  Component-wise multiplication of `a` by `b`.
- **OP_BxA_COMP** = 3  
  Component-wise multiplication of `b` by `a`.
- **OP_ADD** = 4  
  Adds two transforms.
- **OP_A_MINUS_B** = 5  
  Subtracts `a` from `b`.
- **OP_B_MINUS_A** = 6  
  Subtracts `b` from `a`.
- **OP_A_DIV_B** = 7  
  Divides `a` by `b`.
- **OP_B_DIV_A** = 8  
  Divides `b` by `a`.
- **OP_MAX** = 9  
  Represents the enum size.

## Property Descriptions
### operator
- **set_operator**(value: Operator): void  
  Sets the operation type.
- **get_operator**(): Operator  
  Retrieves the operation type.