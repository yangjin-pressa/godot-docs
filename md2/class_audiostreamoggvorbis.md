**AudioStreamOggVorbis**  
A class representing Ogg Vorbis audio data.  

---

### **Description**  
This class is used to handle Ogg Vorbis audio streams, providing methods to load and manage audio data from files or memory.  

---

### **Tutorials**  
- [How to Use AudioStreamOggVorbis](#)  
  A guide on loading and playing Ogg Vorbis files.  

---

### **Properties**  
- **bar_beats**: `int` = `4`  
  A property with a default value of 4.  
- **loop**: `bool` = `false`  
  Controls whether the audio stream loops.  
- **volume**: `float` = `1.0`  
  Sets the playback volume.  

**Methods**  
- **get_bar_beats()**: `int`  
  Returns the current value of `bar_beats`.  
- **set_bar_beats(value: int)**: `void`  
  Sets the `bar_beats` property.  

---

### **Methods**  
- **load_from_buffer(data: bytes)**: `void`  
  Loads audio data from a buffer.  
- **load_from_file(path: str)**: `void`  
  Loads audio data from a file.  

---

### **Property Descriptions**  
- **bar_beats**:  
  An integer value used for tracking beats in the audio stream.  

- **loop**:  
  When set to `true`, the audio stream will repeat indefinitely.  

- **volume**:  
  A float value between 0.0 (muted) and 1.0 (full volume).  

---

### **Method Descriptions**  
- **load_from_buffer(data: bytes)**:  
  Initializes the audio stream from raw binary data.  

- **load_from_file(path: str)**:  
  Loads the audio stream from a file on disk.  

--- 

**Note**: This class is designed for audio processing and requires Ogg Vorbis support in the runtime environment.