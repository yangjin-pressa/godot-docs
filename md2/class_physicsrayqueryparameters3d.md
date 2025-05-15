# PhysicsRayQueryParameters3D

**Inherits:** RefCounted < Object

## Overview
Configures parameters for PhysicsDirectSpaceState3D.intersect_ray().

## Properties
- **collide_with_areas**: bool (default: false)  
  If true, includes Area3D objects in collision checks.

- **collide_with_bodies**: bool (default: true)  
  If true, includes PhysicsBody3D objects in collision checks.

- **collision_mask**: int (default: 4294967295)  
  Bitmask of physics layers to detect. Default includes all layers.

- **exclude**: Array of RID (default: empty)  
  List of objects to exclude from collisions. Changes to this array do not affect the original property.

- **from**: Vector3 (default: (0, 0, 0))  
  Starting point of the ray in global coordinates.

- **hit_back_faces**: bool (default: true)  
  If true, detects back faces of concave polygons or heightmaps.

- **hit_from_inside**: bool (default: false)  
  If true, detects hits starting inside shapes (normal becomes (0, 0, 0)).

- **to**: Vector3 (default: (0, 0, 0))  
  Ending point of the ray in global coordinates.

## Methods
### static PhysicsRayQueryParameters3D.create(
  from: Vector3, 
  to: Vector3, 
  collision_mask: int = 4294967295, 
  exclude: Array<RID> = []
)

Returns a new instance configured with common parameters.  
**Example usage:**
```gdscript
var query = PhysicsRayQueryParameters3D.create(position, position + Vector3(0, -10, 0))
var collision = get_world_3d().direct_space_state.intersect_ray(query)
```

## Notes
- The exclude property returns a copy of the array; modify the copy to update the property.  
- Collision mask documentation: [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)