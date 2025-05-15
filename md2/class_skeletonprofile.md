# SkeletonProfile Class Documentation

## Overview

The `SkeletonProfile` class is used to define the structure and properties of bones for retargeting in a skeleton. It allows setting and retrieving bone names, parents, groups, handle offsets, reference poses, required status, and tail directions. This class is crucial for animation systems where bones need to be mapped between different skeletons in a 3D environment.

---

## Enum: `TailDirection`

This enum defines the direction of the tail for a bone. It is used in conjunction with the `set_tail_direction` method to determine how the tail is calculated.

- **TAIL** - The tail is calculated based on the bone's own properties.
- **CUSTOM** - The tail is calculated using a custom method.

---

## Methods

### `set_bone_name(bone_idx, name)`

**Description:** Sets the name of the bone at the specified index. This name is used in the bone map editor for identification.

**Parameters:**
- `bone_idx`: The index of the bone.
- `name`: The new name for the bone (as a `StringName`).

**Notes:** The name is used in the bone map editor for reference during retargeting.

---

### `get_bone_name(bone_idx)`

**Description:** Retrieves the name of the bone at the specified index.

**Parameters:**
- `bone_idx`: The index of the bone.

**Returns:** The name of the bone as a `StringName`.

---

### `set_bone_parent(bone_idx, parent)`

**Description:** Sets the parent of the bone at the specified index. This defines the hierarchy of the bone in the skeleton.

**Parameters:**
- `bone_idx`: The index of the bone.
- `parent`: The index of the parent bone.

**Notes:** The parent-child relationship is essential for proper animation and retargeting.

---

### `get_bone_parent(bone_idx)`

**Description:** Retrieves the parent of the bone at the specified index.

**Parameters:**
- `boneity`: The index of the bone.

**Returns:** The index of the parent bone.

---

### `set_bone_group(bone_idx, group)`

**Description:** Sets the group of the bone at the specified index. Groups are used to organize bones in the bone map editor.

**Parameters:**
- `bone_idx`: The index of the bone.
- `group`: The group index.

**Notes:** Groups help in managing and organizing bones during retargeting.

---

### `get_bone_group(bone_idx)`

**Description:** Retrieves the group of the bone at the specified index.

**Parameters:**
- `bone_idx`: The index of the bone.

**Returns:** The group index of the bone.

---

### `set_bone_handle_offset(bone_idx, offset)`

**Description:** Sets the handle offset for the bone at the specified index. This determines the position of the handle in the bone map editor.

**Parameters:**
- `bone_idx`: The index of the bone.
- `offset`: The handle offset as a `Vector2`.

**Notes:** The handle offset is used for visual editing of the bone in the editor.

---

### `get_bone_handle_offset(bone_idx)`

**Description:** Retrieves the handle offset for the bone at the specified index.

**Parameters:**
- `bone_idx`: The index of the bone.

**Returns:** The handle offset as a `Vector2`.

---

### `set_bone_reference_pose(bone_idx, pose)`

**Description:** Sets the reference pose for the bone at the specified index. This is a `Transform3D` that defines the bone's position and orientation.

**Parameters:**
- `bone_idx`: The index of the bone.
- `pose`: The reference pose as a `Transform3D`.

**Notes:** The reference pose is used as a base for animation calculations. The actual coordinates are stored externally, so the `TailDirection` enum indicates how the tail is calculated.

---

### `get_bone_reference_pose(bone_idx)`

**Description:** Retrieves the reference pose for the bone at the specified index.

**Parameters:**
- `bone_idx`: The index of the bone.

**Returns:** The reference pose as a `Transform3D`.

---

### `set_bone_required(bone_idx, required)`

**Description:** Sets whether the bone is required for retargeting. This determines if the bone must be included in the retargeting process.

**Parameters:**
- `bone_idx`: The index of the bone.
- `required`: A boolean indicating if the bone is required.

**Notes:** Required bones are essential for the retargeting process and are not optional.

---

### `get_bone_required(bone_idx)`

**Description:** Retrieves whether the bone is required for retargeting.

**Parameters:**
- `bone_idx`: The index of the bone.

**Returns:** A boolean indicating if the bone is required.

---

### `set_bone_tail_direction(bone_idx, direction)`

**Description:** Sets the tail direction for the bone at the specified index. This determines how the tail is calculated during retargeting.

**Parameters:**
- `bone_idx`: The index of the bone.
- `direction`: The tail direction as a `TailDirection` enum.

**Notes:** The tail direction is used in conjunction with the reference pose to calculate the tail's position.

---

### `get_bone_tail_direction(bone_idx)`

**Description:** Retrieves the tail direction for the bone at the specified index.

**Parameters:**
- `bone_idx`: The index of the bone.

**Returns:** The tail direction as a `TailDirection` enum.

---

### `set_group_texture(group_idx, texture)`

**Description:** Sets the texture for the group at the specified index. This is used as a background in the bone map editor.

**Parameters:**
- `group_idx`: The index of the group.
- `texture`: The texture as a `Texture`.

**Notes:** The group texture helps in visually distinguishing groups during editing.

---

## Notes

- **Virtual Methods:** Some methods may be virtual (indicated in the documentation), allowing subclasses to override their behavior if needed.
- **External Coordinates:** The actual coordinates for bones are stored externally, so the `TailDirection` enum is used to determine how the tail is calculated during retargeting.
- **Bone Map Editor:** All methods are used in the context of the bone map editor, where bones are organized, grouped, and edited for animation and retargeting.

---

## Example Usage

```gdscript
var profile = SkeletonProfile.new()
profile.set_bone_name(0, "spine")
profile.set_bone_parent(0, 1)
profile.set_bone_group(0, 1)
profile.set_bone_handle_offset(0, Vector2(10, 20))
profile.set_bone_reference_pose(0, Transform3D.IDENTITY)
profile.set_bone_required(0, true)
profile.set_bone_tail_direction(0, TailDirection.TAIL)
```

This example sets up a basic bone with a name, parent, group, handle offset, reference pose, and tail direction for retargeting.