**Class: GLTFSkin**  
**Inherits:** Resource → RefCounted → Object  

---

### **Tutorials**  
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving)  

---

### **Properties**  
- **godot_skin**  
  - Type: Skin  
  - Set/get: `set_godot_skin(value: Skin)`, `get_godot_skin()`  

- **joints**  
  - Type: PackedInt32Array (default: `PackedInt32Array()`)  
  - Set/get: `set_joints(value: PackedInt32Array)`, `get_joints()`  
  - Note: Returns a copy of the array.  

- **skin_root**  
  - Type: int (default: `-1`)  
  - Set/get: `set_skin_root(value: int)`, `get_skin_root()`  

- **skeleton**  
  - Type: int (default: `-1`)  
  - Set/get: `set_skeleton(value: int)`, `get_skeleton()`  

- **skin_root**  
  - Type: int (default: `-1`)  
  - Set/get: `set_skin_root(value: int)`, `get_skin_root()`  

- **joints**  
  - Type: PackedInt32Array (default: `PackedInt32Array()`)  
  - Set/get: `set_joints(value: PackedInt32Array)`, `get_joints()`  
  - Note: Returns a copy of the array.  

---

### **Methods**  
- **get_inverse_binds()**  
  - Returns: `Array[Transform3D]`  
  - Note: No description available.  

- **get_joint_i_to_bone_i()**  
  - Returns: `Dictionary`  
  - Note: No description available.  

- **get_joint_i_to_name()**  
  - Returns: `Dictionary`  
  - Note: No description available.  

- **set_inverse_binds(inverse_binds: Array[Transform3D])**  
  - Note: No description available.  

- **set_joint_i_to_bone_i(joint_i_to_bone_i: Dictionary)**  
  - Note: No description available.  

- **set_joint_i_to_name(joint_i_to_name: Dictionary)**  
  - Note: No description available.  

---

### **Notes**  
- All properties and methods lack descriptions. Refer to [contributing one](doc_updating_the_class_reference) for details.  
- PackedInt32Array instances return copies, not references.