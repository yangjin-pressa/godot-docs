# Godot Color Class Guide

This guide provides a comprehensive overview of the `Color` class in Godot, including its properties, methods, operators, and usage examples.

---

## **Properties**

### **r, g, b, a**
- **Type**: `float`
- **Description**: Individual color components (red, green, blue, alpha). Values range from 0 (none) to 1 (full intensity).

Example:
```gdscript
var c = Color(1, 0, 0, 1)  # Red color
print(c.r)  # Output: 1
print(c.g)  # Output: 0
```

### **hex**
- **Type**: `String`
- **Description**: Returns the color as a hexadecimal string in the format `RRGGBB` (or `RRGGBBAA` for alpha).

Example:
```gdscript
var c = Color(1, 0, 0, 1)
print(c.hex)  # Output: "ff0000ff"
```

---

## **Methods**

### **is_equal_approx(other: Color) → bool**
- **Description**: Checks if two colors are approximately equal, accounting for floating-point precision errors.
- **Parameters**: `other` — Another `Color` instance.
- **Return**: `true` if colors are close, `false` otherwise.

Example:
```gdscript
var c1 = Color(1, 0, 0, 1)
var c2 = Color(1, 0.0001, 0, 1)
print(c1.is_equal_approx(c2))  # Output: true
```

### **inverted() → Color**
- **Description**: Inverts all color components (r, g, b, a) to create a complementary color.
- **Return**: New `Color` instance with inverted values.

Example:
```gdscript
var c = Color(0.5, 0.5, 0.5, 1)
var inverted = c.inverted()
print(inverted.r)  # Output: 0.5
```

### **lightened(offset: float) → Color**
- **Description**: Lightens the color by adjusting each component by `offset` (0-1 range).
- **Parameters**: `offset` — Amount to lighten (0.0 = no change, 1.0 = maximum).

Example:
```gdscript
var c = Color(0, 0, 0, 1)
var lightened = c.lightened(0.5)
print(lightened)  # Output: (0.5, 0.5, 0.5, 1)
```

### **darkened(offset: float) → Color**
- **Description**: Darkens the color by adjusting each component by `offset` (0-1 range).
- **Parameters**: `offset` — Amount to darken (0.0 = no change, 1.0 = maximum).

Example:
```gdscript
var c = Color(1, 1, 1, 1)
var darkened = c.darkened(0.5)
print(darkened)  # Output: (0.5, 0.5, 0.5, 1)
```

### **to_rgba32() → int**
- **Description**: Converts the color to a 32-bit integer in RGBA format.
- **Return**: 32-bit integer representing the color.

Example:
```gdscript
var c = Color(1, 0, 0, 1)
print(c.to_rgba32())  # Output: 4294967040 (0xff0000ff in hex)
```

### **to_rgba64() → int**
- **Description**: Converts the color to a 64-bit integer in RGBA format.
- **Return**: 64-bit integer representing the color.

Example:
```gdscript
var c = Color(1, 0, 0, 1)
print(c.to_rgba64())  # Output: -140736629309441 (0xff0000ff in hex)
```

---

## **Operators**

### **!= (right: Color) → bool**
- **Description**: Checks if two colors are not exactly equal.
- **Return**: `true` if colors differ, `false` otherwise.

Example:
```gdscript
var c1 = Color(1, 0, 0, 1)
var c2 = Color(1, 0.0001, 0, 1)
print(c1 != c2)  # Output: true (due to precision)
```

### *** (right: Color) → Color**
- **Description**: Multiplies each component of the color by the components of the given color.
- **Parameters**: `right` — Another `Color` instance.

Example:
```gdscript
var c1 = Color(1, 0, 0, 1)
var c2 = Color(0.5, 0.5, 0.5, 1)
var result = c1 * c2
print(result)  # Output: (0.5, 0, 0, 1)
```

### *** (right: float) → Color**
- **Description**: Multiplies each component by the given scalar value.
- **Parameters**: `right` — A `float` value.

Example:
```gdscript
var c = Color(1, 0, 0, 1)
var scaled = c * 0.5
print(scaled)  # Output: (0.5, 0, 0, 0.5)
```

### **+ (right: Color) → Color**
- **Description**: Adds each component of the color to the components of the given color.
- **Parameters**: `right` — Another `Color` instance.

Example:
```gdscript
var c1 = Color(1, 0, 0, 1)
var c2 = Color(0.5, 0.5, 0.5, 1)
var result = c1 + c2
print(result)  # Output: (1.5, 0.5, 0.5, 1)
```

### **- (right: Color) → Color**
- **Description**: Subtracts each component of the given color from the current color.
- **Parameters**: `right` — Another `Color` instance.

Example:
```gdscript
var c1 = Color(1, 0, 0, 1)
var c2 = Color(0.5, 0.5, 0.5, 1)
var result = c1 - c2
print(result)  # Output: (0.5, -0.5, -0.5, 0)
```

### **/ (right: Color) → Color**
- **Description**: Divides each component of the color by the components of the given color.
- **Parameters**: `right` — Another `Color` instance.

Example:
```gdscript
var c1 = Color(1, 0, 0, 1)
var c2 = Color(2, 1, 1, 1)
var result = c1 / c2
print(result)  # Output: (0.5, 0, 0, 1)
```

### **/ (right: float) → Color**
- **Description**: Divides each component of the color by the given scalar value.
- **Parameters**: `right` — A `float` value.

Example:
```gdscript
var c = Color(1, 0, 0, 1)
var divided = c / 2
print(divided)  # Output: (0.5, 0, 0, 0.5)
```

### **unary - (color: Color) → Color**
- **Description**: Inverts all components of the color (same as `inverted()`).
- **Return**: New `Color` instance with inverted values.

Example:
```gdscript
var c = Color(0.5, 0.5, 0.5, 1)
var inverted = -c
print(inverted)  # Output: (0.5, 0.5, 0.5, 0)
```

---

## **Examples**

### **Using to_html()**
```gdscript
var c = Color(1, 0.2, 0.3, 1)
var html = c.to_html()
print(html)  # Output: "ff2233ff" (for RGB with alpha)
```

### **Combining Colors with Operators**
```gdscript
var c1 = Color(1, 0, 0, 1)
var c2 = Color(0, 1, 0, 1)
var blended = c1 + c2
print(blended)  # Output: (1, 1, 1, 1)
```

### **Hex Conversion**
```gdscript
var c = Color(0.1, 0.2, 0.3, 1)
var hex = c.hex
print(hex)  # Output: "336699ff"
```

---

## **Key Notes**
- **Precision**: Use `is_equal_approx()` for comparisons to avoid issues with floating-point precision.
- **Alpha Channel**: The `a` property affects transparency in textures and blending.
- **Hex Format**: `hex` and `hex64` provide quick ways to represent colors as strings.

This guide covers all core functionalities of the `Color` class in Godot, from basic operations to advanced color manipulation.