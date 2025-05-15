# VisualShaderNodeUIntConstant

**Inherits:** VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted < Object

## Description
An unsigned scalar integer constant to be used within the visual shader graph. Translated to `uint` in the shader language.

## Properties
- **constant**: int = 0

## Property Descriptions
- **constant**: An unsigned integer constant which represents a state of this node.

## Methods
- **set_constant(value: int)**: void  
  Sets the value of the constant.
  
- **get_constant()**: int  
  Retrieves the value of the constant.

## Notes
- **set_constant**: This method should typically be overridden by the user to have any effect.
- **get_constant**: This method has no side effects. It doesn't modify any of the instance's member variables.