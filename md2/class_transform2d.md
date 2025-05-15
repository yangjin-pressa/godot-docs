### Transform2D Class Overview

The `Transform2D` class in Godot is used to represent 2D transformations, combining translation, rotation, and scaling. It is commonly used in 2D games and applications to manipulate the position, orientation, and scale of objects. The class provides a variety of methods for applying transformations and operators for efficient matrix operations.

---

### **Methods**

#### **1. Translating**
- **`translated(offset: Vector2) -> Transform2D`**  
  Translates the transform by the given offset. This modifies the origin of the transform, effectively moving the object in the global coordinate system.

- **`translated_local(offset: Vector2) -> Transform2D`**  
  Translates the transform by the given offset relative to the local coordinate system. This is useful when working with local transformations, such as in a parent-child hierarchy.

#### **2. Rotating**
- **`rotated(angle: float) -> Transform2D`**  
  Rotates the transform by the given angle (in radians). This changes the rotation component of the transform.

- **`rotated_local(angle: float) -> Transform2D`**  
  Rotates the transform by the given angle around the local origin. This is useful for rotating an object relative to its local coordinate system.

#### **3. Scaling**
- **`scaled(scale: Vector2) -> Transform2D`**  
  Scales the transform by the given scale factor. This modifies the x and y components of the transform, affecting the size of the object.

- **`scaled_local(scale: Vector2) -> Transform2D`**  
  Scales the transform by the given scale factor relative to the local coordinate system. This is useful for scaling an object relative to its local origin.

#### **4. Getting Components**
- **`get_x() -> Vector2`**  
  Returns the x-axis vector of the transform, representing the direction of the x-axis in the local coordinate system.

- **`get_y() -> Vector2`**  
  Returns the y-axis vector of the transform, representing the direction of the y-axis in the local coordinate system.

- **`get_origin() -> Vector2`**  
  Returns the origin (translation) of the transform, which is the point of rotation and scaling.

#### **5. Matrix Operations**
- **`get_matrix() -> Matrix3`**  
  Returns the transformation matrix as a `Matrix3`, which can be used for low-level matrix operations or passed to shaders.

---

### **Operators**

#### **1. Comparison Operators**
- **`operator != (right: Transform2D) -> bool`**  
  Checks if the current transform is not equal to the right transform. Uses exact equality, which is less reliable due to floating-point errors. Use `is_equal_approx()` for more accurate comparisons.

- **`operator == (right: Transform2D) -> bool`**  
  Checks if the current transform is exactly equal to the right transform. Similar to `!=`, this is less reliable for floating-point values. Use `is_equal_approx()` instead.

#### **2. Matrix Multiplication**
- **`operator * (right: Transform2D) -> Transform2D`**  
  Multiplies the current transform by the right transform. This combines the transformations of the two transforms, commonly used in parent-child node hierarchies.

- **`operator * (right: Vector2) -> Vector2`**  
  Applies the current transform to the given vector, transforming it from the local coordinate system to the global one.

- **`operator * (right: PackedVector2Array) -> PackedVector2Array`**  
  Transforms all vectors in the `PackedVector2Array` using the current transform. This is efficient for large datasets, as it avoids iterating over each vector individually.

#### **3. Uniform Scaling**
- **`operator * (right: float) -> Transform2D`**  
  Scales all components of the transform uniformly by the given float. This affects the x, y, and origin components of the transform.

- **`operator * (right: int) -> Transform2D`**  
  Scales all components of the transform uniformly by the given integer.

#### **4. Scaling Down**
- **`operator / (right: float) -> Transform2D`**  
  Scales all components of the transform uniformly by the reciprocal of the given float. This effectively shrinks the transform.

- **`operator / (right: int) -> Transform2D`**  
  Scales all components of the transform uniformly by the reciprocal of the given integer.

#### **5. Accessing Axes**
- **`operator [] (index: int) -> Vector2`**  
  Accesses the columns of the transformation matrix. Index `0` corresponds to the x-axis, `1` to the y-axis, and `2` to the origin.

---

### **Key Notes**
- **Floating-Point Precision:** Comparisons like `==` and `!=` should be avoided for transforms due to floating-point errors. Use `is_equal_approx()` for reliable equality checks.
- **Local vs. Global Transformations:** Methods like `translated_local()` and `rotated_local()` apply changes relative to the local coordinate system, while their non-local counterparts affect the global system.
- **Efficiency:** Operators like `*` with `PackedVector2Array` are optimized for performance, making them ideal for large-scale transformations.

---

### **Example Usage**
```gdscript
var t = Transform2D.new()
t.origin = Vector2(100, 200)
t.x = Vector2(1, 0)
t.y = Vector2(0, 1)

# Translate globally
t = t.translated(Vector2(50, 50))

# Rotate locally
t = t.rotated_local(Math.PI / 4)

# Scale uniformly
t = t * 2.0

# Apply to a vector
var pos = Vector2(0, 0)
pos = t * pos

# Check equality with tolerance
if t.is_equal_approx(Transform2D.new()): 
    print("Transforms are approximately equal")
```

This class is essential for handling complex 2D transformations efficiently, especially in game development scenarios where objects need to be positioned, rotated, and scaled dynamically.