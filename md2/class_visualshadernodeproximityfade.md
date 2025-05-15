# VisualShaderNodeProximityFade

**Inherits:**  
- VisualShaderNode  
- Resource  
- RefCounted  
- Object  

**Description:**  
- The proximity fade effect fades out each pixel based on its distance to another object.  

**Key Concepts:**  
- This node is used to create an effect where pixels are faded out depending on their proximity to a target object.  
- The effect is calculated based on distance, with pixels farther away fading more.  

**Usage:**  
- Connect this node to a shader to apply the fade effect to a material.  
- The node requires a target object or geometry to calculate proximity.