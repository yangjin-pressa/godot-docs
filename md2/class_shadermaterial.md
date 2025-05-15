# ShaderMaterial

## Overview
A material defined by a custom Shader program and its shader parameters. Inherits from: `Material` → `Resource` → `RefCounted` → `Object`.

---

## Description
- Uses custom Shader for rendering (canvas items, meshes, skies, fog, particles)
- Offers deeper control over shader code compared to other materials
- Multiple instances can use the same shader with different uniform values

---

## Tutorials
- [Shaders documentation index](../tutorials/shaders/index)

---

## Properties
- **Shader** (`Shader`): The shader program used for rendering
  - `set_shader(value: Shader)`
  - `get_shader()`

---

## Methods
### get_shader_parameter(param: StringName) → Variant
- Returns current value of a shader uniform parameter
- **Note:** Parameter names are case-sensitive and must match shader code exactly

### set_shader_parameter(param: StringName, value: Variant)
- Changes value of a shader uniform parameter
- **Note:** Changes affect all instances using this material
  - Use `GeometryInstance3D.set_instance_shader_parameter()` for per-instance control
  - Prefer this over duplicating ShaderMaterial for performance

---

## Key Notes
1. **Resource Changes:**  
   - `Resource.changed` signal only emits when `resource_name` changes
   - In editor, it also emits for `shader` changes

2. **Performance:**  
   - Use per-instance uniforms for better efficiency
   - Duplicate ShaderMaterial only when per-instance solution isn't feasible

3. **Parameter Case Sensitivity:**  
   - Shader parameter names must match code exactly (not inspector display names)

---

## Related Resources
- [Shader documentation](../tutorials/shaders/index)