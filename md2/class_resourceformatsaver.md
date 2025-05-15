# ResourceFormatSaver

**Inherits:** RefCounted < Object

Saves a specific resource type to a file.

## Description

The engine can save resources when you do it from the editor, or when you use the ResourceSaver singleton. This is accomplished thanks to multiple ResourceFormatSaver's, each handling its own format and called automatically by the engine.

By default, Godot saves resources as .tres (text-based), .res (binary) or another built-in format, but you can choose to create your own format by extending this class. Be sure to respect the documented return types and values.

## Methods

- **_get_recognized_extensions**: Returns the list of extensions available for saving the resource object, provided it is recognized.
- **_recognize**: Returns whether the given resource object can be saved by this saver.
- **_recognize_path**: Returns true if this saver handles a given save path and false otherwise.
- **_save**: Saves the given resource object to a file at the target path. Returns OK on success, or an Error constant in case of failure.
- **_set_uid**: Sets a new UID for the resource at the given path. Returns OK on success, or an Error constant in case of failure.

## Method Descriptions

- **_get_recognized_extensions**: 
  - Return type: PackedStringArray
  - Parameters: resource: Resource
  - Notes: This method should typically be overridden by the user to have any effect.

- **_recognize**: 
  - Return type: bool
  - Parameters: resource: Resource
  - Notes: This method has no side effects. It doesn't modify any of the instance's member variables.

- **_recognize_path**: 
  - Return type: bool
  - Parameters: resource: Resource, path: String
  - Notes: If this method is not implemented, the default behavior returns whether the path's extension is within the ones provided by _get_recognized_extensions.

- **_save**: 
  - Return type: Error
  - Parameters: resource: Resource, path: String, flags: int
  - Notes: Flags is a bitmask composed with SaverFlags constants.

- **_set_uid**: 
  - Return type: Error
  - Parameters: path: String, uid: int
  - Notes: Returns OK on success, or an Error constant in case of failure.