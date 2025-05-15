**Class: XRPose**  
**Inherits:** RefCounted < Object  

---

### **Description**  
XR runtimes identify multiple locations on devices (e.g., controllers) with spatial tracking. This class stores orientation, position, linear velocity, and angular velocity for a tracked pose.  

---

### **Tutorials**  
- [XR documentation index](../tutorials/xr/index)  

---

### **Properties**  
- **angular_velocity**: `Vector3` (default: Vector3(0, 0, 0))  
  - Angular velocity for the pose.  
- **has_tracking_data**: `bool` (default: false)  
  - Indicates if tracking data is current.  
- **linear_velocity**: `Vector3` (default: Vector3(0, 0, 0))  
  - Linear velocity of the pose.  
- **name**: `StringName` (default: &"")  
  - Name of the pose (e.g., "root", "aim", "grip").  
- **tracking_confidence**: `TrackingConfidence` (default: 0)  
  - Confidence level (0 = none, 1 = low, 2 = high).  
- **transform**: `Transform3D` (default: Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0))  
  - Transform from the XR runtime.  

---

### **Methods**  
- **get_adjusted_transform()**: `Transform3D` (const)  
  - Returns the transform adjusted for world scale and reference frame.  

---

### **Enumerations**  
**TrackingConfidence**  
- **XR_TRACKING_CONFIDENCE_NONE** = 0  
  - No tracking data available.  
- **XR_TRACKING_CONFIDENCE_LOW** = 1  
  - Tracking may be inaccurate (e.g., partially obscured).  
- **XR_TRACKING_CONFIDENCE_HIGH** = 2  
  - Tracking is accurate and up-to-date.  

---

### **Property Descriptions**  
- **angular_velocity**  
  - Sets/gets the angular velocity.  
- **has_tracking_data**  
  - Sets/gets whether tracking data is valid.  
- **linear_velocity**  
  - Sets/gets the linear velocity.  
- **name**  
  - Sets/gets the pose name (e.g., "root", "aim", "grip").  
- **tracking_confidence**  
  - Sets/gets the confidence level.  
- **transform**  
  - Sets/gets the transform from the XR runtime.  

---

### **Method Descriptions**  
- **get_adjusted_transform()**  
  - Returns the adjusted transform for positioning XRNode3D objects.