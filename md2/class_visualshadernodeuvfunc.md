# VisualShaderNodeUVFunc

**Inherits:** VisualShaderNode → Resource → RefCounted → Object

## Description
UV functions are similar to Vector2 functions, but the input port of this node uses the shader's UV value by default.

## Properties
- Function: 0

## Enumerations
### Function
- **FUNC_PANNING** = 0  
  Translates uv using scale and offset values. uv port connects to UV built-in by default.

- **FUNC_SCALING** = 1  
  Scales uv using scale and pivot values. uv port connects to UV built-in by default.

- **FUNC_MAX** = 2  
  Represents the size of the Function enum.

## Property Descriptions
### function
- Type: Function  
- Default: 0  
- Set: void set_function(value: Function)  
- Get: Function get_function()  
  A function to be applied to the texture coordinates. See Function for options.