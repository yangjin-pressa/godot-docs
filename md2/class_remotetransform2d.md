# RemoteTransform2D

**Inherits:** Node2D → CanvasItem → Node → Object

## Description
Pushes its own Transform2D to another Node2D in the scene. Can update position, rotation, and/or scale. Supports global/local coordinates.

## Properties
- **remote_path**: NodePath (default: "")  
  Path to the remote node relative to this node.

- **update_position**: bool (default: true)  
  If true, updates the remote node's position.

- **update_rotation**: bool (default: true)  
  If true, updates the remote node's rotation.

- **update_scale**: bool (default: true)  
  If true, updates the remote node's scale.

- **use_global_coordinates**: bool (default: true)  
  If true, uses global coordinates; otherwise, local.

## Methods
- **force_update_cache()**: void  
  Forces the remote node cache to update, even if the remote node is no longer present.

## Property Accessors
### remote_path
- `set_remote_node(value: NodePath)`: void  
  Sets the remote node path.
- `get_remote_node()`: NodePath  
  Returns the current remote node path.

### update_position
- `set_update_position(value: bool)`: void  
  Enables/disable position updates.
- `get_update_position()`: bool  
  Returns the current position update state.

### update_rotation
- `set_update_rotation(value: bool)`: void  
  Enables/disable rotation updates.
- `get_update_rotation()`: bool  
  Returns the current rotation update state.

### update_scale
- `set_update_scale(value: bool)`: void  
  Enables/disable scale updates.
- `get_update_scale()`: bool  
  Returns the current scale update state.

### use_global_coordinates
- `set_use_global_coordinates(value: bool)`: void  
  Switches between global/local coordinate systems.
- `get_use_global_coordinates()`: bool  
  Returns the current coordinate system mode.