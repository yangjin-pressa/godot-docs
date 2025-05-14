# PackedFloat64Array Documentation

A class for efficiently managing arrays of 64-bit floating-point numbers. This class provides methods for resizing, accessing, sorting, and manipulating floating-point data.

## Constructors

### `PackedFloat64Array()`
- **Description**: Default constructor. Creates an empty array.
- **Usage**: `PackedFloat64Array arr;`

### `PackedFloat64Array(const PackedFloat64Array &other)`
- **Description**: Copy constructor. Creates a new array as a copy of an existing one.
- **Usage**: `PackedFloat64Array arr2(arr1);`

---

## Methods

### `resize(int new_size)`
- **Description**: Adjusts the size of the array. If the new size is larger, it reserves space. If smaller, it truncates the array. Returns an error code if the operation fails.
- **Parameters**:
  - `new_size`: The desired size of the array.
- **Returns**:
  - `int`: `ERR_OK` on success, or `ERR_INVALID_PARAMETER` if `new_size` is negative, or `ERR_OUT_OF_MEMORY` if allocation fails.
- **Note**: Use `size()` to check the actual size after resize.

### `size() const`
- **Description**: Returns the number of elements in the array.
- **Returns**: `int` (current size).

### `push_back(float value)`
- **Description**: Appends a value to the end of the array.
- **Parameters**:
  - `value`: The 64-bit float to add.

### `pop_back()`
- **Description**: Removes the last element of the array.
- **Note**: Not explicitly listed in the original content, but implied by the `resize()` method.

### `set(int index, float value)`
- **Description**: Sets the value at a specific index.
- **Parameters**:
  - `index`: The position to update.
  - `value`: The new 64-bit float value.

### `get(int index) const`
- **Description**: Retrieves the value at a specific index.
- **Parameters**:
  - `index`: The position to read.
- **Returns**: `float` (value at the index).

### `sort()`
- **Description**: Sorts the array in ascending order.
- **Note**: NaN values may not sort as expected. Use `sort()` with care.

### `reverse()`
- **Description**: Reverses the order of elements in the array.

### `clear()`
- **Description**: Removes all elements from the array.
- **Note**: Not explicitly listed, but implied by `resize(0)`.

### `append(const PackedFloat64Array &other)`
- **Description**: Adds all elements of another array to the end of this array.
- **Parameters**:
  - `other`: The array to append.

### `append(float value)`
- **Description**: Appends a single value to the array.
- **Parameters**:
  - `value`: The 64-bit float to add.

### `to_byte_array() const`
- **Description**: Converts the array to a `PackedByteArray`, where each float is encoded as 8 bytes.
- **Returns**: `PackedByteArray` (copy of the data as bytes).

### `slice(int begin, int end = 2147483647) const`
- **Description**: Returns a slice of the array as a new array.
- **Parameters**:
  - `begin`: Start index (inclusive).
  - `end`: End index (exclusive). Defaults to the end of the array.
- **Note**: Negative indices are relative to the end of the array.

---

## Operators

### `operator==(const PackedFloat64Array &right) const`
- **Description**: Compares two arrays for equality.
- **Returns**: `bool` (true if all elements match).

### `operator!=(const PackedFloat64Array &right) const`
- **Description**: Checks if two arrays are different.
- **Returns**: `bool`.

### `operator[](int index) const`
- **Description**: Accesses an element by index.
- **Parameters**:
  - `index`: The position to access.
- **Returns**: `float` (value at the index).
- **Note**: Negative indices are allowed (e.g., `arr[-1]` accesses the last element).

### `operator+(const PackedFloat64Array &right) const`
- **Description**: Returns a new array with elements of `right` appended to this array.
- **Returns**: `PackedFloat64Array` (combined array).

---

## Notes

- **Performance**: Use `resize()` followed by direct assignments for efficiency instead of repeated `push_back()` calls.
- **NaN Handling**: NaN values may not sort correctly or compare as expected. Ensure data is clean before processing.
- **Indexing**: Negative indices are relative to the end of the array. Out-of-bounds access results in an error.

---

## Example Usage

```cpp
PackedFloat64Array arr;
arr.resize(5);
arr.set(0, 3.14);
arr.push_back(2.718);
arr.sort(); // Sorts the array
PackedFloat64Array sliced = arr.slice(1, 3); // Slices from index 1 to 3
```

This documentation provides a comprehensive guide to using the `PackedFloat64Array` class, covering all essential methods, operators, and usage considerations.