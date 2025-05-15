### RegEx Class Overview

The `RegEx` class provides functionality for working with regular expressions in Godot. It allows users to define patterns for text matching, searching, and replacing. Key features include support for capturing groups, named groups, and backreferences.

---

#### Example Usage
```gdscript
var regex = RegEx.new()
regex.compile("example")
var result = regex.search("This is an example.")
print(result)  # Returns a RegExMatch object containing the match
```

#### Note
This class relies on the **PCRE2** (https://www.pcre.org/) library for regular expression implementation. For advanced patterns, consider using the [Regexr](https://regexr.com/) tool for validation.

---

### Methods

1. **`clear()`**  
   Removes the current pattern from the regex object.  
   *No return value.*

2. **`compile(pattern: String, show_error: Bool = false)`**  
   Compiles the specified pattern into a regular expression.  
   *Parameters:*  
   - `pattern`: The regex pattern to compile.  
   - `show_error`: Whether to display errors during compilation.  
   *Return Value:* `void`

3. **`search(subject: String, offset: Int = 0, end: Int = -1) -> RegExMatch`**  
   Searches the `subject` string for the compiled pattern.  
   *Parameters:*  
   - `subject`: The text to search.  
   - `offset`: The starting position in the string.  
   - `end`: The ending position in the string.  
   *Return Value:* A `RegExMatch` object if a match is found, otherwise `null`.

4. **`search_all(subject: String, offset: Int = 0, end: Int = -1) -> Array<RegExMatch>`**  
   Searches the `subject` string for all non-overlapping matches.  
   *Parameters:* Same as `search()`.  
   *Return Value:* An array of `RegExMatch` objects or an empty array if no matches are found.

5. **`sub(subject: String, replacement: String, all: Bool = false, offset: Int = 0, end: Int = -1) -> String`**  
   Replaces the first or all occurrences of the pattern in the `subject` string.  
   *Parameters:*  
   - `subject`: The text to process.  
   - `replacement`: The string to replace the pattern with.  
   - `all`: Whether to replace all occurrences.  
   - `offset`: The starting position in the string.  
   - `end`: The ending position in the string.  
   *Return Value:* A string with replacements applied.

6. **`get_group_count() -> Int`**  
   Returns the number of capturing groups in the compiled pattern.  
   *Return Value:* An integer representing the count of groups.

7. **`get_names() -> PackedStringArray`**  
   Returns the names of all named capturing groups in the pattern.  
   *Return Value:* An array of group names.

8. **`get_pattern() -> String`**  
   Returns the original pattern used to compile the regex.  
   *Return Value:* The original pattern string.

9. **`is_valid() -> Bool`**  
   Checks if the current regex object has a valid pattern.  
   *Return Value:* `true` if the pattern is valid, otherwise `false`.

---

### Key Concepts
- **Capturing Groups**: Subpatterns enclosed in parentheses, which can be referenced via backreferences (`$1`, `$2`, etc.) or named groups.
- **Named Groups**: Groups with explicit names (e.g., `(?<name>pattern)`), accessible via `$name`.
- **Backreferences**: References to previously captured groups (e.g., `$1`, `$name`).
- **Search vs. Search All**: `search()` finds the first match, while `search_all()` returns all non-overlapping matches.

---

### Example: Named Groups
```gdscript
var regex = RegEx.new()
regex.compile("(?<year>\\d{4})-(?<month>\\d{2})-(?<day>\\d{2})")
var match = regex.search("2023-10-05")
print("Year:", match.get_group("year"))
print("Month:", match.get_group("month"))
```

This example extracts date components using named groups, demonstrating how to access and use captured data.