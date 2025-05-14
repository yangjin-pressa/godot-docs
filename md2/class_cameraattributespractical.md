**Class: CameraAttributesPractical**  
**Description:**  
Manages camera settings for auto-exposure, depth of field, and other visual effects. This class is used in conjunction with the World2D camera system in Godot.

---

### **Properties**  
- **auto_exposure_max_sensitivity**  
  Type: `float`  
  Default: `800.0`  
- **auto_exposure_min_sensitivity**  
  Type: `float`  
  Default: `800.0`  
- **dof_blur_amount**  
  Type: `float`  
  Default: `0.0`  
- **dof_blur_near_distance**  
  Type: `float`  
  Default: `2.0`  
- **dof_blur_near_enabled**  
  Type: `bool`  
  Default: `false`  
- **dof_blur_near_transition**  
  Type: `float`  
  Default: `1.0`  
- **dof_blur_far_distance**  
  Type: `float`  
  Default: `2.0`  
- **dof_blur_far_enabled**  
  Type: `bool`  
  Default: `false`  
- **dof_blur_far_transition**  
  Type: `float`  
  Default: `1.0`  
- **dof_blur_far_sensitivity**  
  Type: `float`  
  Default: `800.0`  

---

### **Property Descriptions**  
- **auto_exposure_max_sensitivity**  
  Controls the maximum sensitivity for auto-exposure adjustments. Higher values increase the range of exposure adjustments.  

- **auto_exposure_min_sensitivity**  
  Controls the minimum sensitivity for auto-exposure adjustments. Lower values reduce the range of exposure adjustments.  

- **dof_blur_amount**  
  Determines the intensity of the depth of field blur effect. A higher value increases the blur effect.  

- **dof_blur_near_distance**  
  Defines the distance from the camera at which objects start being blurred for near depth of field effects.  

- **dof_blur_near_enabled**  
  Enables or disables the near depth of field blur effect. When enabled, objects within the specified distance are blurred.  

- **dof_blur_near_transition**  
  Controls the transition distance for near depth of field blur. A positive value scales blur from 0 to the specified amount over this distance.  

- **dof_blur_far_distance**  
  Defines the distance from the camera at which objects start being blurred for far depth of field effects.  

- **dof_blur_far_enabled**  
  Enables or disables the far depth of field blur effect. When enabled, objects beyond the specified distance are blurred.  

- **dof_blur_far_transition**  
  Controls the transition distance for far depth of field blur. A positive value scales blur from 0 to the specified amount over this distance.  

- **dof_blur_far_sensitivity**  
  Determines the sensitivity of the far depth of field blur effect. Higher values increase the intensity of the blur.  

---

**Notes:**  
- Depth of field blur is supported in **Forward+** and **Mobile** rendering modes but not in **Compatibility** mode.  
- Auto-exposure settings adjust the exposure based on scene brightness, affecting overall image clarity.