# Shape3D

## Inheritance
- `Resource` → `RefCounted` → `Object`

## Inherited By
- BoxShape3D  
- CapsuleShape3D  
- ConcavePolygonShape3D  
- ConvexPolygonShape3D  
- CylinderShape3D  
- HeightMapShape3D  
- SeparationRayShape3D  
- SphereShape3D  
- WorldBoundaryShape3D  

## Description
Abstract base class for 3D shapes used in physics.  
- **Performance:** Primitive shapes like SphereShape3D are fast for collision checks. ConvexPolygonShape3D and HeightMapShape3D are slower, with ConcavePolygonShape3D being the slowest.

## Tutorials
- [Physics introduction](../tutorials/physics/physics_introduction)

## Properties
- **custom_solver_bias** (float) = 0.0  
  - Sets custom solver bias for contact separation. Default uses project settings.  
  - Methods: `set_custom_solver_bias(value: float)`, `get_custom_solver_bias()`

- **margin** (float) = 0.04  
  - Collision margin; higher values improve performance but reduce accuracy.  
  - Methods: `set_margin(value: float)`, `get_margin()`

## Methods
- **get_debug_mesh()** → `ArrayMesh`  
  - Returns mesh for visualizing collision debug data.

## Notes
- `margin` is not used in Godot Physics.  
- `custom_solver_bias` affects how bodies react to enforce contact separation.  

## References
- [SphereShape3D](class_SphereShape3D)  
- [ConvexPolygonShape3D](class_ConvexPolygonShape3D)  
- [HeightMapShape3D](class_HeightMapShape3D)