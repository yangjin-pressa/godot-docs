# ResourceImporterOBJ

**Inherits:** ResourceImporter < RefCounted < Object

## Description
Imports an OBJ 3D model as an independent Mesh resource. Unlike ResourceImporterScene, it creates a single Mesh for use in nodes requiring direct Mesh resources (e.g., GridMap, GPUParticles3D). Advanced settings allow saving mesh resources from 3D scenes.

See also: ResourceImporterScene

## Tutorials
- [Importing 3D scenes](../tutorials/assets_pipeline/importing_3d_scenes/index)

## Properties
- **force_disable_mesh_compression**: false (bool)  
  Prevents mesh compression. Enable if blocky artifacts appear or meshes are large.
- **generate_lightmap_uv2**: false (bool)  
  Generates UV2 for LightmapGI baking. 
- **generate_lightmap_uv2_texel_size**: 0.2 (float)  
  Controls lightmap texel size. Smaller values increase precision but increase file size.
- **generate_lods**: true (bool)  
  Creates lower-detail mesh variants for performance. Not all meshes benefit.
- **generate_shadow_mesh**: true (bool)  
  Generates shadow meshes to optimize shadow rendering. 
- **generate_tangents**: true (bool)  
  Generates vertex tangents using Mikktspace. Preferred to have tangent data in source files.
- **offset_mesh**: Vector3(0, 0, 0) (Vector3)  
  Offsets mesh data for misaligned models.
- **scale_mesh**: Vector3(1, 1, 1) (Vector3)  
  Scales mesh data for misscaled models.

## Notes
- **generate_lightmap_uv2_texel_size** only effective if generate_lightmap_uv2 is true.
- Mesh LOD settings: [Mesh level of detail (LOD)](../tutorials/3d/mesh_lod.html#doc-mesh-lod)