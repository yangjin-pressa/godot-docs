# StaticBody3D

**Inherits:** PhysicsBody3D → CollisionObject3D → Node3D → Node → Object  
**Inherited By:** AnimatableBody3D  

---

## Description  
A 3D physics body that cannot be moved by external forces. When moved manually, it does not affect other bodies in its path.  

- **Manual movement** via code, AnimationMixer (with `ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS`), or RemoteTransform3D.  
- **Use cases:** Static objects (floors, walls), moving surfaces (conveyor belts, rotating platforms).  

---

## Tutorials  
- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)  
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)  
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)  

---

## Properties  

- **constant_angular_velocity**  
  - Type: Vector3  
  - Default: Vector3(0, 0, 0)  
  - Effect: Influences touching bodies as if the body were rotating.  

- **constant_linear_velocity**  
  - Type: Vector3  
  - Default: Vector3(0, 0, 0)  
  - Effect: Influences touching bodies as if the body were moving.  

- **physics_material_override**  
  - Type: PhysicsMaterial  
  - Overrides material for collision physics.  

---

## Property Methods  

- **set_constant_angular_velocity(value: Vector3)**  
- **get_constant_angular_velocity()**  

- **set_constant_linear_velocity(value: Vector3)**  
- **get_constant_linear_velocity()**  

- **set_physics_material_override(value: PhysicsMaterial)**  
- **get_physics_material_override()**  

---

## Key Features  
- **Teleportation:** Moves to new position without affecting other physics bodies.  
- **Override Material:** Assigns custom physics material for collision behavior.  
- **Static vs. Animatable:** Use `AnimatableBody3D` for bodies that require movement simulation.