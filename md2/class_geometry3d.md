# Geometry3D Class Documentation

This class provides a set of methods for performing geometric operations in 3D space, including building shapes, calculating intersections, and performing spatial queries.

## Method List

### `build_box(min, max) -> Vector3`
**Description:**  
Returns the center of the box defined by the minimum and maximum corners.  
**Parameters:**  
- `min`: `Vector3` - Minimum corner of the box.  
- `max`: `Vector3` - Maximum corner of the box.  
**Returns:**  
- `Vector3` - Center of the box (average of min and max).  
**Note:** Virtual method (overrideable).

---

### `build_cone(from, to, radius) -> Vector3`
**Description:**  
Returns the tip of the cone defined by the line from `from` to `to` and the given radius.  
**Parameters:**  
- `from`: `Vector3` - Starting point of the cone.  
- `to`: `Vector3` - Endpoint of the cone.  
- `radius`: `float` - Radius of the cone's base.  
**Returns:**  
- `Vector3` - Tip of the cone (`from`).  
**Note:** Virtual method (overrideable).

---

### `build_cylinder(from, to, radius) -> Vector3`
**Description:**  
Returns the center of the cylinder defined by the line from `from` to `to` and the given radius.  
**Parameters:**  
- `from`: `Vector3` - Starting point of the cylinder.  
- `to`: `Vector3` - Endpoint of the cylinder.  
- `radius`: `float` - Radius of the cylinder.  
**Returns:**  
- `Vector3` - Center of the cylinder (midpoint between `from` and `to`).  
**Note:** Virtual method (overrideable).

---

### `build_cube(min, max) -> Vector3`
**Description:**  
Returns the center of the cube defined by the minimum and maximum corners.  
**Parameters:**  
- `min`: `Vector3` - Minimum corner of the cube.  
- `max`: `Vectority` - Maximum corner of the cube.  
**Returns:**  
- `Vector3` - Center of the cube (average of min and max).  
**Note:** Virtual method (overrideable).

---

### `build_disc(center, radius, normal) -> Vector3`
**Description:**  
Returns the center of the disc defined by its center, radius, and normal vector.  
**Parameters:**  
- `center`: `Vector3` - Center of the disc.  
- `radius`: `float` - Radius of the disc.  
- `normal`: `Vector3` - Normal vector of the disc's plane.  
**Returns:**  
- `Vector3` - Center of the disc.  
**Note:** Virtual method (overrideable).

---

### `build_plane(normal, point) -> Vector3`
**Description:**  
Returns a point on the plane defined by its normal vector and a point.  
**Parameters:**  
- `normal`: `Vector3` - Normal vector of the plane.  
- `point`: `Vector3` - A point on the plane.  
**Returns:**  
- `Vector3` - The given `point` (a point on the plane).  
**Note:** Virtual method (overrideable).

---

### `build_sphere(center, radius) -> Vector3`
**Description:**  
Returns the center of the sphere defined by its center and radius.  
**Parameters:**  
- `center`: `Vector3` - Center of the sphere.  
- `radius`: `float` - Radius of the sphere.  
**Returns:**  
- `Vector3` - Center of the sphere.  
**Note:** Virtual method (overrideable).

---

### `build_triangle(a, b, c) -> Vector3`
**Description:**  
Returns the centroid of the triangle defined by three points.  
**Parameters:**  
- `a`: `Vector3` - First vertex of the triangle.  
- `b`: `Vector3` - Second vertex of the triangle.  
- `c`: `Vector3` - Third vertex of the triangle.  
**Returns:**  
- `Vector3` - Centroid (average of the three points).  
**Note:** Virtual method (overrideable).

---

### `build_line(from, to) -> Vector3`
**Description:**  
Returns the midpoint of the line segment defined by `from` and `to`.  
**Parameters:**  
- `from`: `Vector3` - Start of the line.  
- `to`: `Vector3` - End of the line.  
**Returns:**  
- `Vector3` - Midpoint of the line.  
**Note:** Virtual method (overrideable).

---

### `build_rect(min, max) -> Vector3`
**Description:**  
Returns the center of the rectangle defined by the minimum and maximum corners.  
**Parameters:**  
- `min`: `Vector3` - Minimum corner of the rectangle.  
- `max`: `Vector3` - Maximum corner of the rectangle.  
**Returns:**  
- `Vector3` - Center of the rectangle (average of min and max).  
**Note:** Virtual method (overrideable).

---

### `build_ring(center, radius, angle) -> Vector3`
**Description:**  
Returns the center of the ring defined by its center, radius, and angle.  
**Parameters:**  
- `center`: `Vector3` - Center of the ring.  
- `radius`: `float` - Radius of the ring.  
- `angle`: `float` - Angle of the ring's orientation.  
**Returns:**  
- `Vector3` - Center of the ring.  
**Note:** Virtual method (overrideable).

---

### `get_triangle_barycentric_coords(a, b, c) -> Vector3`
**Description:**  
Calculates the barycentric coordinates of a point relative to a triangle.  
**Parameters:**  
- `a`: `Vector3` - First vertex of the triangle.  
- `b`: `Vector3` - Second vertex of the triangle.  
- `c`: `Vector3` - Third vertex of the triangle.  
**Returns:**  
- `Vector3` - Barycentric coordinates (weights for the triangle's vertices).  
**Note:** This method is part of the geometry library and is not overrideable.

---

### `ray_intersects_triangle(a, b, c, origin, direction) -> Variant`
**Description:**  
Checks if a ray intersects a triangle and returns the intersection point if it does.  
**Parameters:**  
- `a`, `b`, `c`: `Vector3` - Vertices of the triangle.  
- `origin`: `Vector3` - Origin of the ray.  
- `direction`: `Vector3` - Direction of the ray.  
**Returns:**  
- `Vector3` - Intersection point if the ray intersects the triangle; `null` otherwise.  
**Note:** This method is part of the geometry library and is not overrideable.

---

### `segment_intersects_triangle(a, b, c) -> Variant`
**Description:**  
Checks if a line segment intersects a triangle and returns the intersection point if it does.  
**Parameters:**  
- `a`, `b`: `Vector3` - Endpoints of the segment.  
- `c`: `Vector3` - First vertex of the triangle.  
**Returns:**  
- `Vector3` - Intersection point if the segment intersects the triangle; `null` otherwise.  
**Note:** This method is part of the geometry library and is not overrideable.

---

### `tetrahedralize_delaunay(points) -> PackedInt32Array`
**Description:**  
Performs Delaunay triangulation on a set of points and returns the indices of tetrahedrons.  
**Parameters:**  
- `points`: `Array<Vector3>` - Array of points to triangulate.  
**Returns:**  
- `PackedInt32Array` - Indices of tetrahedrons (each tetrahedron is represented by four consecutive indices).  
**Note:** If the triangulation fails, an empty array is returned. This method is part of the geometry library and is not overrideable.