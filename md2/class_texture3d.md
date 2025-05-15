**Texture3D**  

**Inherits**  
- Texture  
- Resource  
- RefCounted  
- Object  

**Inherited by**  
- PlaceholderTexture3D  

**Description**  
Texture3D is the base class for 3D textures. All images must have the same width, height, and mipmap levels.  

**Methods**  
1. **_get_data**  
   - **Return Type**: Array of Image  
   - **Attributes**: Virtual (This method should typically be overridden by the user to have any effect.)  
   - **Description**: This method has no side effects. It doesn't modify any of the instance's member variables.  

2. **_get_depth**  
   - **Return Type**: int  
   - **Attributes**: Virtual (This method should typically be overridden by the user to have any effect.)  
   - **Description**: This method has no side effects. It doesn't modify any of the instance's member variables.  

3. **_get_format**  
   - **Return Type**: Format  
   - **Attributes**: Virtual (This method should typically be overridden by the user to have any effect.)  
   - **Description**: This method has no side effects. It doesn't modify any of the instance's member variables.  

4. **_get_height**  
   - **Return Type**: int  
   - **Attributes**: Virtual (This method should typically be overridden by the user to have any effect.)  
   - **Description**: This method has no side effects. It doesn't modify any of the instance's member variables.  

5. **_get_width**  
   - **Return Type**: int  
   - **Attributes**: Virtual (This method should typically be overridden by the user to have any effect.)  
   - **Description**: This method has no side effects. It doesn't modify any of the instance's member variables.  

6. **_has_mipmaps**  
   - **Return Type**: bool  
   - **Attributes**: Virtual (This method should typically be overridden by the user to have any effect.)  
   - **Description**: This method has no side effects. It doesn't modify any of the instance's member variables.  

7. **create_placeholder**  
   - **Return Type**: Resource  
   - **Attributes**: Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  
   - **Description**: This method creates a placeholder resource.  

8. **get_data**  
   - **Return Type**: Array of Image  
   - **Attributes**: Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  
   - **Description**: This method retrieves the data of the texture.  

9. **get_depth**  
   - **Return Type**: int  
   - **Attributes**: Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  
   - **Description**: This method retrieves the depth of the texture.  

10. **get_height**  
    - **Return Type**: int  
    - **Attributes**: Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  
    - **Description**: This method retrieves the height of the texture.  

11. **get_width**  
    - **Return Type**: int  
    - **Attributes**: Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  
    - **Description**: This method retrieves the width of the texture.  

12. **has_mipmaps**  
    - **Return Type**: bool  
    - **Attributes**: Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  
    - **Description**: This method checks whether mipmaps are enabled for the texture.