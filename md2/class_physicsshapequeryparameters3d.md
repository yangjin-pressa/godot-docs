# PhysicsShapeQueryParameters3D

**Inherits:** RefCounted < Object

## Description
Configures parameters for `PhysicsDirectSpaceState3D.intersect_shape()`. Modify properties like shape to adjust behavior.

---

## Properties

- **collide_with_areas** (bool, default: false)  
  Whether to consider Area3D objects in queries.

- **collide_with_bodies** (bool, default: true)  
  Whether to consider PhysicsBody3D objects in queries.

- **collision_mask** (int, default: 4294967295)  
  Bitmask of collision layers to detect. Default includes all layers.

- **exclude** (Array<RID>, default: [])  
  List of RIDs to exclude from collisions. Note: returns a copy; modify and reassign to update.

- **margin** (float, default: 0.0)  
  Collision margin for the shape.

- **motion** (Vector3, default: (0, 0, 0))  
  Motion vector for the shape being queried.

- **shape** (Resource, default: none)  
  Shape3D resource for collision/intersection queries. Prefer over shape_rid.

- **shape_rid** (RID, default: RID())  
  RID of the shape for queries. Use for performance with Servers API:

  ```gdscript
  var shape_rid = PhysicsServer3D.shape_create(PhysicsServer3D.SHAPE_SPHERE)
  var radius = 2.0
  PhysicsServer3D.shape_set_data(shape_rid, radius)
  
  var params = PhysicsShapeQueryParameters3D.new()
  params.shape_rid = shape_rid
  ```

  ```csharp
  RID shapeRid = PhysicsServer3D.ShapeCreate(PhysicsServer3D.ShapeType.Sphere);
  float radius = 2.0f;
  PhysicsServer3D.ShapeSetData(shapeRid, radius);
  
  var params = new PhysicsShapeQueryParameters3D();
  params.ShapeRid = shapeRid;
  ```

- **transform** (Transform3D, default: identity matrix)  
  Transform matrix for the shape.

---

## Methods

- `set_collide_with_areas(value: bool)`  
- `is_collide_with_areas_enabled()`  

- `set_collide_with_bodies(value: bool)`  
- `is_collide_with_bodies_enabled()`  

- `set_collision_mask(value: int)`  
- `get_collision_mask()`  

- `set_exclude(value: Array<RID>)`  
- `get_exclude()`  

- `set_margin(value: float)`  
- `get_margin()`  

- `set_motion(value: Vector3)`  
- `get_motion()`  

- `set_shape(value: Resource)`  
- `get_shape()`  

- `set_shape_rid(value: RID)`  
- `get_shape_rid()`  

- `set_transform(value: Transform3D)`  
- `get_transform()`  

---

## Notes
- Use `shape_rid` for performance optimization with the Servers API.
- The `exclude` property returns a copy of the array; modify and reassign to update.
- Refer to [Collision layers and masks](https://godot-engine.org/documentation/ru/2.1/classes/physics_server_3d.html#collision-layers-and-masks) for details on collision masks.