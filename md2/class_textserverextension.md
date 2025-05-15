The `TextServerExtension` class provides a set of virtual methods for text processing, including handling original strings, shaped text buffers, and text layout. Below is an explanation of each method, focusing on their purpose and parameters as described in the documentation:

---

### **1. `_string_at_pos`**
**Purpose**: Returns the character at a specific position in the original string.  
**Parameters**:  
- `string`: The original string.  
- `pos`: The position in the string (e.g., index of the character).  
**Note**: This method retrieves the character directly from the original string, not the shaped buffer.

---

### **2. `_string_break`**
**Purpose**: Retrieves break points for the original string based on a specified language.  
**Parameters**:  
- `string`: The original string.  
- `language`: The language used to determine text flow and word breaks.  
**Note**: This is for determining where lines break in the original string, not the shaped buffer.

---

### **3. `_string_bound`**
**Purpose**: Returns the bounding dimensions (e.g., width, height) of the original string.  
**Parameters**:  
- `string`: The original string.  
- `language`: The language used for text layout.  
**Note**: This method computes the size of the original string in the context of the specified language.

---

### **4. `_string_get_char`**
**Purpose**: Retrieves the character at a given position in the original string.  
**Parameters**:  
- `string`: The original string.  
- `pos`: The position in the string.  
**Note**: This is a basic character retrieval method for the original string.

---

### **5. `_string_get_char_from_code`**
**Purpose**: Gets the character corresponding to a code point in the original string.  
**Parameters**:  
- `string`: The original string.  
- `code`: The Unicode code point (e.g., `U+0048` for 'H').  
**Note**: This method maps a code point to its character in the original string.

---

### **6. `_string_get_char_index`**
**Purpose**: Returns the index of a specific character in the original string.  
**Parameters**:  
- `string`: The original string.  
- `char`: The character to find.  
**Note**: This is for finding the position of a character in the original string.

---

### **7. `_string_get_char_info`**
**Purpose**: Retrieves information about a character in the original string, such as glyph index or Unicode properties.  
**Parameters**:  
- `string`: The original string.  
- `pos`: The position in the string.  
**Note**: This method provides metadata about a character in the original string.

---

### **8. `_string_get_glyphs`**
**Purpose**: Returns the glyph data (e.g., font, size, position) for the original string.  
**Parameters**:  
- `string`: The original string.  
- `language`: The language for text layout.  
**Note**: This is for retrieving glyph information for the original string.

---

### **9. `_string_get_length`**
**Purpose**: Gets the length of the original string.  
**Parameters**:  
- `string`: The original string.  
**Note**: This is a simple method to determine the number of characters in the original string.

---

### **10. `_string_get_line`**
**Purpose**: Returns the line information (e.g., start/end positions) for a specific line in the original string.  
**Parameters**:  
- `string`: The original string.  
- `line`: The line number (e.g., 0 for the first line).  
**Note**: This is for retrieving line details in the original string.

---

### **11. `_string_get_line_count`**
**Purpose**: Gets the total number of lines in the original string.  
**Parameters**:  
- `string`: The original string.  
- `language`: The language for text layout.  
**Note**: This method determines how many lines the original string would occupy based on the specified language.

---

### **12. `_string_get_line_offset`**
**Purpose**: Returns the offset (position) of a specific line in the original string.  
**Parameters**:  
- `string`: The original string.  
- `line`: The line number.  
**Note**: This is for finding the start position of a line in the original string.

---

### **13. `_string_get_line_info`**
**Purpose**: Retrieves detailed line information (e.g., width, height) for the original string.  
**Parameters**:  
- `string`: The original string.  
- `line`: The line number.  
**Note**: This method provides metadata about a specific line in the original string.

---

### **14. `_string_get_line_breaks`**
**Purpose**: Gets the line break points for the original string.  
**Parameters**:  
- `string`: The original string.  
- `language`: The language for text layout.  
**Note**: This is for determining where lines break in the original string.

---

### **15. `_string_get_line_breaks_for_oversampling`**
**Purpose**: Returns line breaks for the original string with oversampling adjustments.  
**Parameters**:  
- `string`: The original string.  
- `oversampling`: The level of oversampling.  
**Note**: This method accounts for oversampling when computing line breaks.

---

### **16. `_string_get_line_breaks_for_oversampling_level`**
**Purpose**: Gets line breaks for the original string based on a specific oversampling level.  
**Parameters**:  
- `string`: The original string.  
- `level`: The oversampling level.  
**Note**: This is for fine-tuning line breaks with specific oversampling parameters.

---

### **17. `_string_get_line_breaks_for_language`**
**Purpose**: Retrieves line breaks for the original string based on the specified language.  
**Parameters**:  
- `string`: The original string.  
- `language`: The language for text layout.  
**Note**: This method focuses on line breaks based on the language's text-flow rules.

---

### **18. `_string_get_line_breaks_for_language_and_oversampling`**
**Purpose**: Returns line breaks for the original string, considering both language and oversampling.  
**Parameters**:  
- `string`: The original string.  
- `language`: The language for text layout.  
- `oversampling`: The oversampling level.  
**Note**: This combines language-based and oversampling-based line break calculations.

---

### **Key Notes**:
- The methods primarily handle **original string data** (e.g., character retrieval, line breaks, glyph information).
- The note about "shaped text buffer" may be misleading or incorrect, as these methods are not inherently tied to shaped text processing.
- These methods are likely used as part of a larger system that may later render the original string into a shaped buffer (e.g., for display or layout).

This documentation focuses on text processing for the original string, with parameters that allow for language-specific and oversampling adjustments.