# WorldBoundaryShape3D

**Inherits:** Shape3D → Resource → RefCounted → Object

## Description
A 3D world boundary shape for physics collision. Functions as an infinite plane that restricts physics bodies to "above" it. The **plane** property defines the direction of "above." Used for endless flat floors.

**Note:** With Jolt Physics engine, this shape has finite size (adjustable via ProjectSettings).

## Properties
- **plane**: Plane(0, 1, 0, 0)  
  A Plane object defining the boundary. Normal vector determines "above" direction.

## Method References
- **set_plane(value: Plane)**: Sets the plane property.  
- **get_plane()**: Retrieves the plane property.

## Notes
- **Jolt Physics** setting affects shape size (see: `ProjectSettings.physics/jolt_physics_3d/limits/world_boundary_shape_size`).  
- **plane** property references: `Plane` class (see: `Plane` documentation).