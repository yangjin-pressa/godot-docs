# PrimitiveMesh

## Inheritance
- **Inherits:** Mesh → Resource → RefCounted → Object  
- **Inherited By:** BoxMesh, CapsuleMesh, CylinderMesh, PlaneMesh, PointMesh, PrismMesh, RibbonTrailMesh, SphereMesh, TextMesh, TorusMesh, TubeTrailMesh

## Description
Base class for all primitive meshes. Manages application of a [Material](class_Material). Examples include BoxMesh, CapsuleMesh, CylinderMesh, PlaneMesh, PrismMesh, and SphereMesh.

## Properties
- **add_uv2** (bool): `false`  
  Generates UV2 coordinates with padding. UV2 is needed for lightmapping.
- **custom_aabb** (AABB): `AABB(0, 0, 0, 0, 0, 0)`  
  Overrides the AABB for frustum culling. Useful for avoiding unexpected culling with shaders.
- **flip_faces** (bool): `false`  
  Reverses vertex order in triangles. Equivalent to `CULL_FRONT` in BaseMaterial3D.
- **material** (Material)  
  Current material applied to the primitive mesh.
- **uv2_padding** (float): `2.0`  
  Padding in pixels for UV2 seams. Lower values improve lightmap texture efficiency but may cause bleeding.

## Methods
- **_create_mesh_array** (virtual)  
  Override to customize mesh generation. Returns an Array of vertex data arrays.
- **get_mesh_arrays** (const)  
  Returns mesh arrays for the primitive. Example usage:
  ```gdscript
  var c = CylinderMesh.new()
  var arr_mesh = ArrayMesh.new()
  arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, c.get_mesh_arrays())
  ```
  ```csharp
  var c = new CylinderMesh();
  var arrMesh = new ArrayMesh();
  arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, c.GetMeshArrays());
  ```
- **request_update**  
  Triggers an update of the mesh based on its properties.

## Notes
- `add_uv2` and `uv2_padding` are tied to UV2 generation for lightmapping.
- `custom_aabb` allows user-defined AABB for frustum culling.
- `flip_faces` affects rendering direction, equivalent to material culling settings.