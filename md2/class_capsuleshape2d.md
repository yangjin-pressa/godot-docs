# CapsuleShape2D

**Inherits:** Shape2D → Resource → RefCounted → Object

A 2D capsule shape used for physics collision. Typically used with CollisionShape2D.

**Performance:** Slower than RectangleShape2D and CircleShape2D.

## Properties
- **height**: 30.0 (float)
- **radius**: 10.0 (float)

## Property Descriptions
- **height** (float): Capsule's height.
  - Set: set_height(value: float)
  - Get: get_height()

- **radius** (float): Capsule's radius.
  - Set: set_radius(value: float)
  - Get: get_radius()

## Notes
- This shape is efficient for collision detection but slower than rectangle and circle shapes.