# EditorFileSystemImportFormatSupportQuery

**Inherits:** RefCounted < Object

## Description
Used to query and configure import format support. Works with asset format import plugins.

## Methods
- _get_file_extensions(): Returns supported file extensions.
- _is_active(): Checks if the importer is active.
- _query(): Queries support; returns false if import should stop.

## Method Descriptions
- **_get_file_extensions()**  
  Returns the file extensions supported by this import format.

- **_is_active()**  
  Returns whether this importer is currently active.

- **_query()**  
  Queries support for the import format. Returns `false` if import should not proceed.