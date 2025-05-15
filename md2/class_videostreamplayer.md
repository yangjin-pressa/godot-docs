**VideoStreamPlayer Class**  
- **Inherits**: GodotObject  

---

### **Description**  
A class for playing video streams in Godot. Supports various formats, with built-in support for Ogg Theora.  

---

### **Tutorials**  
- [Video Streaming Basics](https://docs.godotengine.org/en/latest/tutorials/...)  

---

### **Properties**  
- **audio_track**: `int = 0`  
- **autoplay**: `bool = false`  
- **stream**: `VideoStream`  
- **stream_position**: `float`  
- **volume**: `float`  
- **volume_db**: `float = 0.0`  

---

### **Methods**  
- **get_stream_length()**: `float`  
  - Returns the length of the current stream in seconds.  
  - *Note*: For VideoStreamTheora, this is always zero.  

- **get_stream_name()**: `String`  
  - Returns the stream's name or `<No Stream>`.  

- **get_video_texture()**: `Texture2D`  
  - Returns the current frame as a Texture2D.  

- **is_playing()**: `bool`  
  - Returns true if the video is playing (including paused states).  

- **play()**: `void`  
  - Starts playback from the beginning.  

- **stop()**: `void`  
  - Stops playback and resets the stream position to 0.  

---

### **Signals**  
- **finished**: Emitted when the video finishes playing.  

---

### **Notes**  
- **Seeking**: Not implemented yet (except for GDExtension formats).  
- **Volume**: Linear value for `volume`, dB for `volume_db`.  
- **Ogg Theora**: Built-in support, but stream length is not supported.