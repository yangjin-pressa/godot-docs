# QuadOccluder3D

**Inherits:** Occluder3D < Resource < RefCounted < Object

## Description
A flat plane shape for occlusion culling in OccluderInstance3D. See PolygonOccluder3D for customization.

## Tutorials
[Occlusion culling](../tutorials/3d/occlusion_culling)

## Properties
- **size**: Vector2 = Vector2(1, 1)

## Property Descriptions
**size** (Vector2) = Vector2(1, 1)  
The quad's size in 3D units.

## Methods
- void set_size(Vector2 value)
- Vector2 get_size() 

## Inheritance
- Occluder3D
  - Resource
    - RefCounted
      - Object