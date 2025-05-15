# Vector2i Class Documentation

## Class Overview

The `Vector2i` class represents a 2D vector with integer components. It provides a wide range of mathematical operations and utility functions for vector manipulation, including arithmetic operations, comparisons, normalization, interpolation, and component access.

---

## Member Functions

### 1. `clamp(min, max)`
**Description**: Clamps the vector to the range defined by `min` and `max`.
**Parameters**:
- `min`: Minimum value for clamping.
- `max`: Maximum value for clamping.
**Returns**: A new `Vector2i` within the range `[min, max]`.
**Example**:
```cpp
Vector2i v = Vector2i(10, 20).clamp(Vector2i(5, 10), Vector2i(15, 25));
// v = (10, 20)
```

### 2. `lerp(a, b, t)`
**Description**: Linearly interpolates between two vectors `a` and `b` using parameter `t`.
**Parameters**:
- `a`: Start vector.
- `b`: End vector.
- `t`: Interpolation factor (0 ≤ t ≤ 1).
**Returns**: A new `Vector2i` resulting from the interpolation.
**Example**:
```cpp
Vector2i v = Vector2i(0, 0).lerp(Vector2i(10, 20), 0.5);
// v = (5, 10)
```

### 3. `normalize()`
**Description**: Returns a normalized version of the vector (unit vector).
**Returns**: A new `Vector2i` with magnitude 1.
**Example**:
```cpp
Vector2i v = Vector2i(3, 4).normalize();
// v = (0.6, 0.8)
```

### 4. `operator+()`
**Description**: Adds two vectors together.
**Parameters**:
- `other`: Vector to add.
**Returns**: A new `Vector2i` with component-wise addition.
**Example**:
```cpp
Vector2i v = Vector2i(10, 20) + Vector2i(3, 4);
// v = (13, 24)
```

### 5. `operator-()`
**Description**: Subtracts one vector from another.
**Parameters**:
- `other`: Vector to subtract.
**Returns**: A new `Vector2i` with component-wise subtraction.
**Example**:
```cpp
Vector2i v = Vector2i(10, 20) - Vector2i(3, 4);
// v = (7, 16)
```

### 6. `operator*()`
**Description**: Multiplies the vector by a scalar or another vector.
**Parameters**:
- `scalar`: Scalar value.
- `other`: Vector to multiply.
**Returns**: A new `Vector2i` (or `Vector2` for scalar multiplication).
**Example**:
```cpp
Vector2i v = Vector2i(10, 20) * 2;
// v = (20, 40)
```

### 7. `operator/()`
**Description**: Divides the vector by a scalar or another vector.
**Parameters**:
- `scalar`: Scalar value.
- `other`: Vector to divide by.
**Returns**: A new `Vector2i` (or `Vector2` for scalar division).
**Example**:
```cpp
Vector2i v = Vector2i(10, 20) / 2;
// v = (5, 10)
```

### 8. `operator[]()`
**Description**: Accesses vector components via index.
**Parameters**:
- `index`: Index (0 for x, 1 for y).
**Returns**: The component value at the specified index.
**Example**:
```cpp
int x = v[0];
int y = v[1];
```

### 9. `operator unary+()`
**Description**: Returns the vector as-is (no effect).
**Example**:
```cpp
Vector2i v = +vector;
```

### 10. `operator unary-()`
**Description**: Returns the negative of the vector.
**Example**:
```cpp
Vector2i v = -vector;
```

---

## Operators

### 1. `operator<()`
**Description**: Compares two vectors lexicographically (x first, then y).
**Parameters**:
- `other`: Vector to compare.
**Returns**: `true` if this vector is less than `other`.
**Example**:
```cpp
bool result = v1 < v2;
```

### 2. `operator<=()`
**Description**: Compares two vectors lexicographically (x first, then y).
**Parameters**:
- `other`: Vector to compare.
**Returns**: `true` if this vector is less than or equal to `other`.
**Example**:
```cpp
bool result = v1 <= v2;
```

### 3. `operator>()`
**Description**: Compares two vectors lexicographically (x first, then y).
**Parameters**:
- `other`: Vector to compare.
**Returns**: `true` if this vector is greater than `other`.
**Example**:
```cpp
bool result = v1 > v2;
```

### 4. `operator>=()`
**Description**: Compares two vectors lexicographically (x first, then y).
**Parameters**:
- `other`: Vector to compare.
**Returns**: `true` if this vector is greater than or equal to `other`.
**Example**:
```cpp
bool result = v1 >= v2;
```

### 5. `operator==()`
**Description**: Compares two vectors for equality.
**Parameters**:
- `other`: Vector to compare.
**Returns**: `true` if both components are equal.
**Example**:
```cpp
bool result = v1 == v2;
```

### 6. `operator!=()`
**Description**: Compares two vectors for inequality.
**Parameters**:
- `other`: Vector to compare.
**Returns**: `true` if components are not equal.
**Example**:
```cpp
bool result = v1 != v2;
```

---

## Example Usage

### Arithmetic Operations
```cpp
Vector2i v1 = Vector2i(1, 2);
Vector2i v2 = Vector2i(3, 4);
Vector2i v3 = v1 + v2; // (4, 6)
Vector2i v4 = v1 * 2;  // (2, 4)
```

### Clamping
```cpp
Vector2i v = Vector2i(10, 20).clamp(Vector2i(5, 10), Vector2i(15, 25));
// v = (10, 20)
```

### Interpolation
```cpp
Vector2i v = Vector2i(0, 0).lerp(Vector2i(10, 20), 0.5);
// v = (5, 10)
```

### Normalization
```cpp
Vector2i v = Vector2i(3, 4).normalize();
// v = (0.6, 0.8)
```

---

## Notes
- All methods are `const` unless specified otherwise.
- The `operator[]` allows access to components via index (0 for x, 1 for y).
- Arithmetic and comparison operators return new instances of `Vector2i` or `Vector2` as needed.