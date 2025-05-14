# PackedVector4Array Documentation

This class provides a collection of `Vector4` elements, offering efficient operations for manipulation, access, and transformation. Below is a detailed breakdown of its functionality.

---

## **Constructors**

### 1. **Default Constructor**
```cpp
PackedVector4Array()
```
**Description:** Creates an empty array with no elements.

### 2. **Copy Constructor**
```cpp
PackedVector4Array(const PackedVector4Array& other)
```
**Description:** Initializes a new array by copying the contents of an existing `PackedVector4Array`.

### 3. **Array Constructor**
```cpp
PackedVector4Array(const Vector4* array, int count)
```
**Parameters:**
- `array`: A pointer to an array of `Vector4` elements.
- `count`: The number of elements to copy.

**Description:** Constructs an array from a C-style array of `Vector4`.

---

## **Methods**

### 1. **resize(new_size: int) -> int**
**Description:** Modifies the size of the array. If the new size is larger, the array is extended. If smaller, it is truncated.
**Returns:** `OK` on success, or an error code if the new size is negative.
**Note:** Use `size()` to check the current size after resizing.

### 2. **sort()**
**Description:** Sorts the array in ascending order. Elements are compared lexicographically.
**Note:** Handles `NaN` values, but results may be unexpected if present.

### -than 3. **reverse()**
**Description:** Reverses the order of elements in the array.

### 4. **size() -> int**
**Description:** Returns the number of elements in the array.

### 5. **is_empty() -> bool**
**Description:** Returns `true` if the array contains no elements.

### 6. **push_back(value: Vector4) -> bool**
**Description:** Appends a `Vector4` to the end of the array.
**Returns:** `true` if successful, `false` if memory allocation fails.

### 7. **pop_back()**
**Description:** Removes the last element of the array.

### 8. **set(index: int, value: Vector4)**
**Description:** Replaces the element at the specified index.
**Note:** Index out of bounds results in an error.

### 9. **get(index: int) -> Vector4**
**Description:** Returns the element at the specified index. Negative indices are allowed (e.g., `-1` returns the last element).
**Note:** Index out of bounds results in an error.

### 10. **remove_at(index: int)**
**Description:** Removes the element at the specified index.

### 11. **slice(begin: int, end: int = 2147483647) -> PackedVector4Array**
**Description:** Returns a new array containing a subset of elements from `begin` to `end` (exclusive).
**Parameters:**
- `begin`: Start index (inclusive).
- `end`: End index (exclusive).
**Note:** Negative indices are relative to the end of the array. Values are clamped to array bounds.

### 12. **to_byte_array() -> PackedByteArray**
**Description:** Converts the array into a `PackedByteArray`, where each `Vector4` is encoded as bytes.

---

## **Operators**

### 1. **Equality Operator (`==`)**
```cpp
bool operator==(const PackedVector4Array& other) const
```
**Description:** Compares two arrays for equality. Returns `true` if all elements are equal at corresponding indices.

### 2. **Inequality Operator (`!=`)**
```cpp
bool operator!=(const PackedVector4Array& other) const
```
**Description:** Returns `true` if the arrays differ in any element.

### 3. **Addition Operator (`+`)**
```cpp
PackedVector4Array operator+(const PackedVector4Array& other) const
```
**Description:** Returns a new array with elements of `other` appended to the current array.
**Note:** Use `append_array()` for better performance than this operator.

### 4. **Indexing Operator (`[]`)**
```cpp
Vector4 operator[](int index) const
```
**Description:** Accesses the element at the specified index. Negative indices are allowed.
**Note:** Index out of bounds results in an error.

---

## **Key Notes**

- **NaN Handling:** Methods like `sort()` and `slice()` may exhibit unexpected behavior if the array contains `NaN` values.
- **Performance:** `resize()` is efficient for bulk operations, while individual element additions (e.g., `push_back()`) are slower.
- **Memory Safety:** Always validate indices before accessing elements to avoid runtime errors.

---

## **Example Usage**

```cpp
// Create an array with 3 elements
PackedVector4Array arr;
arr.resize(3);
arr.set(0, Vector4(1.0, 2.0, 3.0, 4.0));
arr.set(1, Vector4(5.0, 6.0, 7.0, 8.0));
arr.set(2, Vector4(9.0, 10.0, 11.0, 12.0));

// Slice the array
PackedVector4Array slice = arr.slice(1, 3);

// Compare arrays
bool equal = arr == slice;

// Reverse the array
arr.reverse();

// Convert to byte array
PackedByteArray byteArray = arr.to_byte_array();
```

This documentation provides a clear overview of the `PackedVector4Array` class, its methods, and operators, ensuring developers can effectively manage and manipulate collections of `Vector4` elements.