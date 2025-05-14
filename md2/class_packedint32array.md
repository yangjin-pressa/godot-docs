# PackedInt32Array Guide

A class for managing arrays of 32-bit integers, providing efficient operations for resizing, accessing elements, and manipulating the data.

---

## **Overview**
The `PackedInt32Array` class handles arrays of 32-bit integers with methods to resize, sort, access elements, and convert to byte arrays. It supports operator overloading for comparison and indexing.

---

## **Constructors**

### `PackedInt32Array()`
- **Description:** Creates an empty array.
- **Parameters:** None
- **Return:** A new empty `PackedInt32Array`.

### `PackedInt32Array(const Array& p_array)`
- **Description:** Creates an array from a given `Array` of integers.
- **Parameters:** `p_array` (the source array)
- **Return:** A new `PackedInt32Array` initialized with the values from `p_array`.

---

## **Methods**

### `is_empty() const`
- **Description:** Checks if the array is empty.
- **Return:** `true` if the array has no elements, otherwise `false`.

### `push_back(int p_value)`
- **Description:** Appends a value to the end of the array.
- **Parameters:** `p_value` (the value to add)
- **Return:** `true` if the operation succeeds, `false` otherwise.

### `append(const PackedInt32Array& p_array)`
- **Description:** Appends all elements of another `PackedInt32Array` to this array.
- **Parameters:** `p_array` (the array to append)
- **Return:** `true` if the operation succeeds, `false` otherwise.

### `resize(int new_size)`
- **Description:** Resizes the array to the specified size. If the size is larger, new elements are added. If smaller, elements are truncated.
- **Parameters:** `new_size` (the desired size)
- **Return:** 
  - `OK` if the operation succeeds.
  - `ERR_INVALID_PARAMETER` if `new_size` is negative.
  - `ERR_OUT_OF_MEMORY` if memory allocation fails.
- **Note:** Use `size()` to get the actual size after resize.

### `sort()`
- **Description:** Sorts the array in ascending order.
- **Parameters:** None
- **Return:** void

### `reverse()`
- **Description:** Reverses the order of elements in the array.
- **Parameters:** None
- **Return:** void

### `set(int index, int value)`
- **Description:** Sets the value at a specific index.
- **Parameters:** 
  - `index` (the position in the array)
  - `value` (the new value)
- **Return:** void

### `size() const`
- **Description:** Returns the number of elements in the array.
- **Return:** The current size of the array.

### `slice(int begin, int end = 2147483647) const`
- **Description:** Returns a slice of the array as a new `PackedInt32Array`.
- **Parameters:** 
  - `begin` (start index, inclusive)
  - `end` (end index, exclusive)
- **Return:** A new `PackedInt32Array` containing the sliced elements.
- **Notes:**
  - Indices are clamped to the array's bounds.
  - Negative indices are relative to the end of the array (e.g., `arr.slice(0, -2)` refers to the last two elements).

### `to_byte_array() const`
- **Description:** Converts the array to a `PackedByteArray`, where each 32-bit integer is encoded as 4 bytes.
- **Return:** A `PackedByteArray` with size `original_size * 4`.

---

## **Operators**

### `operator != (const PackedInt32Array& right) const`
- **Description:** Compares this array to another. Returns `true` if the arrays differ.
- **Parameters:** `right` (the array to compare)
- **Return:** `true` if contents differ, `false` otherwise.

### `operator + (const PackedInt32Array& right) const`
- **Description:** Returns a new array with elements of `right` appended to this array.
- **Parameters:** `right` (the array to append)
- **Return:** A new `PackedInt32Array` with combined elements.
- **Note:** For better performance, use `append_array()` instead.

### `operator == (const PackedInt32Array& right) const`
- **Description:** Returns `true` if both arrays have the same elements in the same order.
- **Parameters:** `right` (the array to compare)
- **Return:** `true` if contents are equal, `false` otherwise.

### `operator [] (int index)`
- **Description:** Accesses the element at a specific index.
- **Parameters:** `index` (the position in the array)
- **Return:** The value at the specified index.
- **Notes:**
  - Negative indices are allowed (e.g., `-1` refers to the last element).
  - Out-of-bounds access results in an error.
  - The return type is a 64-bit `int`, which may differ from the stored 32-bit values.

---

## **Key Notes**
1. **Indexing:** The `[]` operator supports negative indices for reverse access, but out-of-bounds access is invalid.
2. **Resizing:** `resize()` can grow or shrink the array. Use `size()` to check the actual size after resize.
3. **Conversion:** `to_byte_array()` converts each 32-bit int to 4 bytes. The resulting array's size is `original_size * 4`.
4. **Performance:** For appending, `append_array()` is more efficient than the `+` operator.
5. **Comparison:** The `==` and `!=` operators compare the entire contents of the arrays, not just the size.

---

## **Example Usage**

```cpp
PackedInt32Array arr;
arr.push_back(10);
arr.push_back(20);

PackedInt32Array arr2 = arr + PackedInt32Array({30, 40});
// arr2 now contains [10, 20, 30, 40]

int value = arr[0]; // 10
arr.reverse(); // array becomes [20, 10]
```

---

This guide provides a clear reference for working with `PackedInt32Array`, covering all essential operations and edge cases.