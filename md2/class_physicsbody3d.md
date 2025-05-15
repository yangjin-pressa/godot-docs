# PhysicsBody3D Class Documentation

## Overview
The `PhysicsBody3D` class serves as an abstract base class for 3D game objects affected by physics in Godot. It provides essential methods and properties for handling collisions, gravity, and axislocking, enabling complex physics interactions in 3D environments.

---

## Key Features
- **Axis Locking**: Control linear and rotational movement along individual axes.
- **Collision Exceptions**: Define bodies that this object cannot collide with.
- **Gravity Handling**: Combine global gravity with area overrides.
- **Collision Detection**: Test and move objects while detecting collisions.

---

## Properties

### Axis Locking
These boolean properties control whether motion is restricted along specific axes:

```gdscript
var x_linear_locked: bool  # Locks linear movement along X axis
var y_linear_locked: bool  # Locks linear movement along Y axis
var z_linear_locked: bool  # Locks linear movement along Z axis
var x_rotational_locked: bool  # Locks rotational movement around X axis
var y_rotational_locked: bool  # Locks rotational movement around Y axis
var z_rotational_locked: bool  # Locks rotational movement around Z axis
```

**Usage:** Use `set_axis_lock()` to enable/disable locking for any axis.

---

## Methods

### `add_collision_exception_with(body: Node)`
Adds a body to the list of entities this physics body cannot collide with.

**Parameters:**
- `body`: The `Node` object to be added as a collision exception.

### `get_collision_exceptions() -> Array[PhysicsBody3D]`
Returns an array of nodes that are collision exceptions for this body.

### `get_gravity() -> Vector3`
Returns the gravity vector affecting this body, combining global gravity and area3D overrides.

### `move_and_collide(motion: Vector3, test_only: bool = false, safe_margin: float = 0.001, recovery_as_collision: bool = false, max_collisions: int = 1) -> KinematicCollision3D`
Moves the body along the `motion` vector, detecting collisions. Returns collision details if a collision occurs.

**Parameters:**
- `motion`: The direction and magnitude of movement.
- `test_only`: If `true`, the body doesn't move but collision data is returned.
- `safe_margin`: Margin for collision recovery (e.g., for floor snapping).
- `recovery_as_collision`: If `true`, depenetration from recovery is reported as collision.
- `max_collisions`: Maximum number of collisions to report.

### `test_move(from: Transform3D, motion: Vector3, collision: KinematicCollision3D = null, safe_margin: float = 0.001, recovery_as_collision: bool = false, max_collisions: int = 1) -> bool`
Checks for collisions without moving the body. Returns `true` if movement would be blocked.

**Parameters:**
- `from`: The transformed position, scale, and rotation to test.
- `motion`: Movement vector.
- `collision`: Optional output for collision details.
- `safe_margin`: Collision recovery margin.
- `recovery_as_collision`: Whether recovery phase collisions are reported.
- `max_collisions`: Maximum collisions to check.

---

## Important Notes

### Non-Uniform Scale
Avoid using non-uniform scaling with physics bodies, as it can cause unexpected behavior in collision detection and physics simulations.

### Gravity Overrides
The `get_gravity()` method aggregates:
- Global world gravity.
- Gravity overrides from `Area3D` nodes.
- Custom gravity settings in the physics body.

### Axis Locking
Use `set_axis_lock(axis: BodyAxis, lock: bool)` to lock/unlock movement or rotation along specific axes. For example:
```gdscript
self.set_axis_lock(BodyAxis.X_LINEAR, true)
```

### Collision Testing
The `test_move()` method is useful for determining if a movement would collide with other objects without altering the physics body's position. This is critical for frame-rate independent checks in `Node._physics_process()`.

---

## Best Practices
1. **Use `delta` for Motion:** When using `move_and_collide()` or `test_move()`, calculate `motion` using `delta` for consistent behavior across different frame rates.
2. **Collision Exceptions:** Use `add_collision_exception_with()` to prevent unintended collisions between specific objects (e.g., a player and a static environment).
3. **Safe Margin:** Adjust `safe_margin` in `move_and_collide()` for better collision recovery, especially in character controllers.

---

This class forms the foundation for creating interactive 3D physics entities in Godot, enabling complex behaviors through precise control over movement, collisions, and gravity.