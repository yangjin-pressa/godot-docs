**CodeHighlighter Class Overview**

**Description**  
A class for highlighting code elements in Godot, allowing customization of colors and syntax rules for different code structures.

---

### **Properties**

1. **color_region**  
   - **Type**: `Dictionary`  
   - **Default**: `Dictionary()`  
   - **Description**: Stores color regions (e.g., comments, strings) defined by start/end keys.

2. **keyword_color**  
   - **Type**: `Dictionary`  
   - **Default**: `Dictionary()`  
   - **Description**: Maps keywords to their highlight colors.

3. **member_variable_color**  
   - **Type**: `Color`  
   - **Default**: `Color(0, 0, 0, 1)`  
   - **Description**: Color for member variables (non-keyword, non-function strings preceded by `.`).

4. **number_color**  
   - **Type**: `Color`  
   - **Default**: `Color(0, 0, 0, 1)`  
   - **Description**: Color for numbers.

5. **symbol_color**  
   - **Type**: `Color`  
   - **Default**: `Color(0, 0, 0, 1)`  
   - **Description**: Color for symbols (e.g., `+`, `=`).

---

### **Methods**

1. **add_color_region(start_key, end_key, color, line_only=false)**  
   - **Parameters**:  
     - `start_key`: String (delimiter for start of region).  
     - `end_key`: String (delimiter for end of region).  
     - `color`: Color (region highlight color).  
     - `line_only`: Boolean (if true, region does not carry over to next line).  
   - **Description**: Adds a color region (e.g., comments, strings) defined by start/end keys.

2. **clear_color_regions()**  
   - **Description**: Removes all color regions.

3. **clear_keyword_colors()**  
   - **Description**: Removes all keyword color mappings.

4. **clear_member_keyword_colors()**  
   - **Description**: Removes all member keyword color mappings.

5. **get_keyword_color(keyword)**  
   - **Parameters**:  
     - `keyword`: String (keyword to check).  
   - **Return**: `Color` (color for the keyword, or default if not set).

6. **get_member_keyword_color(member_keyword)**  
   - **Parameters**:  
     - `member_keyword`: String (member keyword to check).  
   - **Return**: `Color` (color for the member keyword, or default if not set).

7. **has_color_region(start_key)**  
   - **Parameters**:  
     - `start_key`: String (check if a color region exists for this key).  
   - **Return**: `bool` (true if region exists, false otherwise).

8. **has_keyword_color(keyword)**  
   - **Parameters**:  
     - `keyword`: String (check if a keyword is defined).  
   - **Return**: `bool` (true if keyword exists, false otherwise).

9. **has_member_keyword_color(member_keyword)**  
   - **Parameters**:  
     - `member_keyword`: String (check if a member keyword is defined).  
   - **Return**: `bool` (true if member keyword exists, false otherwise).

10. **remove_color_region(start_key)**  
    - **Parameters**:  
      - `start_key`: String (remove the color region associated with this key).  
    - **Description**: Removes a specific color region.

11. **remove_keyword_color(keyword)**  
    - **Parameters**:  
      - `keyword`: String (remove the keyword from color mappings).  
    - **Description**: Removes a keyword from the highlight list.

12. **remove_member_keyword_color(member_keyword)**  
    - **Parameters**:  
      - `member_keyword`: String (remove the member keyword from highlight list).  
    - **Description**: Removes a member keyword from the highlight list.

---

**Key Notes**  
- Keywords and member keywords cannot contain symbols except `_`.  
- Member keywords are only highlighted if not preceded by a `.`.  
- `line_only` parameter in `add_color_region` controls whether regions span lines.