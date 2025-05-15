# XRHandModifier3D

**Inherits:** SkeletonModifier3D < Node3D < Node < Object

A node for driving hand meshes from XRHandTracker data.

## Description
Uses hand tracking data from an XRHandTracker to pose a hand mesh skeleton. Positioning is achieved by creating an XRNode3D ancestor of the mesh, driven by the same tracker. The motion data is scaled by Skeleton3D's motion_scale property.

## Tutorials
- XR documentation index (../tutorials/xr/index)

## Properties
- BoneUpdate bone_update = 0 (0)
- StringName hand_tracker = "/user/hand_tracker/left"

## Enumerations
**BoneUpdate**:
- BONE_UPDATE_FULL = 0 (Full position/rotation)
- BONE_UPDATE_ROTATION_ONLY = 1 (Rotation only, preserve length)
- BONE_UPDATE_MAX = 2 (Enum size)

## Property Descriptions
**bone_update**:
- Set/get method: void set_bone_update(BoneUpdate value), BoneUpdate get_bone_update()
- Specifies bone update type (virtual method)

**hand_tracker**:
- Set/get method: void set_hand_tracker(StringName value), StringName get_hand_tracker()
- Name of XRHandTracker registered with XRServer

## Notes
- Methods marked as "virtual" require user override for functionality
- "const" methods have no side effects
- "vararg" methods accept variable arguments
- "bitfield" values are bitmask combinations
- "void" methods return no value