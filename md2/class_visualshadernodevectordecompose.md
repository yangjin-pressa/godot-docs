# VisualShaderNodeVectorDecompose

## Inheritance
- **VisualShaderNodeVectorDecompose**  
  Inherits: `VisualShaderNodeVectorBase` → `VisualShaderNode` → `Resource` → `RefCounted` → `Object`

## Description
Decomposes a `Vector2`, `Vector3`, or 4D vector (represented as a `Quaternion`) into scalar values for use in the visual shader graph.

## Parameters
- Input: `vec2`, `vec3`, or `vec4` (vector of 2, 3, or 4 components)
- Output: Scalar components derived from the input vector

## Method Attributes
- **virtual** (This method should typically be overridden by the user to have any effect.)
- **const** (This method has no side effects. It doesn't modify any of the instance's member variables.)
- **vararg** (This method accepts any number of arguments after the ones described here.)
- **void** (No return value.)

## References
- :ref:`Vector2<class_Vector2>`  
- :ref:`Vector3<class_Vector3>`  
- :ref:`Quaternion<class_Quaternion>`  
- :ref:`VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>`  
- :ref:`VisualShaderNode<class_VisualShaderNode>`  
- :ref:`Resource<class_Resource>`  
- :ref:`RefCounted<class_RefCounted>`  
- :ref:`Object<class_Object>`