The `Rect2` class in Godot is a fundamental data structure used to represent a rectangle in 2D space. It contains properties for position and size, and provides various methods for geometric operations such as checking intersections, containment, and transformations. Below is a structured breakdown of its key components:

---

### **1. Properties**
- **`position`**: A `Vector2` representing the top-left corner of the rectangle.
- **`size`**: A `Vector2` representing the width and height of the rectangle.

---

### **2. Methods**
#### **Geometric Operations**
- **`has_point(point: Vector2) -> bool`**  
  Checks if a given point lies within the rectangle. **Note**: Points on the edges are excluded by default. Use `abs()` first if the rectangle has negative size.

- **`intersection(rect: Rect2) -> Rect2`**  
  Returns the overlapping area between two rectangles. If they don't intersect, returns an empty `Rect2`.

- **`intersects(rect: Rect2, include_borders: bool = false) -> bool`**  
  Checks if two rectangles overlap. If `include_borders` is `true`, edges are considered overlapping.

- **`merge(rect: Rect2) -> Rect2`**  
  Returns a rectangle that encloses both the current rectangle and the input rectangle.

- **`is_equal_approx(rect: Rect2) -> bool`**  
  Checks if two rectangles are approximately equal, using `Vector2.is_equal_approx()` for position and size.

- **`has_area() -> bool`**  
  Returns `true` if the rectangle has positive width and height.

- **`is_finite() -> bool`**  
  Returns `true` if all rectangle values are finite (no infinities or NaNs).

#### **Transformations**
- **`operator * (transform: Transform2D) -> Rect2`**  
  Inversely transforms the rectangle using a `Transform2D` matrix. Assumes the basis is orthonormal (no scaling/skewing). Equivalent to `transform.inverse() * rect`.

- **`operator == (right: Rect2) -> bool`**  
  Checks if two rectangles have exactly the same position and size.

- **`operator != (right: Rect2) -> bool`**  
  Checks if two rectangles differ in position or size.

---

### **3. Operators**
- **Equality Comparisons**  
  - `==` and `!=` compare position and size exactly. For approximate comparisons, use `is_equal_approx()`.

- **Transformations**  
  Multiplication with `Transform2D` allows transforming the rectangle, but requires careful handling of transformations (e.g., avoiding scaling).

---

### **4. Key Considerations**
- **Negative Size**: Rectangles with negative size are invalid for most operations. Use `abs()` to normalize them before checking containment or intersections.
- **Floating-Point Precision**: Comparisons should use `is_equal_approx()` instead of exact equality to handle floating-point errors.
- **Edge Handling**: Methods like `has_point()` exclude edge points by default, but `intersects()` includes edges if `include_borders` is set.

---

### **Example Usage**
```gdscript
var rect1 = Rect2(0, 0, 5, 10)
var rect2 = Rect2(2, 0, 8, 4)

var intersection = rect1.intersection(rect2)  # Returns Rect2(2, 0, 3, 4)
var overlap = rect1.intersects(rect2)         # Returns true
```

This class is essential for 2D spatial calculations in games, such as collision detection, UI layout, and object positioning.