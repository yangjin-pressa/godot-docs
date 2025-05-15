# ShaderIncludeDB

**Inherits:** Object

## Description
Contains shader fragments for Godot's internal shaders. Used when accessing internal uniform buffers/functions. Only fragments for the current rendering device are loaded.

## Methods

- **get_built_in_include_file(filename: String)**  
  Returns the code for a built-in shader fragment. Accessed via `#include "filename"` in shader code.

- **has_built_in_include_file(filename: String)**  
  Returns `true` if a include file with this name exists.

- **list_built_in_include_files()**  
  Returns a list of currently registered built-in include files.

## Key Notes
- All methods are **static** and do not require instance instantiation.
- Files are device-specific and only loaded for the current rendering device.