# PointMesh

## Hierarchy
- **PointMesh**  
  - Inherits: `PrimitiveMesh`  
    - Inherits: `Mesh`  
      - Inherits: `Resource`  
        - Inherits: `RefCounted`  
          - Inherits: `Object`  

## Description
- **Purpose**: A mesh consisting of a single point, rendered as a rectangle with constant size.  
- **Use Cases**:  
  - Used with Particle systems.  
  - Can act as a cheap billboarded sprite (e.g., point cloud).  
- **Material Requirements**:  
  - Must use a material with a defined point size.  
  - Point size can be accessed in shaders via ` POINT_SIZE `.  
  - In `BaseMaterial3D`, set `use_point_size` and `point_size` properties.  
- **Ignored Properties**:  
  - Billboard mode, grow, and cull face settings.  

## Notes
- Properties altering vertices (e.g., billboard mode) are ignored when using PointMesh.  
- Rendering is based on a single rectangle, not triangle data.