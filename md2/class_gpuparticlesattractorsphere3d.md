# GPUParticlesAttractorSphere3D

**Inherits:** GPUParticlesAttractor3D < VisualInstance3D < Node3D < Node < Object

## Description
A spheroid-shaped attractor that influences particles from GPUParticles3D nodes. Can attract or repel particles toward/from its origin. Supports real-time movement, rotation, scaling, and non-uniform scaling.

**Note:** Only affects GPUParticles3D, not CPUParticles3D.

## Properties
- **radius** (float): 1.0

## Property Descriptions
**radius** (float): Radius of the attractor sphere in 3D units.

**Note:** Ellipsoidal shapes can be created via non-uniform scaling.

## Methods
- `set_radius(value: float)` – Sets the radius.
- `get_radius()` – Retrieves the radius.

## Notes
- Particle attractors only affect GPUParticles3D nodes.