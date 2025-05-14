# BoneMap

**Inherits:** Resource → RefCounted → Object

## Description
A dictionary mapping bone names from Skeleton3D to SkeletonProfile for retargeting. Key names in BoneMap are synchronized with the SkeletonProfile.

## Tutorials
- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons)

## Properties
- **profile**: SkeletonProfile (linked to SkeletonProfile class)

## Methods
- **find_profile_bone_name**(skeleton_bone_name: StringName) → StringName  
  Returns profile bone name for a given skeleton bone name.

- **get_skeleton_bone_name**(profile_bone_name: StringName) → StringName  
  Returns skeleton bone name mapped to a profile bone name.

- **set_skeleton_bone_name**(profile_bone_name: StringName, skeleton_bone_name: StringName)  
  Maps a skeleton bone name to a profile bone name.

## Signals
- **bone_map_updated**  
  Emitted when a key value in BoneMap is changed.

- **profile_updated**  
  Emitted when profile is modified or reference changes.

## Property Descriptions
**profile**: SkeletonProfile  
Specifies the target skeleton profile for mapping. Key names in BoneMap are synchronized with this profile.

## Method Descriptions
- **find_profile_bone_name**: Finds a profile bone name corresponding to a skeleton bone name.
- **get_skeleton_bone_name**: Retrieves the skeleton bone name mapped to a profile bone name.
- **set_skeleton_bone_name**: Establishes a mapping between a skeleton bone name and a profile bone name.