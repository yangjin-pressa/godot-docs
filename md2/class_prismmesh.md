# PrismMesh

**Inherits:** PrimitiveMesh < Mesh < Resource < RefCounted < Object

Class representing a prism-shaped PrimitiveMesh.

## Description
Class representing a prism-shaped PrimitiveMesh.

## Properties
- **left_to_right**: float, 0.5  
  Displacement of the upper edge along the X axis. 0.0 positions edge straight above the bottom-left edge.  
  Methods: set_left_to_right(value: float), get_left_to_right()

- **size**: Vector3, Vector3(1, 1, 1)  
  Size of the prism.  
  Methods: set_size(value: Vector3), get_size()

- **subdivide_depth**: int, 0  
  Number of added edge loops along the Z axis.  
  Methods: set_subdivide_depth(value: int), get_subdivide_depth()

- **subdivide_height**: int, 0  
  Number of added edge loops along the Y axis.  
  Methods: set_subdivide_height(value: int), get_subdivide_height()

- **subdivide_width**: int, 0  
  Number of added edge loops along the X axis.  
  Methods: set_subdivide_width(value: int), get_subdivide_width()