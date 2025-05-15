# VisualShaderNodeVec4Parameter

Inherits: VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object  

A 4D vector parameter to be used within the visual shader graph.  
Translated to `uniform vec4` in the shader language.  

## Properties  
- **Vector4** default_value = Vector4(0, 0, 0, 0)  
- **bool** default_value_enabled = false  

## Property Descriptions  
**default_value**  
A default value to be assigned within the shader.  

Methods:  
- `void set_default_value(Vector4 value)`  
- `Vector4 get_default_value()`  

**default_value_enabled**  
Enables usage of the `default_value`.  

Methods:  
- `void set_default_value_enabled(bool value)`  
- `bool is_default_value_enabled()`