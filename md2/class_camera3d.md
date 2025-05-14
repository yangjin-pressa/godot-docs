Here's a structured summary of the **Godot 3D Camera** class, organized by key properties and methods, along with practical usage examples:

---

### **Key Properties**
1. **`cull_mask`**  
   - **Type**: `int`  
   - **Purpose**: Controls which layers are visible. Use `bitfield` to enable/disable layers (1–20).  
   - **Example**:  
     ```gdscript
     camera.set_cull_mask_value(1, true)  # Enable layer 1
     ```

2. **`fov`**  
   - **Type**: `float`  
   - **Purpose**: Field of view angle in degrees for perspective cameras.  
   - **Example**:  
     ```gdscript
     camera.set_perspective(90, 0.1, 100)  # 90° FOV, near=0.1, far=100
     ```

3. **`frustum_offset`**  
   - **Type**: `Vector2`  
   - **Purpose**: Adjusts the frustum's position offset for custom camera setups.  
   - **Example**:  
     ```gdscript
     camera.set_frustum(10, Vector2(5, 5), 0.1, 100)  # Size=10, offset=(5,5)
     ```

4. **`orthogonal_size`**  
   - **Type**: `float`  
   - **Purpose**: Size of the orthogonal projection's view area (used for 2D games).  
   - **Example**:  
     ```gdscript
     camera.set_orthogonal(200, 0.1, 100)  # Size=200 units
     ```

---

### **Key Methods**
#### **Camera Setup**
- **`set_perspective(fov, z_near, z_far)`**  
  Sets perspective projection.  
  ```gdscript
  camera.set_perspective(60, 0.1, 100)  # 60° FOV, near=0.1, far=100
  ```

- **`set_orthogonal(size, z_near, z_far)`**  
  Sets orthogonal projection.  
  ```gdscript
  camera.set_orthogonal(200, 0.1, 100)  # Size=200 units
  ```

- **`set_frustum(size, offset, z_near, z_far)`**  
  Sets frustum projection for custom cameras.  
  ```gdscript
  camera.set_frustum(10, Vector2(5, 5), 0.1, 100)  # Size=10, offset=(5,5)
  ```

#### **Projection & Unprojection**
- **`project_position(screen_point, z_depth)`**  
  Returns a 3D world point corresponding to a 2D screen coordinate at a given depth.  
  ```gdscript
  var world_point = camera.project_position(Vector2(100, 100), 5)  # z=5 units
  ```

- **`unproject_position(world_point)`**  
  Converts a 3D world point to a 2D screen coordinate.  
  ```gdscript
  var screen_pos = camera.unproject_position(world_point)
  ```

- **`project_ray_origin(screen_point)`**  
  Returns the origin of a ray from the screen point.  
  ```gdscript
  var ray_origin = camera.project_ray_origin(Vector2(100, 100))
  ```

- **`project_ray_normal(screen_point)`**  
  Returns the normal vector of a ray from the screen point.  
  ```gdscript
  var ray_normal = camera.project_ray_normal(Vector2(100, 100))
  ```

#### **3D Position Checks**
- **`is_position_in_frustum(world_point)`**  
  Checks if a point is inside the camera's frustum.  
  ```gdscript
  var is_in_frustum = camera.is_position_in_frustum(world_point)
  ```

- **`is_position_behind(world_point)`**  
  Checks if a point is behind the camera.  
  ```gdscript
  var is_behind = camera.is_position_behind(world_point)
  ```

#### **Cull Mask Control**
- **`set_cull_mask_value(layer, value)`**  
  Enables/disables a specific layer.  
  ```gdscript
  camera.set_cull_mask_value(1, true)  # Enable layer 1
  ```

---

### **Example: UI Element Over 3D Object**
```gdscript
# Check if a 3D point is in front of the camera
var is_in_front = camera.is_position_behind(global_transform.origin)
if not is_in_front:
    # Project the 3D point to 2D for UI
    var screen_pos = camera.unproject_position(global_transform.origin)
    control.position = screen_pos
    control.visible = true
```

---

### **Key Notes**
1. **Camera Modes**:  
   - **Perspective**: Simulates real-world depth (e.g., for 3D scenes).  
   - **Orthogonal**: Flat 2D projection (e.g., for 2D games).  
   - **Frustum**: Custom projection for specialized views (e.g., 3D games with custom clipping).  

2. **Viewport Management**:  
   Use `make_current()` to set the camera as the current camera for the viewport.  
   ```gdscript
   camera.make_current()
   ```

3. **Culling**:  
   Use `cull_mask` to hide objects outside the camera's view.  

4. **Projection Depth**:  
   The `z_depth` parameter in `project_position()` allows precise control over 3D depth in the scene.

---

This guide covers the core functionalities of the Godot 3D Camera, including setup, projection, and visibility checks. Use these methods to create advanced camera systems, UI overlays, and 3D interaction logic in Godot.