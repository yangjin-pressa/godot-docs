# GDExtensionManager

## Overview
Provides access to GDExtension functionality. Loads, initializes, and tracks GDExtension libraries.

## Tutorials
- [GDExtension overview](../tutorials/scripting/gdextension/what_is_gdextension)
- [GDExtension example in C++](../tutorials/scripting/cpp/gdextension_cpp_example)

## Methods

- **get_extension(path: String)** → GDExtension  
  Returns GDExtension at given path or null if not loaded.

- **get_loaded_extensions()** → PackedStringArray  
  Returns file paths of all currently loaded extensions.

- **is_extension_loaded(path: String)** → bool  
  Returns true if extension at path has been successfully loaded.

- **load_extension(path: String)** → LoadStatus  
  Loads extension by absolute path. Returns LOAD_STATUS_OK if successful.

- **reload_extension(path: String)** → LoadStatus  
  Reloads extension. Only works in editor builds. Returns LOAD_STATUS_FAILED in release builds.

- **unload_extension(path: String)** → LoadStatus  
  Unloads extension. Returns LOAD_STATUS_NOT_LOADED if not loaded.

## Signals

- **extension_loaded(extension: GDExtension)**  
  Emited after editor loads new extension. Only in editor builds.

- **extension_unloading(extension: GDExtension)**  
  Emited before editor unloads extension. Only in editor builds.

- **extensions_reloaded()**  
  Emited after editor reloads one or more extensions.

## Enumerations

### LoadStatus
- **LOAD_STATUS_OK** = 0  
  Extension loaded successfully.

- **LOAD_STATUS_FAILED** = 1  
  Extension failed to load (missing dependencies, etc.).

- **LOAD_STATUS_ALREADY_LOADED** = 2  
  Extension already loaded.

- **LOAD_STATUS_NOT_LOADED** = 3  
  Extension not loaded.

- **LOAD_STATUS_NEEDS_RESTART** = 4  
  Extension requires application restart.