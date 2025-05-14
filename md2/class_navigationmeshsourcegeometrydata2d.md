**NavigationMeshSourceGeometryData2D**  

**Description**  
A class for managing geometry data used in navigation mesh baking. It handles obstructed areas, traversable regions, and projected obstructions.  

---

### **Methods**  

1. **add_obstruction_outline**  
   - **Parameters**: `shape_outline` (PackedVector2Array)  
   - **Description**: Adds the outline points of a shape as an obstructed area.  

2. **add_obstruction_outline**  
   - **Parameters**: `shape_outline` (PackedVector2Array)  
   - **Description**: Adds the outline points of a shape as an obstructed area.  

3. **get_bounds**  
   - **Returns**: `Rect2`  
   - **Description**: Returns an axis-aligned bounding box covering all stored geometry. The result is cached until geometry changes.  

4. **get_obstruction_outlines**  
   - **Returns**: Array of PackedVector2Array  
   - **Description**: Returns all obstructed area outlines arrays.  

5. **get_projected_obstructions**  
   - **Returns**: Array of dictionaries  
   - **Description**: Returns projected obstructions. Each dictionary includes:  
     - `vertices`: PackedFloat32Array (outline points of the projected shape)  
     - `carve`: bool (whether the shape is affected by baking offsets)  

6. **get_traversable_outlines**  
   - **Returns**: Array of PackedVector2Array  
   - **Description**: Returns all traversable area outlines arrays.  

7. **has_data**  
   - **Returns**: bool  
   - **Description**: Returns `true` if parsed source geometry data exists.  

8. **merge**  
   - **Parameters**: `other_geometry` (NavigationMeshSourceGeometryData2D)  
   - **Description**: Combines geometry data from another instance into this one.  

9. **set_obstruction_outlines**  
   - **Parameters**: `obstruction_outlines` (Array of PackedVector2Array)  
   - **Description**: Sets all obstructed area outlines arrays.  

10. **set_projected_obstructions**  
    - **Parameters**: `projected_obstructions` (Array of dictionaries)  
    - **Description**: Sets projected obstructions. Each dictionary includes:  
      - `vertices`: PackedFloat32Array  
      - `carve`: bool  

11. **set_traversable_outlines**  
    - **Parameters**: `traversable_outlines` (Array of PackedVector2Array)  
    - **Description**: Sets all traversable area outlines arrays.  

---

### **Key Concepts**  
- **Obstruction/Traversable Areas**: Defined by outlines (PackedVector2Array).  
- **Projected Obstructions**: Stored as arrays of dictionaries with `vertices` and `carve` flags.  
- **Bounds**: Calculated dynamically and cached until geometry changes.  

This class is used to manage spatial data for navigation mesh generation, allowing for complex terrain interactions.