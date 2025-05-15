# PhysicsDirectSpaceState3D

**Inherits:** Object  
**Inherited By:** PhysicsDirectSpaceState3DExtension  

## Description  
Provides direct access to a physics space in PhysicsServer3D. Used for querying objects and areas in a given space.  

## Tutorials  
- Physics introduction: [../tutorials/physics/physics_introduction](../tutorials/physics/physics_introduction)  
- Ray-casting: [../tutorials/physics/ray-casting](../tutorials/physics/ray-casting)  

## Methods  

### cast_motion  
**Returns:** `PackedFloat32Array`  
**Parameters:** `PhysicsShapeQueryParameters3D`  
**Description:** Checks how far a shape can move without colliding. Returns safe/unsafe motion proportions.  
**Note:** Colliding shapes are ignored. Use `collide_shape()` to find them.  

### collide_shape  
**Returns:** `Array<Vector3>`  
**Parameters:** `PhysicsShapeQueryParameters3D`, `max_results=32`  
**Description:** Finds intersection points between a shape and other objects.  
**Note:** Does not consider the `motion` property of the object.  

### get_rest_info  
**Returns:** `Dictionary`  
**Parameters:** `PhysicsShapeQueryParameters3D`  
**Description:** Returns details about the first collision (e.g., collider, normal, position).  
**Note:** Valid only for ConcavePolygonShape3D.  

### intersect_ray  
**Returns:** `Dictionary`  
**Parameters:** `PhysicsRayQueryParameters3D`  
**Description:** Finds intersection of a ray with a shape. Returns normal, position, and other data.  
**Note:** Returns `-1` for face index if the shape is not ConcavePolygonShape3D.  

### intersect_shape  
**Returns:** `Array<Dictionary>`  
**Parameters:** `PhysicsShapeQueryParameters3D`, `max_results=32`  
**Description:** Finds intersecting shapes and returns details about each.  
**Note:** Does not consider the `motion` property of the object.  

### intersect_ray  
**Returns:** `Dictionary`  
**Parameters:** `PhysicsRayQueryParameters3D`  
**Description:** Intersects a ray in the space. Returns surface normal, position, and other collision data.  

### intersect_shape  
**Returns:** `Array<Dictionary>`  
**Parameters:** `PhysicsShapeQueryParameters3D`, `max_results=32`  
**Description:** Identifies intersecting shapes and their properties.  

## Notes  
- All methods query physics data without modifying the object state.  
- `max_results` limits the number of intersections returned.  
- Collision detection ignores existing overlaps unless explicitly checked with `collide_shape()`.