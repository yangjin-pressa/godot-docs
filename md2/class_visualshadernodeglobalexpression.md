# VisualShaderNodeGlobalExpression

**Inherits:** VisualShaderNodeExpression < VisualShaderNodeGroupBase < VisualShaderNodeResizableBase < VisualShaderNode < Resource < RefCounted < Object

## Description
- A custom global visual shader graph expression written in Godot Shading Language
- Allows placement of function definitions for later use in VisualShaderNodeExpression nodes
- Supports declaration of varyings, uniforms, and global constants

## Key Features
- **virtual** (This method should typically be overridden by the user to have any effect.)
- **const** (This method has no side effects. It doesn't modify any of the instance's member variables.)
- **vararg** (This method accepts any number of arguments after the ones described here.)
- **constructor** (This method is used to construct a type.)
- **static** (This method doesn't need an instance to be called, so it can be called directly using the class name.)
- **operator** (This method describes a valid operator to use with this type as left-hand operand.)
- **bitfield** (This value is an integer composed as a bitmask of the following flags.)
- **void** (No return value.)

## Usage Notes
- Functions defined here can be called from VisualShaderNodeExpression nodes
- Provides a way to define global shader variables and helper functions
- Works within the context of the main shader functions in the generated shader code