# VisualShaderNodeVec2Parameter

**Inherits:** VisualShaderNodeParameter < VisualShaderNode < Resource < RefCounted < Object

A Vector2 parameter for visual shader graphs.

## Description
Translated to `uniform vec2` in the shader language.

## Properties
- **Vector2** `default_value` = `Vector2(0, 0)`
- **bool** `default_value_enabled` = `false`

## Property Descriptions

**default_value**
- **Type:** Vector2
- **Default value:** Vector2(0, 0)
- **Description:** Default value assigned within the shader.
- **Methods:**
  - `set_default_value(value: Vector2)`
  - `get_default_value()`

**default_value_enabled**
- **Type:** bool
- **Default value:** false
- **Description:** Enables usage of the `default_value`.
- **Methods:**
  - `set_default_value_enabled(value: bool)`
  - `is_default_value_enabled()`