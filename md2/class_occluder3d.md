# Occluder3D

**Inherits:** Resource < RefCounted < Object  
**Inherited By:** ArrayOccluder3D, BoxOccluder3D, PolygonOccluder3D, QuadOccluder3D, SphereOccluder3D  

**Purpose:**  
A resource for defining occluder shapes used in occlusion culling with `OccluderInstance3D`.  

---

## Tutorials  
- [Occlusion culling](../tutorials/3d/occlusion_culling)  

---

## Methods  
- **get_indices**  
  Returns the occluder shape's vertex indices.  
  - Type: `PackedInt32Array`  
  - `const`: No side effects.  

- **get_vertices**  
  Returns the occluder shape's vertex positions.  
  - Type: `PackedVector3Array`  
  - `const`: No side effects.  

---

## Related Classes  
See [OccluderInstance3D](class_OccluderInstance3D) documentation for setup instructions.