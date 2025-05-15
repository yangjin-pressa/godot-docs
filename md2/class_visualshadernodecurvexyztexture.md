**Class:** VisualShaderNodeCurveXYZTexture  
**Inherits:**  
- VisualShaderNodeResizableBase  
  - VisualShaderNode  
    - Resource  
      - RefCounted  
        - Object  

**Description:**  
Performs a CurveXYZTexture lookup within the visual shader graph. Includes a built-in editor for texture curves.  

**Properties:**  
- **texture**:  
  - Type: CurveXYZTexture  
  - Description: Source texture.  

**Methods:**  
- **set_texture(value: CurveXYZTexture)**:  
  - Virtual method to set the texture.  
- **get_texture()**:  
  - Const method to retrieve the texture.  

**Notes:**  
- Methods are virtual (overrideable) and const (no side effects).  
- The class is part of the Godot engine's visual shader graph system.