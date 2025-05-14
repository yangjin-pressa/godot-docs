# AudioStreamPlayer2D Class Documentation

## Overview
The `AudioStreamPlayer2D` class is a 2D audio stream player node in Godot, designed for playing audio streams in a 2D space. It provides properties and methods to control audio playback, volume, spatial audio, and other audio-related behaviors.

---

## Properties

### `area2d`
- **Type**: `Area2D`
- **Description**: A 2D area that defines the spatial region where the audio is played. This property is used to determine the area of influence for spatial audio effects.

### `area2d_mask`
- **Type**: `int`
- **Description**: A bitmask representing the areas that can interact with this audio player. This is used in spatial audio calculations.

### `area2d_overlap`
- **Type**: `bool`
- **Description**: Whether overlapping with other areas should be considered for spatial audio.

### `area2d_overlap_mask`
- **Type**: `int`
- **Description**: A bitmask specifying the areas that are allowed to overlap with this audio player.

### `area2d_overlap_with`
- **Type**: `Array<Area2D>`
- **Description**: An array of `Area2D` objects that are allowed to overlap with this audio player.

### `area2d_overlap_with_mask`
- **Type**: `int`
- **Description**: A bitmask specifying the areas that are allowed to overlap with this audio player.

---

## Methods

### `get_playback_position()`
- **Return Type**: `float`
- **Description**: Returns the current playback position in the `AudioStream` (in seconds).

### `get_stream_playback()`
- **Return Type**: `AudioStreamPlayback`
- **Description**: Returns the `AudioStreamPlayback` object associated with this `AudioStreamPlayer2D`.

### `has_stream_playback()`
- **Return Type**: `bool`
- **Description**: Returns whether the `AudioStreamPlayer` can return the `AudioStreamPlayback` object.

### `play(from_position=0.0)`
- **Parameters**:
  - `from_position`: `float` (optional) - The starting position in the audio stream (in seconds).
- **Description**: Queues the audio to play on the next physics frame, starting from the specified position.

### `seek(to_position)`
- **Parameters**:
  - `to_position`: `float` - The position in the audio stream (in seconds) to set as the new playback starting point.
- **Description**: Sets the position from which audio will be played.

### `stop()`
- **Description**: Stops the audio playback immediately.

---

## Key Properties (Audio Behavior)

### `stream`
- **Type**: `AudioStream`
- **Description**: The `AudioStream` object to be played. This is the core audio source for the player.

### `stream_paused`
- **Type**: `bool`
- **Description**: If `true`, the audio playback is paused. Setting this to `false` resumes playback.

### `volume_db`
- **Type**: `float`
- **Description**: The base volume in decibels (dB) before attenuation. A value of `0.0` is normal volume.

### `volume_linear`
- **Type**: `float`
- **Description**: The base volume as a linear value. This property is a convenience wrapper for `volume_db`, converting between dB and linear scales.

---

## Experimental Property

### `playback_type`
- **Type**: `PlaybackType`
- **Description**: Controls the playback type of the audio stream. Experimental; may change in future versions.
- **Possible Values**:
  - `PlaybackType.NORMAL`
  - `PlaybackType.REPEAT`
  - `PlaybackType.SHUFFLE`
  - `PlaybackType.LOOP`

---

## Notes

- **Volume Conversion**: `volume_linear` is converted to `volume_db` using `@GlobalScope.db_to_linear()` and vice versa using `@GlobalScope.linear_to_db()`.
- **Area2D Integration**: The `area2d`, `area2d_mask`, and related properties are used to define spatial audio behavior in 2D environments.
- **Spatial Audio**: This class is designed for 2D spatial audio, where audio direction and distance affect the sound's volume and panning.

---

## Example Usage

```gdscript
# Initialize an AudioStreamPlayer2D node
var player = AudioStreamPlayer2D.new()
player.stream = load("res://my_audio_stream.ogg")
player.volume_db = -10.0  # Reduce volume by 10 dB
player.play()
```

This example creates a 2D audio player, sets the audio stream, reduces the volume, and plays the audio.