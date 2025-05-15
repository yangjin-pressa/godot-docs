# VisualShaderNodeFloatParameter

**Inherits:** VisualShaderNodeParameter → VisualShaderNode → Resource → RefCounted → Object

## Description
Translated to `uniform float` in the shader language.

## Properties
- float default_value = 0.0
- bool default_value_enabled = false
- Hint hint = 0
- float max = 1.0
- float min = 0.0
- float step = 0.1

### Property Methods
- **default_value**:  
  - set_default_value(value: float)  
  - get_default_value()  
  Default value to be assigned within the shader.

- **default_value_enabled**:  
  - set_default_value_enabled(value: bool)  
  - is_default_value_enabled()  
  Enables usage of the default_value.

- **hint**:  
  - set_hint(value: Hint)  
  - get_hint()  
  A hint applied to the uniform, controlling input values in the Inspector.

- **max**:  
  - set_max(value: float)  
  - get_max()  
  Minimum value for range hints (used with HINT_RANGE or HINT_RANGE_STEP).

- **min**:  
  - set_min(value: float)  
  - get_min()  
  Maximum value for range hints (used with HINT_RANGE or HINT_RANGE_STEP).

- **step**:  
  - set_step(value: float)  
  - get_step()  
  Step increment for HINT_RANGE_STEP hints.

## Enumerations
### Hint
- **HINT_NONE** = 0  
  No hint used.

- **HINT_RANGE** = 1  
  Limits values between min and max. Translated to `hint_range(min, max)`.

- **HINT_RANGE_STEP** = 2  
  Limits values between min and max with step. Translated to `hint_range(min, max, step)`.

- **HINT_MAX** = 3  
  Represents the size of the Hint enum.