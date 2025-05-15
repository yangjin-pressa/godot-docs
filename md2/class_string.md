# Godot String Class Documentation

## Methods

### `find(substring: String, start: int = 0) -> int`
Returns the index of the first occurrence of the given substring in the string, starting from the specified `start` index. Returns `-1` if the substring is not found.

**Examples:**
```gdscript
var str = "Hello, world!"
var index = str.find("world")
print(index)  # Output: 7
```

---

### `replace(old_substring: String, new_substring: String, all: bool = false) -> String`
Returns a new string with the specified substring replaced. If `all` is `true`, all occurrences are replaced; otherwise, only the first occurrence is replaced.

**Examples:**
```gdscript
var str = "Hello, world!"
var new_str = str.replace("world", "GDScript")
print(new_str)  # Output: "Hello, GDScript!"
```

---

### `split(separator: String, max_split: int = -1) -> Array`
Splits the string into an array of substrings based on the specified `separator`. If `max_split` is `-1`, all splits are allowed.

**Examples:**
```gdscript
var str = "apple,banana,orange"
var parts = str.split(",")
print(parts)  # Output: ["apple", "banana", "orange"]
```

---

### `split_whitespace() -> Array`
Splits the string into an array of substrings based on whitespace (spaces, tabs, newlines).

**Examples:**
```gdscript
var str = "Hello world, how are you?"
var parts = str.split_whitespace()
print(parts)  # Output: ["Hello", "world,", "how", "are", "you?"]
```

---

### `startswith(prefix: String, ignore_case: bool = false) -> bool`
Returns `true` if the string starts with the specified `prefix`, ignoring case if `ignore_case` is `true`.

**Examples:**
```gdscript
var str = "Hello, world!"
var result = str.startswith("Hello", true)
print(result)  # Output: true
```

---

### `endswith(suffix: String, ignore_case: bool = false) -> bool`
Returns `true` if the string ends with the specified `suffix`, ignoring case if `ignore_case` is `true`.

**Examples:**
```gdscript
var str = "Hello, world!"
var result = str.endswith("world!", true)
print(result)  # Output: true
```

---

### `to_lower() -> String`
Converts the string to lowercase.

**Examples:**
```gdscript
var str = "Hello World"
var lower_str = str.to_lower()
print(lower_str)  # Output: "hello world"
```

---

### `to_upper() -> String`
Converts the string to uppercase.

**Examples:**
```gdscript
var str = "Hello World"
var upper_str = str.to_upper()
print(upper_str)  # Output: "HELLO WORLD"
```

---

### `is_valid_filename() -> bool`
Checks if the string is a valid filename, considering allowed characters.

**Examples:**
```gdscript
var str = "valid_file.txt"
var result = str.is_valid_filename()
print(result)  # Output: true
```

---

### `validate_filename() -> String`
Returns a copy of the string with invalid characters replaced by underscores.

**Examples:**
```gdscript
var str = "invalid/filename.txt"
var valid_str = str.validate_filename()
print(valid_str)  # Output: "invalid_filename.txt"
```

---

### `validate_node_name() -> String`
Returns a copy of the string with invalid characters (like `.`, `:`, `@`, etc.) replaced by underscores.

**Examples:**
```gdscript
var str = "node.name:with@symbols"
var valid_str = str.validate_node_name()
print(valid_str)  # Output: "node_name_with_symbols"
```

---

### `xml_escape(escape_quotes: bool = false) -> String`
Escapes special characters in the string for XML. If `escape_quotes` is `true`, also escapes quotes.

**Examples:**
```gdscript
var str = "<script> &amp; &lt; &gt; &apos; &quot; "
var escaped_str = str.xml_escape(true)
print(escaped_str)  # Output: "&lt;script&gt; &amp; &lt; &gt; &apos; &quot; "
```

---

### `xml_unescape() -> String`
Unescapes XML entities back to their original characters.

**Examples:**
```gdscript
var str = "&lt;script&gt; &amp; &lt; &gt; &apos; &quot; "
var unescaped_str = str.xml_unescape()
print(unescaped_str)  # Output: "<script> & < > ' "
```

---

## Operators

### `+ (concatenation)`
Appends the right string to the left string.

**Examples:**
```gdscript
var str1 = "Hello"
var str2 = " World!"
var combined = str1 + str2
print(combined)  # Output: "Hello World!"
```

---

### `% (string formatting)`
Formats the string with placeholders replaced by arguments. For multiple parameters, the right operand must be an `Array`.

**Examples:**
```gdscript
var str = "I caught %d fishes!" % 2
print(str)  # Output: "I caught 2 fishes!"

var my_message = "Travelling to %s, at %2.2f km/h."
var location = "Deep Valley"
var speed = 40.3485
var formatted = my_message % [location, speed]
print(formatted)  # Output: "Travelling to Deep Valley, at 40.35 km/h."
```

---

### `== (comparison)`
Compares two strings for equality. Case-insensitive comparison is not supported by default.

**Examples:**
```gdscript
var str1 = "Hello"
var str2 = "hello"
var result = str1 == str2
print(result)  # Output: false
```

---

### `!= (inequality)`
Checks if two strings are not equal.

**Examples:**
```gdscript
var str1 = "Hello"
var str2 = "World"
var result = str1 != str2
print(result)  # Output: true
```

---

### `[] (indexing)`
Accesses a character at a specific index.

**Examples:**
```gdscript
var str = "Hello, world!"
var char = str[0]
print(char)  # Output: "H"
```

---

## Notes

- **Unicode and Encoding**: String comparisons are based on Unicode values. Ensure that your strings are properly encoded, especially when working with non-ASCII characters.
- **String Safety**: Avoid out-of-bounds indexing with the `[]` operator, as it may cause runtime errors.
- **C# Specifics**: In C#, the `%` operator for string formatting is not directly available. Use interpolated strings or `string.Format()` instead.

This documentation provides a comprehensive guide to the `String` class in Godot, covering all essential methods and operators for string manipulation and comparison.