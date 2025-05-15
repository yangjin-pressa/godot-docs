# ProjectSettings Class Documentation

## Overview

The `ProjectSettings` class in Godot is a critical component for managing global configuration settings for a project. It allows developers to store, retrieve, and modify settings that affect the behavior of the engine, project settings, and custom configurations. This class provides methods for interacting with configuration files, handling file paths, and managing resource packs.

---

## Key Methods

### 1. **`set_setting(name: String, value: Variant)`**
**Purpose**: Sets the value of a specified setting.
**Parameters**:
- `name`: The name of the setting.
- `value`: The new value to assign to the setting.
**Example**:
```gdscript
ProjectSettings.set_setting("application/config/name", "Example")
```
**Note**: To delete a custom setting, set the value to `null`.

---

### 2. **`get_setting(name: String) -> Variant`**
**Purpose**: Retrieves the value of a specified setting.
**Parameters**:
- `name`: The name of the setting.
**Return Value**: The value of the setting, or `null` if it doesn't exist.

---

### 3. **`save()`**
**Purpose**: Saves the configuration to the `project.godot` file.
**Note**: This method is intended for use by editor plugins. Modifications to `ProjectSettings` in exported projects cannot be loaded back into the running app.

---

### 4. **`save_custom(file: String)`**
**Purpose**: Saves the configuration to a custom file.
**Parameters**:
- `file`: The path to the file (e.g., `"override.cfg"` for exported projects).
**Supported Formats**:
- `.godot`: Text-based `ConfigFile` format.
- `.binary`: Binary format.
**Note**: Use `"override.cfg"` for exported projects, which is text-based but not suitable for other formats.

---

### 5. **`load_resource_pack(pack: String, replace_files: bool = true, offset: int = 0)`**
**Purpose**: Loads a .pck or .zip resource pack into the resource filesystem (`res://`).
**Parameters**:
- `pack`: Path to the resource pack file.
- `replace_files`: If `true`, replaces existing files with those from the pack.
- `offset`: Offset in bytes for .pck files.
**Note**: `DirAccess` does not reflect changes made to `res://` after this call.

---

### 6. **`globalize_path(path: String) -> String`**
**Purpose**: Converts a localized path (e.g., `res://`) to an absolute, OS-dependent path.
**Example**:
```gdscript
var absolute_path = ProjectSettings.globalize_path("res://hello.txt")
```
**Note**: For exported projects, prepend the executable's base directory to paths when using `res://`.

---

### 7. **`localize_path(path: String) -> String`**
**Purpose**: Converts an absolute OS path to a localized path (e.g., `res://`).
**See**: [globalize_path()](#6) for related usage.

---

### 8. **`has_setting(name: String) -> bool`**
**Purpose**: Checks if a setting exists.
**Return Value**: `true` if the setting is present.

---

### 9. **`set_order(name: String, position: int)`**
**Purpose**: Sets the order of a setting for file-saving purposes.
**Parameters**:
- `name`: The setting name.
- `position`: Position in the configuration file.

---

### 10. **`set_as_basic(name: String, basic: bool)`**
**Purpose**: Marks a setting as basic or advanced. Basic settings are always visible in the editor.
**Parameters**:
- `name`: Setting name.
- `basic`: `true` for basic, `false` for advanced.

---

### 11. **`set_as_internal(name: String, internal: bool)`**
**Purpose**: Marks a setting as internal. Internal settings are not visible in the editor.
**Parameters**:
- `name`: Setting name.
- `internal`: `true` for internal, `false` for external.

---

### 12. **`set_initial_value(name: String, value: Variant)`**
**Purpose**: Sets the initial value of a setting (reverts to this value if changed).
**Parameters**:
- `name`: Setting name.
- `value`: Initial value.

---

### 13. **`set_restart_if_changed(name: String, restart: bool)`**
**Purpose**: Specifies whether a setting requires an editor restart to take effect.
**Note**: This is a hint for the user; it does not delay the setting's application.

---

## Important Notes

### 1. **Path Handling**
- **`globalize_path()`** converts localized paths (e.g., `res://`) to OS-dependent paths.
- **`localize_path()`** does the reverse.
- For exported projects, use `OS.get_executable_path().get_base_dir()` to handle `res://` paths correctly.

### 2. **Resource Packs**
- Loading a .pck or .zip file replaces existing files in `res://` unless `replace_files` is set to `false`.
- The `offset` parameter is only supported for `.pck` files.

### 3. **Override.cfg**
- Use `save_custom("override.cfg")` for exported projects to persist settings without requiring the `.godot` file.
- This file is text-based and compatible with exported projects.

### 4. **Saving vs. Loading**
- `save()` saves to `project.godot` (editor-specific).
- `save_custom()` saves to a custom file, suitable for exported projects.

---

## Usage Examples

### Example 1: Save Custom Settings
```gdscript
ProjectSettings.set_setting("audio/preferred_device", "Headphones")
ProjectSettings.save_custom("override.cfg")
```

### Example 2: Load a Resource Pack
```gdscript
var success = ProjectSettings.load_resource_pack("res://resource_pack.pck", replace_files=false)
if success:
    print("Resource pack loaded successfully.")
else:
    print("Failed to load resource pack.")
```

### Example 3: Handle Paths in Exported Projects
```gdscript
var base_dir = OS.get_executable_path().get_base_dir()
var localized_path = "res://asset.png"
var absolute_path = ProjectSettings.globalize_path(localized_path)
print("Absolute path: ", absolute_path)
```

---

## Summary

The `ProjectSettings` class offers a robust way to manage global and custom configurations in Godot. By understanding its methods and notes, developers can effectively tailor project behavior, persist settings, and handle resource management across different environments (editor, exported projects, etc.). Always ensure paths are correctly localized and resource packs are handled with care to avoid conflicts.