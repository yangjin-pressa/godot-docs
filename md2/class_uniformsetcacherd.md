# UniformSetCacheRD

**Inherits:** Object

Uniform set cache manager for Rendering Device based renderers.

## Description

Uniform set cache manager for Rendering Device based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.

## Methods

- **get_cache** (static): Returns a cached uniform set based on the provided uniforms for a given shader.

## Method Descriptions

### get_cache
**Returns:** RID

**Parameters:**
- shader: RID
- set: int
- uniforms: Array of RDUniform

**Note:** This method is static. It creates/returns a cached uniform set based on the provided uniforms for a given shader.