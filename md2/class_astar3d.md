Here is a comprehensive documentation for the `AStar3D` class in Godot, detailing its methods and their purposes:

---

### **AStar3D Class Documentation**

The `AStar3D` class is a 3D pathfinding implementation in Godot, designed to handle dynamic point-based environments. It provides methods to manage points, paths, and obstacles, with support for weighted cost calculations.

---

### **Point Management Methods**

1. **`add_point(id: int, position: Vector3, weight_scale: float = 1.0)`**  
   Adds a new point to the points pool.  
   - **Parameters**:  
     - `id`: The unique ID for the point.  
     - `position`: The 3D position of the point.  
     - `weight_scale`: A multiplier for pathfinding cost (default: 1.0).  
   - **Note**: If the ID is already in use, it will be overwritten.

2. **`remove_point(id: int)`**  
   Removes a point from the points pool.  
   - **Parameters**:  
     - `id`: The ID of the point to remove.

3. **`set_point_position(id: int, position: Vector3)`**  
   Updates the position of a point.  
   - **Parameters**:  
     - `id`: The ID of the point.  
     - `position`: The new 3D position.

4. **`set_point_weight_scale(id: int, weight_scale: float)`**  
   Adjusts the weight scale of a point.  
   - **Parameters**:  
     - `id`: The ID of the point.  
     - `weight_scale`: A multiplier for pathfinding cost.

5. **`get_point_position(id: int) -> Vector3`**  
   Returns the position of a point.  
   - **Parameters**:  
     - `id`: The ID of the point.  
   - **Returns**: The 3D position of the point.

6. **`get_point_weight_scale(id: int) -> float`**  
   Returns the weight scale of a point.  
   - **Parameters**:  
     - `id`: The ID of the point.  
   - **Returns**: The weight scale value.

7. **`has_point(id: int) -> bool`**  
   Checks if a point with the given ID exists.  
   - **Parameters**:  
     - `id`: The ID of the point.  
   - **Returns**: `true` if the point exists, `false` otherwise.

8. **`is_point_disabled(id: int) -> bool`**  
   Checks if a point is disabled for pathfinding.  
   - **Parameters**:  
     - `id`: The ID of the point.  
   - **Returns**: `true` if disabled, `false` otherwise.

9. **`set_point_disabled(id: int, disabled: bool = true)`**  
   Disables or enables a point for pathfinding.  
   - **Parameters**:  
     - `id`: The ID of the point.  
     - `disabled`: `true` to disable, `false` to enable.

10. **`get_point_ids() -> PackedInt64Array`**  
    Returns an array of all point IDs.  
    - **Returns**: A list of all existing point IDs.

11. **`get_point_count() -> int`**  
    Returns the number of points in the pool.  
    - **Returns**: The total number of points.

12. **`get_point_connections(id: int) -> PackedInt64Array`**  
    Returns the list of connected points for a given ID.  
    - **Parameters**:  
      - `id`: The ID of the point.  
    - **Returns**: An array of connected point IDs.

---

### **Pathfinding Methods**

1. **`get_point_path(from_id: int, to_id: int, allow_partial_path: bool = false) -> PackedVector3Array`**  
    Returns the path as an array of positions from `from_id` to `to_id`.  
    - **Parameters**:  
      - `from_id`: The starting point ID.  
      - `to_id`: The target point ID.  
      - `allow_partial_path`: If `true`, returns a partial path if no full path exists.  
    - **Note**: This method is **not thread-safe** and may return an empty array if called from a `Thread`.

2. **`get_point_path(from_id: int, to_id: int, allow_partial_path: bool = false) -> PackedVector3Array`**  
    Returns the path as an array of positions from `from_id` to `to_id`.  
    - **Parameters**:  
      - `from_id`: The starting point ID.  
      - `to_id`: The target point ID.  
      - `allow_partial_path`: If `true`, returns a partial path if no full path exists.  
    - **Note**: This is a duplicate of the previous method, likely for code consistency or different overload.

3. **`get_point_path(from_id: int, to_id: int, allow_partial_path: bool = false) -> PackedVector3Array`**  
    Returns the path as an array of positions from `from_id` to `toity`.  
    - **Parameters**:  
      - `from_id`: The starting point ID.  
      - `to_id`: The target point ID.  
      - `allow_partial_path`: If `true`, returns a partial path if no full path exists.  
    - **Note**: This is likely a duplicate or alternative overload of the pathfinding method.

4. **`get_point_path(from_id: int, to_id: int, allow_partial_path: bool = false) -> PackedVector3Array`**  
    Returns the path as an array of positions from `from_id` to `to_id`.  
    - **Parameters**:  
      - `from_id`: The starting point ID.  
      - `to_id`: The target point ID.  
      - `allow_partial_path`: If `true`, returns a partial path if no full path exists.  
    - **Note**: This method is a duplicate of the previous one and may be a formatting error.

5. **`get_point_path(from_id: int, to_id: int, allow_partial_path: bool = false) -> PackedVector3Array`**  
    Returns the path as an array of positions from `from_id` to `to_id`.  
    - **Parameters**:  
      - `from_id`: The starting point ID.  
      - `to_id`: The target point ID.  
      - `allow_partial_path`: If `true`, returns a partial path if no full path exists.  
    - **Note**: This method is likely a duplicate or alternative overload of the pathfinding method.

---

### **Utility Methods**

1. **`get_point_capacity() -> int`**  
    Returns the capacity of the internal structure for points.  
    - **Returns**: The maximum number of points the structure can hold.

2. **`reserve_space(num_nodes: int)`**  
    Reserves space for a specified number of points.  
    - **Parameters**:  
      - `num_nodes`: The number of points to reserve space for.

3. **`get_point_capacity() -> int`**  
    Returns the capacity of the internal structure for points.  
    - **Returns**: The maximum number of points the structure can hold.

---

### **Important Notes**

- **Weight Scale**: The `weight_scale` property affects the cost of moving through a point. Higher values make the point more expensive to traverse, which can be used to represent terrain difficulty (e.g., steep slopes, water, etc.).
  
- **Dynamic Obstacles**: Points can be dynamically disabled to represent obstacles or walls in the environment.

- **Thread Safety**: The `get_point_path` method is not thread-safe, so it should not be called from multiple threads simultaneously.

- **Capacity Management**: Use `reserve_space` to pre-allocate memory for large grids or point sets.

---

### **Use Cases**

- **Dynamic Environments**: Adjust `weight_scale` for different terrain types (e.g., grass → 1.0, rock → 2.0, water → 1.5).
- **Obstacle Avoidance**: Disable points to simulate walls or blocked areas in a 3D space.
- **Path Optimization**: Use `get_point_path` to find the shortest or most efficient route between points, considering weight scales and obstacles.
- **Grid-Based Pathfinding**: Use `add_point` and `reserve_space` to manage a grid of points for complex 3D navigation.

---

This documentation provides a clear overview of the `AStar3D` class's capabilities, ensuring developers can effectively manage and utilize pathfinding in 3D environments.