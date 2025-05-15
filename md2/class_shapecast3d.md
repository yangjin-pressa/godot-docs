The `ShapeCast3D` class in Godot is designed for **3D collision detection** using a shape cast (a line or ray that checks for collisions with objects in the scene). It provides methods to query the environment for intersections and retrieve details about the collisions. Here's a breakdown of its key components and how to use them effectively:

---

### **Core Concepts**
1. **Shape Cast Direction**:
   - The cast originates from the `ShapeCast3D` node and extends toward the `target_position` (a `Vector3` property).
   - The `collision_mask` determines which layers/objects are checked for collisions.

2. **Collision Detection**:
   - The class uses physics data to detect collisions along the cast direction.
   - It supports multiple collision results (e.g., multiple objects intersecting the cast).

3. **Collision Mask**:
   - A bitmask that specifies which layers/objects are considered for collisions.
   - Use `set_collision_mask_value` to enable/disable specific layers (1–32).

---

### **Key Properties**
| Property                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `target_position`           | The end point of the cast line (determines direction and length).           |
| `collision_mask`            | Bitmask controlling which layers/objects are checked for collisions.        |
| `enabled`                   | Whether the cast is active. When `true`, it updates physics data.          |

---

### **Key Methods**
#### **Collision Query**
- **`is_colliding()`**  
  Returns `true` if any object is intersecting the cast.

- **`get_collision_count()`**  
  Returns the number of collisions detected (useful for iterating through results).

- **`get_collision_point(index)`**  
  Returns the point where the cast collided with an object (in global coordinates).

- **`get_collision_normal(index)`**  
  Returns the normal vector of the collision surface at a specific index.

- **`get_collider(index)`**  
  Returns the object (e.g., `Node3D`) that collided with the cast.

- **`get_collider_rid(index)`**  
  Returns the `RID` of the collider object.

- **`get_collider_shape(index)`**  
  Returns the shape ID of the colliding object (e.g., `MeshInstance` or `CollisionShape3D`).

#### **Safety Fractions**
- **`get_closest_collision_safe_fraction()`**  
  Returns the fraction of the cast's length where movement is safe (no collision).

- **`get_closest_collision_unsafe_fraction()`**  
  Returns the fraction where movement would trigger a collision.

#### **Exception Handling**
- **`add_exception(node)` / `remove_exception(node)`**  
  Excludes specific nodes from collision checks.
- **`add_exception_rid(rid)` / `remove_exception_rid(rid)`**  
  Excludes objects by their `RID`.

#### **Force Update**
- **`force_shapecast_update()`**  
  Forces immediate collision detection, bypassing the next physics process call.

---

### **Example Use Case**
```gdscript
# In a Node3D script:
var shape_cast = ShapeCast3D.new()
shape_cast.target_position = Vector3(0, 0, 10)  # Cast upward
shape_cast.collision_mask = 0b1111111111111111111111111111111