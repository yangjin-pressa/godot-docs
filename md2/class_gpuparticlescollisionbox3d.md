**Class Name:** GPUParticlesCollisionBox3D  
**Inherits From:**  
- GPUParticlesCollision3D  
  - VisualInstance3D  
    - Node3D  
      - Node  
        - Object  

---

### **Description**  
A box-shaped 3D particle collision shape affecting `GPUParticles3D` nodes.  
- Real-time collision detection.  
- Can be moved, rotated, and scaled during gameplay.  
- **Note:** Non-uniform scaling is not supported.  

---

### **Key Notes**  
1. **Collision Mode Requirement:**  
   - Set `ParticleProcessMaterial.collision_mode` to `ParticleProcessMaterial.COLLISION_RIGID` or `ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT` for collision to work.  

2. **Affected Targets:**  
   - Only affects `GPUParticles3D`; does not impact `CPUParticles3D`.  

---

### **Properties**  
- **size**: `Vector3` (default: `Vector3(2, 2, 2)`)  
  - Collision box dimensions in 3D units.  

---

### **Methods**  
- **set_size(value: Vector3)**:  
  - Sets the collision box size.  

- **get_size()**:  
  - Returns the collision box size.  

---

### **Property Descriptions**  
- **size**:  
  - Defines the size of the box-shaped collision area.  

--- 

**Generated From:**  
GitHub: [https://github.com/godotengine/godot/tree/master/doc/classes/GPUParticlesCollisionBox3D.xml](https://github.com/godotengine/godot/tree/master/doc/classes/GPUParticlesCollisionBox3D.xml)