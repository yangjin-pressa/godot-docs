# StaticBody2D

**Inherits:** PhysicsBody2D < CollisionObject2D < Node2D < CanvasItem < Node < Object  
**Inherited By:** AnimatableBody2D

## Description
A 2D physics body that cannot be moved by external forces. Manual movement does not affect other bodies. Useful for static objects like floors, walls, and moving surfaces (e.g., conveyor belts).

## Properties
- **constant_angular_velocity** (float) = 0.0  
  Rotational speed affecting touching bodies.  
  Methods: set_constant_angular_velocity(), get_constant_angular_velocity()

- **constant_linear_velocity** (Vector2) = Vector2(0, 0)  
  Linear movement affecting touching bodies.  
  Methods: set_constant_linear_velocity(), get_constant_linear_velocity()

- **physics_material_override** (PhysicsMaterial)  
  Overrides physics material for the body.  
  Methods: set_physics_material_override(), get_physics_material_override()

## Key Features
- Manual movement teleports the body without interacting with other physics bodies.
- Use with AnimationMixer or RemoteTransform2D for dynamic surfaces.
- Physics material override takes precedence over inherited materials.