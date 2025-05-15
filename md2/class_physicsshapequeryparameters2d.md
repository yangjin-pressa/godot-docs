**Class:** PhysicsShapeQueryParameters2D  
**Inherits:** RefCounted < Object  

---

### Description  
Configures parameters for PhysicsDirectSpaceState2D.intersect_shape().  
Modify properties like shape, collide_with_bodies, and margin to adjust query behavior.

---

### Properties  
- **collide_with_areas** (bool)  
  - Default: false  
  - If true, includes Area2D objects in queries.  
  - Methods: set_collide_with_areas(), is_collide_with_areas_enabled()  

- **collide_with_bodies** (bool)  
  - Default: true  
  - If true, includes PhysicsBody2D objects in queries.  
  - Methods: set_collide_with_bodies(), is_collide_with_bodies_enabled()  

- **collision_mask** (int)  
  - Default: 4294967295  
  - Bitmask for collision layers (default: all layers).  
  - Methods: set_collision_mask(), get_collision_mask()  
  - Note: [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)  

- **exclude** (Array<RID>)  
  - Default: []  
  - List of RIDs to exclude from collisions.  
  - Methods: set_exclude(), get_exclude()  
  - Note: Returned array is a copy; modify and reassign to update.  

- **margin** (float)  
  - Default: 0.0  
  - Collision margin for the shape.  
  - Methods: set_margin(), get_margin()  

- **motion** (Vector2)  
  - Default: Vector2(0, 0)  
  - Motion vector for the shape being queried.  
  - Methods: set_motion(), get_motion()  

- **shape** (Resource)  
  - Reference to Shape2D for collision/intersection.  
  - Methods: set_shape(), get_shape()  

- **shape_rid** (RID)  
  - RID of the shape for queries.  
  - Methods: set_shape_rid(), get_shape_rid()  
  - Example:  
    ```gdscript
    var shape_rid = PhysicsServer2D.circle_shape_create()
    PhysicsServer2D.shape_set_data(shape_rid, radius)
    var params = PhysicsShapeQueryParameters2D.new()
    params.shape_rid = shape_rid
    ```  

- **transform** (Transform2D)  
  - Default: Transform2D(1, 0, 0, 1, 0, 0)  
  - Transform matrix for the shape.  
  - Methods: set_transform(), get_transform()  

---

### Key Notes  
- Use shape_rid for performance optimization with Servers API.  
- Exclude property requires RIDs obtained via CollisionObject2D.get_rid().  
- Array methods return copies; reassign to update original values.