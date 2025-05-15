# VisualShaderNodeIntConstant

**Inherits:** VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object

## Description
Translated to `int` in the shader language.

## Properties
- **constant**: `int` = `0`

## Property Descriptions
- **constant**: An integer constant which represents a state of this node.
  - `set_constant(value: int)`: Sets the integer constant.
  - `get_constant()`: Returns the integer constant.

## Notes
- **virtual**: This method should typically be overridden by the user to have any effect.
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.
- **vararg**: This method accepts any number of arguments after the ones described here.
- **constructor**: This method is used to construct a type.
- **static**: This method doesn't need an instance to be called, so it can be called directly using the class name.
- **operator**: This method describes a valid operator to use with this type as left-hand operand.
- **bitfield**: This value is an integer composed as a bitmask of the following flags.
- **void**: No return value.