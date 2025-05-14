<answer>
# AnimatedSprite Class Overview

## Class Inheritance
- Inherits from: `Sprite`

## Description
A 2D sprite that can play animations using a `SpriteFrames` resource.

## Properties

- **speed_scale** (float, 1.0): Speed scaling factor for animations.
- **frame** (int, 0): Current frame index.
- **frame_progress** (float, 0.0): Progress of the current frame (0.0 to 1.0).
- **sprite_frames** (SpriteFrames): Resource containing the animation frames.
- **animation_speed** (float, 1.0): Speed of the current animation.

## Methods

- **get_playing_speed()**:
  - Returns the actual playing speed of the animation.
- **set_playing_speed(value: float)**:
  - Sets the speed of the animation.
- **set_frame(frame: int)**:
  - Changes the current frame to a specific index.
- **set_frame_progress(progress: float)**:
  - Sets the progress to a specific value.
- **set_speed_scale(value: float)**:
  - Sets the speed scale for animations.
- **set_animation_speed(value: float)**:
  - Sets the animation speed.

## Signals

- **animation_finished()**:
  - Emitted when the current animation finishes.

## Example
```gdscript
var old_frame = self.frame
self.frame = new_frame
self.frame_progress = 0.0
self.frame = old_frame
```
</answer>