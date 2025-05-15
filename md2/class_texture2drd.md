# Texture2DRD

**Inherits:** Texture2D < Texture < Resource < RefCounted < Object

Texture for 2D that is bound to a texture created on the RenderingDevice.

---

## Description

This texture class allows you to use a 2D texture created directly on the RenderingDevice as a texture for materials, meshes, etc.

---

## Properties

- **resource_local_to_scene**: bool (false)  
  Overrides Resource's resource_local_to_scene property

- **texture_rd_rid**: RID  
  RID of the texture object created on the RenderingDevice

---

## Property Descriptions

### texture_rd_rid

- **set_texture_rd_rid**(value: RID): void  
- **get_texture_rd_rid**(): RID  

The RID of the texture object created on the RenderingDevice.