# VoxelGI

## Hierarchy
- **Inherits**: VisualInstance3D < Node3D < Node < Object

## Description
- Provides real-time indirect light and reflections using precomputed data.
- Requires baking before visible effects; dynamic objects receive light after baking.
- Supported only in Forward+ rendering. Not suitable for Mobile or Compatibility.
- Procedural generation is supported for levels with pre-generated geometry.
- Performance: High GPU demand. Use lower subdivisions for better performance.
- Light leaks prevented by thick walls, enclosed geometry, and static GI markers.

## Tutorials
- [Using Voxel global illumination](../tutorials/3d/global_illumination/using_voxel_gi)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties
- **camera_attributes**: Camera attributes for baking (auto-exposure ignored).
- **data**: VoxelGIData resource holding baked data.
- **size**: 3D vector (default: Vector3(20, 20, 20)). Size clamped to 1.0+.
- **subdiv**: Subdivision level (default: 128). Controls detail quality.

## Methods
- **bake(from_node=null, create_visual_debug=false)**: Bakes light from static geometry and lights. Generates debug visualizations if enabled.
- **debug_bake()**: Calls bake() with create_visual_debug enabled.

## Enumerations
### Subdiv
- **SUBDIV_64**: 64 subdivisions (lowest quality, fastest).
- **SUBDIV_128**: Default (balances quality and performance).
- **SUBDIV_256**: 256 subdivisions (highest detail, slowest).
- **SUBDIV_512**: 512 subdivisions (ultra-high detail, very slow).

## Key Notes
- Baking requires all geometry and lights to be fully ready.
- Use `call_deferred("bake")` for procedural generation.
- Size and subdivisions affect quality vs. performance tradeoff.
- Debug visualizations show solid cells for data validation.