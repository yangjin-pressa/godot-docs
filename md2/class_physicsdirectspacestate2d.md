# PhysicsDirectSpaceState2D

## Overview
Provides direct access to a physics space in the PhysicsServer2D. Used for querying objects and areas in a physics space.

## Tutorials
- Physics introduction
- Ray-casting

## Methods

- **cast_motion**  
  Parameters: PhysicsShapeQueryParameters2D  
  Return: PackedFloat32Array  
  Checks motion collision safety. Returns safe/unsafe proportions (0-1). Ignores existing collisions.

- **collide_shape**  
  Parameters: PhysicsShapeQueryParameters2D, max_results (32)  
  Return: Array<Vector2>  
  Detects shape intersections. Returns contact points. Limits results to save time.

- **get_rest_info**  
  Parameters: PhysicsShapeQueryParameters2D  
  Return: Dictionary  
  Provides collision details: collider ID, velocity, normal, point, RID, shape.

- **intersect_point**  
  Parameters: PhysicsPointQueryParameters2D, max_results (32)  
  Return: Array<Dictionary>  
  Checks if a point is inside solid shapes. Returns intersecting objects. Note: ConcavePolygonShape2D and CollisionPolygon2D in Segments mode are not solid.

- **intersect_ray**  
  Parameters: PhysicsRayQueryParameters2D  
  Return: Dictionary  
  Detects ray intersections. Returns: collider, normal, position, RID, shape. Returns empty dict if no collision.

- **intersect_shape**  
  Parameters: PhysicsShapeQueryParameters2D, max_results (32)  
  Return: Array<Dictionary>  
  Identifies intersecting shapes. Returns: collider, collider ID, RID, shape. Limits results to reduce processing time.

## Notes
- Methods are used for physics space queries.
- Collision detection considers shape parameters and returns detailed intersection data.
- Special cases (e.g., concave shapes) may not trigger collisions.