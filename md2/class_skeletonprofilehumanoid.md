# SkeletonProfileHumanoid

**Inherits:** SkeletonProfile < Resource < RefCounted < Object

A humanoid SkeletonProfile preset optimized for human form. All parameters are read-only.

## Description
A SkeletonProfile designed for humanoids contains 54 bones organized into 4 groups: "Body", "Face", "LeftHand", and "RightHand". The bone hierarchy is structured as:

Root
├─ Hips
│  ├─ LeftUpperLeg
│  │  └─ LeftLowerLeg
│  │     └─ LeftFoot
│  │        └─ LeftToes
│  └─ RightUpperLeg
│     └─ RightLowerLeg
│        └─ RightFoot
│           └─ RightToes
└─ Spine
   └─ Chest
      └─ UpperChest
         ├─ Neck
         │   └─ Head
         │       ├─ Jaw
         │       ├─ LeftEye
         │       └─ RightEye
         ├─ LeftShoulder
         │  └─ LeftUpperArm
         │     └─ LeftLowerArm
         │        └─ LeftHand
         │           ├─ LeftThumbMetacarpal
         │           │  └─ LeftThumbProximal
         │           │     └─ LeftThumbDistal
         │           ├─ LeftIndexProximal
         │           │  └─ LeftIndexIntermediate
         │           │     └─ LeftIndexDistal
         │           ├─ LeftMiddleProximal
         │           │  └─ LeftMiddleIntermediate
         │           │     └─ LeftMiddleDistal
         │           ├─ LeftRingProximal
         │           │  └─ LeftRingIntermediate
         │           │     └─ LeftRingDistal
         │           └─ LeftLittleProximal
         │              └─ LeftLittleIntermediate
         │                └─ LeftLittleDistal
         └─ RightShoulder
            └─ RightUpperArm
               └─ RightLowerArm
                  └─ RightHand
                     ├─ RightThumbMetacarpal
                     │  └─ RightThumbProximal
                     │     └─ RightThumbDistal
                     ├─ RightIndexProximal
                     │  └─ RightIndexIntermediate
                     │     └─ RightIndexDistal
                     ├─ RightMiddleProximal
                     │  └─ RightMiddleIntermediate
                     │     └─ RightMiddleDistal
                     ├─ RightRingProximal
                     │  └─ RightRingIntermediate
                     │     └─ RightRingDistal
                     └─ RightLittleProximal
                        └─ RightLittleIntermediate
                           └─ RightLittleDistal

## Tutorials
- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons)

## Properties
- bone_size: 56 (overrides SkeletonProfile property)
- group_size: 4 (overrides SkeletonProfile property)
- root_bone: "&"Root"" (overrides SkeletonProfile property)
- scale_base_bone: "&"Hips"" (overrides SkeletonProfile property)

## Notes
- This class provides standardized humanoid skeleton parameters
- All properties are read-only and override base SkeletonProfile values