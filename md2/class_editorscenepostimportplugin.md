**Overview**  
The `EditorScenePostImportPlugin` is a class in Godot used to customize the import process of 3D scenes. It allows adding, modifying, or removing import options and processing scenes before or after loading.  

---

**Methods**  
- **`_get_import_options(path: String)`**  
  *Virtual*  
  Override to add general import options for the main import dock. Use `add_import_option()` or `add_import_option_advanced()` to add options.  

- **`_get_internal_import_options(category: int)`**  
  *Virtual*  
  Override to add internal import options for the 3D scene import dialog. Use `add_import_option()` or `add_import_option_advanced()` to add options.  

- **`_get_internal_option_update_view_required(category: int, option: String)`**  
  *Virtual*  
  Returns `true` if the 3D view needs to update when changing the specified internal option.  

- **`_get_internal_option_visibility(category: int, for_animation: bool, option: String)`**  
  *Virtual*  
  Returns `true` to show an internal option, `false` to hide it, or `null` to ignore.  

- **`_get_option_visibility(path: String, for_animation: bool, option: String)`**  
  *Virtual*  
  Returns `true` to show an option, `false` to hide it, or `null` to ignore.  

- **`_internal_process(category: int, base_node: Node, node: Node, resource: Resource)`**  
  *Virtual*  
  Processes a specific node or resource for a given category (e.g., nodes, meshes, animations).  

- **`_post_process(scene: Node)`**  
  *Virtual*  
  Post-processes the scene after the final scene has been configured.  

- **`_pre_process(scene: Node)`**  
  *Virtual*  
  Pre-processes the scene right after the scene format loader loads it. Adjust internal import options in keys like `"nodes"`, `"meshes"`, etc.  

- **`add_import_option(name: String, value: Variant)`**  
  Adds a basic import option (name and default value). Must be called from `_get_import_options()` or `_get_internal_import_options()`.  

- **`add_import_option_advanced(type: Variant.Type, name: String, default_value: Variant, hint: PropertyHint = 0, hint_string: String = "", usage_flags: int = 6)`**  
  Adds an advanced import option with type, hints, and flags. Must be called from `_get_import_options()` or `_get_internal_import_options()`.  

- **`get_option_value(name: StringName)`**  
  *Const*  
  Retrieves the value of an import option. Used by visibility checks or processing logic.  

---

**Enumerations**  
**`InternalImportCategory`**  
- **`NODES`** (0)  
- **`MESHES`** (1)  
- **`ANIMATIONS`** (2)  
- **`MATERIALS`** (3)  
- **`TEXTURES`** (4)  
- **`SHADERS`** (5)  
- **`OTHER`** (6)  

*Note: Descriptions for these constants are currently empty and require contributions.*  

---

**Key Notes**  
- **Virtual Methods**: Most methods are `virtual`, meaning they should be overridden by subclasses to customize behavior.  
- **Const Methods**: Methods marked `const` (e.g., `get_option_value`) do not modify the object’s state.  
- **Usage**: `add_import_option()` and `add_import_option_advanced()` are used to define options, while methods like `_get_internal_option_visibility()` control their visibility.