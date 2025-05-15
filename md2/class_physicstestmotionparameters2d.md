# PhysicsTestMotionParameters2D

**Inherits:** RefCounted < Object

## Description

Configures parameters for PhysicsServer2D.body_test_motion(). Modifying properties like motion allows customization of collision testing behavior.

## Properties

- **collide_separation_ray**: bool = false  
  - set_collide_separation_ray_enabled(value: bool)  
  - is_collide_separation_ray_enabled()  
  - If true, separation ray shapes detect collisions and can stop motion. Useful for ground snapping.

- **exclude_bodies**: Array[RID] = []  
  - set_exclude_bodies(value: Array[RID])  
  - get_exclude_bodies()  
  - Excludes specified bodies from collision. Use CollisionObject2D.get_rid() to get RIDs.

- **exclude_objects**: Array[int] = []  
  - set_exclude_objects(value: Array[int])  
  - get_exclude_objects()  
  - Excludes objects by unique instance ID. Use Object.get_instance_id().

- **from**: Transform2D = Transform2D(1, 0, 0, 1, 0, 0)  
  - set_from(value: Transform2D)  
  - get_from()  
  - Starting transform in global space. Typically set to Node2D.global_transform.

- **margin**: float = 0.0  
  - set_margin(value: float)  
  - get_margin()  
  - Collision margin for shape movement. Defaults to 0.0.

- **motion**: Vector2 = Vector2(0, 0)  
  - set_motion(value: Vector2)  
  - get_motion()  
  - Direction and magnitude of motion for collision testing.

- **shape**: Shape2D = null  
  - set_shape(value: Shape2D)  
  - get_shape()  
  - Shape used for collision detection. Null means no shape.

- **speed**: float = 0.0  
  - set_speed(value: float)  
  - get_speed()  
  - Speed for motion simulation. Defaults to 0.0.

## Key Methods

- **_validate(): void**  
  - Validates physics parameters before testing. Ensures shape and motion are properly initialized.

- **_get_collision_margin(): float**  
  - Returns current collision margin. Used to adjust collision detection accuracy.

- **_get_collision_shape(): Shape2D**  
  - Returns the shape used for collision testing. Returns null if not set.