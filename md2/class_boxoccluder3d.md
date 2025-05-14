# BoxOccluder3D

**Inherits**: Occluder3D < Resource < RefCounted < Object

Cuboid shape for use with occlusion culling in [OccluderInstance3D](../tutorials/3d/occlusion_culling).

---

## Description

BoxOccluder3D stores a cuboid shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D](../tutorials/3d/occlusion_culling) for instructions on setting up occlusion culling.

---

## Properties

- **size**: Vector3 = (1, 1, 1)

---

## Property Descriptions

### size

**Type**: Vector3  
**Default**: (1, 1, 1)  
**Description**: The box's size in 3D units.

Methods:
- `void set_size(value: Vector3)`: virtual (override)
- `Vector3 get_size()`: const (no side effects)