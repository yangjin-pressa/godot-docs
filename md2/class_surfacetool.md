Here's a structured overview of the **SurfaceTool** class methods in Godot, with explanations of their purposes, parameters, and typical usage scenarios:

---

### **Core Functions for Mesh Construction**
1. **`append_vertex(position, normal, tangent, uv)`**  
   - **Purpose**: Adds a vertex to the current mesh.  
   - **Parameters**:  
     - `position`: Vertex position (e.g., `Vector3`).  
     - `normal`: Vertex normal (e.g., `Vector3`).  
     - `tangent`: Vertex tangent (e.g., `Vector3`).  
     - `uv`: UV coordinates (e.g., `Vector2`).  
   - **Note**: Omitted parameters are optional. For example, `tanget` can be omitted if not needed.

2. **`append_vertex(position, uv)`**  
   - **Purpose**: Adds a vertex with position and UVs (e.g., for a simple texture).  
   - **Parameters**:  
     - `position`: Vertex position.  
     - `uv`: UV coordinates (e.g., `Vector4` for multiple UVs).

3. **`begin(primitive_type, material)`**  
   - **Purpose**: Starts creating a new mesh.  
   - **Parameters**:  
     - `primitive_type`: Mesh type (e.g., `Mesh.PRIMITIVE_TRIANGLES`).  
     - `material`: Material to assign to the mesh.  
   - **Note**: Must be called before any `append_vertex` or `set_*` methods.

4. **`clear()`**  
   - **Purpose**: Removes all vertices and indices from the current mesh.  
   - **Use Case**: Resetting the mesh for re-creation.

5. **`clear_indices()`**  
   - **Purpose**: Removes the index buffer, resetting the mesh to a vertex-only structure.  

6. **`clear_vertex()`**  
   - **Purpose**: Removes all vertices (equivalent to `clear()`).  

7. **`commit()`**  
   - **Purpose**: Finalizes the mesh and returns it.  
   - **Use Case**: When you're done defining the mesh, call this to get the result.

8. **`commit_to_arrays()`**  
   - **Purpose**: Converts the mesh into array data (e.g., for export or further processing).  
   - **Optional Parameter**: Whether to optimize indices (e.g., `true` for better performance).

9. **`commit_to_mesh(mesh)`**  
   - **Purpose**: Merges the current mesh into the provided `mesh` object.  
   - **Use Case**: When building complex meshes incrementally and merging them.

10. **`decal(decal, is_decal)`**  
    - **Purpose**: Adds a decal to the current mesh.  
    - **Parameters**:  
      - `decal`: Decal object (e.g., a texture or material).  
      - `is_decal`: Boolean to specify if it's a decal.  
    - **Note**: Not clearly documented, but likely for adding overlays or textures.

---

### **Vertex Data Control**
11. **`delete_vertex(index)`**  
    - **Purpose**: Removes a specific vertex at a given index.  
    - **Parameters**:  
      - `index`: Index of the vertex to delete.  

12. **`erase_vertex(index)`**  
    - **Purpose**: Similar to `delete_vertex`, but may handle removal of vertices from a list.  

13. **`index()`**  
    - **Purpose**: Creates an index array to optimize rendering performance.  
    - **Optional Parameter**: Whether to optimize indices for cache (e.g., `true` for better performance).  

14. **`optimize_indices_for_cache()`**  
    - **Purpose**: Optimizes the order of indices for better performance.  
    - **Precondition**: Mesh must use triangle primitives.

---

### **Skeletal Animation Support**
15. **`set_bones(bones)`**  
    - **Purpose**: Sets bone indices for the next vertex.  
    - **Parameters**:  
      - `bones`: Array of 4 integers representing bone indices for skeletal animation.  

16. **`set_skin_weight_count(count)`**  
    - **Purpose**: Defines the number of bone weights per vertex.  
    - **Parameters**:  
      - `count`: Enum value (`SKIN_4_WEIGHTS`, `SKIN_8_WEIGHTS`).  

17. **`set_weights(weights)`**  
    - **Purpose**: Sets bone weights for the next vertex.  
    - **Parameters**:  
      - `weights`: Array of 4 floats representing bone weights.

---

### **Texture and Material Properties**
18. **`set_color(color)`**  
    - **Purpose**: Sets the color for the next vertex.  
    - **Note**: Material must have vertex color as albedo for visibility.

19. **`set_custom(channel, value)`**  
    - **Purpose**: Sets a custom value for a specific channel (e.g., for extra data).  
    - **Note**: Must be preceded by `set_custom_format(channel, format)`.  

20. **`set_custom_format(channel, format)`**  
    - **Purpose**: Defines the format of a custom channel (e.g., `CUSTOM_RGBA`).  
    - **Parameters**:  
      - `channel`: Index of the custom channel.  
      - `format`: Enum (`CUSTOM_RGB`, `CUSTOM_RGBA`, etc.).  

21. **`set_material(material)`**  
    - **Purpose**: Assigns a material to the current mesh.  

22. **`set_normal(normal)`**  
    - **Purpose**: Sets the normal for the next vertex.  

23. **`set_tangent(tangent)`**  
    - **Purpose**: Sets the tangent for the next vertex (used in shading).  

24. **`set_uv(uv)`**  
    - **Purpose**: Sets UV coordinates for the next vertex.  

25. **`set_uv2(uv)`**  
    - **Purpose**: Sets a second set of UV coordinates (e.g., for alpha or secondary textures).

---

### **Key Notes**
- **Order Matters**: Methods like `begin()` must be called before `append_vertex` or `set_*` calls.
- **Optimization**: `index()` and `optimize_indices_for_cache()` improve performance by reducing redundant vertex data.
- **Custom Data**: `set_custom_format` and `set_custom` allow for advanced data per vertex (e.g., for custom shaders).
- **Decals**: The `decal()` method is likely for adding overlays (e.g., in 2D) but is not well-documented.

---

This structure allows developers to build complex 3D meshes incrementally, with precise control over geometry, materials, and skeletal animation.