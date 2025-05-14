# PackedByteArray Summary

## Key Methods

### Basic Operations
- **append(value: int)**: Appends a single byte to the end of the array.
- **append_array(array: PackedByteArray)**: Appends all bytes from another array.
- **insert(index: int, value: int)**: Inserts a byte at a specific position.
- **resize(size: int)**: Resizes the array, truncating or padding as needed.
- **clear()**: Removes all bytes from the array.

### Search
- **find(value: int, from: int = 0)**: Returns the first index of a value (from start).
- **rfind(value: int, from: int = -1)**: Returns the last index of a value (from end).
- **has(value: int)**: Checks if a value exists in the array.

### Slicing
- **slice(begin: int, end: int = 2147483647)**: Returns a new array from a range of bytes.
  - Negative indices are relative to the end.
  - Clamped to array bounds.

### Conversion
- **to_float32_array()**: Converts to a `PackedFloat32Array` (requires size multiple of 4).
- **to_float64_array()**: Converts to a `PackedFloat64Array` (requires size multiple of 8).
- **to_int32_array()**: Converts to a `PackedInt32Array` (size multiple of 4).
- **to_int64_array()**: Converts to a `PackedInt64Array` (size multiple of 8).

### Utility
- **size()**: Returns the number of bytes.
- **set(index: int, value: int)**: Modifies a byte at a specific index.
- **sort()**: Sorts the array in ascending order.
- **reverse()**: Reverses the order of bytes.
- **reverse_array()**: Reverses the array (aliased to `reverse()`).

### Indexing
- **[] (index: int)**: Returns a byte at the specified index.
  - Negative indices allowed (e.g., `-1` for last byte).
  - Out-of-bounds access throws an error.

---

## Operators

### Equality
- **== (right: PackedByteArray)**: Checks if two arrays have identical bytes.
- **!= (right: PackedByteArray)**: Returns `true` if arrays differ.

### Concatenation
- **+ (right: PackedByteArray)**: Creates a new array by appending `right` to this one.

---

## Notes
- **Indexing**: Negative indices are relative to the end. Out-of-bounds access is an error.
- **Conversion**: Ensure data is compatible with target type (e.g., 4-byte alignment for `to_float32_array`).
- **Performance**: Use `append_array()` for efficient concatenation instead of `+`.
- **Memory**: `PackedByteArray` is optimized for binary data handling in Godot.