# RDTextureView

**Inherits:** RefCounted < Object

Texture view (used by RenderingDevice).

## Description

This object is used by RenderingDevice.

## Properties

- **format_override**: DataFormat = 232
- **swizzle_a**: TextureSwizzle = 6
- **swizzle_b**: TextureSwizzle = 5
- **swizzle_g**: TextureSwizzle = 4
- **swizzle_r**: TextureSwizzle = 3

## Property Descriptions

### format_override
**Type:** DataFormat  
**Default:** 232  
**Description:** Optional override for the data format to return sampled values in. The corresponding RDTextureFormat must have had this added as a shareable format. The default value of RenderingDevice.DATA_FORMAT_MAX does not override the format.

**Methods:**
- set_format_override(value: DataFormat)
- get_format_override()

### swizzle_a
**Type:** TextureSwizzle  
**Default:** 6  
**Description:** The channel to sample when sampling the alpha channel.

**Methods:**
- set_swizzle_a(value: TextureSwizzle)
- get_swizzle_a()

### swizzle_b
**Type:** TextureSwizzle  
**Default:** 5  
**Description:** The channel to sample when sampling the blue color channel.

**Methods:**
- set_swizzle_b(value: TextureSwizzle)
- get_swizzle_b()

### swizzle_g
**Type:** TextureSwizzle  
**Default:** 4  
**Description:** The channel to sample when sampling the green color channel.

**Methods:**
- set_swizzle_g(value: TextureSwizzle)
- get_swizzle_g()

### swizzle_r
**Type:** TextureSwizzle  
**Default:** 3  
**Description:** The channel to sample when sampling the red color channel.

**Methods:**
- set_swizzle_r(value: TextureSwizzle)
- get_swizzle_r()