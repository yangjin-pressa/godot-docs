# BoxShape3D

## Class Hierarchy
- **BoxShape3D** inherits from:  
  `Shape3D` → `Resource` → `RefCounted` → `Object`

## Description
A 3D box shape for physics collision, typically used with `CollisionShape3D`.  
**Performance:** Faster than CapsuleShape3D and CylinderShape3D, but slower than SphereShape3D.

## Tutorials
- 3D Physics Tests Demo: https://godotengine.org/asset-library/asset/2747  
- 3D Kinematic Character Demo: https://godotengine.org/asset-library/asset/2739  
- 3D Platformer Demo: https://godotengine.org/asset-library/asset/2748

## Properties
- **size**: `Vector3` (default: `Vector3(1, 1, 1)`)  
  Represents the box's width, height, and depth.

## Method Definitions
- **set_size**(value: `Vector3`) → `void`  
  Sets the box dimensions.  
- **get_size**() → `Vector3`  
  Retrieves the current dimensions.

## Notes
- **virtual**: Methods should typically be overridden by the user.  
- **const**: Methods have no side effects.  
- **vararg**: Methods accept variable arguments.  
- **static**: Methods can be called directly via the class name.