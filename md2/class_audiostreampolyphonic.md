# AudioStreamPolyphonic

## Inheritance
- `AudioStream`
  - `Resource`
    - `RefCounted`
      - `Object`

## Description
- Allows playback of custom audio streams from code using a single player.
- Playback control is managed via `AudioStreamPlaybackPolyphonic` instance obtained from `AudioStreamPlayer` methods.

## Properties
- **polyphony**: `int` = 32
  - Maximum number of simultaneous audio streams that can be played.

## Method Descriptions
- **set_polyphony(value: int)**: Sets the maximum number of simultaneous streams.
- **get_polyphony()**: Returns the current value of the maximum number of simultaneous streams.

## Notes
- Methods are virtual (should be overridden by users) and const (no side effects).