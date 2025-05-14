# CSGMesh3D

## Inheritance
- CSGMesh3D ← CSGPrimitive3D ← CSGShape3D ← GeometryInstance3D ← VisualInstance3D ← Node3D ← Node ← Object

## Description
A CSG node that uses a mesh resource as a CSG shape. The mesh must be *manifold* (closed, no self-intersections, no internal faces). See also `CSGPolygon3D` for 2D extrusion.

**Note:** CSG nodes are for level prototyping. They have high CPU cost compared to `MeshInstance3D` with `PrimitiveMesh`. Avoid using them during gameplay.

## Tutorials
- [Prototyping levels with CSG](../tutorials/3d/csg_tools)

## Properties
- **Material**: The material used to draw the CSG shape.
- **Mesh**: The mesh resource to use as a CSG shape.

## Property Descriptions

### material
- **set_material(material)**: Sets the material.
- **get_material()**: Returns the material.
- **Description**: The material used in drawing the CSG shape.

### mesh
- **set_mesh(mesh)**: Sets the mesh.
- **get_mesh()**: Returns the mesh.
- **Description**: The mesh resource to use as a CSG shape.
- **Note**: Mesh types like PlaneMesh, PointMesh, QuadMesh, and RibbonTrailMesh are non-manifold and incompatible. 
- **Note**: For ArrayMesh, only vertex positions and texture coordinates are passed to the GPU. Vertex normals are recomputed for smooth shading. Flat shading requires consistent normals per face.

## Key Notes
- CSG nodes are for prototyping, not gameplay.
- Mesh must be manifold (closed, no self-intersections).
- ArrayMesh limits: only vertex positions and UVs are used. Normals are recalculated.