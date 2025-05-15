# VisualShaderNodeTransformCompose

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

## Description
Creates a 4×4 transform matrix using four vectors of type `vec3`. Each vector is one row in the matrix and the last column is a `vec4(0, 0, 0, 1)`.

## Key Attributes
- **Purpose**: Composes a `Transform3D` from four `Vector3` inputs
- **Matrix Construction**: 
  - First three columns are the input vectors
  - Last column is `vec4(0, 0, 0, 1)` for affine transformation
- **Usage Context**: Visual shader graph node for 3D transformations

## Method Characteristics
- **Virtual**: Methods typically need overriding by users
- **Const**: No side effects, does not modify instance variables
- **Vararg**: Accepts variable arguments after defined parameters
- **Constructor**: Used to instantiate the class
- **Static**: Can be called directly using the class name
- **Operator**: Valid operator for type as left-hand operand
- **Bitfield**: Integer bitmask for flag combinations
- **Void**: No return value

## References
- [Godot Engine Documentation](https://godotengine.org/)