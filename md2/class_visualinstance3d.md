# VisualInstance3D

## Inheritance
- Inherits from: Node3D → Node → Object  
- Inherited by: Decal, FogVolume, GeometryInstance3D, GPUParticlesAttractor3D, GPUParticlesCollision3D, Light3D, LightmapGI, OccluderInstance3D, OpenXRVisibilityMask, ReflectionProbe, RootMotionView, VisibleOnScreenNotifier3D, VoxelGI  

## Description
Used to connect a resource to a visual representation. All visual 3D nodes inherit from this class. Direct manipulation of its properties is generally discouraged as they are managed by derived nodes. Acts as a node representation for RenderingServer.

---

## Properties

- **layers** (int) = 1  
  Render layers this node is drawn on. Controls visibility for Camera3D and interactions with lights/decals.  

- **sorting_offset** (float) = 0.0  
  Adjusts drawing order for 3D models. Higher values place the node later in the rendering pipeline.  

- **sorting_use_aabb** (bool)  
  Enables AABB (bounding box) based sorting for more accurate 3D positioning. Default is position-based sorting.

---

## Methods

- **_get_aabb** (virtual const)  
  Returns bounding box (AABB) for this node. No description available.  

- **get_aabb** (const)  
  Returns the AABB for this node.  

- **get_base** (const)  
  Returns the RID of the associated resource (e.g., Mesh for MeshInstance3D).  

- **get_instance** (const)  
  Returns the RenderingServer instance ID for this node.  

- **get_layer_mask_value** (const)  
  Checks if a specific layer (1-20) is enabled in the layers property.  

- **set_base** (void)  
  Sets the resource associated with this node. Equivalent to RenderingServer.instance_set_base().  

- **set_layer_mask_value** (void)  
  Enables or disables a specific layer in the layers property.  

---

## Notes
- Layer numbers range from 1 to 20.  
- VoxelGI and similar nodes may require special handling for layer interactions.  
- Methods like `_get_aabb` are internal and should be overridden by derived classes.  
- Use `get_instance` when calling RenderingServer functions directly.