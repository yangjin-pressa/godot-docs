Here's a structured explanation of the Vector2 class and its methods/operators, organized for clarity and practical use in GDScript:

---

### **Key Concepts**
- **Vector2** represents a 2D vector with x and y components.
- Methods and operators allow vector arithmetic, comparisons, and transformations.
- **NaN (Not a Number)** handling is critical for floating-point operations.

---

### **Core Methods**
1. **`pos` (property)**  
   - **Purpose**: Returns the current position (x, y).  
   - **Usage**: `v.pos` gives the vector's coordinates.  
   - **Example**: `print(v.pos)` outputs `(x, y)`.

2. **`x` and `y` (accessors)**  
   - **Purpose**: Direct access to individual components.  
   - **Usage**: `v.x` for x-component, `v.y` for y-component.  
   - **Example**: `v.x = 10` sets the x-coordinate.

3. **`normalize()`**  
   - **Purpose**: Returns a unit vector (length = 1).  
   - **Usage**: `v.normalized = v.normalize()`  
   - **Example**: Use for directional movement.

4. **`dot_product(other: Vector2) -> float`**  
   - **Purpose**: Calculates the dot product with another vector.  
   - **Usage**: `v.dot_product(w)` computes `v.x*w.x + v.y*w.y`.

5. **`length_squared()`**  
   - **Purpose**: Returns squared length (avoid sqrt for performance).  
   - **Usage**: `v.length_squared` for faster distance calculations.

6. **`distance_to(other: Vector2) -> float`**  
   - **Purpose**: Computes distance between two points.  
   - **Usage**: `v.distance_to(w)` gives the Euclidean distance.

7. **`angle_to(other: Vector2) -> float`**  
   - **Purpose**: Returns the angle (in radians) between two vectors.  
   - **Usage**: `v.angle_to(w)` for rotation calculations.

8. **`rotate(angle: float) -> Vector2`**  
   - **Purpose**: Rotates the vector by a given angle.  
   - **Usage**: `v.rotate(Math.PI/2)` rotates 90 degrees.

9. **`set_pos(pos: Vector2)`**  
   - **Purpose**: Sets the vector's position.  
   - **Usage**: `v.set_pos(Vector2(10, 20))`.

10. **`set_rot(angle: float)`**  
    - **Purpose**: Sets the rotation angle.  
    - **Usage**: `v.set_rot(Math.PI/4)` for 45-degree rotation.

---

### **Operators**
1. **Arithmetic Operators**  
   - **`+`**: Vector addition.  
     ```gdscript
     v1 + v2  # (x1+x2, y1+y2)
     ```
   - **`-`**: Vector subtraction.  
     ```gdscript
     v1 - v2  # (x1-x2, y1-y2)
     ```
   - **`*`**: Scalar multiplication.  
     ```gdscript
     v * 2    # (2x, 2y)
     ```
   - **`/`**: Scalar division.  
     ```gdscript
     v / 2    # (x/2, y/2)
     ```

2. **Comparison Operators**  
   - **`==`**: Exact equality (not reliable for floats).  
     ```gdscript
     v == w   # True if x and y are exactly equal
     ```
   - **`!=`**: Inequality.  
     ```gdscript
     v != w   # True if x or y differ
     ```
   - **`<` / `>`**: Lexicographical comparison (x first, then y).  
     ```gdscript
     v < w    # True if x < w.x, or x == w.x and y < w.y
     ```

3. **Index Operator**  
   - **`[]`**: Accesses individual components.  
     ```gdscript
     v[0]  # x
     v[1]  # y
     ```
   - **Example**:  
     ```gdscript
     v[0] = 5  # Sets x to 5
     ```

4. **Unary Operators**  
   - **`+`**: No effect, but useful for readability.  
     ```gdscript
     v = -v  # Negates the vector
     ```
   - **`-`**: Negates the vector.  
     ```gdscript
     v = -v  # Equivalent to Vector2(-v.x, -v.y)
     ```

---

### **Important Notes**
- **NaNs**: Vectors with `NaN` values (e.g., `Vector2(NAN, NAN)`) can cause unexpected results in comparisons or calculations. Use `is_equal_approx()` for safe equality checks.
- **Precision**: Direct equality (`==`) is unreliable for floating-point vectors. Use `is_equal_approx()` for tolerance-based comparisons.
- **Normalization**: `normalize()` is essential for directional vectors, but avoid using it in performance-critical paths.

---

### **Example Use Cases**
1. **Movement**  
   ```gdscript
   var direction = Vector2(1, 0).normalize()
   var speed = 5
   var velocity = direction * speed
   ```

2. **Distance Calculation**  
   ```gdscript
   var distance = v.distance_to(w)
   if distance < 10:
       print("Close enough!")
   ```

3. **Rotation**  
   ```gdscript
   var angle = Math.atan2(w.y, w.x)  # Angle of vector w
   var rotated = v.rotate(angle)
   ```

4. **Vector Comparison**  
   ```gdscript
   if v.is_equal_approx(w):
       print("Vectors are approximately equal")
   ```

---

This documentation provides a comprehensive guide to working with vectors in GDScript, covering both basic operations and advanced techniques. Always prioritize `is_equal_approx()` for floating-point comparisons to avoid precision issues.