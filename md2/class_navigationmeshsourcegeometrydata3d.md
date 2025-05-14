**Class Info**  
**NavigationMeshSourceGeometryData3D**  
A container for parsed source geometry data used in navigation mesh baking.  

---

**Methods**  

1. **clear()**  
   - **Description**: Clears the internal data.  

2. **clear_projected_obstructions()**  
   - **Description**: Removes all projected obstructions.  

3. **get_bounds()**  
   - **Returns**: `AABB` – Axis-aligned bounding box covering all geometry data.  
   - **Note**: Bounds are calculated and cached until geometry changes.  

4. **get_indices()**  
   - **Returns**: `PackedInt32Array` – Indices array of parsed geometry data.  

5. **get_projected_obstructions()**  
   - **Returns**: `Array` of dictionaries. Each dictionary contains:  
     - `vertices`: `PackedFloat32Array` (outline points of the projected shape).  
     - `elevation`: `float` (y-axis placement).  
     - `height`: `float` (extrusion along y-axis).  
     - `carve`: `bool` (whether the shape is unaffected by baking offsets).  

6. **get_vertices()**  
   - **Returns**: `PackedFloat32Array` – Vertices array of parsed geometry data.  

7. **has_data()**  
   - **Returns**: `bool` – `true` if geometry data exists.  

8. **merge(other_geometry: NavigationMeshSourceGeometryData3D)**  
   - **Description**: Adds geometry data from another `NavigationMeshSourceGeometryData3D` instance.  

9. **set_indices(indices: PackedInt32Array)**  
   - **Description**: Sets the indices array.  
   - **Warning**: Incorrect data may crash third-party baking libraries.  

10. **set_projected_obstructions(projected_obstructions: Array)**  
    - **Description**: Sets projected obstructions.  
    - **Example**:  
      ```gdscript
      "vertices" : PackedFloat32Array
      "elevation" : float
      "height" : float
      "carve" : bool
      ```  

11. **set_vertices(vertices: PackedFloat32Array)**  
    - **Description**: Sets the vertices array.  
    - **Warning**: Incorrect data may crash third-party baking libraries.  

---

**Notes**  
- **add_faces(faces: PackedVector3Array, xform: Transform3D)**: Adds triangular faces (clockwise order) after applying the transformation.  
- **append_arrays(vertices: PackedFloat32Array, indices: PackedInt32Array)**: Appends vertices and indices to existing arrays.  
- **add_projected_obstruction(...)**: Adds a 2D shape (xz-plane) with y-axis elevation and extrusion.  

**Warning**: Inappropriate geometry data (e.g., mismatched indices/vertices) may cause baking failures. Ensure data consistency before processing.