**Class Hierarchy**  
QuadMesh  
├─ PlaneMesh  
│  └─ PrimitiveMesh  
│     └─ Mesh  
│        └─ Resource  
│           └─ RefCounted  
│              └─ Object  

**Description**  
- Represents a square mesh facing the camera.  
- Inherits from PlaneMesh, which is a flat, thicknessless mesh.  
- Default orientation is `PlaneMesh.FACE_Z` (Z-axis).  
- Aligns with X/Y axes, suitable for billboarded materials.  

**Tutorials**  
- [GUI in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2807)  
- [2D in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2803)  

**Properties**  
- **orientation**: `PlaneMesh.Orientation` (default: `2`)  
  - Overrides `PlaneMesh.orientation` to set face direction.  
- **size**: `Vector2` (default: `Vector2(1, 1)`)  
  - Overrides `PlaneMesh.size` to define square dimensions.  

**Key Notes**  
- This class is equivalent to PlaneMesh but with a fixed default orientation.  
- Properties override base class settings for consistent behavior.