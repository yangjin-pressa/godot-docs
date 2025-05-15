# PhysicsDirectBodyState2D Documentation

## Overview
The `PhysicsDirectBodyState2D` class manages the state of a 2D rigid body in a physics simulation. It provides access to properties such as position, velocity, rotation, and contact information with other bodies. This class is typically used in conjunction with a physics space to query and update the state of a body during simulation.

---

## Properties

### `body_state`
- **Type**: `Ref<PhysicsDirectBodyState2D>`
- **Description**: A reference to the body's current state in the physics space.

### `contact_count`
- **Type**: `int`
- **Description**: The number of contacts this body has with other bodies. This is only non-zero if the physics engine is configured to monitor contacts.

### `contacts`
- **Type**: `Array< PhysicsDirectBodyContact >`
- **Description**: An array containing information about each contact with other bodies.

### `space_state`
- **Type**: `Ref<PhysicsDirectSpaceState2D>`
- **Description**: The current state of the physics space, useful for queries and spatial operations.

---

## Methods

### `get_space_state()`
- **Return Type**: `Ref<PhysicsDirectSpaceState2D>`
- **Description**: Returns the current state of the physics space, useful for spatial queries and debugging.

### `get_contact_count()`
- **Return Type**: `int`
- **Description**: Returns the number of contacts this body has with other bodies. Note that this is only non-zero if contact monitoring is enabled.
- **Note**: See `RigidBody2D.contact_monitor` for configuration details.

### `get_contact_collider(contact_idx)`
- **Return Type**: `RID`
- **Description**: Returns the collider's RID (Resource Identifier) for the specified contact index.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_collider_id(contact_idx)`
- **Return Type**: `int`
- **Description**: Returns the object ID of the collider for the specified contact index.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_collider_object(contact_idx)`
- **Return Type**: `Object`
- **Description**: Returns the collider object for the specified contact index. This depends on how the collider was created (e.g., scene node if used).
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_collider_position(contact_idx)`
- **Return Type**: `Vector2`
- **Description**: Returns the position of the contact point on the collider in the global coordinate system.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_collider_shape(contact_idx)`
- **Return Type**: `int`
- **Description**: Returns the shape index of the collider for the specified contact index.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_collider_velocity_at_position(contact_idx)`
- **Return Type**: `Vector2`
- **Description**: Returns the velocity vector at the contact point on the collider.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_impulse(contact_idx)`
- **Return Type**: `Vector2`
- **Description**: Returns the impulse created by the contact for the specified contact index.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_local_normal(contact_idx)`
- **Return Type**: `Vector2`
- **Description**: Returns the local normal vector at the contact point on the body.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_local_position(contact_idx)`
- **Return Type**: `Vector2`
- **Description**: Returns the position of the contact point on the body in the global coordinate system.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_local_shape(contact_idx)`
- **Return Type**: `int`
- **Description**: Returns the local shape index of the collision for the specified contact index.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_contact_local_velocity_at_position(contact_idx)`
- **Return Type**: `Vector2`
- **Description**: Returns the velocity vector at the contact point on the body.
- **Parameters**:
  - `contact_idx`: Index of the contact in the contacts array.

### `get_velocity_at_local_position(local_position)`
- **Return Type**: `Vector2`
- **Description**: Returns the body's velocity at the given relative position, including both translation and rotation.
- **Parameters**:
  - `local_position`: The position relative to the body's origin.

### `integrate_forces()`
- **Return Type**: `void`
- **Description**: Updates the body's linear and angular velocity by applying gravity and damping for one physics tick.
- **Note**: This method is essential for simulating forces and updating the body's state over time.

### `set_constant_force(force)`
- **Return Type**: `void`
- **Description**: Sets the body's total constant positional forces applied during each physics update.
- **Parameters**:
  - `force`: A `Vector2` representing the constant force.

### `set_constant_torque(torque)`
- **Return Type**: `void`
- **Description**: Sets the body's total constant rotational forces applied during each physics update.
- **Parameters**:
  - `torque`: A `float` representing the constant torque.

---

## Key Concepts

- **Contacts**: Each contact in the `contacts` array contains information about the interaction between this body and another. This includes impulse, velocity, and position data.
- **Local vs. Global Coordinates**: Methods like `get_contact_local_position()` and `get_contact_collider_position()` distinguish between local (relative to the body) and global (absolute) coordinate systems.
- **Contact Monitoring**: The `contact_count` property only reflects contacts if the physics engine is configured to monitor them (via `RigidBody2D.contact_monitor`).

---

## Usage Example

```gdscript
# Example: Get the velocity at a local position
var local_pos = Vector2(0, 0)  # Position relative to body origin
var velocity = physics_body.get_velocity_at_local_position(local_pos)
```

```gdscript
# Example: Access contact information
for contact_idx in 0..physics_body.contact_count - 1:
    var impulse = physics_body.get_contact_impulse(contact_idx)
    var local_normal = physics_body.get_contact_local_normal(contact_idx)
```

```gdscript
# Example: Update forces
var force = Vector2(10, 0)
var torque = 5.0
physics_body.set_constant_force(force)
physics_body.set_constant_torque(torque)
```

---

## Notes

- This class is designed for advanced users who need direct access to physics state and simulation details.
- Always ensure that the physics engine is running in a loop to update the body's state via `integrate_forces()`.
- Contact information is crucial for collision resolution and response in physics simulations.