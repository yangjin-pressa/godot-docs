**Class Name**: CSGBox3D  
**Inherits**: CSGPrimitive3D → CSGShape3D → GeometryInstance3D → VisualInstance3D → Node3D → Node → Object  

---

### Description  
A node for creating a box to use with the CSG system.  

**Note**: CSG nodes are intended for level prototyping. They have higher CPU costs compared to MeshInstance3D with PrimitiveMesh. Moving CSG nodes within other CSG nodes is costly during gameplay.  

**Tutorials**:  
- [Prototyping levels with CSG](../tutorials/3d/csg_tools)  

---

### Properties  
- **Material**: `Material` (default: none)  
  - **Methods**:  
    - `set_material(value: Material)`  
    - `get_material()`  
  - **Description**: Material used to render the box.  

- **Size**: `Vector3(1, 1, 1)`  
  - **Methods**:  
    - `set_size(value: Vector3)`  
    - `get_size()`  
  - **Description**: Box's width, height, and depth.  

---

### Key Points  
- CSGBox3D is a 3D shape for constructive solid geometry (CSG) operations.  
- CPU cost: Higher than standard mesh-based shapes for real-time gameplay.  
- Size defaults to a unit cube (1x1x1).  
- Material can be customized via `set_material()` and `get_material()`.  

--- 

### References  
- [Material class](class_Material)  
- [Vector3 class](class_Vector3)