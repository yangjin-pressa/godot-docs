# FogMaterial

**Inherits:** Material < Resource < RefCounted < Object

A material that controls how volumetric fog is rendered, to be assigned to a FogVolume.

## Description

A Material resource used by FogVolume to draw volumetric effects. For advanced effects, use a custom fog shader.

## Properties

- **albedo**: Color, default Color(1, 1, 1, 1)  
  Represents the color of the fog. Set and get methods available.

- **density**: float, default 1.0  
  Controls fog thickness. Values between -0.001 and 0.001 act as 0.0. Set and get methods available.

- **density_texture**: Texture3D  
  Texture used to modulate fog density. Set and get methods available.

- **edge_fade**: float, default 0.1  
  Controls the fade effect at the edges of fog. Set and get methods available.

- **emission**: Color, default Color(0, 0, 0, 1)  
  Color emitted by the fog. Set and get methods available.

- **height_falloff**: float, default 0.0  
  Controls vertical fog fall-off. Set and get methods available.

## Notes

- Density values between -0.001 and 0.001 are treated as 0.0.
- For animated effects, use a custom fog shader instead of this material.