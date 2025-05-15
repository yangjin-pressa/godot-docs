# VisualShaderNodeUIntFunc

**Inherits:** VisualShaderNode → Resource → RefCounted → Object

## Description
Accepts an unsigned integer scalar (`x`) and applies a function based on the `function` property.

## Properties
- **Function**: `0`  
  - **FUNC_NEGATE** = `0`  
    Negates the `x` using `-(x)`.  
  - **FUNC_BITWISE_NOT** = `1`  
    Returns the result of bitwise `NOT` on the integer. Translates to `~a` in the Godot Shader Language.  
  - **FUNC_MAX** = `2`  
    Represents the size of the Function enum.

## Property Descriptions
- **function**: `0`  
  - **set_function**(`value: Function`)  
  - **get_function**()  
  A function to apply to the scalar. See Function for options.