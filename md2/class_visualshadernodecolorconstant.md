**Class Name**: VisualShaderNodeColorConstant  
**Inherits**: VisualShaderNodeConstant → VisualShaderNode → Resource → RefCounted → Object  

**Description**:  
- Outputs two ports: RGB as `vec3` and alpha as `float` for a `Color` value.  

**Properties**:  
- **constant**:  
  - Type: `Color`  
  - Default: `Color(1, 1, 1, 1)`  

**Property Descriptions**:  
- **constant**:  
  - Represents the color value for this node.  
  - Methods:  
    - `set_constant(value: Color)`: Sets the color value.  
    - `get_constant()`: Retrieves the color value.  

**Citations**:  
- [constant property](class_VisualShaderNodeColorConstant_property_constant)