The `GridMap` class in Godot is a powerful tool for managing a grid-based environment, enabling features like spatial organization, collision detection, and navigation mesh generation. Below is a structured explanation of its properties, methods, and use cases, along with practical examples and considerations.

---

### **Key Properties**
1. **`collision_layer`**  
   A bitmask (32-bit integer) defining which physics layers the grid map interacts with.  
   - **Usage**: Controls which layers the grid map is collidable with.

2. **`collision_mask`**  
   A bitmask (32-bit integer) defining which physics layers the grid map can pass through.  
   - **Usage**: Specifies which layers are ignored for collision checks.

3. **`cell_size`**  
   A `Vector3` representing the size of each grid cell in world coordinates.  
   - **Usage**: Determines the scale of the grid for spatial calculations.

4. **`cell_count`**  
   An array of integers specifying the number of cells along each axis (e.g., `cell_count = [10, 10]` for a 10x10 grid).  
   - **Usage**: Defines the grid's dimensions.

5. **`navigation_map`**  
   A `RID` pointing to a navigation map used for baked navigation meshes.  
   - **Usage**: Integrates with Godot's navigation system for pathfinding.

---

### **Key Methods**
#### **Coordinate Conversion**
- **`local_to_map(local_position: Vector3) -> Vector3i`**  
  Converts a local position (in the node's coordinate system) to grid cell coordinates.  
  - **Example**:  
    ```gdscript
    var local_pos = Vector3(0, 0, 0)
    var cell_pos = gridmap.local_to_map(local_pos)
    ```

- **`map_to_local(map_position: Vector3i) -> Vector3`**  
  Converts a grid cell position to local coordinates.  
  - **Example**:  
    ```gdscript
    var cell_pos = Vector3i(5, 5, 0)
    var local_pos = gridmap.map_to_local(cell_pos)
    ```

#### **Cell Manipulation**
- **`set_cell_item(position: Vector3i, item: int, orientation: int = 0)`**  
  Sets the mesh index for a grid cell. A negative `item` (e.g., `INVALID_CELL_ITEM`) clears the cell.  
  - **Example**:  
    ```gdscript
    gridmap.set_cell_item(Vector3i(5, 5, 0), 1, 2)  # Set item 1 with orientation 2
    ```

- **`get_used_cells() -> Array<Vector3i>`**  
  Returns an array of all occupied grid cells.  
  - **Use Case**: Debugging or dynamic generation.

- **`get_used_cells_by_item(item: int) -> Array<Vector3i>`**  
  Returns cells for a specific item index.  
  - **Use Case**: Efficiently querying cells for a particular mesh type.

#### **Collision Configuration**
- **`set_collision_layer_value(layer_number: int, value: bool)`**  
  Enables or disables a specific collision layer (1–32).  
  - **Example**:  
    ```gdscript
    gridmap.set_collision_layer_value(1, true)  # Enable layer 1
    ```

- **`get_collision_layer_value(layer_number: int) -> bool`**  
  Checks if a specific collision layer is enabled.

- **`set_collision_mask_value(layer_number: int, value: bool)`**  
  Enables or disables a specific collision mask layer.  
  - **Example**:  
    ```gdscript
    gridmap.set_collision_mask_value(2, false)  # Disable layer 2
    ```

#### **Navigation Meshes**
- **`make_baked_meshes(gen_lightmap_uv: bool = false, lightmap_uv_texel_size: float = 0.1)`**  
  Bakes navigation meshes for all cells, optionally generating lightmap UVs.  
  - **Use Case**: Preparing the grid for pathfinding algorithms.

- **`get_navigation_map() -> RID`**  
  Returns the RID of the navigation map used by the grid map.

#### **Utility**
- **`resource_changed(resource: Resource)`**  
  Deprecated. Use `Resource.changed()` instead. No effect.

---

### **Use Cases**
1. **Terrain Generation**  
   - Use `cell_count` and `cell_size` to define a terrain grid.  
   - `set_cell_item` can assign different mesh types (e.g., grass, rock) to cells.

2. **Collision and Physics**  
   - Configure `collision_layer` and `collision_mask` to define which physics layers interact with the grid.

3. **Pathfinding**  
   - Use `navigation_map` with `make_baked_meshes` to generate navigation data for pathfinding algorithms.

4. **Lightmap Baking**  
   - Use `make_baked_meshes` with `gen_lightmap_uv` enabled to bake lighting into the grid cells.

---

### **Example Workflow**
1. **Initialize GridMap**  
   Set `cell_count` and `cell_size` to define the grid dimensions and scale.  
   ```gdscript
   gridmap.cell_count = [20, 20]
   gridmap.cell_size = Vector3(1, 1, 1)
   ```

2. **Assign Meshes to Cells**  
   Use `set_cell_item` to populate cells with different mesh types.  
   ```gdscript
   for x in 0..19:
       for y in 0..19:
           gridmap.set_cell_item(Vector3i(x, y, 0), 1, 0)
   ```

3. **Configure Collision Layers**  
   Enable specific layers for interaction.  
   ```gdscript
   gridmap.set_collision_layer_value(1, true)
   ```

4. **Generate Navigation Mesh**  
   Call `make_baked_meshes` to create navigation data.  
   ```gdscript
   gridmap.make_baked_meshes(true, 0.1)
   ```

---

### **Considerations**
- **Performance**: Large `cell_count` values may impact performance. Use `cell_size` to balance detail and efficiency.
- **Orientation**: Use `get_orthogonal_index_from_basis` to determine orientations based on mesh rotation.
- **Navigation Map**: Ensure the `navigation_map` is properly configured in the project for pathfinding.

---

This class is ideal for creating complex environments with spatial awareness, enabling efficient collision handling, and integrating with Godot's navigation systems.