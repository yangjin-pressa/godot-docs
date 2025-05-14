**Class Name**: NavigationLink2D  
**Description**: A class for handling navigation links in Godot, used to connect points in a navigation mesh.  

---

**Inherits from**: Object  

**Experimental**: This class is experimental and may change in future versions.  

---

**Tutorials**:  
- [NavigationLink2D tutorial](https://godotengine.org/classes/NavigationLink2D)  

---

**Properties**:  
- **start_position**: `Vector2` (Default: `Vector2(0, 0)`)  
  - Starting position of the link. This position is used to find the nearest polygon in the navigation mesh.  

- **end_position**: `Vector2` (Default: `Vector2(0, 0)`)  
  - Ending position of the link. This position is used to find the nearest polygon in the navigation mesh.  

- **navigation_layers**: `int` (Default: `0`)  
  - Bitfield determining which navigation layers the link belongs to. These layers are used when requesting a path.  

- **travel_cost**: `float` (Default: `1.0`)  
  - Multiplied with the distance when pathfinding along the link to determine the shortest path.  

- **enabled**: `bool` (Default: `true`)  
  - Whether the link is active.  

---

**Methods**:  
- **get_global_end_position()**: `Vector2`  
  - Returns the `end_position` as a global position.  

- **get_global_start_position()**: `Vector2`  
  - Returns the `start_position` as a global position.  

- **get_navigation_layer_value(layer_number: int)**: `bool`  
  - Returns whether the specified layer in the `navigation_layers` bitfield is enabled.  

- **get_navigation_map()**: `RID`  
  - Returns the current navigation map `RID` used by this link.  

- **get_rid()**: `RID`  
  - Returns the `RID` of this link in the `NavigationServer2D`.  

- **set_global_end_position(position: Vector2)**: `void`  
  - Sets the `end_position` relative to the link from a global position.  

- **set_global_start_position(position: Vector2)**: `void`  
  - Sets the `start_position` relative to the link from a global position.  

- **set_navigation_layer_value(layer_number: int, value: bool)**: `void`  
  - Enables or disables a specific layer in the `navigation_layers` bitfield.  

- **set_navigation_map(navigation_map: RID)**: `void`  
  - Sets the navigation map for this link. Defaults to the `World2D` default map.  

---

**Notes**:  
- The `navigation_layers` property uses a bitmask to specify which navigation layers the link belongs to.  
- The `start_position` and `end_position` are relative to the link's parent node.