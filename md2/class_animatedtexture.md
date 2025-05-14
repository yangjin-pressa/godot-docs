**Class Name**: AnimatedTexture  
**Status**: Deprecated (may be removed in future).  
**Inherits**: Texture2D → Texture → Resource → RefCounted → Object  

---

### **Description**  
- A resource format for frame-based animations.  
- Allows chaining multiple textures with predefined frame delays.  
- Works as a proxy for Texture2D, usable in TileSet and other contexts.  
- Animation loops automatically after the last frame.  
- **Note**: All frames must have the same size; larger frames are cropped.  
- **Warning**: Not efficient for modern renderers.  
- **Note**: Does not support AtlasTexture; each frame must be a separate Texture2D.  

---

### **Properties**  
- **current_frame**: int (default: 0)  
  - Current visible frame. Setting this resets the frame's timer.  
- **frames**: int (default: 1)  
  - Number of frames in the animation. Max: MAX_FRAMES (256).  
- **one_shot**: bool (default: false)  
  - If true, animation plays once and stops.  
- **pause**: bool (default: false)  
  - If true, animation pauses at current frame.  
- **speed_scale**: float (default: 1.0)  
  - Multiplies animation speed. Negative values play in reverse.  

---

### **Methods**  
- **get_frame_duration(frame: int)** → float  
  - Returns the duration of a specific frame in seconds.  
- **get_frame_texture(frame: int)** → Texture2D  
  - Returns the Texture2D of a specific frame.  
- **set_frame_duration(frame: int, duration: float)**  
  - Sets the duration of a frame. A duration of 0 skips the frame.  
- **set_frame_texture(frame: int, texture: Texture2D)**  
  - Assigns a Texture2D to a frame. Frame IDs start at 0.  

---

### **Constants**  
- **MAX_FRAMES**: 256  
  - Maximum frames supported. Use AnimationPlayer for more frames.  

---

### **Property Details**  
- **current_frame**:  
  - Sets the current frame. Modifies the timer for the selected frame.  
- **frames**:  
  - Defines the total number of frames. Must be ≤ MAX_FRAMES.  
- **one_shot**:  
  - Controls whether the animation loops.  
- **pause**:  
  - Pauses the animation at the current frame. Resumes when set to false.  
- **speed_scale**:  
  - Adjusts playback speed. Negative values reverse the animation.  

---

### **Method Details**  
- **get_frame_duration**:  
  - Retrieves the duration of a specific frame.  
- **get_frame_texture**:  
  - Retrieves the Texture2D associated with a frame.  
- **set_frame_duration**:  
  - Sets the duration for a frame. A duration of 0 skips the frame during playback.  
- **set_frame_texture**:  
  - Assigns a Texture2D to a frame. Frame indices start at 0.  

---

### **Important Notes**  
- **Deprecated**: This class may be removed in future versions.  
- **AtlasTexture Support**: Not supported; each frame must be a separate Texture2D.  
- **Efficiency**: The current implementation is not optimized for modern renderers.