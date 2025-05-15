# VisualShaderNodeParticleEmit

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

A visual shader node that forces emission of a particle from a sub-emitter.

## Description
Calls ``emit_subparticle`` shader method. Emits a particle from the configured sub-emitter, allowing customization. Requires a sub-emitter assigned to the particles node.

## Properties
- **flags**: EmitFlags = 31  
  Flags to override properties from the sub-emitter's process material.

## Enumerations
**EmitFlags**:
- **EMIT_FLAG_POSITION** = 1  
  Particle starts with position from this node.
- **EMIT_FLAG_ROT_SCALE** = 2  
  Particle starts with rotation and scale from this node.
- **EMIT_FLAG_VELOCITY** = 4  
  Particle starts with velocity from this node.
- **EMIT_FLAG_COLOR** = 8  
  Particle starts with color from this node.
- **EMIT_FLAG_CUSTOM** = 16  
  Particle starts with CUSTOM data from this node.

## Methods
- **set_flags** (value: EmitFlags)  
  Sets flags to override sub-emitter properties.
- **get_flags** ()  
  Returns current flags.