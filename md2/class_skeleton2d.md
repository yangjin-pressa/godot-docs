# Skeleton2D Overview

## Inheritance Hierarchy
- **Skeleton2D**  
  - Inherits from: `Node2D` → `CanvasItem` → `Node` → `Object`

## Purpose
Serves as the root node for a hierarchical structure of `Bone2D` nodes, used to create 2D skeletal animations. Manages bone rest poses and provides access to all bones in the hierarchy.

---

## Key Concepts

### SkeletonModificationStack2D
- Used for inverse kinematics
- Modify `modification_count` to apply changes
- Stack is set via `set_modification_stack()`

---

## Methods

### `execute_modifications(delta: float, execution_mode: int)`
- Applies modifications from the attached `SkeletonModificationStack2D`
- `delta`: Time delta for animation
- `execution_mode`: Mode for applying modifications

### `get_bone(idx: int) -> Bone2D`
- Returns a bone from the hierarchy
- Bones are indexed in top-down order, with children processed before siblings

### `get_bone_count() -> int`
- Returns total number of bones in the hierarchy

### `get_bone_local_pose_override(bone_idx: int) -> Transform2D`
- Retrieves local pose override for a specific bone

### `get_modification_stack() -> SkeletonModificationStack2D`
- Returns the attached modification stack (if any)

### `get_skeleton() -> RID`
- Returns the RID of the skeleton instance

### `set_bone_local_pose_override(bone_idx: int, override_pose: Transform2D, strength: float, persistent: bool)`
- Sets a local pose override for a bone
- `strength`: Interpolation strength for pose application
- `persistent`: Whether the pose should remain after applying

### `set_modification_stack(modification_stack: SkeletonModificationStack2D)`
- Assigns a modification stack to the skeleton

---

## Signals

### `bone_setup_changed()`
- Emitted when bone setup changes
- Internal use only

---

## Notes

- Pose transforms must be relative to the target bone's node
- `set_bone_local_pose_override()` requires the transform to be local to the bone
- `SkeletonModificationStack2D` is used for inverse kinematics setup

---

## References
- [2D skeletons tutorial](../tutorials/animation/2d_skeletons)