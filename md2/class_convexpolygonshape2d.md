# ConvexPolygonShape2D

## Overview
- **Inherits**: Shape2D → Resource → RefCounted → Object
- **Purpose**: 2D convex polygon shape for physics collision
- **Key Features**:
  - Solid collision detection (detects objects fully inside)
  - Used internally in CollisionPolygon2D when in BUILD_SOLIDS mode
  - Faster collision checks than ConcavePolygonShape2D but slower than primitive shapes

## Properties
- **points**: PackedVector2Array = PackedVector2Array()
  - List of vertices forming a convex hull
  - Can be in clockwise or counterclockwise order
  - Warning: Must be a valid convex hull; use set_point_cloud() for convex hull generation

## Methods
- **set_point_cloud(point_cloud: PackedVector2Array)**
  - Generates convex hull from arbitrary points
  - Updates points property with convex hull algorithm
  - Uses Geometry2D.convex_hull() for calculation

## Notes
- Points property returns a copied array; changes to the array do not update the original
- Convex decomposition allows complex concave collisions using multiple ConvexPolygonShape2D nodes
- Performance considerations: suitable for medium-sized objects where primitive shapes are insufficient

## Related Concepts
- CollisionPolygon2D.BUILD_SOLIDS mode
- Geometry2D.convex_hull() method
- PackedVector2Array class for vertex data