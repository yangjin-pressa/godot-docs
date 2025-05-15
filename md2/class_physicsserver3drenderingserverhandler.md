# PhysicsServer3DRenderingServerHandler

**Inherits:** Object

A class used to provide `PhysicsServer3DExtension._soft_body_update_rendering_server()` with a rendering handler for soft bodies.

## Methods

- **_set_aabb(AABB)** (virtual)  
  Called by PhysicsServer3D to set the bounding box for SoftBody3D.

- **_set_normal(vertex_id: int, normal: Vector3)** (virtual)  
  Called by PhysicsServer3D to set the normal for SoftBody3D vertex at `vertex_id`.  
  **Note:** The `normal` parameter used to be of type `const void*` prior to Godot 4.2.

- **_set_vertex(vertex_id: int, vertex: Vector3)** (virtual)  
  Called by PhysicsServer3D to set the position for SoftBody3D vertex at `vertex_id`.  
  **Note:** The `vertex` parameter used to be of type `const void*` prior to Godot 4.2.

- **set_aabb(AABB)**  
  Sets the bounding box for SoftBody3D.

- **set_normal(vertex_id: int, normal: Vector3)**  
  Sets the normal for SoftBody3D vertex at `vertex_id`.

- **set_vertex(vertex_id: int, vertex: Vector3)**  
  Sets the position for SoftBody3D vertex at `vertex_id`.