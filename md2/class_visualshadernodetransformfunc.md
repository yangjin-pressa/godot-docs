# VisualShaderNodeTransformFunc

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

## Description
Computes an inverse or transpose function on the provided Transform3D.

## Properties
- **Function**: enum with values 0, 1, 2 (FUNC_INVERSE, FUNC_TRANSPOSE, FUNC_MAX)
- **function**: setter/getter for the function to compute

## Enumerations
**Function**:
- FUNC_INVERSE = 0: Perform inverse operation on Transform3D matrix
- FUNC_TRANSPOSE = 1: Perform transpose operation on Transform3D matrix
- FUNC_MAX = 2: Represents enum size

## Property Descriptions
**function**:
- **set_function**(value: Function): Sets the function to compute
- **get_function**(): Gets the function to compute

## Method Definitions
- set_function: Sets the function to compute
- get_function: Gets the function to compute

## Notes
- The node operates on Transform3D matrices, performing either inverse or transpose operations based on the selected function.