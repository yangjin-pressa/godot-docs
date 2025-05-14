### Dictionary Class Description

The `Dictionary` class in Godot is a dynamic collection of key-value pairs, where each key is unique. It provides methods for accessing, modifying, and managing the collection, as well using operators for comparison and access. Below is a structured overview of its key features and methods.

---

### **Methods**

#### **1. `get(key: Variant) -> Variant`**
- **Description:** Retrieves the value associated with the given key. If the key does not exist, returns `null`.
- **Note:** For safe access, use `has(key)` to check existence before calling `get`.

#### **2. `has(key: Variant) -> bool`**
- **Description:** Checks if the dictionary contains the specified key.
- **Return:** `true` if the key exists; `false` otherwise.

#### **3. `set(key: Variant, value: Variant) -> bool`**
- **Description:** Sets the value of the element at the given key. Returns `true` on success.
- **Note:** Equivalent to using the `[]` operator (e.g., `dict[key] = value`).

#### **4. `keys() -> Array`**
- **Description:** Returns an array of all keys in the dictionary.
- **Use Case:** Useful for iterating over keys or when sorting is required.

#### **5. `values() -> Array`**
- **Description:** Returns an array of all values in the dictionary.
- **Use Case:** For processing values or validating data.

#### **6. `size() -> int`**
- **Description:** Returns the number of entries in the dictionary.
- **Note:** Empty dictionaries return `0`.

#### **7. `is_empty() -> bool`**
- **Description:** Checks if the dictionary is empty.
- **Return:** `true` if the dictionary contains no entries.

#### **8. `merge(dictionary: Dictionary, overwrite: bool = false) -> void`**
- **Description:** Adds entries from another dictionary. If `overwrite` is `true`, existing keys are replaced.
- **Note:** Not recursive; nested dictionaries are treated as values, not merged.

#### **9. `merged(dictionary: Dictionary, overwrite: bool = false) -> Dictionary`**
- **Description:** Returns a new dictionary that is a copy of the current one merged with the provided dictionary.
- **Use Case:** Useful for creating new dictionaries with default values.

#### **10. `sort() -> void`**
- **Description:** Sorts the dictionary by key in ascending order.
- **Effect:** Ensures consistent order for `keys()` and `values()` calls.

#### **11. `recursive_equal(dictionary: Dictionary, recursion_count: int) -> bool`**
- **Description:** Checks if two dictionaries are equal recursively, including nested structures.
- **Note:** `recursion_count` prevents infinite recursion in complex data structures.

#### **12. `make_read_only() -> void`**
- **Description:** Makes the dictionary read-only, preventing modifications.
- **Note:** Nested dictionaries inside the current one can still be modified.

---

### **Operators**

#### **1. `== (right: Dictionary) -> bool`**
- **Description:** Returns `true` if both dictionaries have the same keys and values, regardless of order.
- **Note:** In C#, this operator compares by reference. For GDScript, it checks for value equality.

#### **2. `!= (right: Dictionary) -> bool`**
- **Description:** Returns `true` if the dictionaries differ in keys or values.

#### **3. `[] (key: Variant) -> Variant`**
- **Description:** Accesses the value associated with the key. Returns `null` if the key does not exist.
- **Note:** Use `get(key)` for safer access when a default value is required.

---

### **Key Notes**

- **Dynamic Structure:** Keys can be added, removed, or modified at runtime.
- **Read-Only Safety:** `make_read_only()` prevents accidental modifications but allows nested dictionaries to be altered.
- **Non-Recursive Merge:** The `merge` method does not recursively merge nested dictionaries.
- **Sorting:** `sort()` affects the order of keys, ensuring predictable iteration or string conversion.
- **Recursive Equality:** `recursive_equal()` is essential for deep comparisons of nested data structures.

---

### **Best Practices**
- Use `has(key)` before `get(key)` to avoid `null` values.
- For nested structures, use `merge` with `overwrite: true` to update values.
- Use `sort()` to ensure consistent key ordering during iteration or serialization.
- Always verify data with `recursive_equal()` when comparing complex structures.