**VoxelGIData Class**  
Inherits from: `BaseNode`  

---

### **Description**  
A class containing baked voxel data for the `VoxelGI` node. Used for light propagation in 3D environments. Data is stored in a `.gpb` file and can be modified post-bake.  

**Tutorials**  
- [Link to tutorial about VoxelGI](https://godotengine.org/tutorials/3d/voxel-gi/)  

---

### **Properties**  
| Name            | Type        | Default | Description                                                                 |
|-----------------|-------------|---------|-----------------------------------------------------------------------------|
| **bias**        | `float`     | 0.0     | Controls light reflection. Higher values reduce self-reflectivity.         |
| **normal_bias** | `float`     | 0.0     | Similar to `bias`, affects indirect lighting quality.                     |
| **interior**    | `bool`      | `false` | If `true`, ignores environment lighting; otherwise, uses it.              |
| **use_two_bounces** | `bool`   | `true`  | Enables two light bounces for more natural indirect lighting.             |
| **propagation** | `float`     | 0.5     | Light intensity multiplier for reflections.                              |

**Notes:**  
- Adjust `bias` and `normal_bias` to balance self-reflectivity and lighting quality.  
- `interior` affects how environment lighting is incorporated.  
- `use_two_bounces` increases brightness but may require tweaking `propagation` and `energy`.  

---

### **Methods**  
1. **`allocate()`**  
   - **Parameters:**  
     - `to_cell_xform`: `Transform3D`  
     - `aabb`: `AABB`  
     - `octree_size`: `Vector3`  
     - `octree_cells`: `PackedByteArray`  
     - `data_cells`: `PackedByteArray`  
     - `distance_field`: `PackedByteArray`  
     - `level_counts`: `PackedInt32Array`  
   - **Description:** Initializes voxel data. No description available.  

2. **`get_bounds()`**  
   - **Returns:** `AABB`  
   - **Description:** Returns the bounds of the baked data. Mismatch with `VoxelGI.size` if modified without rebaking.  

3. **`get_data_cells()`**  
   - **Returns:** `PackedByteArray`  
   - **Description:** No description available.  

4. **`get_level_counts()`**  
   - **Returns:** `PackedInt32Array`  
   - **Description:** No description available.  

5. **`get_octree_cells()`**  
   - **Returns:** `PackedByteArray`  
   - **Description:** No description available.  

6. **`get_octree_size()`**  
   - **Returns:** `Vector3`  
   - **Description:** No description available.  

7. **`get_to_cell_xform()`**  
   - **Returns:** `Transform3D`  
   - **Description:** No description available.  

---

### **Key Notes**  
- Save to `.gpb` files for use in projects.  
- Methods like `get_bounds()` may require rebaking if `VoxelGI.size` is modified.  
- Missing method descriptions: Contributions welcome.