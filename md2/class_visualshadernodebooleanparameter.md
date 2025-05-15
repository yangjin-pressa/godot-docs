# VisualShaderNodeBooleanParameter

**Inherits:** VisualShaderNodeParameter → VisualShaderNode → Resource → RefCounted → Object

## Description
Translated to `uniform bool` in the shader language.

## Properties
- `default_value`: `bool` = `false`  
- `default_value_enabled`: `bool` = `false`

## Property Descriptions

### default_value
**Type:** `bool`  
**Default:** `false`  
**Function:** A default value to be assigned within the shader.

**Methods:**
- `set_default_value(value: bool)`  
- `get_default_value()`

### default_value_enabled
**Type:** `bool`  
**Default:** `false`  
**Function:** Enables usage of the `default_value`.

**Methods:**
- `set_default_value_enabled(value: bool)`  
- `is_default_value_enabled()`