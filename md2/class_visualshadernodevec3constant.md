# VisualShaderNodeVec3Constant

## Inheritance Hierarchy
- `VisualShaderNodeVec3Constant`  
  ← `VisualShaderNodeConstant`  
  ← `VisualShaderNode`  
  ← `Resource`  
  ← `RefCounted`  
  ← `Object`

## Description
A constant `Vector3` node for use in visual shader graphs. Provides a way to define a fixed `Vector3` value within the shader graph.

## Properties
- **constant**: `Vector3` = `Vector3(0, 0, 0)`

## Property Descriptions
### constant
- **Type**: `Vector3`  
- **Default Value**: `Vector3(0, 0, 0)`  
- **Function**: Represents the value of this node in the shader graph.

## Methods
- **set_constant(value: Vector3)**: Sets the constant value.  
- **get_constant()**: Retrieves the current constant value.

## Notes
- **virtual**: This method should typically be overridden by the user to have any effect.  
- **const**: This method has no side effects; it only returns a value.  
- **vararg**: This method accepts any number of arguments after the ones described.  
- **constructor**: Used to construct an instance of this class.  
- **static**: Can be called directly using the class name.  
- **operator**: Describes valid operators for this type.  
- **bitfield**: The value is an integer composed as a bitmask.  
- **void**: No return value.  

## References
- [Property constant details](#class_VisualShaderNodeVec3Constant_property_constant)