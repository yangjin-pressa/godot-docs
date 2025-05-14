**Class Name**: GPUParticlesAttractor3D  
**Inherits**: `VisualInstance3D` → `Node3D` → `Node` → `Object`  
**Inherited By**:  
- GPUParticlesAttractorBox3D  
- GPUParticlesAttractorSphere3D  
- GPUParticlesAttractorVectorField3D  

**Description**  
- Abstract base class for 3D particle attractors.  
- Attractors can pull particles toward the origin or push them away.  
- Works in real-time; can be moved, rotated, scaled during gameplay.  
- Non-uniform scaling is supported.  
- Can be disabled by hiding or setting `strength` to `0.0`.  
- **Note**: Only affects `GPUParticles3D`, not `CPUParticles3D`.  

**Properties**  
- **attenuation**: `float` (default: `1.0`)  
- **cull_mask**: `int` (default: `4294967295`)  
- **directionality**: `float` (default: `0.0`)  
- **strength**: `float` (default: `1.0`)  

**Property Descriptions**  
- **attenuation**:  
  - Controls how gradual particles are pushed toward the attractor.  
  - Higher values = slower push near the origin.  
  - Zero or negative values = fast push when particles touch the attractor.  

- **cull_mask**:  
  - Specifies rendering layers affected by the attractor.  
  - Default: all layers.  
  - Can be adjusted to exclude specific particles.  
  - Note: Attractor interaction can be disabled on a per-material basis.  

- **directionality**:  
  - Determines the directionality of the attractor.  
  - `0.0`: uniform pull toward the center.  
  - `1.0`: fully directional (push toward local -Z or +Z).  
  - Rotating the node changes the direction when directionality > 0.  

- **strength**:  
  - Adjusts the attractor's force.  
  - Negative value = push particles away from the origin.  
  - Direction depends on `directionality` and `strength` sign.  

**Notes**  
- Attractors affect only `GPUParticles3D`.  
- Non-uniform scaling is supported.  
- Disable via `hide()` or `strength = 0.0`.