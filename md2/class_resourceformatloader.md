# ResourceFormatLoader Class Documentation

## Overview
The `ResourceFormatLoader` class is used to load and manage resources in the Godot engine. It provides methods to handle resource loading, dependencies, and recognition based on file extensions and types.

---

## Description
- **Purpose**: Defines how the engine loads resources from files, including handling dependencies, resource types, and caching.
- **Key Notes**:
  - Extend this class to customize resource loading behavior.
  - For custom resource types, use `ClassDB` to register them, or return `"Resource"` as a fallback.
  - Use `EditorImportPlugin` for specialized resource import logic.

---

## Enumerations

### `CacheMode`
Defines how the resource cache is used during loading.

- **OK**: Default behavior (no special handling).
- **REUSE**: Reuse existing cached resources.
- **UPDATE**: Update the cache with new data.
- **DISCARD**: Discard the cache and reload.

---

## Methods

### `_get_recognized_extensions()`
**Returns**: `PackedStringArray`  
**Description**: Returns the list of file extensions this loader can read.

### `_get_resource_type(path: String) -> String`
**Description**: Returns the class name of the resource at the given path. Returns `"Resource"` for unknown types.

### `_get_resource_script_class(path: String) -> String`
**Description**: Returns the script class name associated with the resource. Returns `""` if no script is defined.

### `_get_resource_uid(path: String) -> int`
**Description**: Returns a unique ID for the resource. If not overridden, a `.uid` file is generated.

### `_handles_type(type: StringName) -> bool`
**Description**: Determines if this loader can handle a given resource type. Returns `true` for `"Resource"` for custom types.

### `_load(path: String, original_path: String, use_sub_threads: bool, cache_mode: int) -> Variant`
**Description**: Loads a resource. Returns a `Resource` object on success, or an `Error` constant on failure.  
**Parameters**:
- `path`: The file path.
- `original_path`: Source file path if the resource is imported.
- `use_sub_threads`: Whether to use sub-threads for loading.
- `cache_mode`: Control cache behavior (use `CacheMode` enum).

### `_recognize_path(path: String, type: StringName) -> bool`
**Description**: Determines if this loader should load a resource from the given path for the specified type.  
**Default Behavior**:
- Checks if the file extension matches `_get_recognized_extensions()`.
- Checks if the type matches `_get_resource_type()`.

### `_get_dependencies(path: String, add_types: bool) -> PackedStringArray`
**Description**: Returns the dependencies of a resource. If `add_types` is `true`, paths are formatted as `Path::TypeName`.  
**Note**: Custom resource types may return `"Resource"` as a fallback.

### `_rename_dependencies(path: String, renames: Dictionary) -> Error`
**Description**: Renames dependencies within a resource and saves it.  
**Parameters**:
- `renames`: Dictionary mapping old paths to new paths.
**Returns**: `OK` on success, or an `Error` constant on failure.

### `_get_classes_used(path: String) -> PackedStringArray`
**Description**: Returns the classes used by a resource. Currently has no description.

### `_get_resource_uid(path: String) -> int`
**Description**: Returns the unique ID for a resource. If not overridden, a `.uid` file is generated.

---

## Notes
- Custom resource types defined by scripts may not be recognized by `ClassDB`. Use `"Resource"` as a fallback.
- The `cache_mode` parameter controls how resources are cached during loading.
- The `_recognize_path()` method's default behavior is based on file extensions and resource types.