# RemoteTransform3D

**Inherits**: Node3D < Node < Object

RemoteTransform3D pushes its own Transform3D to another Node3D in the scene.

## Description
RemoteTransform3D pushes its own Transform3D to another Node3D derived node (called the remote node) in the scene. It can set to update position, rotation, and/or scale. It can use global or local coordinates.

## Properties
- **remote_path**: NodePath = NodePath("")  
  The NodePath to the remote node, relative to the RemoteTransform3D's position in the scene.  
  - Set and get methods available.

- **update_position**: bool = true  
  If true, the remote node's position is updated.

- **update_rotation**: bool = true  
  If true, the remote node's rotation is updated.

- **update_scale**: bool = true  
  If true, the remote node's scale is updated.

- **use_global_coordinates**: bool = true  
  If true, global coordinates are used. If false, local coordinates are used.

## Methods
- **force_update_cache()**  
  Forces the remote node to update its cache, even if the node is no longer present.