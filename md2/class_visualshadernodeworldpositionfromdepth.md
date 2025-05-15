# VisualShaderNodeWorldPositionFromDepth

**Inherits:**  
- VisualShaderNode  
- Resource  
- RefCounted  
- Object  

**Description:**  
- Calculates the position of the pixel in world space using the depth texture.  
- Used to obtain world space UVs for projection mapping (e.g., Caustics).  

**Key Functionality:**  
- Reconstructs depth position for world space coordinates.  
- Enables spatial mapping techniques requiring world-space data.  

**Documentation Notes:**  
- Inheritance chain reflects the class hierarchy in the Godot engine.  
- The node is designed for shader graph operations, leveraging depth textures for 3D reconstruction.