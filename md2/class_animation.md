# Animation Class Documentation

## Overview
The `Animation` class in Godot is used to manage and control animation data. It provides methods to load, play, stop, and manipulate animations, including their tracks, blend settings, and update modes.

---

## Core Methods

### Basic Animation Control
```gdscript
func animation_get_animation() -> String
    # Returns the name of the current animation.
```

```gdscript
func animation_get_current_time() -> float
    # Returns the current time of the animation (in seconds).
```

```gdscript
func animation_get_duration() -> float
    # Returns the duration of the animation (in seconds).
```

```gdscript
func animation_get_frame_rate() -> int
    # Returns the frame rate of the animation.
```

```gdscript
func animation_set_current_time(time: float) -> void
    # Sets the current time of the animation (in seconds).
```

```gdscript
func animation_set_duration(duration: float) -> void
    # Sets the duration of the animation (in seconds).
```

```gdscript
func animation_set_frame_rate(frame_rate: int) -> void
    # Sets the frame rate of the animation.
```

```gdscript
func animation_play(animation: String = "") -> void
    # Plays the specified animation. If no name is provided, plays the current animation.
```

```gdscript
func animation_stop() -> void
    # Stops the current animation.
```

```gdscript
func animation_get_state() -> int
    # Returns the current state of the animation (e.g., playing, paused, stopped).
```

```gdscript
func animation_get_state_name() -> String
    # Returns the name of the current state (e.g., "playing", "paused").
```

```gdscript
func animation_get_blend_time() -> float
    # Returns the blend time for transitions between animations.
```

```gdscript
func animation_set_blend_time(time: float) -> void
    # Sets the blend time for transitions between animations.
```

```gdscript
func animation_get_blend_mode() -> int
    # Returns the blend mode (e.g., linear, constant).
```

```gdscript
func animation_set_blend_mode(mode: int) -> void
    # Sets the blend mode for transitions between animations.
```

```gdscript
func animation_get_update_mode() -> int
    # Returns the update mode (e.g., continuous, discrete).
```

```gdscript
func animation_set_update_mode(mode: int) -> void
    # Sets the update mode for the animation.
```

```gdscript
func animation_get_loop_mode() -> int
    # Returns the loop mode (e.g., loop, once, ping-pong).
```

```gdscript
func animation_set_loop_mode(mode: int) -> void
    # Sets the loop mode for the animation.
```

---

## Track Management

### Track Count and Access
```gdscript
func animation_get_track_count() -> int
    # Returns the number of tracks in the animation.
```

```gdscript
func animation_get_track(track_idx: int) -> AnimationTrack
    # Returns the track at the specified index.
```

```gdscript
func animation_get_track_name(track_idx: int) -> String
    # Returns the name of the track at the specified index.
```

```gdscript
func animation_get_track_type(track_idx: int) -> int
    # Returns the type of the track (e.g., bone, transform, value).
```

### Track Operations
```gdscript
func animation_add_track(track: AnimationTrack) -> void
    # Adds a new track to the animation.
```

```gdscript
func animation_remove_track(track_idx: int) -> void
    # Removes the track at the specified index.
```

```gdscript
func animation_move_track_down(track_idx: int) -> void
    # Moves the track down in the track list.
```

```gdscript
func animation_move_track_up(track_to_move: int) -> void
    # Moves the track up in the track list.
```

```gdscript
func animation_move_track_to(track_idx: int, to_idx: int) -> void
    # Moves a track to a new position in the track list.
```

```gdscript
func animation_swap_tracks(track_idx: int, with_idx: int) -> void
    # Swaps the positions of two tracks.
```

---

## Bone Track Methods
```gdscript
func animation_bone_track_get_bone(track_idx: int) -> String
    # Returns the bone name associated with the track.
```

```gdscript
func animation_bone_track_get_key_count(track_idx: int) -> int
    # Returns the number of keyframes in the bone track.
```

```gdscript
func animation_bone_track_get_key(track_idx: int, key_idx: int) -> BoneKey
    # Returns the keyframe at the specified index in the bone track.
```

---

## Transform Track Methods
```gdscript
func animation_transform_track_get_type(track_idx: int) -> int
    # Returns the type of the transform track (e.g., TRANSLATE, ROTATE, SCALE).
```

```gdscript
func animation_transform_track_get_key_count(track_idx: int) -> int
    # Returns the number of keyframes in the transform track.
```

```gdscript
func animation_transform_track_get_key(track_idx: int, key_idx: int) -> TransformKey
    # Returns the keyframe at the specified index in the transform track.
```

---

## Value Track Methods
```gdscript
func animation_value_track_get_update_mode(track_idx: int) -> int
    # Returns the update mode for the value track (e.g., continuous, discrete).
```

```gdscript
func animation_value_track_set_update_mode(track_idx: int, mode: int) -> void
    # Sets the update mode for the value track.
```

```gdscript
func animation_value_track_get_key_count(track_idx: int) -> int
    # Returns the number of keyframes in the value track.
```

```gdscript
func animation_value_track_get_key(track_idx: int, key_idx: int) -> ValueKey
    # Returns the keyframe at the specified index in the value track.
```

---

## Keyframe Manipulation
```gdscript
func animation_track_get_key(track_idx: int, key_idx: int) -> Key
    # Returns the keyframe at the specified index in the track.
```

```gdscript
func animation_track_set_key(track_idx: int, key_idx: int, key: Key) -> void
    # Sets the keyframe at the specified index in the track.
```

---

## Enums and Constants

### Update Modes
- `UPDATE_MODE_CONTINUOUS`: Continuous updates.
- `UPDATE_MODE_DISCRETE`: Discrete updates.

### Interpolation Types
- `INTERPOLATION_LINEAR`: Linear interpolation.
- `INTERPOLATION_CONSTANT`: Constant interpolation.
- `INTERPOLATION_SINE`: Sine interpolation.

### Blend Modes
- `BLEND_MODE_LINEAR`: Linear blend.
- `BLEND_MODE_CONSTANT`: Constant blend.

### Loop Modes
- `LOOP_MODE_ONCE`: Play once.
- `LOOP_MODE_LOOP`: Loop infinitely.
- `LOOP_MODE_PING_PONG`: Ping-pong loop.

### Track Types
- `TRACK_TYPE_BONE`: Bone track.
- `TRACK_TYPE_TRANSFORM`: Transform track.
- `TRACK_TYPE_VALUE`: Value track.

---

## Notes
- **Track Management**: Ensure tracks are properly added and indexed before accessing them.
- **Animation Lifecycle**: Load animations before playing or stopping them.
- **Blend Settings**: Adjust blend time and mode for smooth transitions between animations.
- **Update Modes**: Choose the appropriate mode based on the animation's behavior (e.g., discrete for rigid body movements).

This documentation covers all core methods and related enums for the `Animation` class, providing a comprehensive guide for managing animations in Godot.