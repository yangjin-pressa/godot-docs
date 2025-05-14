Here's a structured documentation for the `EditorFileDialog` class, organized into key sections:

---

### **Properties**
- **access**: A constant indicating the type of access (e.g., read, write).  
- **name**: A string representing the name of the dialog.  
- **type**: An enum specifying the dialog type (e.g., FILE, FOLDER, DIRECTORY).  

---

### **Enums**
- **Type**:  
  - `FILE`: Open or save a file.  
  - `FOLDER`: Open a folder.  
  - `DIRECTORY`: Open a directory.  

---

### **Methods**
#### **Properties**
- **get_filename_filter()**:  
  Returns the current filename filter as a string.  

- **set_filename_filter(filter)**:  
  Sets the filename filter.  

- **clear_filename_filter()**:  
  Clears the filename filter.  

- **clear_filters()**:  
  Removes all filters except "All Files (*.*)".  

---

#### **Options**
- **add_option(name, values, default_value_index)**:  
  Adds an option button or checkbox to the dialog. If `values` is empty, a checkbox is added.  

- **get_option_name(option)**:  
  Returns the name of the option at the specified index.  

- **get_option_values(option)**:  
  Returns the values array for the option at the specified index.  

- **get_option_default(option)**:  
  Returns the default value index for the option.  

- **set_option_name(option, name)**:  
  Sets the name of the option.  

- **set_option_values(option, values)**:  
  Sets the values for the option.  

- **set_option_default(option, default_value_index)**:  
  Sets the default value index for the option.  

- **get_selected_options()**:  
  Returns a dictionary of selected values for all options.  

---

#### **UI Elements**
- **get_line_edit()**:  
  Returns the `LineEdit` widget for the selected file.  
  **Note**: This is an internal node. Do not remove or free it; use `visible` to hide it.  

- **get_vbox()**:  
  Returns the `VBoxContainer` used to display the file system.  
  **Note**: This is an internal node. Do not remove or free it; use `visible` to hide it.  

---

#### **Dialog Management**
- **invalidate()**:  
  Notifies the dialog that its data view is outdated. Updates the UI on the next refresh.  

- **popup_file_dialog()**:  
  Displays the dialog at the default size and position, selecting the current file if available.  

- **add_side_menu(menu, title)**:  
  Adds a custom menu to the side of the dialog. Only one side menu is allowed.  

---

### **Important Notes**
- **Internal Nodes**: `LineEdit` and `VBoxContainer` are internal nodes. Modifying them directly may cause crashes. Use `visible` to hide them instead.  
- **Filter Rules**: Filename filters must follow pattern rules (e.g., `*.tscn`). Filters starting with `.` are invalid.  
- **Default Values**: For checkboxes, `default_value_index` should be `1` (checked) or `0` (unchecked).  

---

This documentation covers all methods, properties, and enums of the `EditorFileDialog` class, ensuring clarity and usability for developers.