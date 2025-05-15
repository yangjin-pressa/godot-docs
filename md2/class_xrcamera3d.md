# XRCamera3D

## Class Hierarchy
- `XRCamera3D` inherits from `Camera3D` → `Node3D` → `Node` → `Object`

## Description
- A helper 3D node for AR/VR cameras.
- In VR-HMD scenarios, most camera properties are ignored by the HMD.
- Only `near` and `far` planes are reliable.
- Position/orientation is automatically updated by the XR Server.
- XRCamera3D location may lag slightly behind rendering data due to thread latency.

## Tutorials
- XR documentation index (see ../tutorials/xr/index)

## Properties
- **physics_interpolation_mode**: `PhysicsInterpolationMode` (value: 2)  
  Overrides `Node`'s physics interpolation mode.