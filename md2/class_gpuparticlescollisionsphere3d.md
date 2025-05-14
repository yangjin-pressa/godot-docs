# GPUParticlesCollisionSphere3D

## Inheritance
- GPUParticlesCollision3D  
- VisualInstance3D  
- Node3D  
- Node  
- Object  

## Description
A sphere-shaped 3D particle collision shape affecting GPUParticles3D nodes.

Particle collision shapes work in real-time and can be moved, rotated, and scaled during gameplay. Unlike attractors, non-uniform scaling of collision shapes is *not* supported.

**Note**: [ParticleProcessMaterial.collision_mode](#) must be [ParticleProcessMaterial.COLLISION_RIGID](#) or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT](#) on the GPUParticles3D's process material for collision to work.

**Note**: Particle collision only affects GPUParticles3D, not CPUParticles3D.

## Properties
- **radius**: float = 1.0  

## Property Descriptions
**radius**: float = 1.0  
- **set_radius** (value: float)  
- **get_radius** ()

The collision sphere's radius in 3D units.

## Method Notes
- **set_radius** is virtual (overrides user-defined behavior).  
- **get_radius** is const (no side effects, does not modify instance variables).