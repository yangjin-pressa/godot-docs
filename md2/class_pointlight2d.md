# PointLight2D

**Inherits**: Light2D < Node2D < CanvasItem < Node < Object

## Description
Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.

## Tutorials
- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows)

## Properties
- float height = 0.0
- Vector2 offset = Vector2(0, 0)
- Texture2D texture
- float texture_scale = 1.0

## Property Descriptions
**height** (float)
- **set_height** (value: float)
- **get_height** ()
The height of the light. Used with 2D normal mapping. Units are in pixels.

**offset** (Vector2)
- **set_texture_offset** (value: Vector2)
- **get_texture_offset** ()
The offset of the light's texture.

**texture** (Texture2D)
- **set_texture** (value: Texture2D)
- **get_texture** ()
Texture used for the light's appearance.

**texture_scale** (float)
- **set_texture_scale** (value: float)
- **get_texture_scale** ()
The texture's scale factor.