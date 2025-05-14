# Curve Class Documentation

## Overview
The `Curve` class represents a parametric curve defined by a series of points with associated tangent angles and modes. It provides methods to manipulate the curve's points, tangents, and properties, as well as utilities for sampling values along the curve.

---

## Properties
- **minDomain**: Minimum X value of the curve's domain.
- **maxDomain**: Maximum X value of the curve's domain.
- **minValue**: Minimum Y value of the curve's range.
- **maxValue**: Maximum Y value of the curve's range.

---

## Methods

### **Manipulating Points**
- **clearPoints()**: Removes all points from the curve.
- **removePoint(index)**: Removes the point at the specified index.
- **setPointValue(index, y)**: Sets the vertical position (`y`) of the point at the specified index.
- **setPointOffset(index, offset)**: Sets the offset of the point from `0.5`.

### **Point Attributes**
- **getPointPosition(index)**: Returns the (x, y) coordinates of the point at the specified index.
- **getPointLeftMode(index)**: Returns the left tangent mode for the point at the specified index.
- **getPointRightMode(index)**: Returns the right tangent mode for the point at the specified index.
- **getPointLeftTangent(index)**: Returns the left tangent angle (in degrees) for the point at the specified index.
- **getPointRightTangent(index)**: Returns the right tangent angle (in degrees) for the point at the specified index.
- **setPointLeftMode(index, mode)**: Sets the left tangent mode for the point at the specified index.
- **setPointRightMode(index, mode)**: Sets the right tangent mode for the point at the specified index.
- **setPointLeftTangent(index, tangent)**: Sets the left tangent angle for the point at the specified index.
- **setPointRightTangent(index, tangent)**: Sets the right tangent angle for the point at the specified index.

### **Curve Utilities**
- **bake()**: Recomputes the baked cache of points for the curve.
- **cleanDupes()**: Removes duplicate points (points within 0.00001 units of each other).
- **getDomainRange()**: Returns the difference between `minDomain` and `maxDomain`.
- **getValueRange()**: Returns the difference between `minValue` and `maxValue`.

### **Sampling**
- **sample(offset)**: Returns the Y value for the point at the X position `offset` along the curve.
- **sampleBaked(offset)**: Returns the Y value for the point at the X position `offset` using the baked cache. If the curve isn't baked, it will bake it first.

---

## Signals
- **curveChanged()**: Emitted when the curve's data is modified (e.g., points, tangents, or modes are changed).

---

## Notes
- **Tangent Modes**: 
  - `TANGENT_FREE`: Allows arbitrary tangent angles.
  - `TANGENT_LINEAR`: Uses the slope halfway to the adjacent point.
- **Baked Cache**: The `sampleBaked()` method uses a precomputed cache of points for faster sampling. Call `bake()` before using it if the curve hasn't been baked.
- **Offset**: The `setPointOffset()` method adjusts the horizontal position of a point relative to the curve's domain range.

---

## Example Usage
```cpp
Curve curve;
curve.addPoint(Vector2(0, 0));
curve.addPoint(Vector2(1, 1));
curve.setPointValue(0, 0.5);
curve.bake();
float yValue = curve.sample(0.5);
```

This documentation provides a comprehensive overview of the `Curve` class, enabling developers to manipulate and query curves efficiently.