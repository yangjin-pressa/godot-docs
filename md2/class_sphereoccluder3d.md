# SphereOccluder3D

## Inheritance
- **Occluder3D** < **Resource** < **RefCounted** < **Object**

## Description
A spherical shape used for occlusion culling in 3D scenes. This class defines a sphere that can be utilized by the engine's occlusion culling system.

## Tutorials
- [Occlusion culling](../tutorials/3d/occlusion_culling)

## Properties
- **Radius**: float = 1.0

## Property Descriptions
### radius
- **Type**: float
- **Default**: 1.0
- **Description**: The sphere's radius in 3D units.

## Methods
- **set_radius(value: float)**: void
- **get_radius()**: float

### Notes
- `set_radius` and `get_radius` are virtual methods that can be overridden for custom behavior.
- The `radius` property is a constant value that does not alter the instance's state.