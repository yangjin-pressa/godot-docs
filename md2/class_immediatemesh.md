# ImmediateMesh

**Inherits:** Mesh < Resource < RefCounted < Object

Mesh optimized for creating geometry manually, similar to OpenGL 1.x immediate mode.

## Description
- Created for manual geometry generation
- Example usage:
  ```gdscript
  var mesh = ImmediateMesh.new()
  mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)
  mesh.surface_add_vertex(Vector3.LEFT)
  mesh.surface_add_vertex(Vector3.FORWARD)
  mesh.surface_add_vertex(Vector3.ZERO)
  mesh.surface_end()
  ```
  ```csharp
  var mesh = new ImmediateMesh();
  mesh.SurfaceBegin(Mesh.PrimitiveType.Triangles);
  mesh.SurfaceAddVertex(Vector3.Left);
  mesh.SurfaceAddVertex(Vector3.Forward);
  mesh.SurfaceAddVertex(Vector3.Zero);
  mesh.SurfaceEnd();
  ```
- Note: Generating complex geometry is inefficient; designed for simple, frequently-changing data

## Tutorials
- [Using ImmediateMesh](../tutorials/3d/procedural_geometry/immediatemesh)

## Methods
- clear_surfaces()
- surface_add_vertex(Vector3)
- surface_add_vertex_2d(Vector2)
- surface_begin(PrimitiveType, Material=null)
- surface_end()
- surface_set_color(Color)
- surface_set_normal(Vector3)
- surface_set_tangent(Plane)
- surface_set_uv(Vector2)
- surface_set_uv2(Vector2)

## Method Descriptions
- **clear_surfaces()**: Clear all surfaces
- **surface_add_vertex(Vector3)**: Add 3D vertex with current attributes
- **surface_add_vertex_2d(Vector2)**: Add 2D vertex with current attributes
- **surface_begin(PrimitiveType, Material=null)**: Start a new surface
- **surface_end()**: End and commit current surface
- **surface_set_color(Color)**: Set color attribute for next vertex
- **surface_set_normal(Vector3)**: Set normal attribute for next vertex
- **surface_set_tangent(Plane)**: Set tangent attribute for next vertex
- **surface_set_uv(Vector2)**: Set UV attribute for next vertex
- **surface_set_uv2(Vector2)**: Set UV2 attribute for next vertex