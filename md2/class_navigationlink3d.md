**NavigationLink3D Class**  
*Experimental. A class for defining customizable links between navigation points in a navigation map.*

---

### **Description**  
- **Purpose**: Represents a link between navigation points, allowing for custom paths and connections in a navigation map.  
- **Key Features**:  
  - Connects two points with a specified travel cost.  
  - Can be part of a navigation map for pathfinding.  
  - Supports navigation layers for filtering paths.  

---

### **Tutorials**  
- **Link**: [NavigationLink3D Tutorial](https://godotengine.org/documentation/)

---

### **Properties**  
| Name                  | Type       | Default | Description                                                                 |
|-----------------------|------------|---------|-----------------------------------------------------------------------------|
| `end_position`        | `Vector3` | `(0,0,0)` | The global position of the end point of the link.                          |
| `start_position`      | `Vector3` | `(0,0,0)` | The global position of the start point of the link.                        |
| `navigation_layers`   | `int`      | `0`     | Bitfield of navigation layers this link belongs to.                       |
| `travel_cost`         | `float`    | `1.0`   | Multiplier for pathfinding distance when traversing this link.            |
| `enabled`             | `bool`     | `true`  | Whether the link is active and can be used in pathfinding.                |

---

### **Methods**  
- **`get_global_end_position()`**  
  Returns the end position of the link in global coordinates.  
  - **Return Type**: `Vector3`  

- **`get_global_start_position()`**  
  Returns the start position of the link in global coordinates.  
  - **Return Type**: `Vector3`  

- **`get_navigation_layer_value(layer_number)`**  
  Checks if a specific navigation layer in the bitfield is enabled.  
  - **Parameters**: `layer_number` (int, 1-32)  
  - **Return Type**: `bool`  

- **`get_navigation_map()`**  
  Returns the navigation map RID associated with this link.  
  - **Return Type**: `RID`  

- **`get_rid()`**  
  Returns the unique RID of this link on the `NavigationServer3D`.  
  - **Return Type**: `RID`  

- **`set_global_end_position(position)`**  
  Sets the end position of the link relative to its global coordinates.  
  - **Parameters**: `position` (Vector3)  

- **`set_global_start_position(position)`**  
  Sets the start position of the link relative to its global coordinates.  
  - **Parameters**: `position` (Vector3)  

- **`set_navigation_layer_value(layer_number, value)`**  
  Enables or disables a specific navigation layer in the bitfield.  
  - **Parameters**: `layer_number` (int, 1-32), `value` (bool)  

- **`set_navigation_map(navigation_map)`**  
  Sets the navigation map for this link. Overrides the default map.  
  - **Parameters**: `navigation_map` (RID)  

---

### **Inheritance**  
- **Parent Class**: `NavigationLink`  
- **Derived From**: `NavigationLink` (customizable link between navigation points).  

---

### **Notes**  
- **Navigation Layers**: Use bitmasking to manage multiple layers (e.g., `navigation_layers = 0b101` for layers 1 and 3).  
- **Global Positioning**: `end_position` and `start_position` are relative to the link’s local coordinate system.  
- **Pathfinding**: Enabled links are considered when using `NavigationServer3D.map_get_path()`.  

--- 

This class is essential for creating flexible navigation paths in Godot projects, allowing developers to define custom connections between points while respecting layer-based filtering and cost multipliers.