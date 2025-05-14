**NavigationRegion2D Class**  

**Note**: This class is experimental.  

---

### **Description**  
- **Purpose**: Represents a navigable region in a 2D environment, used for pathfinding and navigation.  
- **Key Features**:  
  - Uses a `NavigationPolygon` resource for defining the region's shape.  
  - Supports edge connections to link with other regions.  
  - Caches navigation data for performance.  

---

### **Tutorials**  
- **Example**: Use `NavigationRegion2D` to define areas for AI movement or player navigation.  

---

### **Properties**  
- **navigation_layers**  
  - **Type**: `int`  
  - **Default**: `0`  
  - **Description**: Bitmask for enabled navigation layers (1–32).  

- **navigation_polygon**  
  - **Type**: `NavigationPolygon`  
  - **Default**: `null`  
  - **Description**: The polygon resource defining the region's shape.  

- **travel_cost**  
  - **Type**: `float`  
  - **Default**: `1.0`  
  - **Description**: Multiplier for distance calculations within the region.  

- **use_edge_connections**  
  - **Type**: `bool`  
  - **Default**: `true`  
  - **Description**: Enables or disables edge-based region linking.  

- **enabled**  
  - **Type**: `bool`  
  - **Default**: `true`  
  - **Description**: Activates or deactivates the region.  

---

### **Methods**  
- **bake_navigation_polygon(on_thread: bool = true)**  
  - **Purpose**: Compiles the `NavigationPolygon` into a navigable format.  
  - **Thread**: Defaults to a background thread.  

- **get_bounds() → Rect2**  
  - **Purpose**: Returns the axis-aligned bounds of the region.  

- **get_navigation_map() → RID**  
  - **Purpose**: Retrieves the navigation map associated with this region.  

- **get_rid() → RID**  
  - **Purpose**: Returns the region's unique identifier on the `NavigationServer2D`.  

- **set_navigation_map(navigation_map: RID)**  
  - **Purpose**: Sets the navigation map for this region.  

- **set_navigation_layer_value(layer_number: int, value: bool)**  
  - **Purpose**: Enables or disables a specific navigation layer.  

---

### **Signals**  
- **bake_finished()**  
  - **Description**: Triggered when the `NavigationPolygon` is successfully baked.  

- **navigation_polygon_changed()**  
  - **Description**: Emitted when the polygon resource is updated.  

---

### **Property Details**  
- **navigation_layers**: Manages which navigation layers are active for this region.  
- **navigation_polygon**: Defines the shape and boundaries of the region.  
- **travel_cost**: Adjusts pathfinding cost for movement within the region.  
- **use_edge_connections**: Controls whether the region connects with others via edges.  
- **enabled**: Toggles the region's active state for navigation purposes.  

---

### **Method Details**  
- **bake_navigation_polygon**: Compiles the polygon data for efficient pathfinding.  
- **get_bounds**: Useful for collision detection or visual alignment.  
- **get_navigation_map**: Identifies the map this region belongs to.  
- **get_rid**: Helps identify the region in the navigation server.  
- **set_navigation_map**: Overrides the default map for custom navigation setups.  
- **set_navigation_layer_value**: Fine-tunes layer activation for complex navigation scenarios.  

---

### **Deprecated Methods**  
- **get_region_rid()**: Use `get_rid()` instead. Returns the region's ID on the server.