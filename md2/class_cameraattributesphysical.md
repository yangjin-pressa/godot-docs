**Class Name:** `CameraAttributesPhysical`  
**Inheritance:** `CameraAttributes` → `Resource`  

---

### **Description**  
The `CameraAttributesPhysical` class manages physically-based camera settings, including **exposure**, **auto-exposure**, and **depth of field**. It is used in three contexts:  
- **WorldEnvironment**: Overrides properties like `Camera3D.far` and `Camera3D.near` when attached to a camera.  
- **Camera3D**: Overrides `Camera3D.fov`, `Camera3D.keep_aspect`, and other properties when assigned as `Camera3D.attributes`.  
- **VoxelGI/LightmapGI**: Sets default values for certain properties.  

**Key Notes:**  
- Default settings are optimized for outdoor environments.  
- Indoor use requires manual adjustments.  
- The class internally calculates depth of field based on `frustum_focal_length` and `frustum_focus_distance`.  

---

### **Tutorials**  
- [Physical Light and Camera Units](https://docs.godotengine.org/en/latest/)... (tutorial link)  

---

### **Properties**  
1. **auto_exposure**  
   - **Type:** `float`  
   - **Default:** `0.0`  
   - **Description:** Controls auto-exposure adjustments.  

2. **frustum_far**  
   - **Type:** `float`  
   - **Default:** `4000.0`  
   - **Description:** Overrides `Camera3D.far`. Used for depth of field calculations.  

3. **frustum_focal_length**  
   - **Type:** `float`  
   - **Default:** `35.0`  
   - **Description:** Lens-to-aperture distance (in mm). Affects field of view and depth of field.  

4. **frustum_focus_distance**  
   - **Type:** `float`  
   - **Default:** `10.0`  
   - **Description:** Distance to the most in-focus object. Clamped to be larger than `frustum_focal_length`.  

5. **frustum_near**  
   - **Type:** `float`  
   - **Default:** `0.05`  
   - **Description:** Overrides `Camera3D.near`. Used for depth of field calculations.  

6. **aperture**  
   - **Type:** `float`  
   - **Default:** `1.0`  
   - **Description:** Controls depth of field. Larger values narrow focus.  

7. **exposure**  
   - **Type:** `float`  
   - **Default:** `1.0`  
   - **Description:** Adjusts overall brightness.  

---

### **Method Descriptions**  
- **get_fov()**  
  - **Returns:** `float` (vertical field of view).  
  - **Description:** Calculates the vertical FOV based on `frustum_focal_length`. This value is recalculated whenever `frustum_focal_length` changes.  

---

### **Key Notes**  
- **Physical Light Units:** Properties like `frustum_focal_length` and `aperture` are tied to real-world units (mm, meters).  
- **Overriding Behavior:** When attached to `Camera3D`, this class overrides properties like `Camera3D.fov` and `Camera3D.keep_aspect`.  
- **Clamping:** `frustum_focus_distance` is internally clamped to be at least 1 mm larger than `frustum_focal_length`.  

--- 

This class is essential for advanced camera control in Godot, allowing precise adjustments for lighting, depth, and field of view in 3D scenes.