# TextureLayeredRD

## Inheritance Hierarchy
- TextureLayeredRD ← TextureLayered ← Texture ← Resource ← RefCounted ← Object

## Inherited Classes
- Texture2DArrayRD
- TextureCubemapRD
- TextureCubemapArrayRD

## Description
Abstract base class for layered texture RD types. Cannot be used directly, but contains functions for derived resource types.

## Properties
- **texture_rd_rid**: RID of the texture object created on the RenderingDevice.

## Property Methods
- **set_texture_rd_rid**(value: RID): Sets the texture object RID.
- **get_texture_rd_rid**(): Retrieves the texture object RID.