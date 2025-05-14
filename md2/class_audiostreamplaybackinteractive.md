# AudioStreamPlaybackInteractive

**Inherits:** AudioStreamPlayback < RefCounted < Object

Playback component of AudioStreamInteractive. Contains functions to change the currently played clip.

## Methods

- **get_current_clip_index**() → int  
  Return the index of the currently playing clip. Use this to get the name of the currently playing clip with AudioStreamInteractive.get_clip_name().

  **Example:**  
  ```gdscript
  var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())
  ```

- **switch_to_clip**(clip_index: int)  
  Switch to a clip (by index).

- **switch_to_clip_by_name**(clip_name: StringName)  
  Switch to a clip (by name).