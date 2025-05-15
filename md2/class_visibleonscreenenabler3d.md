# VisibleOnScreenEnabler3D

**Inherits:** VisibleOnScreenNotifier3D < VisualInstance3D < Node3D < Node < Object

## Description
A box-shaped region of 3D space that, when visible on screen, enables a target node. The target node will be automatically enabled (via its Node.process_mode property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. 

**Note:** This uses an approximate heuristic that doesn't account for walls/occlusion unless occlusion culling is used. Also requires Node3D.visible to be set to true. [1]

## Properties
- **EnableMode** (enum) - enable_mode = 0 [2]
- **NodePath** - enable_node_path = NodePath("..")

## Enumerations
**EnableMode**:
- ENABLE_MODE_INHERIT = 0 (corresponds to Node.PROCESS_MODE_INHERIT)
- ENABLE_MODE_ALWAYS = 1 (corresponds to Node.PROCESS_MODE_ALWAYS)
- ENABLE_MODE_WHEN_PAUSED = 2 (corresponds to Node.PROCESS_MODE_WHEN_PAUSED)

## Property Descriptions
**enable_mode** (EnableMode): Determines how the target node is enabled. Corresponds to ProcessMode. When disabled, uses Node.PROCESS_MODE_DISABLED.

**enable_node_path** (NodePath): Path to target node relative to this object. Defaults to "..". If empty, no node is affected. Invalid paths generate errors.

## Method Definitions
- void set_enable_mode(value: EnableMode)
- EnableMode get_enable_mode()

- void set_enable_node_path(value: NodePath)
- NodePath get_enable_node_path()