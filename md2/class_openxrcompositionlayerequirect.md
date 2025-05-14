# OpenXRCompositionLayerEquirect

**Experimental:** This class may be changed or removed in future versions.

**Inherits from:**
- `OpenXRCompositionLayer`
- `Node3D`
- `Node`
- `Object`

## Description
An OpenXR composition layer that allows rendering a `SubViewport` on an internal slice of a sphere.

## Properties

- **central_horizontal_angle**: `float` (default: 1.5708)  
  The central horizontal angle of the sphere. Used to set the width.

- **fallback_segments**: `int` (default: 10)  
  The number of segments to use in the fallback mesh.

- **lower_vertical_angle**: `float` (default: 0.785398)  
  The lower vertical angle of the sphere. Used with `upper_vertical_angle` to set the height.

- **radius**: `float` (default: 1.0)  
  The radius of the sphere.

- **upper_vertical_angle**: `float` (default: 0.785398)  
  The upper vertical angle of the sphere. Used with `lower_vertical_angle` to set the height.

## Method Definitions

- `set_central_horizontal_angle(value: float)`  
  Sets the central horizontal angle of the sphere.

- `get_central_horizontal_angle()`  
  Returns the central horizontal angle of the sphere.

- `set_fallback_segments(value: int)`  
  Sets the number of segments for the fallback mesh.

- `get_fallback_segments()`  
  Returns the number of segments for the fallback mesh.

- `set_lower_vertical_angle(value: float)`  
  Sets the lower vertical angle of the sphere.

- `get_lower_vertical_angle()`  
  Returns the lower vertical angle of the sphere.

- `set_radius(value: float)`  
  Sets the radius of the sphere.

- `get_radius()`  
  Returns the radius of the sphere.

- `set_upper_vertical_angle(value: float)`  
  Sets the upper vertical angle of the sphere.

- `get_upper_vertical_angle()`  
  Returns the upper vertical angle of the sphere.