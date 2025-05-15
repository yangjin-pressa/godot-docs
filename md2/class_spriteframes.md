**SpriteFrames Overview**  
SpriteFrames is a class that manages animations, allowing for the creation and manipulation of animation frames. It provides methods for adding, removing, and modifying frames, as well as controlling animation speed and looping behavior.

---

**Methods**  
- **add_frame**: Adds a new frame to the specified animation. Parameters include animation name, texture, and optional duration.  
- **remove_frame**: Removes a specific frame from an animation. Parameters include the animation name and frame index.  
- **set_frame**: Sets the texture and duration of a specific frame in an animation. Parameters include animation name, frame index, texture, and optional duration.  
- **get_frame_texture**: Returns the texture of a specific frame in an animation. Parameters include animation name and frame index.  
- **get_frame_duration**: Returns the relative duration of a frame. Parameters include animation name and frame index. Note: Duration affects how long the frame is displayed.  
- **get_animation_names**: Returns an array of animation names in alphabetical order.  
- **get_animation_speed**: Returns the frame rate (frames per second) for an animation.  
- **get_frame_count**: Returns the number of frames in an animation.  
- **has_animation**: Checks if an animation exists.  
- **rename_animation**: Changes the name of an animation.  
- **set_animation_loop**: Enables or disables looping for an animation.  
- **set_animation_speed**: Sets the frame rate for an animation.  

---

**Key Notes**  
- **Relative vs. Absolute Duration**:  
  - Relative duration (e.g., 2.0) affects display time.  
  - Absolute duration calculation: `relative_duration / (animation_fps * abs(playing_speed))`.  
- **Animation Control**: Methods like `set_animation_loop` and `set_animation_speed` allow dynamic control of animation behavior.  
- **Frame Indexing**: Frame indices are zero-based, and removing a frame shifts subsequent indices.  

This documentation provides a clear framework for managing animation frames and their properties in a game or application.