The AABB (Axis-Aligned Bounding Box) class in Godot provides a set of methods and operators for handling 3D spatial relationships and transformations. Below is a structured documentation of these methods and operators:

---

### **Methods**

#### **1. `intersection(aabb)`**
- **Purpose**: Computes the overlapping region between this AABB and another.
- **Parameters**: `aabb` (AABB to intersect with).
- **Returns**: A new AABB representing the intersection, or an empty AABB if no overlap.
- **Note**: Returns a flat AABB if the boxes intersect at their edges.

#### **2. `intersects(aabb)`**
- **Purpose**: Checks if this AABB overlaps with another.
- **Parameters**: `aabb` (AABB to check against).
- **Returns**: `true` if the boxes overlap, `false` otherwise.
- **Note**: Edges of both boxes are excluded from the intersection check.

#### **3. `merge(aabb)`**
- **Purpose**: Combines this AABB with another to create a larger AABB enclosing both.
- **Parameters**: `aabb` (AABB to merge with).
- **Returns**: A new AABB enclosing both.

#### **4. `is_equal_approx(aabb)`**
- **Purpose**: Checks if this AABB and another are approximately equal, considering floating-point tolerance.
- **Parameters**: `aabb` (AABB to compare with).
- **Returns**: `true` if positions and sizes are approximately equal.

#### **5. `is_finite()`**
- **Purpose**: Validates if all values in the AABB are finite (no infinities or NaNs).
- **Returns**: `true` if position and size are finite.

#### **6. `encloses(aabb)`**
- **Purpose**: Checks if another AABB is entirely inside this one.
- **Parameters**: `aabb` (AABB to check).
- **Returns**: `true` if the input AABB is fully contained.

#### **7. `intersects_plane(plane)`**
- **Purpose**: Checks if the AABB is on both sides of a given plane.
- **Parameters**: `plane` (Plane to check against).
- **Returns**: `true` if the AABB spans the plane.

#### **8. `intersects_ray(from, dir)`**
- **Purpose**: Finds the first intersection point between this AABB and a ray.
- **Parameters**: `from` (Ray origin), `dir` (Ray direction).
- **Returns**: Intersection point as `Vector3`, or `null` if no intersection.

#### **9. `intersects_segment(from, to)`**
- **Purpose**: Finds the first intersection point between this AABB and a line segment.
- **Parameters**: `from` (Segment start), `to` (Segment end).
- **Returns**: Intersection point as `Vector3`, or `null` if no intersection.

#### **10. `grow(delta)`**
- **Purpose**: Expands this AABB by a given delta in all directions.
- **Parameters**: `delta` (Vector3 to expand by).
- **Returns**: A new AABB with expanded bounds.

#### **11. `clamp(aabb)`**
- **Purpose**: Clips this AABB to another, returning the overlapping region.
- **Parameters**: `aabb` (AABB to clip against).
- **Returns**: A new AABB representing the clipped region.

---

### **Operators**

#### **1. `operator != (aabb)`**
- **Purpose**: Compares this AABB to another for inequality.
- **Parameters**: `aabb` (AABB to compare).
- **Returns**: `true` if positions or sizes differ.

#### **2. `operator == (aabb)`**
- **Purpose**: Compares this AABB to another for exact equality.
- **Parameters**: `aabb` (AABB to compare).
- **Returns**: `true` if positions and sizes are exactly equal.

#### **3. `operator * (transform)`**
- **Purpose**: Applies a transformation (e.g., rotation, scaling) to this AABB.
- **Parameters**: `transform` (Transform3D to apply).
- **Returns**: A new AABB after transformation.
- **Note**: Assumes the transform is applied to the AABB’s center, with orientation preserved.

---

### **Key Notes**
- **Floating-Point Tolerance**: Use `is_equal_approx` for comparisons to avoid precision issues.
- **Transform Handling**: The `operator *` with `Transform3D` is ideal for applying transformations to the AABB’s center while maintaining axis alignment.
- **Edge Cases**: Methods like `intersects` and `intersection` handle edge cases differently, so choose based on the desired behavior.

---

This documentation provides a clear reference for working with AABBs in Godot, covering spatial queries, transformations, and comparisons.