The `ShapeCast2D` node in Godot is a versatile tool for detecting collisions in 2D space by casting a shape in a specific direction for a defined distance. Below is a detailed breakdown of its usage, properties, and methods.

---

### **Key Properties**
1. **`shape`**  
   - **Type**: `Shape2D` (e.g., `CircleShape2D`, `RectangleShape2D`)  
   - **Purpose**: Defines the shape to cast. This is typically a reference to a `Shape2D` node or a built-in shape.  
   - **Example**:  
     ```gdscript
     shape = preload("res://shapes/circle.tscn")
     ```

2. **`direction`**  
   - **Type**: `Vector2`  
   - **Purpose**: The direction vector (unit vector) in which the cast is performed. This determines the orientation of the cast.  
   - **Example**:  
     ```gdscript
     direction = Vector2(1, 0)  # Cast right
     ```

3. **`target_position`**  
   - **Type**: `Vector2`  
   - **Purpose**: The end point of the cast. This determines the length of the cast (distance from the node's position to the end point).  
   - **Example**:  
     ```gdscript
     target_position = Vector2(100, 0)  # Cast 100 units to the right
     ```

4. **`margin`**  
   - **Type**: `float`  
   - **Purpose**: A collision margin to adjust the cast's boundaries, preventing penetration into collision shapes.

5. **`margin_ratio`**  
   - **Type**: `float`  
   - **Purpose**: A ratio that adjusts the margin dynamically (e.g., based on the shape's size).

6. **`enabled`**  
   - **Type**: `bool`  
   - **Purpose**: Controls whether the cast is active.

---

### **Key Methods**
1. **`get_collision_count()`**  
   - **Returns**: `int`  
   - **Purpose**: Returns the number of collisions detected during the cast.  
   - **Example**:  
     ```gdscript
     var count = get_collision_count()
     ```

2. **`get_collision_point(index: int) -> Vector2`**  
   - **Returns**: `Vector2`  
   - **Purpose**: Retrieves the point of collision for the specified index (0-indexed).  
   - **Example**:  
     ```gdscript
     var point = get_collision_point(0)
     ```

3. **`get_collision_normal(index: int) -> Vector2`**  
   - **Returns**: `Vector2`  
   - **Purpose**: Retrieves the normal vector (direction) of the collision for the specified index.  
   - **Example**:  
     ```gdscript
     var normal = get_collision_normal(0)
     ```

4. **`is_colliding() -> bool`**  
   - **Returns**: `bool`  
   - **Purpose**: Returns `true` if at least one collision was detected.  
   - **Example**:  
     ```gdscript
     if is_colliding():
         print("Collision detected!")
     ```

5. **`get_collider(index: int) -> Node2D`**  
   - **Returns**: `Node2D`  
   - **Purpose**: Retrieves the collided node for the specified index.  
   - **Example**:  
     ```gdscript
     var collider = get_collider(0)
     ```

6. **`get_collider_rid(index: int) -> RID`**  
   - **Returns**: `RID`  
   - **Purpose**: Retrieves the RID of the collided object.  
   - **Example**:  
     ```gdscript
     var rid = get_collider_rid(0)
     ```

7. **`get_collider_shape(index: int) -> int`**  
   - **Returns**: `int`  
   - **Purpose**: Returns the shape ID of the collided object.  
   - **Example**:  
     ```gdscript
     var shape_id = get_collider_shape(0)
     ```

8. **`get_closest_collision_safe_fraction() -> float`**  
   - **Returns**: `float`  
   - **Purpose**: Returns the fraction of the cast distance where the shape can move without collision.  
   - **Example**:  
     ```gdscript
     var safe_fraction = get_closest_collision_safe_fraction()
     ```

9. **`get_closest_collision_unsafe_fraction() -> float`**  
   - **Returns**: `float`  
   - **Purpose**: Returns the fraction where collision is triggered.  
   - **Example**:  
     ```gdscript
     var unsafe_fraction = get_closest_collision_unsafe_fraction()
     ```

---

### **Usage Example**
To use the `ShapeCast2D` in a scene:

1. **Create a ShapeCast2D Node**:  
   - Add a `ShapeCast2D` node to your scene (e.g., a character).
   - Set its `shape` property to a `CircleShape2D` or `RectangleShape2D`.

2. **Set Direction and Target Position**:  
   - Set the `direction` to the desired direction (e.g., `Vector2(1, 0)` for right).
   - Set the `target_position` to the end of the cast (e.g., `Vector2(100, 0)` for 100 units in the direction).

3. **Detect Collisions**:  
   - Use the methods to retrieve collision details in your script.

**GDScript Example**:
```gdscript
func _process(delta):
    if is_colliding():
        var point = get_collision_point(0)
        var normal = get_collision_normal(0)
        print("Collision at point: $", point)
        print("Normal: $", normal)
```

---

### **Tips**
- **Dynamic Shapes**: Use the `shape` property to dynamically change the casting shape (e.g., switching from a circle to a rectangle).
- **Collision Margins**: Adjust `margin` and `margin_ratio` to fine-tune the cast's sensitivity.
- **Physics Process**: Ensure the `ShapeCast2D` is part of the physics process (e.g., in a `RigidBody2D` or `Area2D` node).

---

### **Summary**
The `ShapeCast2D` node is ideal for scenarios like collision detection in games, pathfinding, or object interaction. By setting the direction, target position, and shape, you can create precise casts to detect collisions in any direction. The methods provided allow detailed interaction with the collision results.