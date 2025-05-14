# ImageFormatLoaderExtension

**Inherits:** ImageFormatLoader < RefCounted < Object

## Description
Base class for creating ImageFormatLoader extensions to add support for additional image formats. Extend this class to implement custom image loaders. Call `add_format_loader()` to register the loader during initialization.

## Methods

- **_get_recognized_extensions**  
  Returns file extensions for this image format. Files with these extensions are loaded using this class.

- **_load_image**  
  Loads content from `fileaccess` into `image`. Parameters: image, fileaccess, flags (LoaderFlags), scale (float).

- **add_format_loader**  
  Adds this format loader to the engine, enabling recognition of extensions defined by `_get_recognized_extensions()`.

- **remove_format_loader**  
  Removes this format loader from the engine.

## Method Descriptions

### _get_recognized_extensions
- **Return Type:** PackedStringArray  
- **Purpose:** Define file extensions (e.g., ".myfmt") this loader supports.

### _load_image
- **Parameters:**  
  - `image`: Image object to populate  
  - `fileaccess`: FileAccess object containing the file data  
  - `flags`: LoaderFlags bitmask for loading options  
  - `scale`: Float for image scale factor  
- **Purpose:** Parse file data and populate the image object.

### add_format_loader
- **Purpose:** Register the loader with the engine to enable format recognition.

### remove_format_loader
- **Purpose:** Unregister the loader from the engine.