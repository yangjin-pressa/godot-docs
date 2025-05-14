NavigationRegion3D Class Overview  
- **Experimental**: Marked as experimental.  
- **Purpose**: Manages navigation mesh regions for pathfinding.  

---

### Description  
- **Key Concepts**:  
  - Navigation regions are used to define areas in a navigation map.  
  - Regions can be connected via edge connections (if enabled).  
  - Baking a navigation mesh prepares it for use in the navigation map.  

- **Notes**:  
  - Regions must be connected via edge connections to allow pathfinding between them.  
  - Baking on a separate thread is optional but recommended for performance.  

---

### Tutorials  
- **Link**: [Navigating with Region3D](https://godotengine.org/doc/next/3d/navigation/region3d.html)  

---

### Properties  
- **enabled**:  
  - **Type**: bool  
  - **Default**: true  
  - **Description**: Enables or disables the navigation region.  

- **enter_cost**:  
  - **Type**: float  
  - **Default**: 1.0  
  - **Description**: Cost multiplier for entering the region.  

- **navigation_layers**:  
  - **Type**: uint (bitfield)  
  - **Default**: 0  
  - **Description**: Bitmask of active navigation layers.  

- **navigation_mesh**:  
  - **Type**: NavigationMesh  
  - **Description**: Reference to the navigation mesh.  

- **travel_cost**:  
  - **Type**: float  
  - **Default**: 1.0  
  - **Description**: Cost multiplier for traveling within the region.  

- **use_edge_connections**:  
  - **Type**: bool  
  - **Default**: true  
  - **Description**: Enables edge connections to other regions.  

---

### Methods  
- **bake_navigation_mesh(on_thread: bool = true)**  
  - **Description**: Bakes the navigation mesh.  
  - **Parameters**:  
    - `on_thread`: Whether to bake on a separate thread.  

- **get_bounds() -> AABB**:  
  - **Description**: Returns the axis-aligned bounding box of the region.  

- **get_navigation_layer_value(layer_number: int) -> bool**:  
  - **Description**: Checks if a specific navigation layer is enabled.  

- **get_navigation_map() -> RID**:  
  - **Description**: Returns the current navigation map RID.  

- **get_rid() -> RID**:  
  - **Description**: Returns the region's RID on the navigation server.  

- **is_baking() -> bool**:  
  - **Description**: Checks if the mesh is currently being baked.  

- **set_navigation_map(navigation_map: RID)**:  
  - **Description**: Sets the navigation map for the region.  

- **set_navigation_layer_value(layer_number: int, value: bool)**:  
  - **Description**: Enables or disables a specific navigation layer.  

---

### Signals  
- **bake_finished()**:  
  - **Description**: Emitted when the navigation mesh is baked.  

- **navigation_mesh_changed()**:  
  - **Description**: Emitted when the navigation mesh changes.  

---

### Key Notes  
- **Deprecated**: `get_region_rid()` is deprecated; use `get_rid()` instead.  
- **Thread Safety**: Baking on a separate thread is disabled on systems that don't support threads (e.g., Web).  
- **Edge Connections**: Regions must be within proximity of the edge connection margin to connect.