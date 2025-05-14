**Class: OpenXRHand**  
- **Deprecated**: Use [XRHandModifier3D](class_XRHandModifier3D) instead.  
- **Inherits**: Node3D → Node → Object  

---

### **Description**  
A class for handling hand tracking in 3D environments. Sets the pose positions for a skeleton node based on hand tracking data.  

---

### **Properties**  
- **bone_update** (BoneUpdate): 0  
- **hand** (Hands): 0  
- **hand_skeleton** (NodePath): NodePath("")  
- **motion_range** (MotionRange): 0  
- **skeleton_rig** (SkeletonRig): 0  

---

### **Enumerations**  
#### **BoneUpdate**  
- **BONE_UPDATE_STATIC** (0): Static bone update mode.  
- **BONE_UPDATE_DYNAMIC** (1): Dynamic bone update mode.  

#### **Hands**  
- **HAND_LEFT** (0): Left hand.  
- **HAND_RIGHT** (1): Right hand.  
- **HAND_MAX** (2): Maximum value.  

#### **MotionRange**  
- **MOTION_RANGE_UNOBSTRUCTED** (0): Unrestricted motion.  
- **MOTION_RANGE_CONFORM_TO_CONTROLLER** (1): Motion constrained to controller.  
- **MOTION_RANGE_MAX** (2): Maximum value.  

#### **SkeletonRig**  
- **SKELETON_RIG_OPENXR** (0): OpenXR-compliant skeleton.  
- **SKELETON_RIG_CUSTOM** (1): Custom skeleton.  

---

### **Property Descriptions**  
- **bone_update**: Defines the mode for updating bone positions.  
- **hand**: Specifies which hand (left/right) to track.  
- **hand_skeleton**: A reference to the skeleton node to update.  
- **motion_range**: Constrains hand motion within a defined range.  
- **skeleton_rig**: Determines the type of skeleton rig used.  

--- 

**Note**: This class is deprecated in favor of [XRHandModifier3D](class_XRHandModifier3D).