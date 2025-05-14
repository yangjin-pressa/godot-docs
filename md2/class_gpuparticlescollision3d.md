**Class Name:** GPUParticlesCollision3D  
**Inherits From:** VisualInstance3D → Node3D → Node → Object  

**Inherited By:**  
- GPUParticlesCollisionBox3D  
- GPUParticlesCollisionHeightField3D  
- GPUParticlesCollisionSDF3D  
- GPUParticlesCollisionSphere3D  

---

**Description**  
- Abstract base class for 3D particle collision shapes affecting GPUParticles3D nodes.  
- Particles can stop or bounce against collision shapes.  
- Collision shapes can be moved, rotated, and scaled during gameplay.  
- Non-uniform scaling is **not supported**.  
- Collision shapes can be temporarily disabled by hiding them.  

**Key Notes:**  
- **Collision Mode Requirement:**  
  - `ParticleProcessMaterial.collision_mode` must be set to `COLLECTION_RIGID` or `COLLISION_HIDE_ON_CONTACT` for collision to work.  
- **Targeted Effect:**  
  - Only affects GPUParticles3D, not CPUParticles3D.  
- **Stuttering Issue:**  
  - Particles pushed by moving colliders may experience visible stuttering.  
  - Mitigate by setting `GPUParticles3D.fixed_fps` to `0` or a value matching the target framerate.  

---

**Properties**  
**cull_mask** (int) = 4294967295  
- **Description:**  
  - Determines which particle rendering layers (VisualInstance3D.layers) are affected by the collision shape.  
  - By default, all particles with `collision_mode` set to `COLLISION_RIGID` or `COLLISION_HIDE_ON_CONTACT` are affected.  
  - Specific layers can be unchecked to exclude certain particles from collision.  
  - Collision can also be disabled per-process material via `collision_mode`.  

**Methods**  
- **set_cull_mask(value: int)**  
- **get_cull_mask()**  

---

**Citations**  
- [class_GPUParticlesCollision3D_property_cull_mask](class_GPUParticlesCollision3D_property_cull_mask)  
- [ParticleProcessMaterial.collision_mode](ParticleProcessMaterial_property_collision_mode)  
- [GPUParticles3D.fixed_fps](GPUParticles3D_property_fixed_fps)