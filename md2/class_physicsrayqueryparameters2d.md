# PhysicsRayQueryParameters2D

**Inherits:** RefCounted < Object

## Overview
Provides parameters for PhysicsDirectSpaceState2D.intersect_ray().

## Properties
- **collide_with_areas**: bool = false  
  If true, the query will take Area2D objects into account.
- **collide_with_bodies**: bool = true  
  If true, the query will take PhysicsBody2D objects into account.
- **collision_mask**: int = 4294967295  
  Physics layers the query will detect (bitmask). Default: all layers.
- **exclude**: Array[RID] = []  
  List of object RIDs to exclude from collisions. Changes to the returned array do not update the original.
- **from**: Vector2 = Vector2(0, 0)  
  Starting point of the ray in global coordinates.
- **hit_from_inside**: bool = false  
  If true, detects hits when starting inside shapes. Normal is Vector2(0, 0).
- **to**: Vector2 = Vector2(0, 0)  
  Ending point of the ray in global coordinates.

## Methods
- **create(from: Vector2, to: Vector2, collision_mask: int = 4294967295, exclude: Array[RID] = [])** (static)  
  Returns a new pre-configured PhysicsRayQueryParameters2D object.  
  Example:  
  ```  
  var query = PhysicsRayQueryParameters2D.create(global_position, global_position + Vector2(0, 100))  
  var collision = get_world_2d().direct_space_state.intersect_ray(query)  
  ```

## Notes
- Use CollisionObject2D.get_rid() to get RIDs for exclusion.  
- Collision layers and masks: [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)