### XRHandTracker Class Overview

The `XRHandTracker` class is designed to manage and provide access to hand tracking data, including joint positions, orientations, velocities, and other related properties. It supports both retrieving and setting tracking data, and includes flags to indicate the validity and tracking state of each joint.

---

### **Enums**

#### **HandJoint**
Defines the possible joints in a hand, each with a unique identifier:
- **HAND_JOINT_INDEX** (0): Index finger tip
- **HAND_JOINT_MIDDLE** (1): Middle finger tip
- **HAND_JOINT_RING** (2): Ring finger tip
- **HAND_JOINT_PINKY** (3): Pinky finger tip
- **HAND_JOINT_THUMB** (4): Thumb tip
- **HAND_JOINT_WRESTLE** (5): Wrestle joint (for grip tracking)
- **HAND_JOINT_WRESTLE_PALM** (6): Wrestle palm joint

#### **HandJointFlags**
Flags indicating the validity and tracking state of a joint's data:
- **HAND_JOINT_FLAG_ORIENTATION_VALID** (1): Orientation data is valid
- **HAND_JOINT_FLAG_ORIENTATION_TRACKED** (2): Orientation is actively tracked
- **HAND_JOINT_FLAG_POSITION_VALID** (4): Position data is valid
- **HAND_JOINT_FLAG_POSITION_TRACKED** (8): Position is actively tracked
- **HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID** (16): Linear velocity data is valid
- **HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID** (32): Angular velocity data is valid

#### **HandTrackingSource**
Specifies the source of hand tracking data:
- **HAND_TRACKING_SOURCE_CAMERA** (0): Camera-based tracking
- **HAND_TRACKING_SOURCE_AIM** (1): Aim-based tracking (e.g., using a controller)

---

### **Properties**

#### **hand_tracking_source**
- **Type**: `HandTrackingSource`
- **Access**: Read-write
- **Description**: The source of the hand tracking data (e.g., camera or aim).

#### **has_tracking_data**
- **Type**: `bool`
- **Access**: Read-write
- **Description**: Indicates whether the hand tracking data is valid (`true`) or invalid (`false`).

---

### **Methods**

#### **get_hand_joint_angular_velocity(joint)**
- **Returns**: `Vector3` – Angular velocity for the specified joint.
- **Note**: This is a `const` method (no side effects).

#### **get_hand_joint_flags(joint)**
- **Returns**: `HandJointFlags` – Flags indicating the validity and tracking state of the joint's data.

#### **get_hand_joint_linear_velocity(joint)**
- **Returns**: `Vector3` – Linear velocity for the specified joint.
- **Note**: This is a `const` method.

#### **get_hand_joint_radius(joint)**
- **Returns**: `float` – Radius of the joint (e.g., for collision detection).

#### **get_hand_joint_transform(joint)**
- **Returns**: `Transform3D` – Transform (position and orientation) for the specified joint.

#### **set_hand_joint_angular_velocity(joint, angular_velocity)**
- **Parameters**: 
  - `joint`: `HandJoint` – Target joint.
  - `angular_velocity`: `Vector3` – Angular velocity to set.
- **Note**: This method is virtual and should be overridden by the user for meaningful behavior.

#### **set_hand_joint_flags(joint, flags)**
- **Parameters**: 
  - `joint`: `HandJoint` – Target joint.
  - `flags`: `HandJointFlags` – Flags to set (bitfield combination).
- **Note**: Sets the validity and tracking state flags for the joint.

#### **set_hand_joint_linear_velocity(joint, linear_velocity)**
- **Parameters**: 
  - `joint`: `HandJoint` – Target joint.
  - `linear_velocity`: `Vector3` – Linear velocity to set.
- **Note**: This method is virtual and should be overridden by the user for meaningful behavior.

#### **set_hand_joint_radius(joint, radius)**
- **Parameters**: 
  - `joint`: `HandJoint` – Target joint.
  - `radius`: `float` – Radius value to set.
- **Note**: This method is virtual and should be overridden by the user for meaningful behavior.

#### **set_hand_joint_transform(joint, transform)**
- **Parameters**: 
  - `joint`: `HandJoint` – Target joint.
  - `transform`: `Transform3D` – Transform (position and orientation) to set.
- **Note**: This method is virtual and should be overridden by the user for meaningful behavior.

---

### **Key Concepts**

- **Flags**: The `HandJointFlags` enum allows checking if tracking data is valid (`OrientationValid`, `PositionValid`, etc.) or actively tracked (`OrientationTracked`, `PositionTracked`).
- **Transform Data**: The `get_hand_joint_transform()` method provides the 3D position and orientation of a joint, which is essential for rendering or simulation.
- **Joint Radius**: The `get_hand_joint_radius()` method returns the radius of a joint, useful for collision detection or physics simulations.
- **Data Validity**: The `has_tracking_data` property and flags indicate whether the tracking data is reliable for the current frame.

---

### **Use Cases**
- **Hand Simulation**: Setting joint transforms and velocities for custom hand movements.
- **Tracking Validation**: Checking flags to determine if data from a joint is valid before using it.
- **Camera/Aim Source**: Switching between camera-based and aim-based tracking sources for different use cases.

This class is ideal for applications requiring precise hand tracking, such as VR gesture recognition, augmented reality, or robotics.