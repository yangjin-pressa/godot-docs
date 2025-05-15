# PhysicsTestMotionResult2D

## Inheritance
- Inherits from: RefCounted < Object

## Description
Describes motion and collision result from PhysicsServer2D.body_test_motion().

## Methods

- **get_collider()** → Object  
  Returns the colliding body's attached Object, if a collision occurred.

- **get_collider_id()** → int  
  Returns the unique instance ID of the colliding body's Object. See Object.get_instance_id().

- **get_collider_rid()** → RID  
  Returns the colliding body's RID used by PhysicsServer2D.

- **get_collider_shape()** → int  
  Returns the colliding body's shape index. See CollisionObject2D.

- **get_collider_velocity()** → Vector2  
  Returns the colliding body's velocity.

- **get_collision_depth()** → float  
  Returns the length of overlap along the collision normal.

- **get_collision_local_shape()** → int  
  Returns the moving object's colliding shape.

- **get_collision_normal()** → Vector2  
  Returns the colliding body's shape's normal at collision point.

- **get_collision_point()** → Vector2  
  Returns the collision point in global coordinates.

- **get_collision_safe_fraction()** → float  
  Returns maximum fraction of motion without collision (0-1).

- **get_collision_unsafe_fraction()** → float  
  Returns minimum fraction of motion needed to collide (0-1).

- **get_remainder()** → Vector2  
  Returns the moving object's remaining movement vector.

- **get_travel()** → Vector2  
  Returns the moving object's travel before collision.