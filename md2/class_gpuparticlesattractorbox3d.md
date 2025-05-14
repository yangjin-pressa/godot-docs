# GPUParticlesAttractorBox3D

## Inheritance
- **GPUParticlesAttractor3D**  
  - **VisualInstance3D**  
    - **Node3D**  
      - **Node**  
        - **Object**

## Description
A box-shaped attractor that influences particles from `GPUParticles3D` nodes. Can attract particles toward its origin or push them away.  
**Note:** Particle attractors only affect `GPUParticles3D`, not `CPUParticles3D`.

## Properties
- **size**: `Vector3` = `Vector3(2, 2, 2)`  
  The attractor box's size in 3D units.

## Method Definitions
- **set_size**(value: `Vector3`) → `void`  
  Sets the attractor box's size.  
- **get_size**() → `Vector3`  
  Returns the attractor box's size.

## Key Notes
- This method is used to construct a type.  
- This method has no side effects; it doesn't modify member variables.  
- This method is used to construct a type.  

## References
- [GPUParticles3D](class_GPUParticles3D_8class)  
- [CPUParticles3D](class_CPUParticles3D_8class)