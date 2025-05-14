# CapsuleShape3D

## Inheritance
- **Shape3D**  
  - **Resource**  
    - **RefCounted**  
      - **Object**

## Description
A 3D capsule shape used for physics collision. Typically used to provide a shape for a `CollisionShape3D`.  
**Performance:** Faster than `CylinderShape3D`, slower than `SphereShape3D` and `BoxShape3D`.

## Tutorials
- 3D Physics Tests Demo: [https://godotengine.org/asset-library/asset/2747](https://godotengine.org/asset-library/asset/2747)

## Properties
- **height**: 2.0 (float)  
- **radius**: 0.5 (float)

## Property Descriptions
### height
- **set_height**(value: float)  
- **get_height**()  
  The capsule's height.

### radius
- **set_radius**(value: float)  
- **get_radius**()  
  The capsule's radius.