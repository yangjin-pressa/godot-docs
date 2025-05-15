# Quaternion Class Documentation

## Overview

The `Quaternion` class represents a 4-dimensional vector used to describe rotations in 3D space. It supports operations such as rotation, normalization, inversion, and various mathematical operations with other quaternions, vectors, and scalars.

---

## Constructors

### `Quaternion(float x, float y, float z, float w)`
**Description**: Constructs a new Quaternion with specified components.
- **Parameters**:
  - `x`: X component of the quaternion.
  - `y`: Y component of the quaternion.
  - `z`: Z component of the quaternion.
  - `w`: W component of the quaternion.

---

## Methods

### `angle() const`
**Description**: Returns the angle of the quaternion in radians.
- **Return Value**: Angle of rotation in radians.

### `axis() const`
**Description**: Returns the axis of rotation as a `Vector3`.
- **Return Value**: The axis of rotation represented as a `Vector3`.

### `dot(const Quaternion& other) const`
**Description**: Computes the dot product between this quaternion and another.
- **Parameters**:
  - `other`: The quaternion to compute the dot product with.
- **Return Value**: The dot product result as a float.

### `identity() const`
**Description**: Returns the identity quaternion, which represents no rotation.
- **Return Value**: A `Quaternion` with values (1, 0, 0, 0).

### `invert() const`
**Description**: Returns the inverse of the quaternion, which is useful for undoing a rotation.
- **Return Value**: The inverted quaternion.

### `normalize() const`
**Description**: Normalizes the quaternion to have a length of 1.
- **Return Value**: A normalized `Quaternion`.

---

## Operators

### `!= (const Quaternion& right) const`
**Description**: Returns `true` if the components of both quaternions are not exactly equal.
- **Note**: Due to floating-point precision errors, consider using `is_equal_approx()` instead.

### `== (const Quaternion& right) const`
**Description**: Returns `true` if the components of both quaternions are exactly equal.
- **Note**: Due to floating-point precision errors, consider using `is_equal_approx()` instead.

### `+ (const Quaternion& right) const`
**Description**: Adds each component of the left quaternion to the right quaternion.
- **Note**: This operation is not meaningful on its own but can be used in larger expressions.

### `- (const Quaternion& right) const`
**Description**: Subtracts each component of the left quaternion by the right quaternion.
- **Note**: This operation is not meaningful on its own but can be used in larger expressions.

### `* (const Quaternion& right) const`
**Description**: Composes (multiplies) two quaternions. This rotates the `right` quaternion by this quaternion.
- **Note**: This is a quaternion multiplication operation.

### `* (const Vector3& right) const`
**Description**: Rotates the `right` vector by this quaternion, returning a `Vector3`.
- **Example**: `quat * vec` rotates the vector.

### `* (float right) const`
**Description**: Multiplies each component of the quaternion by the right float value.
- **Note**: This operation is not meaningful on its own but can be used in larger expressions.

### `* (int right) const`
**Description**: Multiplies each component of the quaternion by the right int value.
- **Note**: This operation is not meaningful on its own but can be used in larger expressions.

### `/ (float right) const`
**Description**: Divides each component of the quaternion by the right float value.
- **Note**: This operation is not meaningful on its own but can be used in larger expressions.

### `/ (int right) const`
**Description**: Divides each component of the quaternion by the right int value.
- **Note**: This operation is not meaningful on its own but can be used in larger expressions.

### `[] (int index) const`
**Description**: Accesses each component of the quaternion by index.
- **Indices**:
  - `0`: X component
  - `1`: Y component
  - `2`: Z component
  - `3`: W component

---

## Notes

- **Normalization**: The `normalize()` method ensures the quaternion is a unit vector, which is essential for accurate rotation calculations.
- **Inversion**: The `invert()` method is critical for undoing a rotation represented by a quaternion.
- **Identity Quaternion**: The identity quaternion `(1, 0, 0, 0)` represents no rotation and is often used as a reference in transformations.
- **Precision**: For comparisons, use `is_equal_approx()` instead of `==` or `!=` to handle floating-point precision issues.

---

## Example Usage

```cpp
Quaternion quat(1.0f, 0.0f, 0.0f, 0.0f); // Identity quaternion
Vector3 vec(1.0f, 0.0f, 0.0f);
Vector3 rotated = quat * vec; // Rotate the vector
```

This documentation provides a comprehensive reference for working with quaternions, including their mathematical properties and practical applications in 3D rotations.