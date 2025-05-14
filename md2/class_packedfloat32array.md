# PackedFloat32Array Class Documentation

A class representing a packed array of 32-bit floating-point numbers. This class provides methods for manipulating and accessing the array's contents, including resizing, sorting, and slicing.

## Constructors

### `PackedFloat32Array()`
- **Description:** Creates an empty array.
- **Parameters:** None
- **Returns:** A new empty `PackedFloat32Array` instance.

---

## Methods

### `resize(new_size: int) -> int`
- **Description:** Adjusts the size of the array. If the size is increased, new elements are reserved at the end. If decreased, the array is truncated.
- **Parameters:**
  - `new_size`: The desired size of the array.
- **Returns:**
  - `@GlobalScope.OK`: Success.
  - `@GlobalScope.ERR_INVALID_PARAMETER`: If `new_size` is negative.
  - `@GlobalScope.ERR_OUT_OF_MEMORY`: If memory allocation fails.
- **Note:** Use `size()` to check the actual size after resizing.

### `sort()`
- **Description:** Sorts the array in ascending order.
- **Note:** NaN values may not sort as expected.

### `reverse()`
- **Description:** Reverses the order of elements in the array.

### `set(index: int, value: float)`
- **Description:** Updates the value at the specified index.
- **Parameters:**
  - `index`: The index of the element to update.
  - `value`: The new value to assign.

### `size() -> int`
- **Description:** Returns the number of elements in the array.
- **Returns:** The current size of the array.

### `to_byte_array() -> PackedByteArray`
- **Description:** Converts the array to a `PackedByteArray`, where each 32-bit float is encoded as 4 bytes.
- **Returns:** A new `PackedByteArray` with the converted data.

### `slice(begin: int, end: int = 2147483647) -> PackedFloat32Array`
- **Description:** Returns a new array containing a slice of the current array.
- **Parameters:**
  - `begin`: The starting index (inclusive).
  - `end`: The ending index (exclusive).
- **Note:** Negative indices are relative to the end of the array. The default `end` value slices to the end of the array.

### `remove_at(index: int)`
- **Description:** Removes the element at the specified index.

### `append_array(array: PackedFloat32Array)`
- **Description:** Appends the elements of another array to the end of this array.
- **Note:** For better performance, use this method instead of manually adding elements.

### `operator[] (index: int) -> float`
- **Description:** Returns the float at the specified index. Negative indices can be used to access elements from the end.
- **Note:** The returned value is a 64-bit float, even though the array stores 32-bit floats.

---

## Operators

### `operator == (right: PackedFloat32Array) -> bool`
- **Description:** Returns `true` if both arrays have the same elements at corresponding indices.

### `operator != (right: PackedFloat32Array) -> bool`
- **Description:** Returns `true` if the arrays differ in content.

### `operator + (right: PackedFloat32Array) -> PackedFloat32Array`
- **Description:** Returns a new array with the elements of `right` appended to this array.
- **Note:** For performance, consider using `append_array()` instead.

---

## Notes

- **Storage:** Each element is a 32-bit float (4 bytes), so the total size of the array is `size() * 4` bytes.
- **Indexing:** Negative indices are valid but must be within bounds. Out-of-bounds access will throw an error.
- **NaN Handling:** NaN values may not sort or compare as expected due to their special floating-point behavior.