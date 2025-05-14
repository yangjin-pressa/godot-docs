**GPUParticlesCollisionHeightField3D Class Overview**

---

### **Description**
- **Purpose**: A heightmap-based collision system for particles, updating based on visible layers in the scene.
- **Key Notes**:
  - Only `MeshInstance3D` meshes with layers matching `heightfield_mask` are considered for collision updates.
  - `follow_camera_enabled` forces heightmap updates on camera movement, with performance trade-offs.
  - `update_mode` controls update frequency: `UPDATE_MODE_ALWAYS` (high cost) or `UPDATE_MODE_ON_CHANGE` (default).

---

### **Properties**
1. **`follow_camera_enabled`**  
   - **Type**: `bool`  
   - **Default**: `false`  
   - **Set/Get**:  
     - `set_follow_camera_enabled(value: bool)`  
     - `is_follow_camera_enabled()`  
   - **Description**: If `true`, the heightmap follows the camera in global space. Use lower resolution for performance when enabled.

2. **`heightfield_mask`**  
   - **Type**: `int`  
   - **Default**: `1048575` (all 20 user-visible layers)  
   - **Set/Get**:  
     - `set_heightfield_mask(value: int)`  
     - `get_heightfield_mask()`  
   - **Description**: Visual layers included in collision updates. Layers 1–20 are user-visible; 21–32 are internal engine layers.

3. **`resolution`**  
   - **Type**: `Resolution`  
   - **Default**: `2` (lowest resolution)  
   - **Set/Get**:  
     - `set_resolution(value: Resolution)`  
     - `get_resolution()`  
   - **Description**: Higher resolution improves detail but reduces performance. Use lowest resolution when `update_mode` is `UPDATE_MODE_ALWAYS`.

4. **`size`**  
   - **Type**: `Vector3`  
   - **Default**: `Vector3(2, 2, 2)`  
   - **Set/Get**:  
     - `set_size(value: Vector3)`  
     - `get_size()`  
   - **Description**: 3D size of the heightmap. Smaller size improves quality but may not cover the entire scene.

5. **`update_mode`**  
   - **Type**: `UpdateMode`  
   - **Default**: `0` (UPDATE_MODE_ON_CHANGE)  
   - **Set/Get**:  
     - `set_update_mode(value: UpdateMode)`  
     - `get_update_mode()`  
   - **Description**: Controls when the heightmap updates. `UPDATE_MODE_ALWAYS` is costly and used only for significant scene changes.

---

### **Enumerations**
1. **`Resolution`**  
   - **Values**:  
     - `0` (lowest), `1`, `2`, etc. (higher values for more detail).  
   - **Description**: Defines the resolution of the heightmap.

2. **`UpdateMode`**  
   - **Values**:  
     - `0` (UPDATE_MODE_ON_CHANGE): Updates when scene layers change.  
     - `1` (UPDATE_MODE_ALWAYS): Updates every frame (high cost).

---

### **Methods**
1. **`get_heightfield_mask_value(layer_number: int)`**  
   - **Type**: `bool`  
   - **Const**: Yes  
   - **Description**: Returns `true` if the specified layer in `heightfield_mask` is enabled (1–20).

2. **`set_heightfield_mask_value(layer_number: int, value: bool)`**  
   - **Type**: `void`  
   - **Description**: Enables or disables a specific layer in `heightfield_mask`.

---

### **Important Notes**
- **Performance Considerations**:
  - Use `follow_camera_enabled` sparingly; lower resolution improves performance.
  - `UPDATE_MODE_ALWAYS` is reserved for scenarios with frequent scene changes.
- **Layer Management**:
  - Layers 1–20 are user-visible. Layers 21–32 are internal; they can be toggled via scripting for custom plugins.