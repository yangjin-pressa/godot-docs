**SkeletonModification2DTwoBoneIK**  
*Inherits: SkeletonModification2D < Resource < RefCounted < Object*  

---

### **Description**  
A modification for skeleton animation that uses the TwoBoneIK algorithm to animate bones based on a target position. This method is suitable for simple joint animations where two bones are involved.  

---

### **Properties**  
- **flip** (bool): Default: false. Determines whether the bones should be flipped.  
- **target** (NodePath): Default: empty. The target node for the animation.  
- **target_offset** (Vector2): Default: (0, 0). Offset to apply to the target position.  

**Methods:**  
- **set_flip(value: bool)**: Sets the flip state.  
- **get_flip()**: Gets the flip state.  
- **set_target(value: NodePath)**: Sets the target node.  
- **get_target()**: Gets the target node.  
- **set_target_offset(value: Vector2)**: Sets the target offset.  
- **get_target_offset()**: Gets the target offset.  

---

### **Methods for Bone Indices**  
- **get_joint_one_bone_idx()**: Returns the index of the first bone in the TwoBoneIK modification.  
- **set_joint_one_bone_idx(value: int)**: Sets the index of the first bone.  
- **get_joint_two_bone_idx()**: Returns the index of the second bone.  
- **set_joint_two_bone_idx(value: int)**: Sets the index of the second bone.  

---

### **Bone Node References**  
- **get_joint_one_bone2d_node()**: Returns the first Bone2D node.  
- **set_joint_one_bone2d_node(value: NodePath)**: Sets the first Bone2D node.  
- **get_joint_two_bone2d_node()**: Returns the second Bone2D node.  
- **set_joint_two_bone2d_node(value: NodePath)**: Sets the second Bone2D node.  

---

### **Key Features**  
- Uses the TwoBoneIK algorithm for joint animation.  
- Requires two bones for animation.  
- Supports flipping bones and target offset adjustments.  
- Inherits from `SkeletonModification2D`, `Resource`, and `RefCounted`.