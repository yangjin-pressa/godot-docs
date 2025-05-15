**Class Name**: VisualShaderNodeVaryingGetter  
**Inherits**: VisualShaderNodeVarying < VisualShaderNode < Resource < RefCounted < Object  

**Description**:  
- Outputs a value of a varying defined in the shader.  
- Requires a varying to be created with the mode set to **VisualShader.VARYING_MODE_VERTEX_TO_FRAG_LIGHT** for use in the Fragment shader.  

**Key Notes**:  
- The node must be used after defining a varying with the specified mode.  
- The varying mode is critical for the node to function correctly in the shader.  

**Citations**:  
- Reference to: `VisualShader.VARYING_MODE_VERTEX_TO_FRAG_LIGHT` (class_VisualShader_constant_VARYING_MODE_VERTEX_TO_FRAG_LIGHT)