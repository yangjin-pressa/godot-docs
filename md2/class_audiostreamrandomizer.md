**AudioStreamRandomizer Class (Godot)**

---

### **Overview**
A class for managing random playback of audio streams, with support for enumerating playback modes, manipulating stream collections, and adjusting probabilities for selection.

---

### **Properties**
- **PlaybackMode** (enum): Determines how streams are selected.  
  - Default: `0` (Random playback).  
  - Other values may represent different modes (e.g., sequential, weighted).

---

### **Enumerations**
- **PlaybackMode**  
  - **0**: Random playback (default).  
  - **1**: Sequential playback.  
  - **2**: Weighted playback (higher weights favor certain streams).  

---

### **Methods**
- **add_stream(index: int, stream: AudioStream, weight: float = 1.0)**  
  Adds a stream to the collection at a specified index. Default weight is 1.0.

- **get_stream(index: int)**  
  Returns the stream at the specified index.

- **get_stream_probability_weight(index: int)**  
  Returns the weight associated with the stream at the given index.

- **move_stream(index_from: int, index_to: int)**  
  Moves a stream from one index to another.

- **remove_stream(index: int)**  
  Removes the stream at the specified index.

- **set_stream(index: int, stream: AudioStream)**  
  Sets the AudioStream at the specified index.

- **set_stream_probability_weight(index: int, weight: float)**  
  Sets the probability weight for the stream at the specified index. Higher values increase the likelihood of selection.

---

### **Key Features**
- **Random Playback**: Randomly selects streams based on the `PlaybackMode` enum.
- **Weighted Selection**: Adjusts probabilities for stream selection via `set_stream_probability_weight()`.
- **Stream Management**: Supports adding, removing, and reordering streams.