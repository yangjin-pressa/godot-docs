# VisibleOnScreenEnabler2D

**Inherits:** VisibleOnScreenNotifier2D < Node2D < CanvasItem < Node < Object

## Description
- A rectangular region of 2D space that enables a target node when any part becomes visible on screen.
- Target node's process mode is set based on `enable_mode`.
- Used to activate entities (e.g., enemies) when the player approaches.
- **Note:** Uses render culling. Must set `CanvasItem.visible` to `true` for functionality.

## Properties
- **enable_mode**: EnableMode = 0  
- **enable_node_path**: NodePath("..")

## Enumerations
### EnableMode
- **ENABLE_MODE_INHERIT** = 0 (Node.PROCESS_MODE_INHERIT)  
- **ENABLE_MODE_ALWAYS** = 1 (Node.PROCESS_MODE_ALWAYS)  
- **ENABLE_MODE_WHEN_PAUSED** = 2 (Node.PROCESS_MODE_WHEN_PAUSED)

## Property Descriptions
### enable_mode
- **set_enable_mode(value: EnableMode)**  
- **get_enable_mode()**  
- Determines target node's process mode. When disabled, uses Node.PROCESS_MODE_DISABLED.

### enable_node_path
- **set_enable_node_path(value: NodePath)**  
- **get_enable_node_path()**  
- Path to target node relative to this class. Cached; assigned when property is set.  
  - Empty path: no node affected.  
  - Invalid path: error occurs.