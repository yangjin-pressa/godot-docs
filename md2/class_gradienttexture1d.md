# GradientTexture1D

## Inheritance
- Texture2D < Texture < Resource < RefCounted < Object

## Description
A 1D texture that fills data using colors from a Gradient. The texture may not exactly match the gradient due to pixel limitations. Related classes: GradientTexture2D, CurveTexture, CurveXYZTexture.

## Properties

- **gradient** (Gradient): The Gradient used to fill the texture.
- **use_hdr** (bool): If true, the texture supports high dynamic range (Image.FORMAT_RGBAF). Defaults to false.
- **width** (int): Number of color samples from the Gradient. Defaults to 256.

## Property Details

### gradient
- **set_gradient** (Gradient): Sets the Gradient.
- **get_gradient** (): Retrieves the Gradient.

### use_hdr
- **set_use_hdr** (bool): Enables/disables HDR support.
- **is_using_hdr** (): Checks if HDR is enabled.

### width
- **set_width** (int): Sets the number of color samples.
- **get_width** (): Retrieves the width value.

## Notes
- The texture format depends on use_hdr: RGBAF for HDR, RGBA8 for standard.
- HDR support allows glow effects when Environment.glow_enabled is enabled.