# ParticleProcessMaterial Documentation

## Overview
The `ParticleProcessMaterial` class manages properties and behaviors for particles in a simulation. It includes properties for velocity, acceleration, rotation, and other particle-related parameters, as well as methods to configure these properties.

---

## Properties

### `acceleration`
- **Type**: `Vector3`
- **Default**: `Vector3(0, 0, 0)`
- **Description**: Applies a constant acceleration to all particles. This value is used to influence the direction and magnitude of each particle's motion over time.

### `acceleration_curve`
- **Type**: `Texture2D`
- **Default**: `Texture2D()`
- **Description**: A 2D texture that defines a curve for varying acceleration over time. The texture is interpolated to determine the acceleration value for each particle at a specific time in its lifetime.

### `angle`
- **Type**: `float`
- **Default**: `0.0`
- **Description**: The rotation angle of the particle. This value determines how the particle rotates relative to its direction of motion.

### `angular_velocity`
- **Type**: `float`
- **Default**: `0.0`
- **Description**: The rate at which the particle rotates around its axis. This affects how fast the particle spins during its lifetime.

### `angular_velocity_curve`
- **Type**: `Texture2D`
- **Default**: `Texture2D()`
- **Description**: A 2D texture that defines a curve for varying angular velocity over time. The texture is interpolated to determine the angular velocity value for each particle at a specific time in its lifetime.

### `color`
- **Type**: `Color`
- **Default**: `Color(1, 1, 1, 1)`
- **Description**: The color of the particle. This value is used to set the visual appearance of the particle in the simulation.

### `color_curve`
- **Type**: `Texture2D`
- **Default**: `Texture2D()`
- **Description**: A 2D texture that defines a curve for varying color over time. The texture is interpolated to determine the color value for each particle at a specific time in its lifetime.

### `density`
- **Type**: `float`
- **Default**: `1.0`
- **Description**: The density of the particle. This value influences how the particle interacts with other particles or forces in the simulation.

### `density_curve`
- **Type**: `Texture2D`
- **Default**: `Texture2D()`
- **Description**: A 2D texture that defines a curve for varying density over time. The texture is interpolated to determine the density value for each particle at a specific time in its lifetime.

### `emissive`
- **Type**: `Color`
- **Default**: `Color(0, 0, 0, 0)`
- **Description**: The emissive color of the particle. This defines how much light the particle emits, affecting its visual appearance in the simulation.

### `emissive_curve`
- **Type**: `Texture2D`
- **Default**: `Texture2D()`
- **Description**: A 2D texture that defines a curve for varying emissive color over time. The texture is interpolated to determine the emissive color value for each particle at a specific time in its lifetime.

### `velocity_limit_curve`
- **Type**: `Texture2D`
- **Default**: `Texture2D()`
- **Description**: A 2D texture that defines the maximum velocity of a particle during its lifetime. The texture is interpolated to determine the velocity limit for each particle at a specific time in its lifetime.

### `velocity_pivot`
- **Type**: `Vector3`
- **Default**: `Vector3(0, 0, 0)`
- **Description**: A pivot point used to calculate radial and orbital velocity of particles. This value determines the reference point for velocity calculations.

---

## Methods

### `get_param(param: Parameter) -> Vector2`
- **Description**: Returns the minimum and maximum values of the given parameter as a vector. The `x` component corresponds to the minimum value, and the `y` component corresponds to the maximum value.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to retrieve.
- **Returns**: `Vector2` containing the minimum and maximum values.

### `get_param_max(param: Parameter) -> float`
- **Description**: Returns the maximum value range for the given parameter.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to retrieve.
- **Returns**: `float` representing the maximum value.

### `get_param_min(param: Parameter) -> float`
- **Description**: Returns the minimum value range for the given parameter.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to retrieve.
- **Returns**: `float` representing the minimum value.

### `get_param_texture(param: Parameter) -> Texture2D`
- **Description**: Returns the `Texture2D` used by the specified parameter.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to retrieve.
- **Returns**: `Texture2D` object associated with the parameter.

### `get_particle_flag(particle_flag: ParticleFlags) -> bool`
- **Description**: Returns `true` if the specified particle flag is enabled. See `ParticleFlags` for valid options.
- **Parameters**:
  - `particle_flag`: `ParticleFlags` enum value indicating the flag to check.
- **Returns**: `bool` indicating whether the flag is set.

### `set_param(param: Parameter, value: Vector2)`
- **Description**: Sets the minimum and maximum values for the specified parameter. The `value` vector contains the new minimum and maximum values.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to set.
  - `value`: `Vector2` containing the new minimum and maximum values.
- **Returns**: `void`

### `set_param_max(param: Parameter, value: float)`
- **Description**: Sets the maximum value for the specified parameter.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to set.
  - `value`: `float` representing the new maximum value.
- **Returns**: `void`

### `set_param_min(param: Parameter, value: float)`
- **Description**: Sets the minimum value for the specified parameter.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to set.
  - `value`: `float` representing the new minimum value.
- **Returns**: `void`

### `set_param_texture(param: Parameter, value: Texture2D)`
- **Description**: Sets the `Texture2D` used by the specified parameter.
- **Parameters**:
  - `param`: `Parameter` enum value indicating which parameter to set.
  - `value`: `Texture2D` object to be associated with the parameter.
- **Returns**: `void`

### `set_particle_flag(particle_flag: ParticleFlags, value: bool)`
- **Description**: Sets the specified particle flag to the given value.
- **Parameters**:
  - `particle_flag`: `ParticleFlags` enum value indicating the flag to set.
  - `value`: `bool` indicating whether to enable or disable the flag.
- **Returns**: `void`

---

## Notes

- **Virtual Methods**: Some methods in this class may need to be overridden in derived classes to customize behavior.
- **Const Methods**: Methods like `get_param` and `get_param_max` are const and do not modify the object's state.
- **Parameter Enum**: The `Parameter` enum defines which properties (e.g., acceleration, color) are being accessed or modified.
- **ParticleFlags Enum**: This enum defines flags that control various behaviors of particles, such as whether they are affected by gravity or friction.