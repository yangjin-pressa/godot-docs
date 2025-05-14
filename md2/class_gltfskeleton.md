# GLTFSkeleton

Inherits: Resource → RefCounted → Object

## Tutorials
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving)

## Properties
- **joints**: PackedInt32Array (default: empty)  
  - Set/Get: `set_joints()`, `get_joints()`
  - Note: Returns a copied array; changes do not affect the original.

- **roots**: PackedInt32Array (default: empty)  
  - Set/Get: `set_roots()`, `get_roots()`
  - Note: Returns a copied array; changes do not affect the original.

## Methods
- **get_bone_attachment(idx: int)** → BoneAttachment3D  
  - No description available.

- **get_bone_attachment_count()** → int  
  - No description available.

- **get_godot_bone_node()** → Dictionary  
  - Maps skeleton bone indices to glTF node indices. Used during export.

- **get_godot_skeleton()** → Skeleton3D  
  - No description available.

- **get_unique_names()** → Array<String>  
  - No description available.

- **set_godot_bone_node(godot_bone_node: Dictionary)**  
  - Sets mapping from skeleton bone indices to glTF node indices. Used during export.

- **set_unique_names(unique_names: Array<String>)**  
  - No description available.

## Notes
- Properties and methods marked with "No description available" require documentation updates.  
- The `get_godot_bone_node` method's Dictionary is unused during import but set during export.