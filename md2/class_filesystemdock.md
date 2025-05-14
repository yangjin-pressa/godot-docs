# FileSystemDock

## Inheritance Hierarchy
- `FileSystemDock`  
  → `VBoxContainer`  
  → `BoxContainer`  
  → `Container`  
  → `Control`  
  → `CanvasItem`  
  → `Node`  
  → `Object`

## Description
- Available only in `EditorPlugin` classes.
- Cannot be instantiated directly.
- Accessed via `EditorInterface.get_file_system_dock()`.

## Methods
- **add_resource_tooltip_plugin(plugin: `EditorResourceTooltipPlugin`)**  
  Registers a resource tooltip plugin.

- **navigate_to_path(path: `String`)**  
  Sets the specified path as currently selected, ensuring the file/directory is visible.

- **remove_resource_tooltip_plugin(plugin: `EditorResourceTooltipPlugin`)**  
  Removes a registered resource tooltip plugin (fails if not present).

## Signals
- **display_mode_changed()**  
  Emitted when file display mode or split mode changes.

- **file_removed(file: `String`)**  
  Emitted when the specified file is removed.

- **files_moved(old_file: `String`, new_file: `String`)**  
  Emitted when a file is moved from `old_file` to `new_file`.

- **folder_color_changed()**  
  Emitted when folders change color.

- **folder_moved(old_folder: `String`, new_folder: `String`)**  
  Emitted when a folder is moved from `old_folder` to `new_folder`.

- **folder_removed(folder: `String`)**  
  Emitted when the specified folder is removed.

- **inherit(file: `String`)**  
  Emitted when a new scene is created that inherits from the specified file.

- **instantiate(files: `PackedStringArray`)**  
  Emitted when scenes in the `files` list are being instantiated.

- **resource_removed(resource: `Resource`)**  
  Emitted when an external resource's file is removed.