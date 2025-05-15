- **Class Name**: VisualShaderNodeTextureSDFNormal  
- **Inheritance**:  
  - VisualShaderNode  
  - Resource  
  - RefCounted  
  - Object  

- **Description**:  
  - Performs an SDF (signed-distance field) normal texture lookup within the visual shader graph.  
  - Translates to `texture_sdf_normal(sdf_pos)` in the shader language.  

- **Key Functionality**:  
  - Operates as a node in the visual shader graph for normal texture calculations.  
  - Utilizes SDF (signed-distance field) input to compute normals.  

- **Shader Equivalent**:  
  - `texture_sdf_normal(sdf_pos)`