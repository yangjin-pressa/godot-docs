# ParallaxLayer

**Deprecated:** Use the Parallax2D node instead.

**Inherits:** Node2D < CanvasItem < Node < Object

A parallax scrolling layer used with ParallaxBackground.

## Description

A ParallaxLayer must be a child of ParallaxBackground. Each can move at different speeds relative to camera movement or ParallaxBackground.scroll_offset.

Children of this node are affected by its scroll offset.

**Note:** Position and scale changes after scene entry are ignored.

## Properties

- **motion_mirroring**: Vector2 = (0, 0)  
  Interval for repeating the ParallaxLayer. If an axis is 0, the layer is drawn once.  
  **Note:** Mirroring is repetition, not reflection.  
  **Method**:  
  - `set_mirroring(Vector2 value)`  
  - `get_mirroring()`

- **motion_mirroring**: Vector2 = (0, 0)  
  **Note:** Mirroring is repetition, not reflection.  
  **Method**:  
  - `set_mirroring(Vector2 value)`  
  - `get_mirroring()`

- **physics_interpolation_mode**: Integer = 2  
  Overrides Node's default physics interpolation mode.

## Notes

- **Mirroring**: The value determines how often the ParallaxLayer repeats, not its direction.  
- **Position/Scale Changes**: Modifications after initialization are ignored.  
- **Physics Mode**: This property sets the interpolation behavior for physics simulations.