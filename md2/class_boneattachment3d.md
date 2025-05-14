# BoneAttachment3D

**Inherits:** Node3D < Node < Object

А node that dynamically copies or overrides the 3D transform of a bone in its parent Skeleton3D.

## Description

This node selects a bone in a Skeleton3D and attaches to it. This means that the BoneAttachment3D node will either dynamically copy or override the 3D transform of the selected bone.

## Properties

- **bone_idx** (int) = -1  
  The index of the attached bone.

- **bone_name** (String) = ""  
  The name of the attached bone.

- **override_pose** (bool) = false  
  Whether the BoneAttachment3D node will override the bone pose of the bone it is attached to. When set to true, the BoneAttachment3D node can change the pose of the bone. When set to false, the BoneAttachment3D will always be set to the bone's transform.  
  **Note:** This override performs interruptively in the skeleton update process using signals due to the old design. It may cause unintended behavior when used at the same time with SkeletonModifier3D.

- **physics_interpolation_mode** (PhysicsInterpolationMode) = 2  
  Overrides Node's physics_interpolation_mode. Default is 2 (linear).

## Methods

- **get_external_skeleton** () → NodePath  
  Returns the NodePath to the external Skeleton3D node, if one has been set.

- **get_skeleton** () → NodePath  
  Returns the Skeleton3D node (either the external one or the parent).

- **get_use_external_skeleton** () → bool  
  Returns whether the BoneAttachment3D node uses an external Skeleton3D node.

- **on_skeleton_update** ()  
  Automatically called when the Skeleton3D is updated. This method should typically be overridden by the user to have any effect.

- **set_external_skeleton** (use_external_skeleton: bool)  
  Sets whether the BoneAttachment3D node will use an external Skeleton3D node. When set to true, the node uses the external Skeleton3D set in set_external_skeleton().

- **set_use_external_skeleton** (use_external_skeleton: bool)  
  Sets whether the BoneAttachment3D node will use an external Skeleton3D node. When set to true, the node uses the external Skeleton3D set in set_external_skeleton().