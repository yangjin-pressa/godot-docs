# StringName Class in Godot

The `StringName` class in Godot represents a string optimized for performance, particularly useful as keys in dictionaries or node names. It is a reference type, meaning comparisons between instances check for reference equality (memory address) rather than content equality. Below is a detailed overview of its methods, operators, and key considerations.

---

## **Key Features of StringName**
- **Performance Optimization**: Faster than `String` for hash-based operations and as keys in dictionaries.
- **Reference Equality**: Comparisons (`==`, `!=`) check if two `StringName` instances refer to the same memory address.
- **String Manipulation**: Includes methods for trimming, converting cases, escaping, and encoding.
- **URL Handling**: Methods for encoding and decoding URLs.
- **Validation**: Ensures strings meet criteria for filenames, node names, etc.

---

## **Methods**

### **Basic Manipulation**
- **`trim()`**: Removes leading/trailing whitespace.
- **`length()`**: Returns the length of the string.
- **`to_lower()` / `to_upper()`**: Converts the string to lowercase/uppercase.
- **`replace(old, new)`**: Replaces occurrences of `old` with `new`.

### **Comparison**
- **`compare_string(string)`**: Compares with a `String` (lexicographical order).
- **`compare_stringn(string, max_length)`**: Compares with a `String` up to `max_length`.
- **`compare_stringn_utf8(string, max_length)`**: Compares with a UTF-8 string.
- **`is_valid_filename()`**: Checks if the string is a valid filename.
- **`is_valid_node_name()`**: Validates if the string is a valid node name.

### **Encoding/Decoding**
- **`url_encode()` / `url_decode()`**: Encodes/decodes strings for URLs.
- **`to_utf8()`**: Converts the `StringName` to a UTF-8 string.
- **`from_utf8(utf8_str)`**: Creates a `StringName` from a UTF-8 string.
- **`xml_escape(escape_quotes=false)`**: Escapes XML special characters.
- **`xml_unescape()`**: Unescapes XML special characters.

### **Validation**
- **`validate_filename()`**: Replaces invalid filename characters with underscores.
- **`validate_node_name()`**: Replaces invalid node name characters with underscores.

### **Hashing**
- **`get_hash()` / `get_hash64()`**: Returns a hash of the string for fast lookups.

### **Formatting**
- **`formatv(fmt, *args)`**: Formats the string using `printf`-style formatting.
- **`operator % (right)`**: Interpolates values into the string (e.g., "Hello %s" % "World").

---

## **Operators**

### **Equality Operators**
- **`==`**: Checks if two `StringName` instances refer to the same memory address.
- **`!=`**: Checks if two `StringName` instances do not refer to the same memory address.

### **Concatenation**
- **`+`**: Appends another `String` or `StringName` to the current string (e.g., `"Hello" + " World"`).

### **Comparison Operators**
- **`<` / `>`**: Compares memory addresses (not lexicographical order).
- **`<=` / `>=`**: Compares memory addresses with equality.

---

## **Use Cases**
- **Node Names**: Efficiently use `StringName` as keys in dictionaries or node properties.
- **Hash-Based Lookups**: Use `get_hash()` for quick dictionary lookups.
- **URL Encoding**: Use `url_encode()` and `url_decode()` for safe URL handling.
- **Validation**: Use `validate_filename()` to ensure strings conform to file naming rules.

---

## **Important Notes**
- **Reference Equality**: `==` and `!=` compare memory addresses, not content. For content comparison, use methods like `compare_string()` or `equals()`.
- **Performance**: `StringName` is faster than `String` for hash and comparison operations.
- **String vs. StringName**: Use `StringName` for performance-critical paths; `String` for general text manipulation.

---

## **Example**
```gdscript
var name: StringName = "example"
var another_name: StringName = "example"

# Reference equality
if name == another_name:
    print("Same instance")

# Content comparison
if name.compare_string(another_name) == 0:
    print("Same content")

# URL encoding
var encoded: String = name.url_encode()
var decoded: StringName = StringName(url_decode(encoded))
```

This example demonstrates how `StringName` is used for reference checks and content comparison, along with URL handling.