# VisualShaderNodeVec3Parameter

**Inherits:** VisualShaderNodeParameter → VisualShaderNode → Resource → RefCounted → Object

A Vector3 parameter used in the visual shader graph.

## Description
Translated to `uniform vec3` in the shader language.

## Properties
- **default_value**: Vector3(0, 0, 0)
- **default_value_enabled**: false

## Property Descriptions
**default_value**  
A default value to be assigned within the shader.  
- `set_default_value(value: Vector3)`  
- `get_default_value()`  

**default_value_enabled**  
Enables usage of the `default_value`.  
- `set_default_value_enabled(value: bool)`  
- `is_default_value_enabled()`