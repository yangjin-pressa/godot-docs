# PackedColorArray Class Documentation

The `PackedColorArray` class in Godot provides a flexible and efficient way to handle arrays of `Color` values. It supports a wide range of operations for managing, modifying, and querying color data, including slicing, sorting, and converting to byte arrays.

---

## **Constructors**

### **Constructor 1**
```cpp
PackedColorArray()
```
**Description**: Initializes an empty `PackedColorArray`.

### **Constructor 2**
```cpp
PackedColorArray(int size)
```
**Description**: Initializes a `PackedColorArray` with a specified initial size. The array is initially empty, but the size is set to the given value.

---

## **Adding Elements**

### **append()**
```cpp
void append(Color value)
```
**Description**: Adds a `Color` value to the end of the array. Equivalent to `push_back()`.

### **push_back()**
```cpp
bool push_back(Color value)
```
**Description**: Appends a `Color` value to the end of the array. Returns `true` on success.

### **append_array()**
```cpp
void append_array(const PackedColorArray &arr)
```
**Description**: Appends all elements from another `PackedColorArray` to the current array. For better performance, consider this over manual iteration.

---

## **Resizing the Array**

### **resize()**
```cpp
int resize(int new_size)
```
**Description**: Sets the size of the array. If the array is grown, elements are added to the end. If shrunk, the array is truncated. Returns `OK` on success, or an error code if the size is invalid.

**Return Values**:
- `OK` (0): Success.
- `ERR_INVALID_PARAMETER`: If `new_size` is negative.
- `ERR_OUT_OF_MEMORY`: If memory allocation fails.

---

## **Accessing Elements**

### **get()**
```cpp
Color get(int index) const
```
**Description**: Returns the `Color` at the specified index. Negative indices are allowed (e.g., `-1` refers to the last element).

### **operator[]**
```cpp
Color operator[](int index) const
```
**Description**: Returns the `Color` at the specified index. Negative indices are allowed. Throws an error if the index is out of bounds.

---

## **Modifying Elements**

### **set()**
```cpp
void set(int index, Color value)
```
**Description**: Sets the `Color` at the specified index.

### **insert()**
```cpp
int insert(int at_index, Color value)
```
**Description**: Inserts a `Color` at the specified position. Returns the new size of the array after insertion.

### **remove_at()**
```cpp
void remove_at(int index)
```
**Description**: Removes the element at the specified index.

---

## **Slicing the Array**

### **slice()**
```cpp
PackedColorArray slice(int begin, int end = 2147483647) const
```
**Description**: Returns a new `PackedColorArray` containing a slice of the current array. The slice is from `begin` (inclusive) to `end` (exclusive).

**Notes**:
- `begin` and `end` can be negative (relative to the end of the array).
- Values are clamped to the array's bounds.
- Default `end` value (`2147483647`) slices to the end of the array.

**Example**:
```cpp
auto slice = arr.slice(1, -2);  // Slices from index 1 to index arr.size()-2
```

---

## **Array State**

### **is_empty()**
```cpp
bool is_empty() const
```
**Description**: Returns `true` if the array is empty.

### **size()**
```cpp
int size() const
```
**Description**: Returns the number of elements in the array.

---

## **Sorting and Reversing**

### **sort()**
```cpp
void sort()
```
**Description**: Sorts the array in ascending order.

### **reverse()**
```cpp
void reverse()
```
**Description**: Reverses the order of elements in the array.

---

## **Searching for Values**

### **find()**
```cpp
int find(Color value) const
```
**Description**: Returns the first index of `value` in the array. Returns `-1` if not found.

### **rfind()**
```cpp
int rfind(Color value, int from = -1) const
```
**Description**: Returns the last index of `value` in the array. If `from` is negative, it is treated as a relative index from the end.

---

## **Checking for Values**

### **has()**
```cpp
bool has(Color value) const
```
**Description**: Returns `true` if the array contains `value`.

### **contains()**
```cpp
bool contains(Color value) const
```
**Description**: Returns `true` if the array contains `value`.

---

## **Conversion to Byte Array**

### **to_byte_array()**
```cpp
PackedByteArray to_byte_array() const
```
**Description**: Converts the array to a `PackedByteArray` where each `Color` is encoded as four bytes (RGBA). The resulting byte array is four times the size of the original array.

---

## **Comparison Operators**

### **operator !=**
```cpp
bool operator!=(const PackedColorArray &other) const
```
**Description**: Returns `true` if the arrays differ in content.

### **operator ==**
```cpp
bool operator==(const PackedColorArray &other) const
```
**Description**: Returns `true` if both arrays have identical elements at corresponding indices.

### **operator +**
```cpp
PackedColorArray operator+(const PackedColorArray &other) const
```
**Description**: Returns a new array with the contents of `other` appended to the current array.

---

## **Key Notes**

- **Efficiency**: Use `resize()` for bulk operations (e.g., growing/shrinking arrays) instead of adding elements one by one.
- **Negative Indices**: Valid for `get()`, `operator[]`, and `slice()`, but invalid for `resize()` or `insert()`.
- **Memory**: The `to_byte_array()` method is useful for exporting color data in a format compatible with byte-based systems.

---

## **Example Usage**

```cpp
PackedColorArray colors;
colors.append(Color(1, 0, 0, 1));  // Red
colors.append(Color(0, 1, 0, 1));  // Green
colors.reverse();                 // Now [Green, Red]

auto slice = colors.slice(0, -1); // All elements except the last
auto byteData = colors.to_byte_array(); // 4 * 2 = 8 bytes
```

This documentation covers all core operations for the `PackedColorArray` class, ensuring developers can efficiently manage and manipulate color data in Godot.