# Skeleton3D Class Documentation

The `Skeleton3D` class in Godot is used to manage skeletal animation, allowing you to define bones, their hierarchies, and poses. Below is a detailed documentation of its methods and their purposes:

---

## **Bone Management**

### `set_bone_name`
```gdscript
func set_bone_name(bone_idx: int, name: String)
```
**Description:**  
Sets the name of the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.
- `name`: New name for the bone.

---

### `get_bone_name`
```gdscript
func get_bone_name(bone_idx: int) -> String
```
**Description:**  
Retrieves the name of the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.

---

### `set_bone_parent`
```gdscript
func set_bone_parent(bone_idx: int, parent_idx: int)
```
**Description:**  
Sets the parent of the bone at the specified index. If `parent_idx` is -1, the bone has no parent.

**Parameters:**
- `bone_idx`: Index of the bone.
- `parent_idx`: Index of the parent bone.

**Note:** `parent_idx` must be less than `bone_idx` to maintain hierarchy.

---

### `get_bone_parent`
```gdscript
func get_bone_parent(bone_idx: int) -> int
```
**Description:**  
Retrieves the parent index of the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.

---

### `unparent_bone_and_rest`
```gdscript
func unparent_bone_and_rest(bone_idx: int)
```
**Description:**  
Removes the bone from its parent hierarchy and sets its rest position to the position it had before being reset.

**Parameters:**
- `bone_idx`: Index of the bone.

---

## **Pose Management**

### `set_bone_pose`
```gdscript
func set_bone_pose(bone_idx: int, pose: Transform3D)
```
**Description:**  
Sets the pose (transform) of the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.
- `pose`: New pose for the bone.

**Note:** This method modifies the bone's pose directly, which may affect performance if multiple bones are modified.

---

### `set_bone_pose_position`
```gdscript
func set_bone_pose_position(bone_idx: int, position: Vector3)
```
**Description:**  
Sets the position of the bone's pose, local to the skeleton.

**Parameters:**
- `bone_idx`: Index of the bone.
- `position`: New position for the bone.

---

### `set_bone_pose_rotation`
```gdscript
func set_bone_pose_rotation(bone_idx: int, rotation: Quaternion)
```
**Description:**  
Sets the rotation of the bone's pose, local to the skeleton.

**Parameters:**
- `bone_idx`: Index of the bone.
- `rotation`: New rotation for the bone.

---

### `set_bone_pose_scale`
```gdscript
func set_bone_pose_scale(bone_idx: int, scale: Vector3)
```
**Description:**  
Sets the scale of the bone's pose, local to the skeleton.

**Parameters:**
- `bone_idx`: Index of the bone.
- `scale`: New scale for the bone.

---

### `reset_bone_pose`
```gdscript
func reset_bone_pose(bone_idx: int)
```
**Description:**  
Resets the bone's pose to its rest position.

---

### `reset_bone_poses`
```gdscript
func reset_bone_poses()
```
**Description:**  
Resets all bones to their rest positions.

---

### `set_bone_enabled`
```gdscript
func set_bone_enabled(bone_idx: int, enabled: bool = true)
```
**Description:**  
Enables or disables the bone's pose. If `enabled` is `false`, the bone's pose is not applied.

**Parameters:**
- `bone_idx`: Index of the bone.
- `enabled`: Boolean to enable or disable the pose.

---

## **Rest Pose Management**

### `set_bone_rest`
```gdscript
func set_bone_rest(bone_idx: int, rest: Transform3D)
```
**Description:**  
Sets the rest transform for the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.
- `rest`: New rest transform for the bone.

---

### `get_bone_rest`
```gdscript
func get_bone_rest(bone_idx: int) -> Transform3D
```
**Description:**  
Retrieves the rest transform of the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.

---

## **Global Pose Management**

### `set_bone_global_pose`
```gdscript
func set_bone_global_pose(bone_idx: int, pose: Transform3D)
```
**Description:**  
Sets the global pose of the bone. This method may cause performance issues if applied to multiple bones.

**Parameters:**
- `bone_idx`: Index of the bone.
- `pose`: New global pose for the bone.

---

## **Metadata**

### `set_bone_meta`
```gdscript
func set_bone_meta(bone_idx: int, key: String, value: Variant)
```
**Description:**  
Sets a metadata key-value pair for the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.
- `key`: Metadata key.
- `value`: Value to associate with the key.

---

### `get_bone_meta`
```gdscript
func get_bone_meta(bone_idx: int, key: String) -> Variant
```
**Description:**  
Retrieves the value of a metadata key for the bone at the specified index.

**Parameters:**
- `bone_idx`: Index of the bone.
- `key`: Metadata key.

---

## **Skin Management**

### `register_skin`
```gdscript
func register_skin(skin: Skin) -> SkinReference
```
**Description:**  
Binds a skin to the skeleton, allowing it to use the skin's mesh data for animation.

**Parameters:**
- `skin`: Skin object to bind.

**Returns:**
- A `SkinReference` object representing the registered skin.

---

## **Deprecated Methods**

### `set_bone_global_pose_override` (Deprecated)
```gdscript
func set_bone_global_pose_override(bone_idx: int, pose: Transform3D, amount: float, persistent: bool = false)
```
**Description:**  
Sets a global pose with interpolation strength and persistence. This method is deprecated and should be replaced with `set_bone_global_pose`.

**Parameters:**
- `bone_idx`: Index of the bone.
- `pose`: New global pose.
- `amount`: Interpolation strength.
- `persistent`: Whether the pose remains after interpolation.

---

## **Notes**
- **Bone Hierarchy:** Bones are organized in a hierarchy, where a bone's parent is always indexed lower than it.
- **Local vs Global:** Methods like `set_bone_pose` work in local space relative to the skeleton, while `set_bone_global_pose` affects the global transform.
- **Performance:** Repeatedly modifying poses can impact performance, so use with care.

This class is fundamental for creating and managing skeletal animations in Godot, allowing for complex character movements and interactions.