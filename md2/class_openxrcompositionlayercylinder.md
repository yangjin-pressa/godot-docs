**Class Name:** OpenXRCompositionLayerCylinder  
**Experimental:** May change or be removed in future versions.  

**Inherits:**  
- OpenXRCompositionLayer  
  - Node3D  
    - Node  
      - Object  

**Description**  
An OpenXR composition layer that allows rendering a SubViewport on an internal slice of a cylinder.  

**Properties**  
- **aspect_ratio** (float): 1.0  
  - The aspect ratio of the slice. Used to set the height relative to the width.  
  - Set/Get: `set_aspect_ratio(value: float)`, `get_aspect_ratio()`

- **central_angle** (float): 1.5708  
  - The central angle of the cylinder. Used to set the width.  
  - Set/Get: `set_central_angle(value: float)`, `get_central_angle()`

- **fallback_segments** (int): 10  
  - The number of segments to use in the fallback mesh.  
  - Set/Get: `set_fallback_segments(value: int)`, `get_fallback_segments()`

- **radius** (float): 1.0  
  - The radius of the cylinder.  
  - Set/Get: `set_radius(value: float)`, `get_radius()`  

**Notes**  
- This class is part of the Godot engine's OpenXR module.  
- Properties define parameters for rendering a cylindrical slice in OpenXR.