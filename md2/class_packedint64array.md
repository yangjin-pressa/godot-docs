# PackedInt64Array Class Documentation

## Overview
The `PackedInt64Array` class is a specialized data structure that stores an array of 64-bit integers. It provides a range of operations for manipulating the array, including appending, inserting, removing, sorting, and slicing. The class also supports operator overloading for convenient array manipulation.

---

## Methods

### `resize(new_size: int) -> int`
**Description**: Adjusts the size of the array. If the array is grown, it reserves elements at the end. If shrunk, it truncates the array.  
**Return Value**: 
- `OK` on success.
- `ERR_INVALID_PARAMETER` if the size is negative.
- `ERR_OUT_OF_MEMORY` if memory allocation fails.

**Notes**:
- Use `size()` to check the actual size after resizing.
- Resizing is more efficient than adding elements one by one.

### `sort() -> void`
**Description**: Sorts the array elements in ascending order.

### `reverse() -> void`
**Description**: Reverses the order of elements in the array.

### `size() -> int`
**Description**: Returns the number of elements in the array.

### `is_empty() -> bool`
**Description**: Returns `true` if the array is empty.

### `push_back(value: int) -> bool`
**Description**: Appends a value to the end of the array.

### `append(value: int) -> bool`
**Description**: Appends a value to the end of the array (alias for `push_back`).

### `insert(index: int, value: int) -> void`
**Description**: Inserts a value at the specified index. The array is expanded if necessary.

### `remove_at(index: int) -> void`
**Description**: Removes the element at the specified index.

### `set(index: int, value: int) -> void`
**Description**: Updates the value at the specified index.

### `set_all(value: int) -> void`
**Description**: Sets all elements of the array to the specified value.

### `clear() -> void`
**Description**: Removes all elements from the array.

### `slice(begin: int, end: int = 2147483647) -> PackedInt64Array`
**Description**: Returns a new array containing a slice of the current array.  
**Parameters**:
- `begin`: Start index (inclusive).
- `end`: End index (exclusive).
**Notes**:
- `begin` and `end` are clamped to the array size.
- Negative indices are relative to the end of the array.

### `to_byte_array() -> PackedByteArray`
**Description**: Converts the array to a `PackedByteArray`, where each 64-bit integer is encoded as 8 bytes.  
**Return Value**: A new `PackedByteArray` with size `original_size * 8`.

---

## Operators

### `operator[] (index: int) -> int`
**Description**: Returns the integer at the specified index.  
**Notes**:
- Negative indices are allowed (e.g., `-1` returns the last element).
- Out-of-bounds access results in an error.

### `operator+ (right: PackedInt64Array) -> PackedInt64Array`
**Description**: Returns a new array with elements of `right` appended to the current array.  
**Note**: Use `append_array()` for better performance.

### `operator== (right: PackedInt64Array) -> bool`
**Description**: Returns `true` if all elements in both arrays are equal.

### `operator!= (right: PackedInt64Array) -> bool`
**Description**: Returns `true` if the arrays differ in content.

---

## Example Usage

```python
arr = PackedInt64Array()
arr.push_back(10)
arr.push_back(20)
arr.sort()
print(arr[0])  # Output: 10
print(arr[-1])  # Output: 20
slice = arr.slice(0, -1)
print(slice.size())  # Output: 1
```

---

## Notes
- The `resize()` method is efficient for bulk modifications.
- The `operator[]` supports negative indices for reverse access.
- `to_byte_array()` is useful for serialization or interoperability with byte-based systems.