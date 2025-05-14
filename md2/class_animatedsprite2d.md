# AnimatedSprite2D Class Documentation

The `AnimatedSprite2D` class is a fundamental component in Godot for rendering and controlling 2D animations. It provides properties and methods to manage sprite animations, including frame progression, playback speed, and direction. Below is a detailed breakdown of its features.

---

## **Overview**

The `AnimatedSprite2D` class is used to play 2D animations defined in a `SpriteFrames` resource. It allows developers to control animation playback, speed, direction, and frame progression, making it ideal for character movement, UI effects, and other dynamic visual elements.

---

## **Properties**

### **speed_scale** (float)
- **Description**: Scales the playback speed of the current animation. A value of `1.0` represents normal speed. Values like `0.5` slow the animation down, while `2.0` speeds it up. Negative values reverse the animation direction.
- **Range**: Float (e.g., `0.0` to `10.0`)
- **Default**: `1.0`

### **frame_progress** (float)
- **Description**: Represents the progress between `0.0` (start of the current frame) and `1.0` (end of the current frame). This value determines how far into the current frame the animation is.
- **Range**: `0.0` to `1.0`
- **Default**: `0.0`

### **offset** (Vector2)
- **Description**: An offset vector that shifts the texture's position when rendering. Useful for adjusting the sprite's alignment or positioning.
- **Default**: `Vector2(0, 0)`

### **sprite_frames** (SpriteFrames)
- **Description**: A reference to the `SpriteFrames` resource containing the animation data. This allows loading, editing, and managing animation frames directly in the editor.

---

## **Methods**

### **get_playing_speed()** → float
- **Description**: Returns the current playback speed of the animation. If the animation is not playing, it returns `0.0`. Negative values indicate reverse playback.
- **Example**: 
  ```gdscript
  var current_speed = animated_sprite.get_playing_speed()
  ```

### **is_playing()** → bool
- **Description**: Returns `true` if an animation is currently playing, regardless of speed or speed scaling settings.
- **Example**:
  ```gdscript
  if animated_sprite.is_playing():
      print("Animation is playing.")
  ```

### **pause()**
- **Description**: Pauses the current animation. The current frame and frame progress are retained, allowing resumption from the same position.
- **See Also**: `stop()`

### **play(name: StringName = "", custom_speed: float = 1.0, from_end: bool = false)** → void
- **Description**: Starts or resumes playing an animation. If `custom_speed` is negative, the animation plays in reverse. The `from_end` parameter determines whether the animation starts from the end (for reverse playback).
- **Example**:
  ```gdscript
  animated_sprite.play("walk_another_skin", 2.0, true)
  ```

### **play_backwards(name: StringName = "")** → void
- **Description**: Plays the animation in reverse. This is a shorthand for `play(name, -1.0, true)`.
- **See Also**: `play()`

### **set_frame_and_progress(frame: int, progress: float)** → void
- **Description**: Sets the current frame and frame progress without resetting the progress. Useful for switching animations while maintaining the current frame position.
- **Example**:
  ```gdscript
  var current_frame = animated_sprite.get_frame()
  var current_progress = animated_sprite.get_frame_progress()
  animated_sprite.play("walk_another_skin")
  animated_sprite.set_frame_and_progress(current_frame, current_progress)
  ```

### **stop()**
- **Description**: Stops the current animation. Resets the animation position to `0` and the `custom_speed` to `1.0`.
- **See Also**: `pause()`

---

## **Key Concepts and Example Use Cases**

### **Controlling Animation Speed**
```gdscript
animated_sprite.set_speed_scale(0.5)  # Play at half speed
animated_sprite.play("run", 2.0)      # Play "run" animation at double speed
```

### **Reversing Animation**
```gdscript
animated_sprite.play_backwards("jump")  # Play "jump" animation in reverse
```

### **Switching Animations While Preserving State**
```gdscript
# Save current frame and progress
var current_frame = animated_sprite.get_frame()
var current_progress = animated_sprite.get_frame_progress()

# Switch to a new animation
animated_sprite.play("walk_another_skin")

# Restore frame and progress
animated_sprite.set_frame_and_progress(current_frame, current_progress)
```

---

## **Tips and Best Practices**

1. **Use `SpriteFrames` Resource**: Edit animations in the Godot editor to manage frames, transitions, and keyframes.
2. **Track Frame Progress**: Use `get_frame()` and `get_frame_progress()` to synchronize animations with game logic.
3. **Pause for Smooth Transitions**: Pause the animation before switching to a new state to avoid abrupt frame jumps.
4. **Negative Speed Scaling**: Use negative `speed_scale` values for reverse playback, but ensure `custom_speed` is non-zero to avoid freezing.

---

## **Conclusion**

The `AnimatedSprite2D` class provides powerful tools for controlling 2D animations in Godot. By understanding its properties and methods, developers can create dynamic, responsive animations for games and applications. Whether you're working with character movement, UI interactions, or environmental effects, this class is essential for any 2D project.