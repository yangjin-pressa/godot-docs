**Class Name**: XROrigin3D  
**Inherits**: Node3D → Node → Object  

---

### **Description**  
- A special node in AR/VR systems that maps physical location (tracking space center) to virtual location in the game world.  
- Only one origin node can be active at a time.  
- Other nodes like XRCamera3D, XRController3D, and XRAnchor3D must be direct children for spatial tracking to function.  
- Updates the position of this node when the character moves in the game world (e.g., driving a car, teleport systems).  

---

### **Tutorials**  
- [XR documentation index](../tutorials/xr/index)  

---

### **Properties**  
1. **current**:  
   - Type: bool  
   - Default: false  
   - Indicates if this origin node is currently used by XRServer.  

2. **world_scale**:  
   - Type: float  
   - Default: 1.0  
   - Scales the game world relative to the real world. Defaults to 1 game unit = 1 real meter.  

---

### **Property Descriptions**  
- **current**  
  - **set_current(value: bool)**: Sets the current status.  
  - **is_current()**: Checks if the origin is current.  

- **world_scale**  
  - **set_world_scale(value: float)**: Sets the scale.  
  - **get_world_scale()**: Retrieves the scale.  

---

### **Key Notes**  
- Only one origin node is active at a time.  
- The world_scale property mirrors XRServer.world_scale.  
- Direct children of the origin node are essential for spatial tracking.