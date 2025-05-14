### **AudioStreamPlayer Class Summary**

The `AudioStreamPlayer` is a node in Godot used to play audio streams. It provides properties and methods to control playback, volume, and other audio-related settings. Below is a structured overview of its key features:

---

### **Key Properties**

1. **`stream`**  
   - **Type**: `AudioStream`  
   - **Purpose**: Specifies the audio stream to be played. Setting this property stops any currently playing sounds. If empty, the node does not function.

2. **`stream_paused`**  
   - **Type**: `bool`  
   - **Purpose**: Pauses or resumes playback. When `true`, the stream is paused. This property is automatically adjusted based on the node's process mode (e.g., when the node is added/removed from the scene).

3. **`volume_db`**  
   - **Type**: `float`  
   - **Purpose**: Volume in decibels (dB). This is an offset to the stream's volume. Use `db_to_linear` or `linear_to_db` for conversion.

4. **`volume_linear`**  
   - **Type**: `float`  
   - **Purpose**: Volume as a linear value. Directly controls the volume. Modifies `volume_db` internally for convenience.

5. **`playing`**  
   - **Type**: `bool`  
   - **Purpose**: Indicates whether the node is currently playing. Setting this property has the same effect as `play()` or `stop()`.

6. **`playback_type`**  
   - **Type**: `PlaybackType` (experimental)  
   - **Purpose**: Forces the playback type (e.g., loop, single play). May change in future versions.

7. **`playback_type`**  
   - **Default**: `PlaybackType.SINGLE` (plays once, then stops). Other types may include loop or custom behaviors.

---

### **Key Methods**

1. **`play(from_position: float = 0.0)`**  
   - **Purpose**: Starts playback from the beginning or a specified position (in seconds).  
   - **Note**: For interactive streams (e.g., `AudioStreamInteractive`), this may not work as expected.

2. **`seek(to_position: float)`**  
   - **Purpose**: Jumps to a specific position (in seconds) in the stream. Does nothing if no sounds are playing.

3. **`stop()`**  
   - **Purpose**: Stops all active sounds from this node.

4. **`get_playback_position()`**  
   - **Purpose**: Returns the current playback position in seconds.  
   - **Note**: May be inaccurate due to audio server mixing delays. Add `AudioServer.get_time_since_last_mix()` for better accuracy.

5. **`get_stream_playback()`**  
   - **Purpose**: Returns the latest `AudioStreamPlayback` instance (most recently created by `play()`). Returns an empty playback if none are active.

6. **`has_stream_playback()`**  
   - **Purpose**: Checks if any sound is active, even if `stream_paused` is `true`.

---

### **Important Notes**

- **Interactive Streams**: `get_playback_position()` returns `0.0` for `AudioStreamInteractive` because they can have multiple clips.
- **Volume Conversion**: Use `db_to_linear` or `linear_to_db` to convert between decibel and linear volume values.
- **Experimental Features**: `playback_type` is experimental and may change in future versions.
- **Process Mode**: `stream_paused` is automatically adjusted based on the node's process mode (e.g., when entering/leaving the scene).

---

### **Usage Example**

```gdscript
# Play a stream from the beginning
var player = AudioStreamPlayer.instance()
player.stream = load("res://sound.mp3")
player.play()

# Pause the stream
player.stream_paused = true

# Resume the stream
player.stream_paused = false

# Seek to 5 seconds
player.seek(5.0)

# Stop the stream
player.stop()
```

This class is essential for managing audio playback in Godot projects, allowing developers to control timing, volume, and stream behavior dynamically.