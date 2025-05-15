Here's a comprehensive overview of the `Vector4` class methods and operators, organized by functionality:

---

### **Vector Arithmetic Operations**
**Purpose:** Perform component-wise operations on vectors.

1. **`operator + (other: Vector4) -> Vector4`**  
   Adds two vectors.  
   **Example:** `v1 + v2` → Returns a new vector where each component is the sum of corresponding components.

2. **`operator - (other: Vector4) -> Vector4`**  
   Subtracts one vector from another.  
   **Example:** `v1 - v2` → Returns a new vector where each component is the difference between corresponding components.

3. **`operator * (scalar: float) -> Vector4`**  
   Multiplies a vector by a scalar.  
   **Example:** `v * 2.0` → Scales each component by 2.0.

4. **`operator / (scalar: float) -> Vector4`**  
   Divides a vector by a scalar.  
   **Example:** `v / 2.0` → Returns a new vector with each component halved.

5. **`operator * (other: Vector4) -> Vector4`**  
   Component-wise multiplication.  
   **Example:** `v1 * v2` → Each component is the product of corresponding components.

6. **`operator / (other: Vector4) -> Vector4`**  
   Component-wise division.  
   **Example:** `v1 / v2` → Each component is the division of corresponding components.

---

### **Vector Comparison Operators**
**Purpose:** Compare vectors lexicographically (component-wise).

1. **`operator < (other: Vector4) -> bool`**  
   Compares vectors in order of x, y, z, w.  
   **Example:** `v1 < v2` → Returns `true` if all components of `v1` are less than those of `v2`.

2. **`operator <= (other: Vector4) -> bool`**  
   Compares vectors with lexicographical ordering.  
   **Example:** `v1 <= v2` → Returns `true` if `v1` is less than or equal to `v2`.

3. **`operator > (other: Vectority) -> bool`**  
   Compares vectors in order of x, y, z, w.  
   **Example:** `v1 > v2` → Returns `true` if all components of `v1` are greater than those of `v2`.

4. **`operator >= (other: Vector4) -> bool`**  
   Compares vectors with lexicographical ordering.  
   **Example:** `v1 >= v2` → Returns `true` if `v1` is greater than or equal to `v2`.

5. **`operator == (other: Vector4) -> bool`**  
   Checks if all components are exactly equal.  
   **Note:** Use `is_equal_approx` for tolerance-based comparisons.

6. **`operator != (other: Vector4) -> bool`**  
   Checks if vectors are not exactly equal.

---

### **Vector Utility Methods**
**Purpose:** Compute properties or transformations of vectors.

1. **`dot(other: Vector4) -> float`**  
   Computes the dot product.  
   **Example:** `v1.dot(v2)` → Returns the sum of the products of corresponding components.

2. **`cross(other: Vector4) -> Vector4`**  
   Computes the cross product.  
   **Example:** `v1.cross(v2)` → Returns a vector perpendicular to both `v1` and `v2`.

3. **`length() -> float`**  
   Returns the Euclidean length of the vector.  
   **Example:** `v.length()` → Calculates `sqrt(x² + y² + z² + w²)`.

4. **`length_squared() -> float`**  
   Returns the squared length (avoiding the square root for efficiency).  
   **Example:** `v.length_squared()` → Computes `x² + y² + z² + w²`.

5. **`normalize() -> Vector4`**  
   Returns a normalized (unit) vector.  
   **Example:** `v.normalize()` → Returns `v / v.length()`.

6. **`normalize_in_place() -> Vector4`**  
   Normalizes the vector in place.  
   **Example:** `v.normalize_in_place()` → Modifies `v` to be a unit vector.

7. **`lerp(other: Vector4, alpha: float) -> Vector4`**  
   Linear interpolation between two vectors.  
   **Example:** `v1.lerp(v2, 0.5)` → Returns a vector halfway between `v1` and `v2`.

8. **`clamp(min: Vector4, max: Vector4) -> Vector4`**  
   Clamps each component between `min` and `max`.  
   **Example:** `v.clamp(Vector4(0, 0, 0, 0), Vector4(1, 1, 1, 1))` → Limits components to [0, 1].

9. **`reflect(normal: Vector4) -> Vector4`**  
   Computes the reflection of the vector over a plane with normal `normal`.  
   **Example:** `v.reflect(normal)` → Used in physics or lighting calculations.

---

### **Component Access**
**Purpose:** Access individual components of the vector.

1. **`operator [] (index: int) -> float`**  
   Accesses components by index (0 = x, 1 = y, 2 = z, 3 = w).  
   **Example:** `v[0]` → Returns `v.x`.

2. **`x, y, z, w -> float`**  
   Direct access to individual components.  
   **Example:** `v.x` → Returns the x-component.

---

### **Unary Operators**
**Purpose:** Modify the vector's sign or value.

1. **`operator unary+ () -> Vector4`**  
   Returns the vector as-is.  
   **Example:** `+v` → Same as `v`.

2. **`operator unary- () -> Vector4`**  
   Returns the vector negated.  
   **Example:** `-v` → Returns `(-v.x, -v.y, -v.z, -v.w)`.

---

### **Important Notes**
- **NaN Handling:** Vectors containing `NaN` (Not a Number) may produce unexpected results in comparisons or operations. Use `is_equal_approx` for tolerance-based checks.
- **Precision:** Methods like `==` are strict and may fail for floating-point imprecision. Use `is_equal_approx` for comparisons.
- **Normalization:** `normalize()` returns a new vector, while `normalize_in_place()` modifies the original.
- **Lexicographical Order:** Comparison operators compare components in order (x → y → z → w).

---

This structure ensures clarity for developers working with vector mathematics in GDScript, emphasizing both low-level operations and high-level utility functions.