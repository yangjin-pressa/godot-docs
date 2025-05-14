# CSGCylinder3D

## Inheritance Hierarchy
- CSGCylinder3D
  - CSGPrimitive3D
    - CSGShape3D
      - GeometryInstance3D
        - VisualInstance3D
          - Node3D
            - Node
              - Object

## Description
This node creates a cylinder (or cone) for use with the CSG system.  
**Note:** CSG nodes are for level prototyping. They have higher CPU costs than MeshInstance3D with PrimitiveMesh. Avoid moving CSG nodes during gameplay.

## Tutorials
[Prototyping levels with CSG](../tutorials/3d/csg_tools)

## Properties
- **cone** (bool): false. If true, creates a cone; radius applies to one side.
- **height** (float): 2.0. The height of the cylinder.
- **material** (Material): Default value unspecified. Material for rendering.
- **radius** (float): 0.5. The radius of the cylinder.
- **sides** (int): 8. Number of sides affecting detail (higher = more detail).
- **smooth_faces** (bool): true. Smooth normals for rounded appearance; false for flat shading.

## Method Descriptions
- **set_cone** (value: bool): virtual (Override to customize behavior).
- **is_cone** (): const (No side effects; returns current cone state).

- **set_height** (value: float): virtual (Override to customize behavior).
- **get_height** (): const (No side effects; returns current height).

- **set_material** (value: Material): virtual (Override to customize behavior).
- **get_material** (): const (No side effects; returns current material).

- **set_radius** (value: float): virtual (Override to customize behavior).
- **get_radius** (): const (No side effects; returns current radius).

- **set_sides** (value: int): virtual (Override to customize behavior).
- **get_sides** (): const (No side effects; returns current sides count).

- **set_smooth_faces** (value: bool): virtual (Override to customize behavior).
- **get_smooth_faces** (): const (No side effects; returns current smooth_faces state).