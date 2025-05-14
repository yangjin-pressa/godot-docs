**Class: AudioStreamPlayback**  
**Inherits:** `AudioStream`  

---

### **Description**  
A class for playing audio streams. It provides methods to control playback, seek, and retrieve stream information.  

---

### **Tutorials**  
- [AudioStreamPlayback tutorial](https://godotengine.org/doc/classes/audiostreamplayer.html)  

---

### **Methods**  

#### **Private Methods (Overrideable)**  
1. **_seek(position: float)**  
   - **Description:** Custom seek behavior for the audio stream.  
   - **Note:** Override to handle seeking (e.g., call `AudioStreamPlayer.seek()`).  

2. **_start(from_pos: float)**  
   - **Description:** Custom start behavior for the audio stream.  
   - **Note:** Override to handle starting at a specific position (e.g., call `AudioStreamPlayer.play()`).  

3. **_stop()**  
   - **Description:** Custom stop behavior for the audio stream.  
   - **Note:** Override to handle stopping (e.g., call `AudioStreamPlayer.stop()`).  

4. **_tag_used_streams()**  
   - **Description:** Tag used audio streams for editor preview.  
   - **Note:** Called when `AudioServer.set_enable_tagging_used_audio_streams()` is enabled.  

5. **_set_parameter(name: StringName, value: Variant)**  
   - **Description:** Set a playback parameter (e.g., volume, pan).  

6. **_get_loop_count()**  
   - **Description:** Return the number of times the stream has looped.  

7. **_get_playback_position()**  
   - **Description:** Return the current position in the stream (in seconds).  

---

#### **Public Methods**  
1. **seek(time: float = 0.0)**  
   - **Description:** Seek the stream to the specified time (in seconds).  

2. **start(from_pos: float = 0.0)**  
   - **Description:** Start the stream from the specified position (in seconds).  

3. **stop()**  
   - **Description:** Stop the stream.  

4. **mix_audio(rate_scale: float, frames: int) → PackedVector2Array**  
   - **Description:** Mix audio frames from the stream.  
   - **Returns:** A `PackedVector2Array` with left/right channel data per frame.  

5. **get_sample_playback() → AudioSamplePlayback**  
   - **Description:** Experimental: Get the associated `AudioSamplePlayback` object.  
   - **Note:** May be removed in future versions.  

6. **set_sample_playback(playback_sample: AudioSamplePlayback)**  
   - **Description:** Experimental: Set the `AudioSamplePlayback` object for this stream.  

7. **is_playing() → bool**  
   - **Description:** Check if the stream is currently playing.  

8. **get_loop_count() → int**  
   - **Description:** Return the number of times the stream has looped.  

9. **get_playback_position() → float**  
   - **Description:** Return the current position in the stream (in seconds).  

---

### **Notes**  
- **Experimental Methods:** `get_sample_playback()` and `set_sample_playback()` may change or be removed.  
- **Virtual Methods:** Private methods (e.g., `_seek()`, `_start()`) are overrideable; public methods (e.g., `seek()`, `start()`) are standard.  
- **Tagging:** `_tag_used_streams()` is used for editor preview tracking.