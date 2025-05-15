**Class:** VisualShaderNodeParticleEmitter  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  
**Inherited By:** VisualShaderNodeParticleBoxEmitter, VisualShaderNodeParticleMeshEmitter, VisualShaderNodeParticleRingEmitter, VisualShaderNodeParticleSphereEmitter  

---

### Description  
Particle emitter nodes are used in the "start" step of particle shaders to define the starting position of particles. Connect them to the Position output port.  

---

### Properties  
- **mode_2d** (bool) = false  
  Determines if the emitter result is projected to 2D space. Default is false for 3D use.  

---

### Method Descriptions  
- **set_mode_2d(value: bool)**  
  Sets the 2D mode flag.  

- **is_mode_2d()**  
  Returns the current 2D mode status.  

---

### Key Notes  
- This node defines the initial position for particles in shaders.  
- The `mode_2d` property controls spatial projection (2D vs 3D).  
- Inherited classes implement specific emitter shapes (box, mesh, ring, sphere).