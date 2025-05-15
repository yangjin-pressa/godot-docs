**Class:** VisualShaderNodeUIntParameter  
**Inherits:** VisualShaderNodeParameter, VisualShaderNode, Resource, RefCounted, Object  

**Description**  
A VisualShaderNodeParameter of type unsigned int. Offers additional customization for range of accepted values.  

**Properties**  
- **default_value**: int, default 0  
- **default_value_enabled**: bool, default false  

**Property Descriptions**  
- **default_value**  
  - **Set**: set_default_value(value: int)  
  - **Get**: get_default_value()  
  - Default value of this parameter. Must have default_value_enabled enabled for it to take effect.  

- **default_value_enabled**  
  - **Set**: set_default_value_enabled(value: bool)  
  - **Get**: is_default_value_enabled()  
  - If true, the node uses a custom default value.  

**Notes**  
- The default_value is only applied if default_value_enabled is enabled.