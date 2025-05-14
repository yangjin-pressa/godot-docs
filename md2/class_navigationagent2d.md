The `NavigationAgent2D` class in Godot is a core component for handling pathfinding and movement in 2D navigation scenes. It integrates with the `NavigationServer2D` to provide agents with navigation capabilities, including avoiding obstacles, adhering to layers, and reaching targets. Below is a structured summary of its key properties, methods, and their interactions:

---

### **Key Properties**
1. **`navigation_map`**:  
   - **Type**: `RID`  
   - **Description**: The navigation map associated with the agent.  
   - **Usage**: Specifies the map the agent uses for pathfinding. Changing this requires `set_navigation_map()`.

2. **`navigation_layers`**:  
   - **Type**: Bitfield (e.g., 32 bits)  
   - **Description**: Bitmask controlling which navigation layers the agent considers.  
   - **Usage**: Enables or disables specific layers for pathfinding.

3. **`avoidance_layers`**:  
   - **Type**: Bitfield  
   - **Description**: Bitmask for dynamic obstacles (e.g., moving objects) the agent avoids.  
   - **Usage**: Configures avoidance behavior.

4. **`avoidance_mask`**:  
   - **Type**: Bitfield  
   - **Description**: Bitmask for dynamic obstacles (e.g., dynamic objects) that the agent avoids.  
   - **Usage**: Enables or disables specific masks for avoidance.

5. **`target_position`**:  
   - **Type**: `Vector2`  
   - **Description**: The target position the agent aims to reach.  
   - **Usage**: Set via `set_target_position()`.

6. **`target_desired_distance`**:  
   - **Type**: `float`  
   - **Description**: Distance within which the agent considers the target reached.  
   - **Usage**: Controls when the agent stops moving toward the target.

---

### **Key Methods**

#### **Navigation & Pathfinding**
- **`get_navigation_map()`**:  
  Returns the `RID` of the current navigation map.  
- **`set_navigation_map(RID map)`**:  
  Sets the navigation map for the agent.  
- **`get_next_path_position()`**:  
  Returns the next valid position the agent can move to, ensuring a clear path.  
  **Usage**: Called every physics frame to update the agent's path.  
- **`is_navigation_finished()`**:  
  Checks if the agent has completed its navigation (target reached or path is invalid).  
- **`get_final_position()`**:  
  Returns the final reachable position of the current path.  
- **`get_current_navigation_result()`**:  
  Returns the result of the last path query (e.g., success/failure).  
- **`is_target_reachable()`**:  
  Checks if the final position is within `target_desired_distance` of the target.  
- **`is_target_reached()`**:  
  Confirms if the agent has reached the target.  

#### **Layer & Mask Control**
- **`set_navigation_layer_value(int layer, bool value)`**:  
  Enables/disables a specific navigation layer.  
- **`set_avoidance_layer_value(int layer, bool value)`**:  
  Enables/disables a specific avoidance layer.  
- **`set_avoidance_mask_value(int mask, bool value)`**:  
  Enables/disables a specific avoidance mask.  
- **`get_navigation_layer_value(int layer)`**:  
  Checks the status of a navigation layer.  
- **`get_avoidance_layer_value(int layer)`**:  
  Checks the status of an avoidance layer.  
- **`get_avoidance_mask_value(int mask)`**:  
  Checks the status of an avoidance mask.  

#### **Movement & Simulation**
- **`set_velocity_forced(Vector2 velocity)`**:  
  Forcibly sets the agent's velocity in the collision avoidance simulation.  
  **Usage**: Useful for teleporting agents but should be used sparingly.  
- **`get_rid()`**:  
  Returns the agent's `RID` on the `NavigationServer2D`.  

---

### **Key Signals**
- **`path_changed()`**:  
  Emits when the navigation path changes (e.g., due to obstacles or target movement).  
- **`target_reached()`**:  
  Emits when the agent reaches the target.  

---

### **Usage Example**
```gdscript
# Set target position
agent.set_target_position(Vector2(100, 100))

# Enable navigation layer 1
agent.set_navigation_layer_value(1, true)

# Set velocity for forced movement
agent.set_velocity_forced(Vector2(5, 5))

# Check if navigation is finished
if agent.is_navigation_finished():
    print("Agent reached target or path is invalid.")
```

---

### **Key Considerations**
- **Bitfield Layers**: Use 32-bit layers/masks to define distinct areas (e.g., static obstacles, dynamic objects).  
- **Path Updates**: Call `get_next_path_position()` every frame to keep the agent moving.  
- **Avoid Jumping**: Avoid frequent calls to `set_velocity_forced()` to prevent unstable movement.  
- **Signal Handling**: Connect to `path_changed` and `target_reached` for event-driven logic.

This class is essential for creating intelligent, obstacle-aware agents in 2D environments, leveraging the `NavigationServer2D` for efficient pathfinding.