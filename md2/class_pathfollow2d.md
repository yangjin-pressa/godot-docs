# PathFollow2D

**Inherits**: Node2D < CanvasItem < Node < Object

Point sampler for a Path2D. Used to make other nodes follow a path without coding movement.

## Description
- Takes parent Path2D and returns coordinates based on distance from first vertex.
- Children nodes follow path when progress is set.
- Useful for creating motion along a path.

## Properties

- **cubic_interp**: bool = true  
  Interpolates between points using cubic (true) or linear (false) method.  
  Methods: set_cubic_interpolation(value: bool), get_cubic_interpolation()

- **h_offset**: float = 0.0  
  Offset along the curve.  
  Methods: set_h_offset(value: float), get_h_offset()

- **loop**: bool = true  
  Wraps path when offset exceeds length.  
  Methods: set_loop(value: bool), has_loop()

- **progress**: float = 0.0  
  Distance along path in pixels.  
  Methods: set_progress(value: float), get_progress()

- **progress_ratio**: float = 0.0  
  Ratio of path (0.0 = first vertex, 1.0 = last).  
  Methods: set_progress_ratio(value: float), get_progress_ratio()  
  *Requires Path2D to be in scene tree with non-zero Curve2D length.*

- **rotates**: bool = true  
  Rotates node to align with path direction.  
  Methods: set_rotates(value: bool), is_rotating()

- **v_offset**: float = 0.0  
  Offset perpendicular to curve.  
  Methods: set_v_offset(value: float), get_v_offset()

## Key Functionality
- Precomputed points for faster calculations.
- Interpolation options for smooth/path accuracy.
- Looping support for cyclic paths.
- Progress/ratio control for position along path.