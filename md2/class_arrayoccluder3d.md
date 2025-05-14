# ArrayOccluder3D

**Inherits:** Occluder3D < Resource < RefCounted < Object

A 3D polygon shape for occlusion culling in OccluderInstance3D.

## Description
Stores arbitrary 3D polygon shape for occlusion culling. Similar to ArrayMesh but for occluders.

## Tutorials
- Occlusion culling:../tutorials/3d/occlusion_culling

## Properties
- indices: PackedInt32Array()  
- vertices: PackedVector3Array()

## Methods
- set_arrays(vertices: PackedVector3Array, indices: PackedInt32Array): Sets vertices and indices, updating occluder once.

## Property Descriptions
### indices
- Type: PackedInt32Array
- Default: PackedInt32Array()
- Description: Determines which vertices to draw and in what order. Note: occluder is updated after setting. Use set_arrays() to avoid double updates.

### vertices
- Type: PackedVector3Array
- Default: PackedVector3Array()
- Description: Vertex positions in local 3D coordinates. Note: occluder is updated after setting. Use set_arrays() to avoid double updates.

## Method Descriptions
### set_arrays
- Parameters: vertices (PackedVector3Array), indices (PackedInt32Array)
- Description: Sets vertices and indices, updating occluder once after both are set.