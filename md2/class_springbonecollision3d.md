**Class: SpringBoneCollision3D**  
**Inherits:** Node3D → Node → Object  
**Inherited By:** SpringBoneCollisionCapsule3D, SpringBoneCollisionPlane3D, SpringBoneCollisionSphere3D  

---

### **Description**  
- A collision object that interacts with `SpringBoneSimulator3D`.  
- Must be a child of `SpringBoneSimulator3D` to function; otherwise, it has no effect.  
- Collisions and sliding are processed in the simulator's collision list order (set via `set_collision_path`).  
- If `are_all_child_collisions_enabled` is true, the order matches the SceneTree hierarchy.  
- If `bone` is set, it synchronizes with the ancestor `Skeleton3D`'s bone pose before the simulator's modification process.  
- **Warning:** Scaling a `SpringBoneCollision3D` may cause unexpected behavior. Ensure the parent `Skeleton3D` and its bones are not scaled.  

---

### **Properties**  
- **bone**: `int` = `-1`  
  - Index of the attached bone.  
- **bone_name**: `String` = `""`  
  - Name of the attached bone.  
- **position_offset**: `Vector3`  
  - Offset of the position from the skeleton's bone pose.  
- **rotation_offset**: `Quaternion`  
  - Offset of the rotation from the skeleton's bone pose.  

---

### **Methods**  
- **get_skeleton() → Skeleton3D**  
  - Returns the parent `Skeleton3D` of the simulator if found.  

---

### **Key Notes**  
- **Bone Synchronization**: If `bone` is set, the collision object's position/rotation is derived from the ancestor `Skeleton3D`'s bone pose.  
- **Collision Order**: Depends on the simulator's collision list and whether `are_all_child_collisions_enabled` is true.  
- **Scaling Warning**: Avoid scaling `SpringBoneCollision3D` as it may disrupt collision behavior.  

---  
**References**  
- [Skeleton3D](https://godotengine.org/documentation/standalone/classes/class_skeleton3d.html)  
- [SpringBoneSimulator3D](https://godotengine.org/documentation/standalone/classes/class_springbonesimulator3d.html)