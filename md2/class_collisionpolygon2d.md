# CollisionPolygon2D

## Description
A node that provides a polygon shape to a `CollisionObject2D` parent, allowing for dynamic adjustment of the shape. The shape can be concave or convex, and is used for collision detection, solid object behavior, and other physics-related tasks.

**Warning:** Non-uniform scaling may cause unexpected behavior.

---

## Properties
- **build_mode**: `BuildMode`, default `0`  
  *Collision build mode. Use one of the `BuildMode` constants.*

- **disabled**: `bool`, default `false`  
  *Whether the shape is disabled or not.*

- **one_way_collision**: `bool`, default `false`  
  *Enables one-way collision behavior for this shape.*

- **one_way_collision_margin**: `float`, default `1.0`  
  *A margin value for one-way collision adjustments.*

- **polygon**: `PackedVector2Array`, default `empty`  
  *A list of vertices defining the polygon shape. Coordinates are in local space.*

---

## Enumerations
### BuildMode
- **BUILD_SOLIDS**  
  Uses solid collision detection for the shape.

- **BUILD_SEGMENTS**  
  Treats the shape as a series of line segments for collision detection.

---

## Notes
- The `polygon` property's vertices are defined in local space relative to the node.
- The `one_way_collision` flag affects how collisions are resolved with other objects.
- The `one_way_collision_margin` adjusts the distance for one-way collision interactions.