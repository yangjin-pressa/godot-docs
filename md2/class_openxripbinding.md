# OpenXRIPBinding

**Inherits:** `Resource` → `RefCounted` → `Object`

## Overview
A class that binds an OpenXR action to an input/output device path. Supports multiple bindings for symmetric controllers (e.g., left/right hand actions).

---

## Core Properties

- **action**  
  - Type: `OpenXRAction`  
  - Description: Action bound to `binding_path`  
  - setter: `set_action()`  
  - getter: `get_action()`  

- **binding_modifiers**  
  - Type: `Array`  
  - Default: `[]`  
  - Description: Modifiers for this binding  
  - setter: `set_binding_modifiers()`  
  - getter: `get_binding_modifiers()`  

- **binding_path**  
  - Type: `String`  
  - Default: `""`  
  - Description: Suggests input/output path (runtime may vary)  
  - setter: `set_binding_path()`  
  - getter: `get_binding_path()`  

- **paths**  
  - Type: `PackedStringArray`  
  - Deprecated: Use `binding_path` instead  
  - Description: Array of input/output paths (copied, not linked)  
  - setter: `set_paths()`  
  - getter: `get_paths()`  

---

## Core Methods

- **add_path(path: String)**  
  - Deprecated: Use `binding_path` instead  
  - Adds a single input/output path  

- **get_binding_modifier(index: int)**  
  - Returns a binding modifier at specified index  

- **get_binding_modifier_count()**  
  - Returns number of binding modifiers  

- **get_path_count()**  
  - Deprecated: Use `binding_path` instead  
  - Returns number of paths (always 1)  

- **has_path(path: String)**  
  - Deprecated: Use `binding_path` instead  
  - Checks if path exists in binding  

- **remove_path(path: String)**  
  - Deprecated: Use `binding_path` instead  
  - Removes a path from binding  

---

## Notes
- Multiple bindings allowed for symmetric controllers (e.g., left/right fire actions)  
- `paths` property is deprecated in favor of `binding_path`  
- Binding paths are suggestions; runtime may adjust them  
- `PackedStringArray` methods return copies, not references