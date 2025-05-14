# CapsuleMesh

## Class Hierarchy
- `PrimitiveMesh` < `Mesh` < `Resource` < `RefCounted` < `Object`

## Description
Class representing a capsule-shaped `PrimitiveMesh`.

## Properties
- **height**: `float` = 2.0  
  Total height of the capsule mesh (including the hemispherical ends).
- **radial_segments**: `int` = 64  
  Number of radial segments on the capsule mesh.
- **radius**: `float` = 0.5  
  Radius of the capsule mesh.
- **rings**: `int` = 8  
  Number of rings along the height of the capsule.

## Property Methods
### height
- `set_height(value: float)`
- `get_height()`

### radial_segments
- `set_radial_segments(value: int)`
- `get_radial_segments()`

### radius
- `set_radius(value: float)`
- `get_radius()`

### rings
- `set_rings(value: int)`
- `get_rings()`

## Notes
- **virtual**: This method should typically be overridden by the user to have any effect.
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.