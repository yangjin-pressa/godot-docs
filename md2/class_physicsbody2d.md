# PhysicsBody2D

**Inherits:** CollisionObject2D → Node2D → CanvasItem → Node → Object  
**Inherited By:** CharacterBody2D, RigidBody2D, StaticBody2D  

Abstract base class for 2D physics objects.

---

## Description
PhysicsBody2D is an abstract base class for 2D game objects affected by physics. All 2D physics bodies inherit from it.

---

## Tutorials
- [Physics introduction](../tutorials/physics/physics_introduction)

---

## Properties
- **input_pickable**: false (overrides CollisionObject2D property)

---

## Methods
- **add_collision_exception_with(body: Node)**: Adds a body to the list of bodies that this body can't collide with.
- **get_collision_exceptions()**: Returns an array of nodes that were added as collision exceptions for this body.
- **get_gravity()**: Returns the gravity vector computed from all sources affecting the body.
- **move_and_collide(motion: Vector2, test_only: bool = false, safe_margin: float = 0.08, recovery_as_collision: bool = false)**: Moves the body along the vector motion. Returns collision info if collision occurs.
- **remove_collision_exception_with(body: Node)**: Removes a body from the collision exception list.
- **test_move(from: Transform2D, motion: Vector2, collision: KinematicCollision2D = null, safe_margin: float = 0.08, recovery_as_collision: bool = false)**: Checks for collisions without moving the body. Returns true if collision would stop movement.

---

## Key Notes
- `move_and_collide` and `test_move` handle collision detection with parameters for motion and safety margins.
- Collision exceptions allow specifying bodies that this body should not collide with.
- Gravity is calculated from global settings and area2D overrides.