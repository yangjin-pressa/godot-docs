# VisualShaderNodeExpression

## Inheritance Hierarchy
- VisualShaderNodeExpression
  - VisualShaderNodeGroupBase
    - VisualShaderNodeResizableBase
      - VisualShaderNode
        - Resource
          - RefCounted
            - Object

## Inherited By
- VisualShaderNodeGlobalExpression

## Description
A custom visual shader graph expression written in Godot Shading Language.

### Key Notes
- Code is injected into shader functions (vertex, fragment, light)
- Cannot declare functions, varyings, uniforms, or global constants
- See VisualShaderNodeGlobalExpression for global definitions

## Properties
- **expression**: String = ""

## Property Descriptions
### expression
- **Type**: String
- **Default**: ""
- **Methods**:
  - set_expression(value: String)
  - get_expression()

## Functionality
- Expression code is injected at the start of the matching shader function
- Cannot be used for:
  - Function declarations
  - Varying definitions
  - Uniform declarations
  - Global constant definitions

## Related Documentation
- [VisualShaderNodeGlobalExpression](https://github.com/godotengine/godot/tree/master/doc/classes/VisualShaderNodeGlobalExpression) for global expressions