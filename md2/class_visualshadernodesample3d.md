**Class Name:** VisualShaderNodeSample3D  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  

**Inherited By:** VisualShaderNodeTexture2DArray, VisualShaderNodeTexture3D  

**Description:**  
A virtual class, use the descendants instead.  

**Properties**  
- **source**:  
  - Type: Source  
  - Default: 0  
  - Description: An input source type.  

**Enumerations**  
**Source**  
- **SOURCE_TEXTURE** = 0  
  - Creates internal uniform and provides a way to assign it within node.  
- **SOURCE_PORT** = 1  
  - Use the uniform texture from sampler port.  
- **SOURCE_MAX** = 2  
  - Represents the size of the Source enum.  

**Property Descriptions**  
- **source**  
  - **set_source(value: Source)**: Sets the source type.  
  - **get_source()**: Retrieves the current source type.  

**Methods**  
- **set_source(value: Source)**: Sets the source type.  
- **get_source()**: Retrieves the current source type.