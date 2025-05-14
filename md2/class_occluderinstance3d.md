**OccluderInstance3D**  
**Inherits**: VisualInstance3D → Node3D → Node → Object  

---

### **Overview**  
Used for occlusion culling to optimize rendering in 3D environments. This class defines an occluder resource that helps reduce the number of objects drawn in complex scenes.  

---

### **Key Features**  
- **Baking**: Generate an occluder resource via the **Bake Occluders** button in the editor.  
- **Occluder Types**: Supports custom polygons or primitives like QuadOccluder3D, BoxOccluder3D, SphereOccluder3D.  
- **Bake Mask**: Controls which layers of the scene are included in the occlusion calculation.  

---

### **Properties**  
1. **bake_mask**  
   - **Type**: `int`  
   - **Default**: `4294967295`  
   - **Description**: Bitmask controlling which scene layers are considered for occlusion.  

2. **bake_simplification_distance**  
   - **Type**: `float`  
   - **Default**: `0.1`  
   - **Description**: Distance threshold for simplifying occlusion calculations.  

3. **occluder**  
   - **Type**: `Occluder3D`  
   - **Description**: Reference to the occluder resource (e.g., a polygon or primitive shape).  

---

### **Methods**  
1. **get_bake_mask_value(layer_number)**  
   - **Returns**: `bool`  
   - **Description**: Checks if a specific layer (1–32) in the `bake_mask` is enabled.  

2. **set_bake_mask_value(layer_number, value)**  
   - **Description**: Enables or disables a specific layer in the `bake_mask`.  

---

### **Notes**  
- **Recomputation**: Moving an `OccluderInstance3D` requires re-baking to update its occluder resource.  
- **Project Settings**: Adjust occlusion settings in the project's **Physics 3D** configuration.  
- **Embree**: Used for efficient ray tracing in occlusion calculations. [Embree](https://www.embree.org/)  
- **meshoptimizer**: Tool for optimizing polygon meshes used in occluders. [meshoptimizer](https://meshoptimizer.org/)  

---

### **Tutorial**  
- [Bake Occluders](https://docs godotengine.org/en/latest/…/tutorial_occluder.html) for generating occluder resources.  

--- 

This class simplifies complex rendering by leveraging occlusion culling, improving performance in environments with large, overlapping objects.