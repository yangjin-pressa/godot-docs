# EditorExportPreset Class Documentation

The `EditorExportPreset` class manages export configurations for a game engine (e.g., Godot), allowing customization of export paths, filters, encryption settings, and other parameters. Below are the detailed methods and their purposes:

---

## **get_or_env**
```cpp
Variant get_or_env(StringName name, String env_var) const
```
**Description:**  
Returns an export option value or the value of an environment variable if it is set.  
**Parameters:**  
- `name`: The name of the export option.  
- `env_var`: The environment variable name to check.  
**Return:**  
A `Variant` representing the resolved value.  
**Note:** This method is `const` and does not modify the object.

---

## **get_export_filter**
```cpp
ExportFilter get_export_filter() const
```
**Description:**  
Returns the export filter mode selected in the "Resources" tab of the export dialog.  
**Return:**  
An `ExportFilter` enum value (e.g., `ExportFilter::EXPORT_ALL`, `ExportFilter::EXPORT_ONLY_TEXTURES`).  
**Note:** This method is `const`.

---

## **get_export_path**
```cpp
String get_export_path() const
```
**Description:**  
Returns the target export path.  
**Return:**  
A `String` representing the export directory.  
**Note:** This method is `const`.

---

## **get_file_export_mode**
```cpp
FileExportMode get_file_export_mode(String path, FileExportMode default = 0) const
```
**Description:**  
Returns the file export mode for a specific file.  
**Parameters:**  
- `path`: The file path to check.  
- `default`: Default mode if the file is not found.  
**Return:**  
A `FileExportMode` enum value (e.g., `FileExportMode::EXPORT_AS_PCK`, `FileExportMode::EXPORT_AS_TXT`).  
**Note:** This method is `const`.

---

## **get_files_to_export**
```cpp
PackedStringArray get_files_to_export() const
```
**Description:**  
Returns an array of files to export.  
**Return:**  
A `PackedStringArray` containing the file names.  
**Note:** This method is `const`.

---

## **get_encrypt_pck**
```cpp
bool get_encrypt_pck() const
```
**Description:**  
Returns whether PCK encryption is enabled.  
**Return:**  
A `bool` indicating the encryption status.  
**Note:** This method is `const`.

---

## **get_encrypt_directory**
```cpp
bool get_encrypt_directory() const
```
**Description:**  
Returns whether PCK directory encryption is enabled.  
**Return:**  
A `bool` indicating the encryption status.  
**Note:** This method is `const`.

---

## **get_encryption_key**
```cpp
String get_encryption_key() const
```
**Description:**  
Returns the PCK encryption key.  
**Return:**  
A `String` representing the encryption key.  
**Note:** This method is `const`.

---

## **get_encryption_in_filter**
```cpp
String get_encryption_in_filter() const
```
**Description:**  
Returns include filters for PCK encryption.  
**Return:**  
A `String` with filter patterns.  
**Note:** This method is `const`.

---

## **get_encryption_ex_filter**
```cpp
String get_encryption_ex_filter() const
```
**Description:**  
Returns exclude filters for PCK encryption.  
**Return:**  
A `String` with filter patterns.  
**Note:** This method is `const`.

---

## **get_exclude_filter**
```cpp
String get_exclude_filter() const
```
**Description:**  
Returns exclude filters for the export process.  
**Return:**  
A `String` with filter patterns.  
**Note:** This method is `const`.

---

## **get_include_filter**
```cpp
String get_include_filter() const
```
**Description:**  
Returns include filters for the export process.  
**Return:**  
A `String` with filter patterns.  
**Note:** This method is `const`.

---

## **get_patches**
```cpp
PackedStringArray get_patches() const
```
**Description:**  
Returns the list of packs to base a patch export on.  
**Return:**  
A `PackedStringArray` containing pack names.  
**Note:** This method is `const`.

---

## **get_preset_name**
```cpp
String get_preset_name() const
```
**Description:**  
Returns the name of the export preset.  
**Return:**  
A `String` representing the preset name.  
**Note:** This method is `const`.

---

## **get_project_setting**
```cpp
Variant get_project_setting(StringName name) const
```
**Description:**  
Returns a project setting using preset overrides instead of the current OS features.  
**Parameters:**  
- `name`: The name of the setting.  
**Return:**  
A `Variant` representing the setting value.  
**Note:** This method is `const`.

---

## **get_script_export_mode**
```cpp
int get_script_export_mode() const
```
**Description:**  
Returns the script export mode as an integer.  
**Return:**  
An `int` representing the mode (e.g., `SCRIPT_EXPORT_MODE_DEFAULT`).  
**Note:** This method is `const`.

---

## **get_version**
```cpp
String get_version(StringName name, bool windows_version) const
```
**Description:**  
Returns the version number, possibly falling back to project settings.  
**Parameters:**  
- `name`: The name of the version.  
- `windows_version`: Whether to format for Windows.  
**Return:**  
A `String` representing the version.  
**Note:** This method is `const`.

---

## **has**
```cpp
bool has(StringName property) const
```
**Description:**  
Checks if the preset has a specific property.  
**Parameters:**  
- `property`: The property name.  
**Return:**  
A `bool` indicating the presence of the property.  
**Note:** This method is `const`.

---

## **has_export_file**
```cpp
bool has_export_file(String path) const
```
**Description:**  
Checks if a specific file is included in the export.  
**Parameters:**  
- `path`: The file path to check.  
**Return:**  
A `bool` indicating whether the file is exported.  
**Note:** This method is `const`.

---

## **is_dedicated_server**
```cpp
bool is_dedicated_server() const
```
**Description:**  
Checks if dedicated server mode is selected.  
**Return:**  
A `bool` indicating the mode status.  
**Note:** This method is `const`.

---

## **is_runnable**
```cpp
bool is_runnable() const
```
**Description:**  
Checks if the "Runnable" option is enabled.  
**Return:**  
A `bool` indicating the status.  
**Note:** This method is `const`.

---

## **Notes**
- All methods are `const`, meaning they do not modify the object.  
- Some methods (e.g., `get_or_env`) may be overridden in subclasses to extend functionality.  
- The `ExportFilter` and `FileExportMode` enums define specific export behaviors (e.g., including textures, exporting as PCK, etc.).  
- The `get_version` method may use project settings as a fallback if no version is specified.  

This class provides a comprehensive way to customize and retrieve export configurations for a game engine project.