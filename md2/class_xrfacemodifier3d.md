# XRFaceModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** Node3D < Node < Object

A node for driving standard face meshes from XRFaceTracker weights.

## Description

This node applies weights from an XRFaceTracker to a mesh with supporting face blend shapes.

- Supports Unified Expressions blend shapes
- Supports ARKit and SRanipal blend shapes
- Identifies blend shapes via name matching
- Blend shapes must match names in Unified Expressions Compatibility chart

## Tutorials

- [XR documentation index](../tutorials/xr/index)

## Properties

- **face_tracker** (StringName) = "/user/face_tracker"
- **target** (NodePath) = NodePath("")

## Property Descriptions

### face_tracker
Type: StringName  
Default: "/user/face_tracker"

- **set_face_tracker** (value: StringName)
- **get_face_tracker** ()

The path to the XRFaceTracker instance

### target
Type: NodePath  
Default: NodePath("")

- **set_target** (value: NodePath)
- **get_target** ()

The NodePath of the face MeshInstance3D

## Notes
- This class is experimental and may change in future versions
- Inherits from Node3D -> Node -> Object
- Uses Unified Expressions blend shapes and ARKit/SRanipal support
- Requires matching blend shape names to compatibility chart