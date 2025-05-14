# CSGSphere3D

## Hierarchy
- `CSGSphere3D` → `CSGPrimitive3D` → `CSGShape3D` → `GeometryInstance3D` → `VisualInstance3D` → `Node3D` → `Node` → `Object`

## Description
A CSG Sphere shape.  
**Note:** CSG nodes are intended for level prototyping. They have higher CPU costs than `MeshInstance3D` with `PrimitiveMesh`. Moving CSG nodes within other CSG nodes is inefficient during gameplay.

## Tutorials
- [Prototyping levels with CSG](../tutorials/3d/csg_tools)

## Properties
- **Material**: `Material` (default: none)  
  The material used to render the sphere.  
  - `set_material(value: Material)`  
  - `get_material()`

- **radial_segments**: `int` (default: 12)  
  Number of vertical slices for the sphere.  
  - `set_radial_segments(value: int)`  
  - `get_radial_segments()`

- **radius**: `float` (default: 0.5)  
  Radius of the sphere.  
  - `set_radius(value: float)`  
  - `get_radius()`

- **rings**: `int` (default: 6)  
  Number of horizontal slices for the sphere.  
  - `set_rings(value: int)`  
  - `get_rings()`

- **smooth_faces**: `bool` (default: true)  
  If `true`, the sphere appears smooth. If `false`, it has a flat shaded look.  
  - `set_smooth_faces(value: bool)`  
  - `get_smooth_faces()`