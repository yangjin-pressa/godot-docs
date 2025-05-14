# ConvexPolygonShape3D

**Inherits**: Shape3D → Resource → RefCounted → Object

A 3D convex polyhedron shape for physics collision. Used for collision detection with solid objects, unlike hollow shapes.

## Description
- **Solid**: Detects collisions from objects fully inside it.
- **Convex decomposition**: Concave shapes can be split into multiple convex shapes for complex collisions (performance cost).
- **Performance**: Faster than ConcavePolygonShape3D but slower than primitives like SphereShape3D and BoxShape3D. Best for medium-sized objects not representable by primitives.

## Tutorials
- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)_

## Properties
- **points**: PackedVector3Array (default: empty)  
  List of 3D points forming the convex polygon.  
  **Note**: The returned array is copied; changes to it do not update the original.

## Methods
- **set_points(value: PackedVector3Array)**: Sets the points array.  
- **get_points()**: Returns a copied version of the points array.

## Notes
- Use **MeshInstance3D** to decompose meshes into convex shapes via "Create Multiple Convex Collision Siblings" or script calls.