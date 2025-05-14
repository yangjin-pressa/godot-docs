**Class: GPUParticlesCollisionSDF3D**  
**Inherits**: GPUParticlesCollision3D < VisualInstance3D < Node3D < Node < Object  

---

### **Description**  
- A collider for particles that uses a signed distance field (SDF) texture.  
- The SDF texture defines the shape of the collision area.  
- The SDF is hollow on the inside, and the `thickness` property controls the internal padding.  
- Baking requires a resolution (e.g., 2, 3, 4) and a size in 3D units.  
- The `bake_mask` specifies which visual layers are included in the SDF generation.  

---

### **Key Notes**  
- **Bake Mask**: Only `MeshInstance3D` objects with matching visual layers are included in the SDF.  
- **Resolution**: Higher resolutions improve accuracy but increase performance cost and memory usage.  
- **Thickness**: Adjusts the internal padding to prevent tunneling at high speeds.  
- **Texture**: Must be baked again when resolution or size changes.  

---

### **Properties**  
- **Resolution**  
  - Type: `Resolution` (enum)  
  - Default: 2  
  - Description: Defines the SDF texture resolution (e.g., 2 = 2x2, 3 = 3x3).  

- **Size**  
  - Type: `Vector3`  
  - Default: `Vector3(2, 2, 2)`  
  - Description: The collision shape's dimensions in 3D units.  

- **Texture**  
  - Type: `Texture3D`  
  - Description: The 3D texture representing the SDF.  

- **Thickness**  
  - Type: `float`  
  - Default: 1.0  
  - Description: Controls the internal padding of the collision shape.  

- **Bake Mask**  
  - Type: `int` (bitmask)  
  - Description: Specifies visual layers included in the SDF generation.  

---

### **Methods**  
- **get_bake_mask_value(layer_number)**  
  - Returns: `bool`  
  - Description: Checks if a specific layer (1–32) is enabled in the bake mask.  

- **set_bake_mask_value(layer_number, value)**  
  - Description: Enables or disables a specific layer in the bake mask.  

---

### **Enumeration: Resolution**  
- **2**: 2x2 resolution (lowest performance cost).  
- **3**: 3x3 resolution (balanced accuracy and performance).  
- **4**: 4x4 resolution (highest accuracy, but costly).  

---

### **Performance Considerations**  
- Use the lowest resolution possible for optimal performance.  
- Larger `size` values increase memory and VRAM usage.  
- Baking time and VRAM usage scale with resolution and object complexity.