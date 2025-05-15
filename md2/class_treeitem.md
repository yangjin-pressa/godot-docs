Here's a concise guide to using the `TreeItem` class in Godot with the methods provided:

---

### **Key Methods for TreeItem**

#### **1. Text-related Methods**
- **`set_text(column, text)`**
  - Sets the text of a specific column.
  - **Example:**  
    ```gdscript
    tree_item.set_text(0, "Hello, World!")
    ```

- **`set_text_alignment(column, alignment)`**
  - Sets the text alignment for a column.
  - **Alignment Options:** `HORIZONTAL_ALIGNMENT_LEFT`, `HORIZONTAL_ALIGNMENT_CENTER`, `HORIZONTAL_ALIGNMENT_RIGHT`.
  - **Example:**  
    ```gdscript
    tree_item.set_text_alignment(1, HORIZONTAL_ALIGNMENT_CENTER)
    ```

- **`set_suffix(column, suffix)`**
  - Appends a suffix to the text in a column (e.g., "kg" after a number).
  - **Example:**  
    ```gdscript
    tree_item.set_suffix(0, " kg")
    ```

---

#### **2. Range (Sliders) Methods**
- **`set_range(column, value)`**
  - Sets the numeric value of a range column.
  - **Example:**  
    ```gdscript
    tree_item.set_range(0, 50.0)
    ```

- **`set_range_config(column, min, max, step, use_exponential)`**
  - Configures the range column's min, max, step, and exponential scale.
  - **Example:**  
    ```gdscript
    tree_item.set_range_config(0, 0, 100, 1, false)
    ```

---

#### **3. Indeterminate State (e.g. Checkboxes)**
- **`set_indeterminate(column, indeterminate)`**
  - Marks a column as indeterminate (e.g., for checkboxes with partial selection).
  - **Example:**  
    ```gdscript
    tree_item.set_indeterminate(0, true)
    ```

---

#### **4. Language and Metadata**
- **`set_language(column, language)`**
  - Sets the language code for text processing (e.g., `en`, `es`).
  - **Example:**  
    ```gdscript
    tree_item.set_language(1, "es")
    ```

- **`set_metadata(column, key, value)`**
  - Stores arbitrary data with a column for later retrieval.
  - **Example:**  
    ```gdscript
    tree_item.set_metadata(0, "source", "data123")
    ```

---

#### **5. Column Properties**
- **`set_selectable(column, selectable)`**
  - Enables or disables column selection.
  - **Example:**  
    ```gdscript
    tree_item.set_selectable(0, true)
    ```

---

### **Important Notes**
- **Columns are 0-indexed.**
- **Column modes** (e.g., `CELL_MODE_TEXT`, `CELL_MODE_RANGE`) must be set by the Tree widget before using these methods.
- **Use `get_metadata()`** to retrieve stored data.
- **Text alignment** and **suffix** are typically used for text columns, while **range** methods are for numeric sliders.

---

### **Example Workflow**
```gdscript
# Create a TreeItem
var item = TreeItem.new()

# Set text for column 0
item.set_text(0, "Sample Text")

# Set alignment for column 1
item.set_text_alignment(1, HORIZONTAL_ALIGNMENT_RIGHT)

# Configure a range column (column 2)
item.set_range(2, 75.0)
item.set_range_config(2, 0, 100, 1, false)

# Mark column 0 as indeterminate
item.set_indeterminate(0, true)

# Store metadata for column 1
item.set_metadata(1, "important", "yes")
```

This guide covers the core methods for customizing TreeItem columns in Godot, allowing for flexible UI elements.