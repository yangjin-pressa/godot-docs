Here is a structured description of the `SpringBoneSimulator3D` class methods, organized by their functionality and parameters:

---

### **1. Bone Chain Initialization**
- **`set_root_bone(index: int, bone: int)`**  
  Sets the root bone index for a specific bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index (e.g., 0, 1, 2).  
    - `bone`: Index of the root bone in the bone hierarchy.

- **`set_end_bone(index: int, bone: int)`**  
  Sets the end bone index for a specific bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `bone`: Index of the end bone.

- **`set_root_bone_name(index: int, name: str)`**  
  Sets the name of the root bone for a bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `name`: String name of the root bone.

- **`set_end_bone_name(index: int, name: str)`**  
  Sets the name of the end bone for a bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `name`: String name of the end bone.

---

### **2. Joint Configuration**
- **`set_individual_config(index: int, enabled: bool)`**  
  Enables or disables individual joint configuration for a bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `enabled`: Boolean flag to toggle per-joint settings.

- **`set_joint_drag(index: int, joint: int, drag: float)`**  
  Sets drag force for a specific joint in a bone chain (when `individual_config` is enabled).  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `joint`: Joint index within the chain.  
    - `drag`: Drag force value.

- **`set_joint_gravity(index: int, joint: int, gravity: float)`**  
  Sets gravity magnitude for a specific joint.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `joint`: Joint index.  
    - `gravity`: Gravity value.

- **`set_joint_gravity_direction(index: int, joint: int, direction: Vector3)`**  
  Sets gravity direction for a specific joint.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `joint`: Joint index.  
    - `direction`: 3D vector for gravity direction.

- **`set_joint_radius(index: int, joint: int, radius: float)`**  
  Sets joint radius for a specific joint.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `joint`: Joint index.  
    - `radius`: Radius value.

- **`set_joint_rotation_axis(index: int, joint: int, axis: RotationAxis)`**  
  Sets rotation axis for a specific joint.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `joint`: Joint index.  
    - `axis`: Rotation axis enum (e.g., X, Y, Z).

- **`set_joint_stiffness(index: int, joint: int, stiffness: float)`**  
  Sets stiffness force for a specific joint.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `joint`: Joint index.  
    - `stiffness`: Stiffness value.

---

### **3. Global Chain Settings**
- **`set_rotation_axis(index: int, axis: RotationAxis)`**  
  Sets the rotation axis for an entire bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `axis`: Rotation axis (e.g., X, Y, Z).

- **`set_stiffness(index: int, stiffness: float)`**  
  Sets stiffness force for an entire bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `stiffness`: Stiffness value.

- **`set_drag(index: int, drag: float)`**  
  Sets drag force for an entire bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `drag`: Drag value.

- **`set_radius(index: int, radius: float)`**  
  Sets joint radius for an entire bone chain.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `radius`: Radius value.

---

### **4. Damping Curves**
- **`set_drag_damping_curve(index: int, curve: Curve)`**  
  Sets a damping curve for drag settings.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `curve`: Curve object for damping.

- **`set_radius_damping_curve(index: int, curve: Curve)`**  
  Sets a damping curve for radius settings.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `curve`: Curve object for damping.

- **`set_stiffness_damping_curve(index:_one, curve: Curve)`**  
  Sets a damping curve for stiffness settings.  
  - **Parameters**:  
    - `index`: Bone chain index.  
    - `curve`: Curve object for damping.

---

### **5. Important Notes**
- **Rotation Axis and Forward Vector**: The rotation axis and forward direction of the bone chain should not be colinear to avoid unintended twisting or rotation.  
- **Per-Joint vs. Global Settings**: Methods like `set_joint_drag` and `set_rotation_axis` apply to individual joints or the entire chain, depending on whether `individual_config` is enabled.  
- **Curve Modulation**: Damping curves (e.g., `set_drag_damping_curve`) modulate values like drag, radius, or stiffness over time, enabling dynamic behavior.

---

This structure allows precise control over bone chain dynamics, with options for global or per-joint adjustments. Ensure proper alignment of rotation axes and gravity directions to maintain intended physics behavior.