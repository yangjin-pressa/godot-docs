# VisualShaderNodeParticleMeshEmitter

**Inherits:** VisualShaderNodeParticleEmitter < VisualShaderNode < Resource < RefCounted < Object

## Description
A visual shader node that emits particles in a shape defined by a Mesh. Emits from the mesh's surfaces, either all or a specified one.

## Properties

- **mesh**: Mesh (🔗)  
  The Mesh that defines emission shape.  
  Methods: set_mesh(Mesh), get_mesh()

- **surface_index**: int = 0 (🔗)  
  Index of the surface that emits particles. use_all_surfaces must be false for this to take effect.  
  Methods: set_surface_index(int), get_surface_index()

- **use_all_surfaces**: bool = true (🔗)  
  If true, particles emit from all surfaces of the mesh.  
  Methods: set_use_all_surfaces(bool), is_use_all_surfaces()

## Key Functionality
- Particles are emitted based on the assigned mesh's geometry.
- Surface index and all-surfaces flags control emission behavior.