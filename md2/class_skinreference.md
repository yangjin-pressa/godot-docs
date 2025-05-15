# SkinReference

**Inherits:** RefCounted < Object

## Description
A reference-counted object for a skeleton RID used in RenderingServer. It maps a Skin to a skeleton RID, enabling dynamic skeletal animation in MeshInstance3D. Key points:
- Serves as a bridge between MeshInstance3D and RenderingServer's skeleton system
- A Skeleton3D node may not be directly referenced by RenderingServer if it has no MeshInstance3D children
- Multiple SkinReference instances can exist for a single Skin if used across different Skeleton3D nodes

## Methods
- **get_skeleton()** → RID  
  Returns the skeleton RID associated with this SkinReference, created via RenderingServer.skeleton_create()

- **get_skin()** → Skin  
  Returns the Skin linked to this reference. If no skin is assigned to MeshInstance3D, returns an internal default Skin

## Notes
- The skeleton RID in RenderingServer does not directly correspond to Skeleton3D nodes
- A single Skin can be referenced by multiple SkinReference instances across different Skeleton3D nodes
- See also: MeshInstance3D.get_skin_reference(), RenderingServer.instance_attach_skeleton()