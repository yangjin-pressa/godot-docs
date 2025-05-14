The `FileDialog` class in Godot is a powerful tool for allowing users to interact with files and folders in your application. Below is a structured breakdown of how to use and customize this class effectively:

---

### **Key Properties**
1. **`mode`**  
   - **Type**: `FileDialog.Mode`  
   - **Description**: Specifies the dialog mode (open, save, folder).  
   - **Example**:  
     ```gdscript
     file_dialog.mode = FileDialog.MODE_OPEN
     ```

2. **`title`**  
   - **Type**: `String`  
   - **Description**: Sets the title of the dialog.  
   - **Example**:  
     ```gdscript
     file_dialog.title = "Select a File"
     ```

3. **`root`**  
   - **Type**: `String`  
   - **Description**: Sets the starting directory for the dialog.  
   - **Example**:  
     ```gdscript
     file_dialog.root = "user_home"
     ```

4. **`default_file`**  
   - **Type**: `String`  
   - **Description**: Sets a default file to pre-select.  
   - **Example**:  
     ```gdscript
     file_dialog.default_file = "example.txt"
     ```

5. **`file_filter`**  
   - **Type**: `String`  
   - **Description**: Filters files by extension (e.g., "txt, pdf").  
   - **Example**:  
     ```gdscript
     file_dialog.file_filter = "Text files (*.txt), All files (*.*)"
     ```

---

### **Methods**
1. **`show()`**  
   - **Description**: Displays the dialog.  
   - **Example**:  
     ```gdscript
     file_dialog.show()
     ```

2. **`get_file()`**  
   - **Description**: Returns the selected file path.  
   - **Example**:  
     ```gdscript
     var selected_file = file_dialog.get_file()
     ```

3. **`get_directory()`**  
   - **Description**: Returns the selected directory path.  
   - **Example**:  
     ```gdscript
     var selected_directory = file_dialog.get_directory()
     ```

4. **`get_preview()`**  
   - **Description**: Returns the preview of the selected file (if enabled).  
   - **Example**:  
     ```gdscript
     var preview = file_dialog.get_preview()
     ```

5. **`get_selected_options()`**  
   - **Description**: Retrieves user-selected options (e.g., checkboxes).  
   - **Example**:  
     ```gdscript
     var options = file_dialog.get_selected_options()
     ```

6. **`add_option()`**  
   - **Description**: Adds custom controls (e.g., checkboxes, buttons) to the dialog.  
   - **Example**:  
     ```gdscript
     var options = [
         {"name": "Option 1", "values": ["A", "B", "C"]},
         {"name": "Option 2", "values": ["X", "Y", "Z"]}
     ]
     file_dialog.add_option(options)
     ```

---

### **Theme Customization**
1. **Custom Icons**  
   - Use `theme_icon_*` properties to replace default icons (e.g., `back_folder`, `reload`).  
   - **Example**:  
     ```gdscript
     file_dialog.theme_icon_back_folder = preload("res://icons/back.png")
     ```

2. **Color Themes**  
   - Modify theme colors for disabled files, icons, etc.  
   - **Example**:  
     ```gdscript
     file_dialog.theme_color_file_disabled_color = Color(0.5, 0.5, 0.5, 0.3)
     ```

3. **Custom Controls**  
   - Use `get_vbox()` to add custom UI elements to the dialog.  
   - **Example**:  
     ```gdscript
     var vbox = file_dialog.get_vbox()
     var button = VBoxContainer.new()
     button.add_child(Button.new())
     vbox.add_child(button)
     ```

---

### **Handling Native File Dialogs**
- **`invalidate()`**: No effect on native dialogs. Use `show()` to trigger the dialog.  
- **`root` and `default_file`**: These are respected by the native dialog, but the user must ensure the path exists.  
- **`file_filter`**: Supported in most platforms, but ensure the filter is compatible with the OS (e.g., Windows vs. macOS).

---

### **Common Use Cases**
1. **Open a File**:  
   ```gdscript
   file_dialog.mode = FileDialog.MODE_OPEN
   file_dialog.show()
   var file_path = file_dialog.get_file()
   ```

2. **Save a File**:  
   ```gdscript
   file_dialog.mode = FileDialog.MODE_SAVE
   file_dialog.show()
   var save_path = file_dialog.get_file()
   ```

3. **Select a Folder**:  
   ```gdscript
   file_dialog.mode = FileDialog.MODE_FOLDER
   file_dialog.show()
   var folder_path = file_dialog.get_directory()
   ```

4. **Custom Checkbox Options**:  
   ```gdscript
   var options = [
       {"name": "Format", "values": ["PDF", "DOCX"]},
       {"name": "Compression", "values": ["None", "ZIP"]}
   ]
   file_dialog.add_option(options)
   ```

---

### **Best Practices**
- **Error Handling**: Check if `get_file()` or `get_directory()` returns a valid path before using it.  
- **Platform Compatibility**: Test with native file dialogs (e.g., Windows Explorer, macOS Finder) to ensure consistent behavior.  
- **Performance**: Avoid frequent calls to `invalidate()` on native dialogs.  

By leveraging these properties and methods, you can create a flexible and visually customized file dialog that integrates seamlessly into your Godot project.