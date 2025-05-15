**XRNode3D Class Overview**  
- Inherits from: `Node3D`  

---

### **Description**  
- A class for handling extended reality (XR) interactions.  
- Supports features like haptic feedback and pose tracking.  

---

### **Tutorials**  
- [XR documentation index](../tutorials/xr/index)  

---

### **Properties**  
- **physics_interpolation_mode**: `PhysicsInterpolationMode`  
  - Controls interpolation settings for physics simulations.  
  - Default value: `PhysicsInterpolationMode::PHYSICS_INTERPOLATION_LINEAR`.  

- **pose**: `String`  
  - Name of the pose (e.g., "hand", "head").  
  - Godot defines standard pose names.  

- **show_when_tracked**: `bool`  
  - Determines whether the object is visible when the tracking is active.  
  - Default: `true`.  

- **tracker**: `Node3D`  
  - Reference to the tracker node used for spatial awareness.  

---

### **Methods**  
- **get_has_tracking_data()**: `bool`  
  - Returns whether tracking data is available.  
  - **Note**: This method should be overridden by the user for custom behavior.  

- **get_is_active()**: `bool`  
  - Returns whether the XR interface is active.  
  - **Note**: This method has no side effects.  

- **get_pose()**: `String`  
  - Returns the current pose name.  

- **trigger_haptic_pulse(action_name: String, frequency: Float = 0.0, amplitude: Float, duration_sec: Float, delay_sec: Float) → void**  
  - Triggers a haptic pulse on connected devices.  
  - **Parameters**:  
    - `action_name`: Name of the haptic action.  
    - `frequency`: Pulse frequency (default: 0.0 for system default).  
    - `amplitude`: Pulse amplitude (0.0–1.0).  
    - `duration_sec`: Duration of the pulse in seconds.  
    - `delay_sec`: Delay before the pulse is applied.  

---

### **Signals**  
- **tracking_changed()**:  
  - Emitted when tracking state changes (e.g., from untracked to tracked).  

---

### **Additional Notes**  
- **Virtual methods**: Override these methods in subclasses to customize behavior.  
- **Constants**: Methods like `get_is_active()` are static and do not modify instance variables.  
- **Haptic parameters**: Amplitude and frequency are normalized values.