**Class Name:** PathFollow3D  
**Inherits:** Node3D → Node → Object  

---

### **Description**  
A node that samples a point from a Path3D based on a distance from the first vertex. Enables other nodes to follow the path by being its children.  

---

### **Properties**  
- **cubic_interp** (bool, default: `true`)  
  If `true`, interpolates between cached points using cubic methods; otherwise, linear.  

- **progress_ratio** (float, default: `0.0`)  
  Represents progress as a ratio (0.0 = first vertex, 1.0 = last). Multiplied by path length internally.  

- **rotation_mode** (RotationMode, default: `3`)  
  Determines axis rotation behavior (e.g., `3` allows full rotation).  

- **tilt_enabled** (bool, default: `true`)  
  If enabled, the Curve3D's tilt property affects orientation.  

- **v_offset** (float, default: `0.0`)  
  Offset perpendicular to the curve path.  

- **use_model_front** (bool, default: `false`)  
  If `true`, aligns the node's forward direction with the model's front axis.  

- **progress** (float, default: `0.0`)  
  Distance from the first vertex along the path.  

- **v_offset** (float, default: `0.0`)  
  Offset perpendicular to the curve.  

- **model_front** (bool, default: `false`)  
  If `true`, uses the model's front axis for orientation.  

---

### **Methods**  
- **correct_posture** (static)  
  Adjusts a Transform3D based on rotation_mode. Defines forward, up, and sideway directions.  

---

### **Enumerations**  
**RotationMode**  
- `0`: No rotation.  
- `1`: Rotate around Y-axis.  
- `2`: Rotate around X-axis.  
- `3`: Full rotation (default).  

---

### **Key Relationships**  
- Uses **Path3D** for path data.  
- Depends on **Curve3D** for tilt and offset calculations.  
- Interacts with **Vector3.FORWARD** and **Vector3.MODEL_FRONT** for orientation.  

--- 

**Note:** Properties like `progress` and `progress_ratio` are interdependent, with `progress_ratio` scaled by the path's length.