# FBXState

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** GLTFState < Resource < RefCounted < Object

## Description
The FBXState handles the state data imported from FBX files.

## Properties
- allow_geometry_helper_nodes: false (bool)

## Property Descriptions
**allow_geometry_helper_nodes** (bool) = false ⬆️class_FBXState_property_allow_geometry_helper_nodes

- **set_allow_geometry_helper_nodes**(value: bool): void
- **get_allow_geometry_helper_nodes**(): bool

If true, the import process uses auxiliary nodes called geometry helper nodes. These nodes help preserve the pivots and transformations of the original 3D model during import.