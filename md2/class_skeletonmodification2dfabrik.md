# SkeletonModification2DFABRIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:**SkeletonModification2D → Resource → RefCounted → Object

A modification that uses FABRIK to manipulate a series of Bone2D nodes to reach a target.

## Description

This SkeletonModification2D uses the FABRIK algorithm to rotate a bone chain so it reaches a target. FABRIK works by:
1. Placing the final bone at the target position
2. Adjusting other bones to maintain chain structure
3. Using a magnet vector for each joint to influence positioning

The class allows customization of bone joints and includes options to control rotation behavior.

## Properties

- **fabrik_joints**: Array of joint configurations
- **target_rotation**: Boolean to control final joint rotation
- **magnet_positions**: Array of magnet vectors for each joint

## Methods

- **set_fabrik_joint_bone2d_node(joint_idx, bone2d_nodepath)**: Assigns a Bone2D node to a joint
- **set_fabrik_joint_bone_index(joint_idx, bone_idx)**: Sets the bone index for a joint
- **set_fabrik_joint_magnet_position(joint_idx, magnet_position)**: Sets magnet vector for a joint
- **set_fabrik_joint_use_target_rotation(joint_idx, use_target_rotation)**: Controls if a joint uses target rotation
- **get_fabrik_joint_bone2d_node(joint_idx)**: Retrieves Bone2D node for a joint
- **get_fabrik_joint_bone_index(joint_idx)**: Retrieves bone index for a joint
- **get_fabrik_joint_magnet_position(joint_idx)**: Retrieves magnet vector for a joint
- **get_fabrik_joint_use_target_rotation(joint_idx)**: Checks if a joint uses target rotation

## Notes

- The class uses a "joint" system that differs from direct Bone2D node manipulation
- Magnet vectors influence positioning but don't directly control joint rotation
- The target rotation option only affects the final joint in the chain
- Methods that end with "_node" require a NodePath parameter
- The class is part of Godot's physics/animation system for skeletal character control