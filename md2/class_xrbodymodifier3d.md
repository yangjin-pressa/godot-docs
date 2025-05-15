# XRBodyModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** SkeletonModifier3D < Node3D < Node < Object

A node for driving body meshes from XRBodyTracker data.

## Description

This node uses body tracking data from an XRBodyTracker to pose the skeleton of a body mesh.

Positioning of the body is performed by creating an XRNode3D ancestor of the body mesh driven by the same XRBodyTracker.

The body tracking position-data is scaled by Skeleton3D.motion_scale when applied to the skeleton, which can be used to adjust the tracked body to match the scale of the body model.

## Tutorials

- XR documentation index

## Properties

- body_tracker: &"/user/body_tracker"
- body_update: 7
- bone_update: 0

## Enumerations

### BodyUpdate
- BODY_UPDATE_UPPER_BODY = 1: Upper body joints
- BODY_UPDATE_LOWER_BODY = 2: Lower body joints
- BODY_UPDATE_HANDS = 4: Hand joints

### BoneUpdate
- BONE_UPDATE_FULL = 0: Full update (position and rotation)
- BONE_UPDATE_ROTATION_ONLY = 1: Rotation only
- BONE_UPDATE_MAX = 2: Enum size

## Property Descriptions

### body_tracker
- Type: StringName
- Default: &"/user/body_tracker"
- Description: Name of XRBodyTracker registered with XRServer

### body_update
- Type: Bitfield of BodyUpdate
- Default: 7
- Description: Body parts to update

### bone_update
- Type: BoneUpdate
- Default: 0
- Description: Type of bone updates to perform