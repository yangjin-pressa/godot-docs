The `EditorExportPlugin` class in Godot is designed to allow developers to customize the export process for their projects, enabling the addition of custom files, resources, and platform-specific configurations. Below is a structured explanation of its key methods and their purposes:

---

### **Private Methods**
1. **`_export_file(path, file, remap)`**
   - **Purpose**: Called when exporting a file. Overrides this method to handle custom export logic, such as skipping files or remapping resources.
   - **Parameters**:
     - `path`: The virtual path of the file to be exported.
     - `file`: The binary data of the file.
     - `remap`: If `true`, the current file is replaced with this custom file.
   - **Use Case**: Used to skip files or remap resources during the export process.

2. **`_get_export_options()`**
   - **Purpose**: Returns the export options for the plugin, such as custom settings or parameters.
   - **Return**: A `PackedStringArray` containing the options.

3. **`_get_export_preset()`**
   - **Purpose**: Returns the current export preset being used, which defines the export configuration (e.g., platform, settings).
   - **Return**: An `EditorExportPreset` instance.

4. **`_customize_resource(resource, path)`**
   - **Purpose**: Customizes a resource before it is exported. Useful for modifying resource paths, replacing assets, or altering file content.
   - **Parameters**:
     - `resource`: The resource to be customized.
     - `path`: The path of the resource in the project.

5. **`_update_android_prebuilt_manifest(manifest_data)`**
   - **Purpose**: Modifies the Android prebuilt manifest file. Developers can adjust the manifest's binary data (e.g., adding permissions, changing configurations).
   - **Parameters**:
     - `manifest_data`: The binary manifest data as a `PackedByteArray`.
   - **Return**: Modified manifest data as a `PackedByteArray`. If no changes are needed, return an empty array.

---

### **Public Methods**
1. **`add_file(path, file, remap)`**
   - **Purpose**: Adds a custom file to the export. The file is loaded from `path` and included in the export.
   - **Parameters**:
     - `path`: The virtual path for the file (e.g., `"res://custom.txt"`).
     - `file`: The binary data of the file.
     - `remap`: If `true`, the current file is replaced with this one.
   - **Use Case**: Adds static files (e.g., text files, JSON) that are not part of the project's standard assets.

2. **`add_ios_bundle_file(path)`**
   - **Purpose**: Adds an iOS bundle file (e.g., `..bundle`) to the export.
   - **Parameters**:
     - `path`: The path to the bundle file in the project.

3. **`add_ios_cpp_code(code)`**
   - **Purpose**: Adds C++ code to the iOS export. This code is appended to the final export and can be used for custom logic.
   - **Parameters**:
     - `code`: The C++ code to add.

4. **`add_ios_embedded_framework(path)`**
   - **Purpose**: Embeds a dynamic library (`.dylib`, `.framework`) into the iOS application bundle.
   - **Parameters**:
     - `path`: The path to the framework or library.

5. **`add_ios_framework(path)`**
   - **Purpose**: Adds a static library (`.a`) or dynamic library (`.dylib`, `.framework`) to the iOS project's linking phase.
   - **Parameters**:
     - `path`: The path to the library.

6. **`add_ios_linker_flags(flags)`**
   - **Purpose**: Adds linker flags for the iOS export (e.g., `-framework CoreData`).
   - **Parameters**:
     - `flags`: The linker flags as a string.

7. **`add_ios_plist_content(plist_content)`**
   - **Purpose**: Adds content to an iOS Property List (`.plist`) file. This is useful for configuring app settings or data.
   - **Parameters**:
     - `plist_content`: The content to add to the `.plist` file.

8. **`add_macos_plugin_file(path)`**
   - **Purpose**: Adds a file or directory to the `PlugIns` folder of a macOS app bundle.
   - **Parameters**:
     - `path`: The path to the file or directory.

9. **`add_shared_object(path, tags, target)`**
   - **Purpose**: Adds a shared object (e.g., `.so`) or directory containing shared objects to the export. On macOS, these are placed in the `Frameworks` directory.
   - **Parameters**:
     - `path`: The path to the shared object or directory.
     - `tags`: A list of tags for the shared object (e.g., `"native"`).
     - `target`: The destination path in the export.

10. **`get_export_platform()`**
    - **Purpose**: Returns the current export platform (e.g., `PLATFORM_WIN`, `PLATFORM_MAC`, etc.).
    - **Return**: An `EditorExportPlatform` enum value.

11. **`get_export_preset()`**
    - **Purpose**: Returns the current export preset being used.
    - **Return**: An `EditorExportPreset` instance.

12. **`get_option(name)`**
    - **Purpose**: Retrieves the current value of an export option defined by `_get_export_options()`.
    - **Parameters**:
      - `name`: The name of the option.
    - **Return**: The value of the option as a `Variant`.

13. **`skip()`**
    - **Purpose**: Skips the current file during the export process, preventing it from being included.
    - **Use Case**: Used to exclude specific files or resources from the export.

---

### **Key Considerations**
- **Platform-Specific Methods**: Many methods are tailored for specific platforms (e.g., iOS, Android, macOS). For example, `add_ios_framework` is only relevant for iOS, while `add_shared_object` is useful for macOS.
- **Customization Flow**: Plugins often override methods like `_customize_resource` to modify assets or `_update_android_prebuilt_manifest` to adjust manifest files.
- **File Remapping**: The `add_file` method with `remap = true` allows replacing files during export, useful for overriding assets with custom versions.

---

### **Example Use Case**
Suppose you want to add a custom font for iOS:
```gdscript
func _ready():
    add_ios_framework("res://Fonts/MyFont.framework")
```
This adds the Font framework to the iOS project, ensuring it's linked and available in the app.

---

### **Summary**
The `EditorExportPlugin` provides extensive control over the export process, allowing developers to add custom files, modify platform-specific configurations, and customize resources. By overriding key methods, plugins can tailor the export to meet specific project requirements, making it a powerful tool for advanced users.