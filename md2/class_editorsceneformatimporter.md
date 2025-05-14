**EditorSceneFormatImporter**

**Description**  
A class for handling scene import logic, allowing users to define and process custom import options and behaviors.

---

**Methods**

- **_get_extensions**  
  Returns a `PackedStringArray` of supported file extensions.  
  - **Note**: This method is virtual and const, meaning it should be overridden by subclasses.

- **_get_import_options**  
  Adds specific import options (name and default value).  
  - **Note**: This method can only be called from `_get_import_options()`.

- **_get_option_visibility**  
  Determines if an import option is visible, returning a `Variant` (true/false/ignore).  
  - **Note**: This method is virtual and const.

- **_import_scene**  
  Performs the core scene import logic, using libraries like `GLTFDocument` or `FBXDocument`.  
  - **Parameters**: `path` (String), `flags` (int), `options` (Dictionary).  
  - **Note**: This method is virtual and must be implemented by subclasses.

- **add_import_option**  
  Adds a specific import option (name and default value).  
  - **Note**: This method is used within `_get_import_options()`.

- **add_import_option_advanced**  
  Adds a specific import option with advanced parameters (type, hint, etc.).  
  - **Note**: This method is also used within `_get_import_options()`.

---

**Constants**

- **IMPORT_SCENE**  
  Value: `1`  
  - **Note**: No description provided.

- **IMPORT_FLAG**  
  Value: `2`  
  - **Note**: No description provided.

- **IMPORT_OPTION**  
  Value: `3`  
  - **Note**: No description provided.

---

**Notes**  
- Methods like `_get_import_options` are used to define custom import settings.  
- Constants like `IMPORT_SCENE` are bitmask flags for import behavior.  
- The class is designed to be extended for custom formats (e.g., GLTF, FBX).