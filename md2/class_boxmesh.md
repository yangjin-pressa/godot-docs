# BoxMesh

**Inherits:** PrimitiveMesh < Mesh < Resource < RefCounted < Object

## Description
Generates an axis-aligned box mesh. The UV layout is 3×2, allowing individual texture application to each face. For uniform textures, set the material's UV property to Vector3(3, 2, 1).

**Note:** For large textured BoxMeshes (e.g., floors), UV jittering may occur. Increase `subdivide_depth`, `subdivide_height`, and `subdivide_width` until jittering disappears.

## Properties

- **size** (Vector3): Vector3(1, 1, 1)  
  Defines the box's width, height, and depth.

- **subdivide_depth** (int): 0  
  Number of extra edge loops along the Z axis.

- **subdivide_height** (int): 0  
  Number of extra edge loops along the Y axis.

- **subdivide_width** (int): 0  
  Number of extra edge loops along the X axis.

## Property Descriptions

**size**  
- `set_size(value: Vector3)`: Sets the box dimensions.  
- `get_size()`: Returns the current dimensions.

**subdivide_depth**  
- `set_subdivide_depth(value: int)`: Adjusts depth subdivision.  
- `get_subdivide_depth()`: Retrieves depth subdivision value.

**subdivide_height**  
- `set_subdivide_height(value: int)`: Adjusts height subdivision.  
- `get_subdivide_height()`: Retrieves height subdivision value.

**subdivide_width**  
- `set_subdivide_width(value: int)`: Adjusts width subdivision.  
- `get_subdivide_width()`: Retrieves width subdivision value.