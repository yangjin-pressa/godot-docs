# AnimationMixer Class Documentation

The `AnimationMixer` class in Godot is used to manage and blend animations. It provides methods to handle animation libraries, individual animations, and root motion properties. Below is a detailed documentation of its methods.

---

## **Animation Libraries**

### `add_animation_library(name: StringName, library: AnimationLibrary) -> void`
Adds an `AnimationLibrary` under a specified key.

**Parameters**:
- `name`: The key under which the library is stored.
- `library`: The `AnimationLibrary` to add.

**Note**: This method is virtual and should be overridden by the user to have any effect.

---

### `remove_animation_library(name: StringName) -> void`
Removes the `AnimationLibrary` associated with the given key.

**Parameters**:
- `name`: The key of the library to remove.

---

### `rename_animation_library(old_name: StringName, new_name: StringName) -> void`
Moves the `AnimationLibrary` from one key to another.

**Parameters**:
- `old_name`: The old key of the library.
- `new_name`: The new key for the library.

---

### `has_animation_library(name: StringName) -> bool`
Checks if an `AnimationLibrary` exists under the given key.

**Parameters**:
- `name`: The key to check.

**Return**:
- `true` if the library exists, otherwise `false`.

---

### `get_animation_library(name: StringName) -> AnimationLibrary`
Retrieves the `AnimationLibrary` associated with the given key.

**Parameters**:
- `name`: The key of the library.

**Return**:
- The `AnimationLibrary` if it exists, otherwise `null`.

---

## **Animations**

### `add_animation(name: StringName, animation: Animation) -> void`
Adds an `Animation` under a specified key.

**Parameters**:
- `name`: The key under which the animation is stored.
- `animation`: The `Animation` to add.

**Note**: This method is virtual and should be overridden by the user to have any effect.

---

### `remove_animation(name: StringName) -> void`
Removes the `Animation` associated with the given key.

**Parameters**:
- `name`: The key of the animation to remove.

---

### `has_animation(name: StringName) -> bool`
Checks if an `Animation` exists under the given key.

**Parameters**:
- `name`: The key to check.

**Return**:
- `true` if the animation exists, otherwise `false`.

---

### `get_animation(name: StringName) -> Animation`
Retrieves the `Animation` associated with the given key.

**Parameters**:
- `name`: The key of the animation.

**Return**:
- The `Animation` if it exists, otherwise `null`.

---

## **Root Motion Properties**

### `get_root_motion_position() -> Vector3`
Retrieves the root motion position delta from the root motion track.

**Return**:
- A `Vector3` representing the position delta.

**Note**: Returns `Vector3(0, 0, 0)` if the root motion track is not a 3D rotation track.

---

### `get_root_motion_rotation() -> Quaternion`
Retrieves the root motion rotation delta from the root motion track.

**Return**:
- A `Quaternion` representing the rotation delta.

**Note**: Returns `Quaternion(0, 0, 0, 1)` if the root motion track is not a 3D rotation track.

---

### `get_root_motion_scale() -> Vector3`
Retrieves the root motion scale delta from the root motion track.

**Return**:
- A `Vector3` representing the scale delta.

**Note**: Returns `Vector3(0, 0, 0)` if the root motion track is not a 3D scale track.

---

### `get_root_motion_position_accumulator() -> Vector3`
Retrieves the accumulated root motion position from the root motion track.

**Return**:
- A `Vector3` representing the accumulated position.

**Note**: Useful for tracking changes between frames.

---

### `get_root_motion_rotation_accumulator() -> Quaternion`
Retrieves the accumulated root motion rotation from the root motion track.

**Return**:
- A `Quaternion` representing the accumulated rotation.

**Note**: Necessary for applying root motion position correctly with rotation.

---

### `get_root_motion_scale_accumulator() -> Vector3`
Retrieves the accumulated root motion scale from the root motion track.

**Return**:
- A `Vector3` representing the accumulated scale.

**Note**: Useful for tracking changes between frames.

---

## **Utilities**

### `advance(delta: float) -> void`
Advances the animation mixer by a given delta time.

**Parameters**:
- `delta`: The time delta to advance the mixer.

**Note**: This method is virtual and should be overridden by the user to have any effect.

---

### `get_animation_time() -> float`
Retrieves the current time of the animation mixer.

**Return**:
- The current time in seconds.

---

### `set_animation_time(time: float) -> void`
Sets the current time of the animation mixer.

**Parameters**:
- `time`: The time in seconds to set.

---

## **Key Notes**
- **Virtual Methods**: Methods like `add_animation_library`, `advance`, and `set_animation_time` are virtual, meaning they should be overridden by subclasses to provide custom behavior.
- **Const Methods**: Methods like `has_animation`, `get_animation_library`, and `get_root_motion_position` are const, indicating they do not modify the object's state.
- **Root Motion**: Root motion properties (position, rotation, scale) are used to apply movement from animations to a character's transform. Accumulators help track changes between frames for smooth transitions.

This documentation provides a clear overview of how to use the `AnimationMixer` class to manage animations and root motion in Godot projects.