# CSGPrimitive3D

## Class Hierarchy
- **Inherits:** CSGShape3D → GeometryInstance3D → VisualInstance3D → Node3D → Node → Object  
- **Inherited By:** CSGBox3D, CSGCylinder3D, CSGMesh3D, CSGPolygon3D, CSGSphere3D, CSGTorus3D  

## Description
Base class for CSG primitives. Contains shared functionality but cannot be used directly. Use derived classes like CSGBox3D instead.

## Tutorials
- [Prototyping levels with CSG](../tutorials/3d/csg_tools)

## Properties
- **flip_faces**: bool, default false  
  Toggles vertex order in triangles to reverse mesh drawing direction.

## Methods
- `void set_flip_faces(value: bool)`  
- `bool get_flip_faces()`  

## Notes
- CSG nodes are for level prototyping only.  
- High CPU cost compared to MeshInstance3D. Avoid moving CSG nodes within other CSG nodes during gameplay.