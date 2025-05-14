# Int Class Reference

This document provides a comprehensive reference to the `Int` class in GDScript, detailing all its operators and methods. The class supports arithmetic, bitwise, comparison, and unary operations, with detailed explanations and examples for each.

---

## Arithmetic Operators

### `+` (Addition)
**Description**: Returns the sum of two `Int` values.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 5
var b = 3
var result = a + b  # 8
```

### `-` (Subtraction)
**Description**: Returns the difference between two `Int` values.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 10
var b = 4
var result = a - b  # 6
```

### `*` (Multiplication)
**Description**: Returns the product of two `Int` values.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 7
var b = 3
var result = a * b  # 21
```

### `/` (Division)
**Description**: Returns the integer division result of two `Int` values, truncating any decimal part.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 6
var b = 2
var result = a / b  # 3
var result = 5 / 3  # 1
```

---

## Bitwise Operators

### `&` (Bitwise AND)
**Description**: Returns a new `Int` where each bit is 1 only if both corresponding bits in the operands are 1.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 0b1100
var b = 0b1010
var result = a & b  # 0b1000 (8)
```

### `|` (Bitwise OR)
**Description**: Returns a new `Int` where each bit is ity 1 if at least one of the corresponding bits in the operands is 1.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 0b1100
var b = 0b1010
var result = a | b  # 0b1110 (14)
```

### `^` (Bitwise XOR)
**Description**: Returns a new `Int` where each bit is 1 if the corresponding bits in the operands are different.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 0b1100
var b = 0b1010
var result = a ^ b  # 0b0110 (6)
```

### `<<` (Bitwise Shift Left)
**Description**: Shifts the bits of the operand to the left by the specified number of positions, effectively multiplying by 2^n.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 0b1010  # 10
var result = a << 1  # 20 (0b10100)
```

### `>>` (Bitwise Shift Right)
**Description**: Shifts the bits of the operand to the right by the specified number of positions, effectively dividing by 2^n.
**Parameters**: `right: Int`
**Return**: `Int`
**Example**:
```gdscript
var a = 0b1010  # 10
var result = a >> 1  # 5 (0b101)
```

### `~` (Bitwise NOT)
**Description**: Returns the bitwise negation of the operand. Due to two's complement, this is equivalent to `-(int + 1)`.
**Parameters**: None
**Return**: `Int`
**Example**:
```gdscript
var a = 4
var result = ~a  # -5
var result = ~(-7)  # 6
```

---

## Comparison Operators

### `<` (Less Than)
**Description**: Returns `true` if the left `Int` is less than the right `Int` or `Float`.
**Parameters**: `right: Int` or `Float`
**Return**: `bool`
**Example**:
```gdscript
var a = 5
var b = 3
var result = a < b  # false
```

### `<=` (Less Than or Equal To)
**Description**: Returns `true` if the left `Int` is less than or equal to the right `Int` or `Float`.
**Parameters**: `right: Int` or `Float`
**Return**: `bool`
**Example**:
```gdscript
var a = 5
var b = 5
var result = a <= b  # true
```

### `>` (Greater Than)
**Description**: Returns `true` if the left `Int` is greater than the right `Int` or `Float`.
**Parameters**: `right: Int` or `Float`
**Return**: `bool`
**Example**:
```gdscript
var a = 10
var b = 4
var result = a > b  # true
```

### `>=` (Greater Than or Equal To)
**Description**: Returns `true` if the left `Int` is greater than or equal to the right `Int` or `Float`.
**Parameters**: `right: Int` or `Float`
**Return**: `bool`
**Example**:
```gdscript
var a = 5
var b = 5
var result = a >= b  # true
```

### `==` (Equal To)
**Description**: Returns `true` if the two `Int` values are equal.
**Parameters**: `right: Int`
**Return**: `bool`
**Example**:
```gdscript
var a = 5
var b = 5
var result = a == b  # true
```

### `!=` (Not Equal To)
**Description**: Returns `true` if the two `Int` values are not equal.
**Parameters**: `right: Int`
**Return**: `bool`
**Example**:
```gdscript
var a = 5
var b = 3
var result = a != b  # true
```

---

## Unary Operators

### `+` (Unary Plus)
**Description**: Returns the same value as the operand. Unary `+` does nothing but can improve readability.
**Parameters**: None
**Return**: `Int`
**Example**:
```gdscript
var a = 5
var result = +a  # 5
```

### `-` (Unary Minus)
**Description**: Returns the negated value of the operand. If positive, turns the number negative. If negative, turns it positive. If zero, does nothing.
**Parameters**: None
**Return**: `Int`
**Example**:
```gdscript
var a = 10
var result = -a  # -10
```

---

## Notes

- All arithmetic operations (addition, subtraction, multiplication, division) return integer results, truncating any decimal parts.
- Bitwise operations are performed using two's complement representation.
- Comparison operators accept both `Int` and `Float` parameters.
- Unary operators are context-sensitive and do not alter the value of the operand (except for negation).

This documentation covers all standard operators for the `Int` class, ensuring clarity and ease of use for developers working with GDScript.