# SpotLight3D

## Inheritance
- Inherits from: Light3D < VisualInstance3D < Node3D < Node < Object

## Description
A spotlight emits light in a conical shape, with attenuation based on distance. Key features:
- Light direction and shape are controlled via angle and range parameters
- Attenuation can be adjusted through energy, radius, and attenuation settings
- Mobile rendering: max 8 spotlights per mesh (adjustable via ProjectSettings)
- Compatibility rendering: same restriction, but configurable via max_lights_per_object

## Tutorials
- 3D lights and shadows
- Faking global illumination
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties
- light_specular: 0.5 (overrides Light3D)
- shadow_bias: 0.03 (overrides Light3D)
- shadow_normal_bias: 1.0 (overrides Light3D)
- spot_angle: 45.0
- spot_angle_attenuation: 1.0
- spot_attenuation: 1.0
- spot_range: 5.0

## Property Descriptions
- **spot_angle**: Spotlight cone angle in degrees. Not affected by scale.
- **spot_angle_attenuation**: Angular attenuation curve. Higher values create sharper edges.
- **spot_attenuation**: Distance attenuation factor. 
  - 0.0: constant brightness with edge fading
  - 2.0: physically accurate inverse-square attenuation
  - Values >10 may cause unexpected results
- **spot_range**: Maximum distance spotlight can reach. Not affected by scale.

## Notes
- Spotlights affect meshes only if their AABB intersects with the light's AABB
- Deformed meshes may require increased extra_cull_margin
- Attenuation values affect lighting efficiency and visibility at distance
- Mobile/Compatibility rendering has per-mesh spotlight limits