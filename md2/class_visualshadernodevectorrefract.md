# VisualShaderNodeVectorRefract

## Class Hierarchy
- Inherits: VisualShaderNodeVectorBase  
- Inherits: VisualShaderNode  
- Inherits: Resource  
- Inherits: RefCounted  
- Inherits: Object  

## Description
Returns the vector that points in the direction of refraction.  
Translated to `refract(I, N, eta)` in the shader language, where:  
- `I` is the incident vector  
- `N` is the normal vector  
- `eta` is the ratio of the indices of refraction  

## Method Notes
- **virtual**: This method should typically be overridden by the user to have any effect.  
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.  
- **vararg**: This method accepts any number of arguments after the ones described here.  
- **void**: No return value.