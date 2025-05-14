# CSGTorus3D

## Inheritance Hierarchy
- CSGTorus3D
  - CSGPrimitive3D
    - CSGShape3D
      - GeometryInstance3D
        - VisualInstance3D
          - Node3D
            - Node
              - Object

## Description
A CSG Torus shape.  
**Note:** CSG nodes are intended for level prototyping. Creating CSG nodes has significant CPU cost compared to using MeshInstance3D with PrimitiveMesh. Moving CSG nodes within other CSG nodes also has significant CPU cost, so avoid during gameplay.

## Tutorials
- [Prototyping levels with CSG](../tutorials/3d/csg_tools)

## Properties
- **inner_radius**: float = 0.5  
  The inner radius of the torus.
- **material**: Material  
  The material used to render the torus.
- **outer_radius**: float = 1.0  
  The outer radius of the torus.
- **ring_sides**: int = 6  
  The number of edges each ring of the torus is constructed of.
- **sides**: int = 8  
  The number of slices the torus is constructed of.
- **smooth_faces**: bool = true  
  If true, normals give smooth effect; if false, flat shaded look.

## Property Descriptions
- **set_inner_radius**(value: float): void  
  Sets the inner radius of the torus.
- **get_inner_radius**(): float  
  Retrieves the inner radius of the torus.

- **set_material**(value: Material): void  
  Sets the material used to render the torus.
- **get_material**(): Material  
  Retrieves the material used to render the torus.

- **set_outer_radius**(value: float): void  
  Sets the outer radius of the torus.
- **get_outer_radius**(): float  
  Retrieves the outer radius of the torus.

- **set_ring_sides**(value: int): void  
  Sets the number of edges per ring.
- **get_ring_sides**(): int  
  Retrieves the number of edges per ring.

- **set_sides**(value: int): void  
  Sets the number of slices.
- **get_sides**(): int  
  Retrieves the number of slices.

- **set_smooth_faces**(value: bool): void  
  Sets whether normals are smooth.
- **get_smooth_faces**(): bool  
  Retrieves whether normals are smooth.