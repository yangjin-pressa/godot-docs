# PhysicsPointQueryParameters3D

**Inherits:** RefCounted < Object

## Description
Configure parameters for `PhysicsDirectSpaceState3D.intersect_point()` by modifying properties like point position.

## Properties

- **collide_with_areas** (bool) = false  
  If true, the query will consider Area3D instances.

- **collide_with_bodies** (bool) = true  
  If true, the query will consider PhysicsBody3D instances.

- **collision_mask** (int) = 4294967295  
  Physics layers to detect (bitmask). Default: all layers.

- **exclude** (Array<RID>) = []  
  List of RIDs to exclude from collisions. Changes to the array do not affect the property; reassign to update.

- **position** (Vector3) = Vector3(0, 0, 0)  
  Global coordinates for the query.

## Method Definitions

- **set_collide_with_areas**(value: bool)  
- **is_collide_with_areas_enabled**()  

- **set_collide_with_bodies**(value: bool)  
- **is_collide_with_bodies_enabled**()  

- **set_collision_mask**(value: int)  
- **get_collision_mask**()  

- **set_exclude**(value: Array<RID>)  
- **get_exclude**()  

- **set_position**(value: Vector3)  
- **get_position**()  

## Notes
The `exclude` property returns a copied array. Modifications to the returned array do not update the original property value. To update, modify the array and reassign it.