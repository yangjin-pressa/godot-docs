**Class Name**: VisualShaderNodeVectorLen  
**Inherits**: VisualShaderNodeVectorBase → VisualShaderNode → Resource → RefCounted → Object  

**Description**:  
- Returns the length of a `Vector3` within the visual shader graph.  
- Translated to `length(p0)` in the shader language.  

**Key Behavior**:  
- **Virtual Method**: This method should typically be overridden by the user to have any effect.  
- **Const Method**: This method has no side effects. It doesn't modify any of the instance's member variables.  
- **Shader Translation**: Directly maps to the shader function `length(p0)`.  

**Documentation Notes**:  
- The class is part of the Godot engine's visual shader graph system.  
- Designed for vector operations, specifically calculating the magnitude of a 3D vector.