# Shader

## Overview
A shader implemented in the Godot shading language, saved with the `.gdshader` extension. Used by `ShaderMaterial` to define custom rendering behavior.

---

## Key Features
- **Inherits**: `Resource` → `RefCounted` → `Object`
- **Used By**: `ShaderMaterial`
- **File Extension**: `.gdshader`
- **Available In**: Editor (inspect_native_shader_code)

---

## Tutorials
- [Shaders documentation index](../tutorials/shaders/index)

---

## Properties
### `code`
- **Type**: `String`
- **Default**: `""`
- **Description**: Returns the user-written shader code (not internal generated code)
- **Methods**:
  - `set_code(value: String)`: Sets the shader code
  - `get_code()`: Retrieves the shader code

---

## Modes (enum Shader_Mode)
### `MODE_SPATIAL` = 0
- **Purpose**: 3D object rendering

### `MODE_CANVAS_ITEM` = 1
- **Purpose**: 2D object rendering

### `MODE_PARTICLES` = 2
- **Purpose**: Per-particle calculations (not for rendering)

### `MODE_SKY` = 3
- **Purpose**: Sky rendering (used with `Sky` nodes)

### `MODE_FOG` = 4
- **Purpose**: Volumetric fog color/density settings

---

## Methods
### `get_default_texture_parameter(name: StringName, index: int = 0)`
- **Returns**: `Texture`
- **Notes**:
  - `name` must match the uniform name exactly
  - Use `index` for sampler arrays

### `get_mode()`
- **Returns**: `Mode`
- **Description**: Current shader mode (e.g., spatial, canvas item)

### `get_shader_uniform_list(get_groups: bool = false)`
- **Returns**: `Array` of uniforms
- **Notes**:
  - Includes parameter grouping hints if `get_groups` is true
  - Format similar to `Object.get_property_list()`

### `inspect_native_shader_code()`
- **Editor Only**: Displays generated shader code, variants, and internal code

### `set_default_texture_parameter(name: StringName, texture: Texture, index: int = 0)`
- **Notes**:
  - Default texture used if not specified in `ShaderMaterial`
  - `index` for sampler arrays

---

## Notes
- Shader code is compiled into a format compatible with the graphics API
- `ShaderMaterial` uses this shader to apply custom rendering logic
- `inspect_native_shader_code()` helps debug shader variants and internal code structure