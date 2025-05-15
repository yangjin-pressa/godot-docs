# VisualShaderNodeTexture2DArrayParameter

## Inheritance Hierarchy
- `VisualShaderNodeTextureParameter`  
  < `VisualShaderNodeTextureParameter`  
  < `VisualShaderNodeParameter`  
  < `VisualShaderNode`  
  < `Resource`  
  < `RefCounted`  
  < `Object`

## Description
A visual shader node for shader parameter (uniform) of type `Texture2DArray`.  
This parameter allows to provide a collection of textures for the shader. You can use `VisualShaderNodeTexture2DArray` to extract the textures from array.

## Method Attributes
- **virtual**: This method should typically be overridden by the user to have any effect.  
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.  
- **vararg**: This method accepts any number of arguments after the ones described here.  
- **constructor**: This method is used to construct a type.  
- **static**: This method doesn't need an instance to be called, so it can be called directly using the class name.  
- **operator**: This method describes a valid operator to use with this type as left-hand operand.  
- **bitfield**: This value is an integer composed as a bitmask of the following flags.  
- **void**: No return value.  

## Notes
- The node is used to pass a `Texture2DArray` uniform to a shader.  
- Use `VisualShaderNodeTexture2DArray` for extracting individual textures from the array.