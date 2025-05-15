# VisualShaderNodeParticleAccelerator

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

A visual shader node that accelerates particles.

## Description
Particle accelerator can be used in "process" step of particle shader. It will accelerate the particles. Connect it to the Velocity output port.

## Properties
- Mode: mode = 0 (🔗enum_VisualShaderNodeParticleAccelerator_Mode)

## Enumerations
enum Mode: enum_VisualShaderNodeParticleAccelerator_Mode

- MODE_LINEAR = 0: The particles will be accelerated based on their velocity.
- MODE_RADIAL = 1: The particles will be accelerated towards or away from the center.
- MODE_TANGENTIAL = 2: The particles will be accelerated tangentially to the radius vector from center to their position.
- MODE_MAX = 3: Represents the size of the Mode enum.

## Property Descriptions
- mode: Mode = 0 (🔗enum_VisualShaderNodeParticleAccelerator_Mode)
  - set_mode(value: Mode): void
  - get_mode(): Mode

  Defines in what manner the particles will be accelerated.