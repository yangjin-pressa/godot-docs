# ResourceSaver

## Overview
A singleton for saving resource types to the filesystem. Uses `ResourceFormatSaver` classes to save resources to text-based or binary files.

---

## Key Methods

- **add_resource_format_saver**  
  Registers a `ResourceFormatSaver` for resource saving.  
  Parameters: `format_saver` (ResourceFormatSaver), `at_front` (bool)  

- **get_recognized_extensions**  
  Returns extensions available for a given resource type.  
  Parameter: `type` (Resource)  

- **get_resource_id_for_path**  
  Retrieves resource ID for a path. Generates if `generate` is true.  
  Parameters: `path` (String), `generate` (bool)  

- **remove_resource_format_saver**  
  Unregisters a `ResourceFormatSaver`.  
  Parameter: `format_saver` (ResourceFormatSaver)  

- **save**  
  Saves a resource to disk. Uses flags to customize behavior.  
  Parameters: `resource` (Resource), `path` (String), `flags` (bitfield of SaverFlags)  

- **set_uid**  
  Sets UID for a resource path.  
  Parameters: `resource` (String), `uid` (int)  

---

## SaverFlags (Bitfield)

- **FLAG_NONE** = 0  
  No resource saving option.  

- **FLAG_RELATIVE_PATHS** = 1  
  Save with path relative to the scene.  

- **FLAG_BUNDLE_RESOURCES** = 2  
  Bundles external resources.  

- **FLAG_CHANGE_PATH** = 4  
  Updates resource path to new location.  

- **FLAG_OMIT_EDITOR_PROPERTIES** = 8  
  Excludes editor-specific metadata.  

- **FLAG_SAVE_BIG_ENDIAN** = 16  
  Save as big endian (FileAccess.big_endian).  

- **FLAG_COMPRESS** = 32  
  Compresses resource using ZSTD.  

- **FLAG_REPLACE_SUBRESOURCE_PATHS** = 64  
  Overrides subresource paths.  

---

## Notes
- When running, generated UID is not saved (only editor mode applies).  
- `set_uid` is for specific cases where automatic UID generation is not desired.