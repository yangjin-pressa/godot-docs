# CylinderShape3D

**Inherits:** Shape3D → Resource → RefCounted → Object

A 3D cylinder shape used for physics collision.

## Description
A 3D cylinder shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

Note: There are several known bugs with cylinder collision shapes. Using CapsuleShape3D or BoxShape3D instead is recommended.

Performance: CylinderShape3D is fast to check collisions against, but it is slower than CapsuleShape3D, BoxShape3D, and SphereShape3D.

## Tutorials
- Third Person Shooter (TPS) Demo: https://godotengine.org/asset-library/asset/2710
- 3D Physics Tests Demo: https://godotengine.org/asset-library/asset/2747
- 3D Voxel Demo: https://godotengine.org/asset-library/asset/2755

## Properties
- height: float = 2.0
- radius: float = 0.5

## Property Descriptions

### height
- Type: float
- Default: 2.0
- Description: The cylinder's height.
- Methods:
  - set_height(value: float)
  - get_height()

### radius
- Type: float
- Default: 0.5
- Description: The cylinder's radius.
- Methods:
  - set_radius(value: float)
  - get_radius()