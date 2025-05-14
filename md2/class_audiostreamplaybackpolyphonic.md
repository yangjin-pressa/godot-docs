# AudioStreamPlaybackPolyphonic

**Inherits:** AudioStreamPlayback → RefCounted → Object

Playback instance for AudioStreamPolyphonic.

## Description

- Provides playback functionality for AudioStreamPolyphonic
- After setting the "stream" property of AudioStreamPlayer, AudioStreamPlayer2D, or AudioStreamPlayer3D, use get_stream_playback() to obtain this instance
- Returns a unique integer ID for stream control

## Constants

- **INVALID_ID** = -1
  - Returned by play_stream() when no stream can be allocated

## Methods

### is_stream_playing(stream: int) → bool
- Returns true if the stream with the given ID is playing
- Check play_stream() for when the ID becomes invalid

### play_stream(stream: AudioStream, from_offset: float=0, volume_db: float=0, pitch_scale: float=1.0, playback_type: PlaybackType=0, bus: StringName="Master") → int
- Plays an AudioStream at specified offset, volume, pitch, playback type, and bus
- Returns unique integer ID for stream control
- ID becomes invalid when:
  - Stream ends (if not looping)
  - Object is stopped
  - stop_stream() is called
- Returns INVALID_ID if current streams reach AudioStreamPolyphonic.polyphony limit

### set_stream_pitch_scale(stream: int, pitch_scale: float)
- Changes pitch scale for a stream
- Stream ID must come from play_stream()

### set_stream_volume(stream: int, volume_db: float)
- Changes stream volume (in decibels)
- Stream ID must come from play_stream()

### stop_stream(stream: int)
- Stops a stream
- Stream ID must come from play_stream()

## Key Notes
- Stream IDs are unique and valid until:
  - Stream completes (non-looping)
  - AudioStreamPlaybackPolyphonic is stopped
  - stop_stream() is explicitly called
- Use AudioStreamPolyphonic.polyphony to adjust maximum polyphony capacity