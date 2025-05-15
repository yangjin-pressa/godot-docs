# PhysicsPointQueryParameters2D

**Inherits**: RefCounted < Object

## Description
Configures parameters for PhysicsDirectSpaceState2D.intersect_point() by modifying properties like point position.

## Properties

- **canvas_instance_id**: int = 0  
  Restricts query to specific canvas layer (0 = default)
- **collide_with_areas**: bool = false  
  Includes Area2D objects in query
- **collide_with_bodies**: bool = true  
  Includes PhysicsBody2D objects in query
- **collision_mask**: int = 4294967295  
  Bitmask of physics layers to detect (default: all)
- **exclude**: Array<RID> = []  
  List of RIDs to exclude from collision
- **position**: Vector2 = Vector2(0, 0)  
  Query position in global coordinates

## Property Descriptions

### canvas_instance_id
- **set_canvas_instance_id**(value: int): void  
- **get_canvas_instance_id**(): int  
  Controls canvas layer restriction

### collide_with_areas
- **set_collide_with_areas**(value: bool): void  
- **is_collide_with_areas_enabled**(): bool  
  Enables/disables Area2D detection

### collide_with_bodies
- **set_collide_with_bodies**(value: bool): void  
- **is_collide_with_bodies_enabled**(): bool  
  Enables/disables PhysicsBody2D detection

### collision_mask
- **set_collision_mask**(value: int): void  
- **get_collision_mask**(): int  
  Configures collision layer detection (see [Collision Layers and Masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks))

### exclude
- **set_exclude**(value: Array<RID>): void  
- **get_exclude**(): Array<RID]  
  Excludes specific objects from collisions (use CollisionObject2D.get_rid() to get RIDs)

### position
- **set_position**(value: Vector2): void  
- **get_position**(): Vector2  
  Sets/query position in global coordinates

## Notes
- Exclude array returns a copy; changes require reassignment
- Collision mask uses bitmask notation for layer detection