# VisualShaderNodeVarying

**Inherits:** VisualShaderNode → Resource → RefCounted → Object  
**Inherited By:** VisualShaderNodeVaryingGetter, VisualShaderNodeVaryingSetter  

## Description  
Varying values are shader variables passed between shader functions, e.g., from Vertex to Fragment shaders.  

## Properties  
- **varying_name**: String (default: "[None]")  
- **varying_type**: VaryingType (default: 0)  

## Property Descriptions  
### varying_name  
- **Type**: String  
- **Default**: "[None]"  
- **Purpose**: Name of the variable (must be unique).  

### varying_type  
- **Type**: VaryingType  
- **Default**: 0  
- **Purpose**: Determines where the variable can be accessed.  

## Methods  
- **set_varying_name(value: String)**  
- **get_varying_name()**  

- **set_varying_type(value: VaryingType)**  
- **get_varying_type()**