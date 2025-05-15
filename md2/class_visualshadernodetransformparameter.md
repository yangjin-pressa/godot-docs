# VisualShaderNodeTransformParameter

## Inheritance Hierarchy
- VisualShaderNodeTransformParameter
  - VisualShaderNodeParameter
    - VisualShaderNode
      - Resource
        - RefCounted
          - Object

## Description
A Transform3D parameter for use within the visual shader graph. Translated to `uniform mat4` in the shader language.

## Properties
- **default_value**: Transform3D = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
- **default_value_enabled**: bool = `false`

## Property Descriptions
### default_value
- **Type**: Transform3D
- **Description**: A default value to be assigned within the shader.
- **Methods**:
  - `set_default_value(value: Transform3D)`: Sets the default value.
  - `get_default_value()`: Retrieves the default value.

### default_value_enabled
- **Type**: bool
- **Description**: Enables usage of the `default_value`.
- **Methods**:
  - `set_default_value_enabled(value: bool)`: Enables/disables the default value.
  - `is_default_value_enabled()`: Checks if the default value is enabled.

## Notes
- **virtual**: This method should typically be overridden by the user to have any effect.
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.