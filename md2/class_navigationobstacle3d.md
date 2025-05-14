**NavigationObstacle3D Class Overview**

**Description**  
A 3D obstacle used for navigation, affecting agents' paths. It supports both 2D and 3D avoidance, with properties to define its shape, position, and interaction rules.

**Tutorials**  
- [Link to tutorial about NavigationObstacle3D](https://example.com)

---

**Properties**  
1. **affect_navigation_map**  
   - Type: `bool`  
   - Default: `false`  
   - Description: Determines if the obstacle influences the navigation map. Requires this to be true for features like `use_3d_avoidance`.

2. **avoidance_layers**  
   - Type: `int`  
   - Default: `0`  
   - Description: Bitmask for layers (1-32) controlling which avoidance layers this obstacle affects.

3. **height**  
   - Type: `float`  
   - Default: `1.0`  
   - Description: Height used in 2D avoidance. Agents ignore obstacles below or above this value.

4. **radius**  
   - Type: `float`  
   - Default: `0.0`  
   - Description: Avoidance radius for 2D/3D agents. Determines how close agents must be to the obstacle to avoid it.

5. **use_3d_avoidance**  
   - Type: `bool`  
   - Default: `false`  
   - Description: If true, the obstacle affects 3D avoidance using its radius. If false, it uses vertices and radius for 2D avoidance.

6. **velocity**  
   - Type: `Vector3`  
   - Default: `(0, 0, 0)`  
   - Description: Desired velocity for the obstacle. Affects prediction of its movement for agents.

7. **vertices**  
   - Type: `PackedVector3Array`  
   - Default: Empty array  
   - Description: Outline vertices defining the obstacle's shape. Clockwise vertices push agents inward; counter-clockwise push them out. Cannot overlap or cross.

**Note:** The vertices array is copied; changes to it do not affect the original property. Use `PackedVector3Array` methods for manipulation.

---

**Methods**  
1. **get_avoidance_layer_value(layer_number)**  
   - Returns: `bool`  
   - Description: Checks if a specific layer (1-32) in the `avoidance_layers` bitmask is enabled.

2. **get_navigation_map()**  
   - Returns: `RID`  
   - Description: Gets the navigation map assigned to this obstacle. Not the server's map; use `set_navigation_map()` to update.

3. **get_rid()**  
   - Returns: `RID`  
   - Description: Gets the obstacle's RID from the NavigationServer3D.

4. **set_avoidance_layer_value(layer_number, value)**  
   - Description: Enables or disables a specific layer in the `avoidance_layers` bitmask.

5. **set_navigation_map(navigation_map)**  
   - Description: Sets the navigation map for this obstacle and updates the server's obstacle.

---

**Key Notes**  
- **Obstacle Movement:** If the obstacle is warped, agents may get trapped. Use `velocity` for predictable movement.  
- **Layer Requirements:** `use_3d_avoidance` requires `affect_navigation_map` to be true.  
- **Shape Constraints:** Vertices must not overlap or cross. Clockwise vs. counter-clockwise affects agent prediction.