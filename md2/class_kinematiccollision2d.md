# KinematicCollision2D

**Inherits:** RefCounted < Object

## Description
Holds collision data from the movement of a PhysicsBody2D, typically from PhysicsBody2D.move_and_collide(). When a PhysicsBody2D is moved, it stops if it detects a collision. A KinematicCollision2D object is returned upon collision. The data includes the colliding object, remaining motion, and collision position.

## Methods

- **get_angle**(up_direction: Vector2 = Vector2(0, -1)) → float  
  Returns the collision angle according to up_direction. Default is Vector2.UP. Always positive.

- **get_collider**() → Object  
  Returns the colliding body's attached Object.

- **get_collider_id**() → int  
  Returns the unique instance ID of the colliding body's Object. See Object.get_instance_id().

- **get_collider_rid**() → RID  
  Returns the RID of the colliding body.

- **get_position**() → Vector2  
  Returns the collision point in global coordinates.

- **get_remainder**() → Vector2  
  Returns the moving object's remaining movement vector after collision.

- **get_travel**() → Vector2  
  Returns the moving object's travel distance before collision.

- **get_collider**() → Object  
  Returns the colliding body's attached Object.

- **get_collider**() → Object  
  Returns the colliding body's attached Object.

- **get_collider**() → Object  
  Returns the colliding body's attached Object.