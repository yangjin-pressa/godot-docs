# PlaneMesh

## Inheritance
- **PlaneMesh** → [PrimitiveMesh](class_PrimitiveMesh.md) → [Mesh](class_Mesh.md) → [Resource](class_Resource.md) → [RefCounted](class_RefCounted.md) → [Object](class_Object.md)

## Inherited By
- [QuadMesh](class_QuadMesh.md)

## Description
A planar mesh that does not have thickness. By default, it is aligned on the X and Z axes. For billboarded materials, use `orientation = FACE_Z`.  
**Note:** UV jittering in large textured PlaneMeshes can be mitigated by increasing `subdivide_depth` and `subdivide_width`.

---

## Properties

### Center Offset
- **Type:** `Vector3`  
- **Default:** `Vector3(0, 0, 0)`  
- **Description:** Offset for the plane's center. Useful for particles.  
- **Methods:**  
  - `set_center_offset(value: Vector3)`  
  - `get_center_offset()`

### Orientation
- **Type:** `Orientation`  
- **Default:** `1`  
- **Description:** Direction the mesh faces.  
- **Methods:**  
  - `set_orientation(value: Orientation)`  
  - `get_orientation()`

### Size
- **Type:** `Vector2`  
- **Default:** `Vector2(2, 2)`  
- **Description:** Size of the plane.  
- **Methods:**  
  - `set_size(value: Vector2)`  
  - `get_size()`

### Subdivide Depth
- **Type:** `int`  
- **Default:** `0`  
- **Description:** Subdivision depth along the Z axis.  
- **Methods:**  
  - `set_subdivide_depth(value: int)`  
  - `get_subdivide_depth()`

### Subdivide Width
- **Type:** `int`  
- **Default:** `0`  
- **Description:** Subdivision depth along the X axis.  
- **Methods:**  
  - `set_subdivide_width(value: int)`  
  - `get_subdivide_width()`

---

## Enumerations

### Orientation
- **FACE_X** = `0`  
  - Mesh faces the positive X-axis.  
- **FACE_Y** = `1`  
  - Mesh faces the positive Y-axis (Godot 3.x behavior).  
- **FACE_Z** = `2`  
  - Mesh faces the positive Z-axis (QuadMesh behavior).  

---

## Notes
- Use `FACE_Z` for billboarded materials.  
- Adjust `subdivide_depth` and `subdivide_width` to reduce UV jittering in large textures.