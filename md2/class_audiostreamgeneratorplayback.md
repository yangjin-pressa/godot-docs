**Class:** AudioStreamGeneratorPlayback  
**Inherits:** AudioStreamPlaybackResampled → AudioStreamPlayback → RefCounted → Object  

**Description**  
Used with AudioStreamGenerator to play back generated audio in real-time.  

**Tutorials**  
- Audio Generator Demo: https://godotengine.org/asset-library/asset/2759  
- Godot 3.2 will get new audio features: https://godotengine.org/article/godot-32-will-get-new-audio-features  

**Methods**  
- **can_push_buffer(amount: int)** → bool  
  Returns true if a buffer of size `amount` can be pushed without overflowing.  

- **clear_buffer()** → void  
  Clears the audio sample data buffer.  

- **get_frames_available()** → int  
  Returns the number of frames that can be pushed without overflowing.  

- **get_skips()** → int  
  Returns the number of times playback skipped due to buffer underrun.  

- **push_buffer(frames: PackedVector2Array)** → bool  
  Pushes multiple audio frames. More efficient in compiled languages.  

- **push_frame(frame: Vector2)** → bool  
  Pushes a single audio frame. More efficient in GDScript.  

**Notes**  
- `push_buffer` is generally more efficient in C#/GDExtension, while `push_frame` may be better in GDScript.  
- `get_skips` resets at the start of playback.