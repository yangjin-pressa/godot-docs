The `SkeletonModification` class in Godot (likely part of a physics or animation system) is used to configure **jiggle joints** for a skeleton, allowing dynamic physics-based movement. Below is a structured breakdown of its properties and methods:

---

### **Key Concepts**
- **Jiggle Joints**: Physics joints that allow flexible, bouncy movement for skeletal animations.
- **Collision Mask**: Determines which colliders the jiggle modifier interacts with.
- **Bone Index/Node**: Links the jiggle joint to a specific bone in the skeleton.
- **Physics Parameters**: Damping, mass, gravity, and override settings control how each joint behaves.

---

### **Properties**
1. **collision_mask**  
   - **Type**: `int`  
   - **Purpose**: Collision mask for the jiggle modifier. Determines which colliders the physics interaction considers.

2. **default_joint_settings**  
   - **Properties**:  
     - `damping`: Default damping for joints.  
     - `gravity`: Default gravity vector.  
     - `mass`: Default mass.  
     - `override`: Whether joints override default settings.  
     - `use_gravity`: Whether gravity is applied to the joint.

---

### **Methods**
#### **Joint-Specific Settings**
- **set_jiggle_joint_bone2d_node(joint_idx, bone2d_node)**  
  Links a joint to a specific bone (via `NodePath`).  

- **set_jiggle_joint_bone_index(joint_idx, bone_idx)**  
  Sets the bone index in the skeleton. This updates the bone2d_node automatically if possible.  

- **set_jiggle_joint_damping(joint_idx, damping)**  
  Sets damping for a joint. Higher values reduce oscillation.  

- **set_jiggle_joint_gravity(joint_idx, gravity)**  
  Sets the gravity vector for a joint.  

- **set_jiggle_joint_mass(joint_idx, mass)**  
  Sets the mass of a joint (affects how it responds to forces).  

- **set_jiggle_joint_override(joint_idx, override)**  
  If `true`, the joint uses its own settings instead of default ones.  

- **set_jiggle_joint_stiffness(joint_idx, stiffness)**  
  Controls how rigid the joint is. Higher stiffness reduces flexibility.  

- **set_jiggle_joint_use_gravity(joint_idx, use_gravity)**  
  Whether the joint is influenced by gravity.  

#### **Collision Settings**
- **set_collision_mask(collision_mask)**  
  Sets the collision mask for the modifier.  

- **set_use_colliders(use_colliders)**  
  If `true`, the modifier avoids colliding with physics objects.  

---

### **Example Workflow**
```gdscript
# Assume 'skeleton_mod' is an instance of SkeletonModification
# Link a joint to a bone
skeleton_mod.set_jiggle_joint_bone_index(0, 2)  # Joint 0 uses bone index 2
skeleton_mod.set_jiggle_joint_damping(0, 0.5)   # Damp joint 0
skeleton_mod.set_jiggle_joint_mass(0, 1.0)      # Set mass to 1.0
skeleton_mod.set_use_colliders(true)            # Enable collision avoidance
```

---

### **Key Notes**
- **Bone Indexing**: Use the skeleton's bone indices to link joints. Ensure the bone2d_node is correctly set.
- **Override Behavior**: Use `override` to customize individual joints instead of applying global settings.
- **Collision Mask**: Useful for isolating interactions with specific objects (e.g., avoiding collisions with ground).

This class is ideal for creating dynamic, physics-based animations where joints need to flexibly move while avoiding obstacles or adhering to environmental constraints.