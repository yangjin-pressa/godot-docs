# CurveTexture

## Description
A 1D texture where pixel brightness corresponds to points on a unit Curve resource, either in grayscale or red. This visual representation simplifies saving curves as image files.

Alternative: Use CurveXYZTexture for up to 3 curves. Related: GradientTexture1D, GradientTexture2D.

---

## Properties
- **Curve** → `curve`: The Curve object rendered onto the texture. Must be a unit Curve.
- **bool** → `resource_local_to_scene`: false (overrides Resource's default)
- **TextureMode** → `texture_mode`: 0
- **int** → `width`: 256

---

## Enumerations
### TextureMode
- **TEXTURE_MODE_RGB** = 0  
  Stores curve across red, green, and blue channels. Uses more video memory but is shader-compatible.
- **TEXTURE_MODE_RED** = 1  
  Stores curve only in red channel. Saves memory but may not work with some shaders.

---

## Property Descriptions
### curve
- **set_curve**(value: Curve): Sets the Curve.
- **get_curve**(): Returns the Curve.
- **Description**: The Curve object rendered onto the texture. Must be a unit Curve.

### texture_mode
- **set_texture_mode**(value: TextureMode): Sets the texture format.
- **get_texture_mode**(): Returns the texture format.
- **Description**: Determines how the texture is generated. Affects shader compatibility.

### width
- **set_width**(value: int): Sets the texture width in pixels.
- **get_width**(): Returns the texture width.
- **Description**: Higher values improve high-frequency data representation but increase memory usage.