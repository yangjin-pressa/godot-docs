# VehicleWheel Class Documentation

## Overview

The `VehicleWheel` class is used to represent a wheel in a 3D vehicle physics simulation within Godot. It provides properties for configuring wheel behavior, physics parameters, and methods to retrieve contact information with the environment. This class is typically used in conjunction with a `VehicleBody3D` to simulate real-world vehicle dynamics.

---

## Properties

### `wheel_radius` (float)
- **Default**: `0.5`
- **Description**: The radius of the wheel in meters.
- **Note**: This defines the physical size of the wheel in the scene.

---

### `wheel_rest_length` (float)
- **Default**: `0.15`
- **Description**: The distance the wheel is lowered from its origin point. This determines the position of the wheel when the car is in rest.
- **Note**: Adjust the origin point of the wheel in the scene first, then use this value to set the resting position.

---

### `wheel_friction_slip` (float)
- **Default**: `10.5`
- **Description**: Determines the grip of the wheel. A value of 1.0 represents normal grip, while 0.0 means no grip.
- **Note**: Adjust this for drift cars or tire wear simulations. Start with 1.0 for normal use.

---

### `wheel_roll_influence` (float)
- **Default**: `0.1`
- **Description**: Influences how the vehicle resists body roll. A value of 1.0 resists body roll, while 0.0 makes the vehicle prone to rolling over.
- **Note**: Set this to 1.0 for all wheels for a rigid vehicle behavior.

---

### `use_as_steering` (bool)
- **Default**: `false`
- **Description**: If `true`, this wheel is used for steering. This is used in conjunction with `VehicleBody3D.steering`.
- **Note**: Use this with per-wheel steering if you're not using the `VehicleBody3D` steering property.

---

### `use_as_traction` (bool)
- **Default**: `false`
- **Description**: If `true`, this wheel transfers engine force to the ground for propulsion. This is used in conjunction with `VehicleBody3D.engine_force`.
- **Note**: Use this with per-wheel engine force if you're not using the `VehicleBody3D` engine force property.

---

### `engine_force` (float)
- **Default**: `0.0`
- **Description**: The force applied to the wheel for propulsion. Positive values push the vehicle forward, negative values push it backward.
- **Note**: This property is overridden if `use_as_traction` is set to `true`.

---

### `brake_force` (float)
- **Default**: `0.0`
- **Description**: The braking force applied to the wheel. Positive values decelerate the vehicle.
- **Note**: This is used in conjunction with `VehicleBody3D.brake_force`.

---

### `steering` (float)
- **Default**: `0.0`
- **Description**: The angle of the wheel in radians. Positive values steer the vehicle to the right, negative to the left.
- **Note**: This is used in conjunction with `VehicleBody3D.steering`.

---

## Methods

### `get_contact_body()` → `Node3D` (const)
- **Description**: Returns the body node that the wheel is currently in contact with. If not in contact, returns `null`.
- **Note**: Supports `PhysicsBody3D` types, not `GridMap`.

### `get_contact_normal()` → `Vector3` (const)
- **Description**: Returns the normal vector of the suspension's collision in world space. If not in contact, returns a vector pointing along the suspension axis.
- **Note**: This helps determine the direction of the collision.

### `get_contact_point()` → `Vector3` (const)
- **Description**: Returns the point of the suspension's collision in world space. If not in contact, returns the maximum point of the wheel's ray cast.
- **Note**: The ray cast distance is defined by `wheel_rest_length + wheel_radius`.

### `get_rpm()` → `float` (const)
- **Description**: Returns the rotational speed of the wheel in revolutions per minute (RPM).
- **Note**: Useful for tracking engine performance or wheel speed.

### `get_skidinfo()` → `float` (const)
- **Description**: Returns a value between 0.0 and 1.0 indicating whether the wheel is skidding. 0.0 means skidding (e.g., icy terrain), 1.0 means no skidding (e.g., dry asphalt).
- **Note**: Helps detect tire slippage or loss of traction.

### `is_in_contact()` → `bool` (const)
- **Description**: Returns `true` if the wheel is currently in contact with a surface.
- **Note**: Used to determine if the wheel is on the ground or in the air.

---

## Notes

- **Physics Setup**: Ensure the wheel's origin point is correctly positioned in the scene before adjusting `wheel_rest_length`.
- **Traction and Steering**: Use `use_as_traction` and `use_as_steering` to control whether a wheel contributes to propulsion or steering.
- **Friction**: Adjust `wheel_friction_slip` to simulate different tire grip levels for realism or gameplay mechanics.
- **Roll Behavior**: Modify `wheel_roll_influence` to control how the vehicle responds to body roll during turns.

---

## Example Use Case

```gdscript
# Example: Configure a wheel for steering and traction
var wheel = VehicleWheel.new()
wheel.use_as_steering = true
wheel.use_as_traction = true
wheel.steering = 0.5  # Steer to the right
wheel.engine_force = 100.0  # Apply forward force
```

This class is essential for creating realistic vehicle physics in 3D games, allowing developers to simulate complex interactions between wheels, terrain, and vehicle dynamics.