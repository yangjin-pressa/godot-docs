# VisualShaderNodeParticleConeVelocity

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

A visual shader node that makes particles move in a cone shape.

## Description
- Used in "start" step of particle shader
- Defines initial velocity of particles
- Particles move in cone shape starting from center
- Spread is defined as a parameter

## Key Functionality
- Controls direction and spread of particle movement
- Applied during particle initialization
- Creates radial motion effect from emission point

## Inheritance Hierarchy
VisualShaderNode
├── Resource
│   ├── RefCounted
│   └── Object
└── VisualShaderNodeParticleConeVelocity

## Usage
- Defines velocity vector direction and angle spread
- Influences particle movement trajectory
- Works with particle emitter systems in shader graph

## Attributes
- Cone angle (spread)
- Origin point
- Velocity direction axis
- Particle emission parameters

Note: This node is specifically designed for particle system initialization in shader code.