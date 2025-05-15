# Plane Class Documentation

A 3D plane in Godot, represented by a normal vector and a distance from the origin. This class provides methods to calculate intersections, distances, and transformations.

## Overview

The `Plane` class represents a flat, infinite surface in 3D space. It's defined by a normal vector (`normal`) and a distance (`d`) from the origin to the plane. This class includes methods to calculate distances, check for point intersections, transform planes, and more.

---

## Properties

- **normal**: A `Vector3` representing the normal vector of the plane.
- **d**: A `float` representing the distance from the origin to the plane.
- **center**: A `Vector3` representing the center of the plane (calculated from the plane's equation).

---

## Methods

### `distance_to(point: Vector3) -> float`
Returns the shortest distance from the plane to the given point. Positive if the point is above the plane, negative if below.

**Example:**
```gdscript
var distance = plane.distance_to(Vector3(1, 0, 0))
```

---

### `get_center() -> Vector3`
Returns the center of the plane.

**Example:**
```gdscript
var center = plane.get_center()
```

---

### `has_point(point: Vector3, tolerance: float = 1e-05) -> bool`
Checks if a point is inside the plane within a given tolerance.

**Example:**
```gdscript
var in_plane = plane.has_point(Vector3(0, 0, 0), 0.001)
```

---

### `intersect_3(plane_b: Plane, plane_c: Plane) -> Variant`
Returns the intersection point of three planes (this, `plane_b`, and `plane_c`). Returns `null` if no intersection.

**Example:**
```gdscript
var intersection = plane.intersect_3(plane_b, plane_c)
```

---

### `intersects_ray(from: Vector3, dir: Vector3) -> Variant`
Returns the intersection point of a ray with this plane. Returns `null` if no intersection.

**Example:**
```gdscript
var ray_intersection = plane.intersects_ray(Vector3(0, 0, 0), Vector3(1, 0, 0))
```

---

### `intersects_segment(from: Vector3, to: Vector3) -> Variant`
Returns the intersection point of a segment with this plane. Returns `null` if no intersection.

**Example:**
```gdscript
var segment_intersection = plane.intersects_segment(Vector3(0, 0, 0), Vector3(1, 0, 0))
```

---

### `is_equal_approx(to_plane: Plane) -> bool`
Checks if this plane and `to_plane` are approximately equal, using a tolerance.

**Example:**
```gdscript
var equal = plane.is_equal_approx(to_plane)
```

---

### `is_finite() -> bool`
Checks if the plane is finite (all components are finite).

**Example:**
```gdscript
var is_finite = plane.is_finite()
```

---

### `is_point_over(point: Vector3) -> bool`
Checks if a point is located above the plane.

**Example:**
```gdscript
var above = plane.is_point_over(Vector3(0, 0, 0))
```

---

### `normalized() -> Plane`
Returns a copy of the plane with a normalized normal vector. Returns a zero plane if normalization fails.

**Example:**
```gdscript
var normalized_plane = plane.normalized()
```

---

### `project(point: Vector3) -> Vector3`
Returns the orthogonal projection of the point onto the plane.

**Example:**
```gdscript
var projection = plane.project(Vector3(1, 0, 0))
```

---

## Operators

### `!= (right: Plane) -> bool`
Returns `true` if the planes are not equal.

**Note:** Use `is_equal_approx()` for better precision due to floating-point errors.

### `* (right: Transform3D) -> Plane`
Inversely transforms the plane by the given transformation matrix.

**Example:**
```gdscript
var transformed_plane = plane * transform
```

### `== (right: Plane) -> bool`
Returns `true` if the planes are exactly equal.

**Note:** Use `is_equal_approx()` for better precision due to floating-point errors.

### `unary+ () -> Plane`
Returns the same plane (no change).

### `unary- () -> Plane`
Returns the negative of the plane (flips normal and distance).

**Example:**
```gdscript
var negated_plane = -plane
```

---

## Examples

### Transforming a Plane
```gdscript
var transform = Transform3D()
var transformed_plane = plane * transform
```

### Checking if a Point is on a Plane
```gdscript
var on_plane = plane.has_point(Vector3(0, 0, 0), 0.001)
```

### Projecting a Point
```gdscript
var projected_point = plane.project(Vector3(1, 0, 0))
```

---

## Notes
- The `distance_to()` method's sign depends on the plane's normal direction.
- For precision comparisons, use `is_equal_approx()` instead of `==`.
- The `normalized()` method ensures the normal vector is a unit vector.

This class is essential for 3D geometry operations, including collision detection, ray casting, and spatial transformations.