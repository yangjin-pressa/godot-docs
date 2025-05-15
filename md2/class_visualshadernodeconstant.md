# VisualShaderNodeConstant

## Class Overview

- **Inherits**: VisualShaderNode < Resource < RefCounted < Object  
- **Inherited By**:  
  - VisualShaderNodeBooleanConstant  
  - VisualShaderNodeColorConstant  
  - VisualShaderNodeFloatConstant  
  - VisualShaderNodeIntConstant  
  - VisualShaderNodeTransformConstant  
  - VisualShaderNodeUIntConstant  
  - VisualShaderNodeVec2Constant  
  - VisualShaderNodeVec3Constant  
  - VisualShaderNodeVec4Constant  

## Description

- **Abstract class**: This is a base type for constants in the visual shader graph.  
- **Derived types**: See individual derived classes for details on possible values.  

## Key Attributes

- **Purpose**: Serves as a base for constant nodes in visual shader graphs.  
- **Usage**: Abstract class requires implementation via derived types.  

## Method Behavior

- **Virtual methods**: Typically overridden by derived classes for specific behavior.  
- **Static methods**: May be called directly using the class name.  
- **Const methods**: Do not modify instance variables or state.  

## Notes

- This class is part of the Godot engine's visual shader graph system.  
- Derived classes implement specific constant types (e.g., boolean, float, vector).