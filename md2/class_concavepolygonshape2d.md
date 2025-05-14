# ConcavePolygonShape2D

**Inherits:** Shape2D < Resource < RefCounted < Object

## Description

A 2D polyline shape for physics collision. Used internally in CollisionPolygon2D when in BUILD_SEGMENTS mode.

Key characteristics:
- Composed of interconnected line segments
- Most configurable 2D shape
- Hollow by default (even if enclosed)
- Not suitable for physics detection
- Best for level geometry

**Note:** For collision, works with static bodies like StaticBody2D. Not recommended for CharacterBody2D or RigidBody2D.

**Warning:** Fast-moving objects may clip through this shape due to hollow nature.

**Performance:** Slowest 2D collision shape. Use cautiously.

## Properties

Property: segments
Type: PackedVector2Array
Default: PackedVector2Array()

## Property Description

The array of points defining the shape's line segments:
- Length is even, divided into pairs (start/end of segments)
- Each pair represents a single segment
- The returned array is a copy; changes don't affect the original

**Usage:** 
- For closed polygons, use CollisionPolygon2D's BUILD_SOLIDS mode
- Decomposes into convex shapes (ConvexPolygonShape2D)

## Notes
- Shape is hollow by default
- Not suitable for collision detection
- Best for level geometry
- Performance: slowest 2D shape

## Related Classes
- CollisionPolygon2D: For polygon decomposition
- ConvexPolygonShape2D: For convex shapes
- StaticBody2D: Compatible with this shape
- CharacterBody2D: Not suitable for this shape

## Important
- Use this shape for static geometry
- Avoid for dynamic physics bodies
- Consider alternative shapes for performance
- For closed polygons, use BUILD_SOLIDS mode in CollisionPolygon2D