# ResourcePreloader

**Inherits:** Node < Object

A node used to preload sub-resources inside a scene.

## Description

Preloads resources in a scene for immediate access. Useful for complex scenarios where GDScript's `@GDScript.preload()` isn't sufficient.

## Methods

- **add_resource(name: StringName, resource: Resource)**  
  Adds a resource. If a name exists, it will be renamed to "name N".

- **get_resource(name: StringName)** → Resource  
  Retrieves a resource by name.

- **get_resource_list()** → PackedStringArray  
  Returns a list of all preloaded resources.

- **has_resource(name: StringName)** → bool  
  Checks if a resource exists by name.

- **remove_resource(name: StringName)**  
  Removes a resource by name.

- **rename_resource(name: StringName, newname: StringName)**  
  Renames a resource within the preloader.

## Notes
- Use with caution for large resources to avoid memory issues.
- Resources are preloaded when the scene is loaded.