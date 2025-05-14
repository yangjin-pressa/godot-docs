# GPUParticlesAttractorVectorField3D

**Inherits:** GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object

A box-shaped attractor that uses a 3D texture to influence particles from GPUParticles3D nodes. Unlike GPUParticlesAttractorBox3D, this uses a texture to define direction and strength variations.

## Description

- **Functionality:** Influences particles in GPUParticles3D nodes based on a 3D texture.
- **Use Case:** Create complex attraction patterns like sandstorms.
- **Note:** Only affects GPUParticles3D, not CPUParticles3D.

## Properties

- **size:** Vector3(2, 2, 2) - Size of the vector field box in 3D units.
- **texture:** Texture3D - 3D texture for defining direction/force. Values are linearly interpolated between pixels.

## Method Descriptions

### size
- **set_size(value:** Vector3) - Sets the size of the vector field box.
- **get_size()** - Retrieves the current size.

### texture
- **set_texture(value:** Texture3D) - Sets the 3D texture.
- **get_texture()** - Retrieves the current texture.

## Notes

- Texture resolution should match the attractor's size for optimal performance. Low-resolution textures (e.g., 64×64×64) are acceptable for low-frequency data.
- Non-uniform scaling of attractors is supported during gameplay.