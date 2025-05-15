# VisualShaderNodeVec4Constant

## Inheritance
- `VisualShaderNodeVec4Constant`  
  < `VisualShaderNodeConstant`  
  < `VisualShaderNode`  
  < `Resource`  
  < `RefCounted`  
  < `Object`

## Description
A constant 4D vector, used as an input node in the visual shader graph.

## Properties
- **constant**: `Quaternion` = `Quaternion(0, 0, 0, 1)`

## Property Descriptions
- **constant**: A 4D vector (as a `Quaternion`) constant for this node.  
  - **set_constant**: Sets the value of the constant.  
  - **get_constant**: Retrieves the value of the constant.

## Method Definitions
- `void set_constant(value: Quaternion)`  
- `Quaternion get_constant()`

## Notes
- The `Quaternion` represents a 4D vector in this context.  
- The `constant` property is virtual and has no side effects.