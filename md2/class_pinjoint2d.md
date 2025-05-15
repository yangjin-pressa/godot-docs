# PinJoint2D

**Inherits:** Joint2D < Node2D < CanvasItem < Node < Object

A physics joint that connects two 2D physics bodies at a single point, allowing free rotation. Useful for creating pendulums or seesaws.

## Description
A joint that attaches two 2D physics bodies at a single point, allowing them to rotate freely. Example: a RigidBody2D can be attached to a StaticBody2D to create a pendulum.

## Properties
- angular_limit_enabled: bool = false
- angular_limit_lower: float = 0.0
- angular_limit_upper: float = 0.0
- motor_enabled: bool = false
- motor_target_velocity: float = 0.0
- softness: float = 0.0

## Property Descriptions

**angular_limit_enabled** (bool): Controls if angular limits are applied. When true, angular_limit_lower and angular_limit_upper are enforced.

**angular_limit_lower** (float): Minimum rotation angle. Active only when angular_limit_enabled is true.

**angular_limit_upper** (float): Maximum rotation angle. Active only when angular_limit_enabled is true.

**motor_enabled** (bool): Activates a motor to rotate the joint.

**motor_target_velocity** (float): Target rotational speed in radians per second. Active when motor_enabled is true.

**softness** (float): Flexibility of the joint. Higher values allow more movement.

## Method Definitions
- set_angular_limit_enabled(value: bool): Sets angular limit enabled state.
- is_angular_limit_enabled(): Returns angular limit enabled state.

- set_angular_limit_lower(value: float): Sets minimum rotation angle.
- get_angular_limit_lower(): Returns minimum rotation angle.

- set_angular_limit_upper(value: float): Sets maximum rotation angle.
- get_angular_limit_upper(): Returns maximum rotation angle.

- set_motor_enabled(value: bool): Enables or disables the motor.
- is_motor_enabled(): Returns motor enabled state.

- set_motor_target_velocity(value: float): Sets target rotational speed.
- get_motor_target_velocity(): Returns target rotational speed.

- set_softness(value: float): Sets joint flexibility.
- get_softness(): Returns joint flexibility.