# SeparationRayShape2D

**Inherits:** Shape2D < Resource < RefCounted < Object

## Description
A 2D ray shape used for physics. Typically used to provide a shape for a CollisionShape2D. When colliding, it attempts to separate itself from the object by moving its endpoint to the collision point. Example: a separation ray next to a character can allow it to move up when touching stairs.

## Properties
- **length**: float = 20.0 (🔗 class_SeparationRayShape2D_property_length)
- **slide_on_slope**: bool = false (🔗 class_SeparationRayShape2D_property_slide_on_slope)

## Property Descriptions
### length
- **Type**: float
- **Default**: 20.0
- **Description**: The ray's length.
- **Methods**:
  - `set_length(value: float)`
  - `get_length()`

### slide_on_slope
- **Type**: bool
- **Default**: false
- **Description**: 
  - If false (default), the shape always separates and returns a normal along its own direction.
  - If true, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.
- **Methods**:
  - `set_slide_on_slope(value: bool)`
  - `get_slide_on_slope()`