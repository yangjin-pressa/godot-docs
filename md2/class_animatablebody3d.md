# AnimatableBody3D

**Inherits:** StaticBody3D < PhysicsBody3D < CollisionObject3D < Node3D < Node < Object

A 3D physics body that cannot be moved by external forces. When moved manually, it affects other bodies in its path.

## Description
- Cannot be moved by external forces or contacts
- Can be moved manually via:
  - Code
  - AnimationMixer (with AnimationMixer.callback_mode_process set to AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS)
  - RemoteTransform3D
- When moved, linear/angular velocity is estimated to affect other physics bodies
- Useful for moving platforms, doors, and other dynamic objects

## Tutorials
- 3D Physics Tests Demo: https://godotengine.org/asset-library/asset/2747
- Third Person Shooter (TPS) Demo: https://godotengine.org/asset-library/asset/2710
- 3D Voxel Demo: https://godotengine.org/asset-library/asset/2755

## Properties
- sync_to_physics: true (bool)

## Property Descriptions
sync_to_physics = true
- Controls synchronization with physics frame
- Useful for animation via AnimationPlayer
- Do not use with PhysicsBody3D.move_and_collide()

## Method Definitions
- void set_sync_to_physics(value: bool)
- bool is_sync_to_physics_enabled()

Note: This method should typically be overridden by the user to have any effect.