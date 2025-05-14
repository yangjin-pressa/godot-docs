# OmniLight3D

**Inherits**: Light3D < VisualInstance3D < Node3D < Node < Object

Omnidirectional light, such as a light bulb or a candle.

## Description
An Omnidirectional light emits light in all directions. The light is attenuated by distance and this attenuation can be configured by changing its energy, radius, and attenuation parameters.

**Note**: When using the Mobile rendering method, only 8 omni lights can be displayed on each mesh resource. Attempting to display more than 8 omni lights on a single mesh resource will result in omni lights flickering in and out as the camera moves. When using the Compatibility rendering method, only 8 omni lights can be displayed on each mesh resource by default, but this can be increased by adjusting `ProjectSettings.rendering/limits/opengl/max_lights_per_object`.

**Note**: When using the Mobile or Compatibility rendering methods, omni lights will only correctly affect meshes whose visibility AABB intersects with the light's AABB. If using a shader to deform the mesh in a way that makes it go outside its AABB, `GeometryInstance3D.extra_cull_margin` must be increased on the mesh. Otherwise, the light may not be visible on the mesh.

## Tutorials
- 3D lights and shadows ../tutorials/3d/lights_and_shadows
- Faking global illumination ../tutorials/3d/global_illumination/faking_global_illumination

## Properties
- **omni_attenuation** (float, default: 1.0): Controls the distance attenuation function for omnilights. A value of 0.0 maintains constant brightness but smoothly attenuates at the edge. Use 2.0 for physically accurate lights. Setting attenuation to 2.0 or higher may result in distant objects receiving minimal light. Using negative or values above 10.0 may lead to unexpected results.
- **omni_range** (float, default: 5.0): The light's radius. The effectively lit area may appear smaller depending on the attenuation. The light will never reach anything outside this radius. This property is not affected by Node3D.scale.
- **omni_shadow_mode** (ShadowMode, default: 1): See ShadowMode. Options: 0 (SHADOW_DUAL_PARABOLOID) for faster, lower-quality shadows; 1 (SHADOW_CUBE) for slower, higher-quality shadows.

## Enumerations
### ShadowMode
- **SHADOW_DUAL_PARABOLOID** (0): Shadows rendered to a dual-paraboloid texture. Faster than SHADOW_CUBE but lower-quality.
- **SHADOW_CUBE** (1): Shadows rendered to a cubemap. Slower than SHADOW_DUAL_PARABOLOID but higher-quality.