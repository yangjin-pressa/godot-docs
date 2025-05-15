# TriangleMesh

**Inherits:** RefCounted < Object

Triangle geometry for efficient, physicsless intersection queries.

## Description

Creates a bounding volume hierarchy (BVH) tree structure around triangle geometry.  
The triangle BVH tree can be used for efficient intersection queries without involving a physics engine.  
For example, this can be used in editor tools to select objects with complex shapes based on the mouse cursor position.

**Performance:** Creating the BVH tree for complex geometry is a slow process and best done in a background thread.

## Methods

- **create_from_faces** (faces: PackedVector3Array): Returns `true` if the tree is successfully built, `false` otherwise.
- **get_faces** (): Returns a copy of the geometry faces.
- **intersect_ray** (begin: Vector3, dir: Vector3): Returns a Dictionary with intersection details if a triangle is intersected.
- **intersect_segment** (begin: Vector3, end: Vector3): Returns a Dictionary with intersection details if a triangle is intersected.

## Method Descriptions

### create_from_faces
Creates the BVH tree from an array of faces. Each 3 vertices of the input `faces` array represent one triangle (face).

### get_faces
Returns a copy of the geometry faces. Each 3 vertices of the array represent one triangle (face).

### intersect_ray
Tests for intersection with a ray starting at `begin` and facing `dir` and extending toward infinity.  
Returns a Dictionary with the following fields if an intersection happens:
- `position`: The position on the intersected triangle.
- `normal`: The normal of the intersected triangle.
- `face_index`: The index of the intersected triangle.

### intersect_segment
Tests for intersection with a segment going from `begin` to `end`.  
Returns a Dictionary with the following fields if an intersection happens:
- `position`: The position on the intersected triangle.
- `normal`: The normal of the intersected triangle.
- `face_index`: The index of the intersected triangle.