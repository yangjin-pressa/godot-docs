# PolygonOccluder3D

## Inheritance Hierarchy
- **PolygonOccluder3D**  
  < :ref:`Occluder3D<class_Occluder3D>`  
  < :ref:`Resource<class_Resource>`  
  < :ref:`RefCounted<class_RefCounted>`  
  < :ref:`Object<class_Object>`

## Description
A flat 2D polygon shape used for occlusion culling in 3D environments.  
- Points must lie on the same 2D plane.  
- Cannot create arbitrary 3D shapes. Use **ArrayOccluder3D** or **OccluderInstance3D** for complex shapes.  
- See: [OccluderInstance3D documentation](class_OccluderInstance3D) for setup instructions.

## Tutorials
- [Occlusion culling](../tutorials/3d/occlusion_culling)

## Properties
- **polygon**: :ref:`PackedVector2Array<class_PackedVector2Array>` (default: empty)  
  - Defines the 2D polygon for occlusion culling.  
  - Must not have intersecting lines (triangulation fails otherwise).  
  - The array is copied; changes to it do not update the original property.

## Method Definitions
- **set_polygon(value: PackedVector2Array)**: Sets the polygon.  
- **get_polygon()**: Returns the polygon (copied array).

## Notes
- The polygon can be convex or concave, but performance is optimized with fewer points.  
- The returned array is a copy, so modifications to it do not affect the original property.