# RayCast2D Class Documentation

## Overview
The `RayCast2D` class in Godot is used to cast a ray in 2D space and detect collisions with other physics bodies. It provides properties and methods to control the ray's behavior, query collision information, and manage exceptions.

---

## Properties

### `enabled` (bool)
Determines whether the ray is active and processing collisions. If `false`, the ray will not detect collisions.

### `collide_with_bodies` (bool)
Enables collision detection with `PhysicsBody2D` nodes.

### `collide_with_areas` (bool)
Enables collision detection with `Area2D` nodes.

### `collide_with_tight` (bool)
If `true`, the ray will only detect collisions with the tightest possible shape (e.g., a polygon) rather than the entire area of the object.

### `hit_from_inside` (bool)
If `true`, the ray will consider collisions that occur at the origin of the ray (i.e., when the ray starts inside a shape).

### `target` (Object)
The object that the ray is cast from. This is typically a `Node2D` or a `KinematicBody2D`.

### `collision_mask` (uint)
A bitmask representing the layers that the ray will collide with. Layers are numbered from 1 to 32.

---

## Methods

### `add_exception(node: CollisionObject2D) -> void`
Adds a collision exception so the ray does not report collisions with the specified `CollisionObject2D` node.

### `add_exception_rid(rid: RID) -> void`
Adds a collision exception so the ray does not report collisions with the specified `RID`.

### `clear_exceptions() -> void`
Removes all collision exceptions for this ray.

### `force_raycast_update() -> void`
Updates the collision information for the ray immediately, without waiting for the next `_physics_process` call. Use this to manually refresh the ray's state.

### `get_collider() -> Object`
Returns the first object that the ray intersects, or `null` if no collision is detected.

### `get_collider_rid() -> RID`
Returns the `RID` of the first object that the ray intersects, or an empty `RID` if no collision is detected.

### `get_collider_shape() -> int`
Returns the shape ID of the first object that the ray intersects, or `0` if no collision is detected.

### `get_collision_mask_value(layer_number: int) -> bool`
Returns whether the specified layer in the `collision_mask` is enabled.

### `get_collision_normal() -> Vector2`
Returns the normal of the intersecting object's shape at the collision point, or `Vector2(0, 0)` if the ray starts inside a shape and `hit_from_inside` is `true`.

### `get_collision_point() -> Vector2`
Returns the collision point at which the ray intersects the closest object, in the global coordinate system.

### `is_colliding() -> bool`
Returns whether any object is intersecting with the ray's vector.

### `remove_exception(node: CollisionObject2D) -> void`
Removes a collision exception so the ray reports collisions with the specified `CollisionObject2D` node.

### `remove_exception_rid(rid: RID) -> void`
Removes a collision exception so the ray reports collisions with the specified `RID`.

### `set_collision_mask_value(layer_number: int, value: bool) -> void`
Enables or disables the specified layer in the `collision_mask`.

---

## Notes and Examples

### Collision Mask Example
```gdscript
# Enable layer 1 in the collision mask
set_collision_mask_value(1, true)

# Check if layer 2 is enabled
var is_enabled = get_collision_mask_value(2)
```

### Getting Shape Information
```gdscript
var target = get_collider() # A CollisionObject2D
var shape_id = get_collider_shape() # Shape index in the collider
var owner_id = target.shape_find_owner(shape_id) # Owner ID in the collider
var shape = target.shape_owner_get_owner(owner_id) # The actual shape
```

### Important Notes
- Use `is_colliding()` before accessing `get_collision_normal()` or `get_collision_point()` to ensure valid results.
- `enabled` does not need to be `true` for `force_raycast_update()` to work.
- `hit_from_inside` affects the behavior of `get_collision_normal()` and `get_collision_point()`.

---

## Summary
The `RayCast2D` class provides a powerful way to detect and interact with 2D physics bodies in Godot. By configuring properties like `collision_mask` and `hit_from_inside`, and using methods like `force_raycast_update()`, you can precisely control how rays interact with the game world. Always check `is_colliding()` before accessing collision-related properties to avoid invalid data.