# BaseMaterial3D Class Documentation

## Overview
The `BaseMaterial3D` class serves as a foundation for 3D material properties in a graphics engine. It provides methods to manage textures, lighting, color, and other material attributes, with support for advanced features like triplanar mapping and sRGB color conversion.

---

## Properties

### Texture Parameters
- **`albedo_texture`**: Albedo texture (base color).
- **`normal_texture`**: Normal map texture.
- **` specular_texture`**: Specular map texture.
- **`emissive_texture`**: Emissive texture (self-illumination).
- **`occlusion_texture`**: Ambient occlusion texture.
- **`height_texture`**: Height map texture.
- **`displacement_texture`**: Displacement map texture.
- **`metallic_texture`**: Metallic map texture.
- **`roughness_texture`**: Roughness map texture.
- **`ambient_texture`**: Ambient texture (for older rendering methods).

### Material Features
- **`vertex_color_use_as_albedo`**: Whether vertex colors are used as albedo.
- **`vertex_color_is_srgb`**: Whether vertex colors are in sRGB color space.
- **`use_vertex_color`**: Whether vertex colors are used (deprecated, use `vertex_color_use_as_albedo` instead).
- **`use_albedo_texture`**: Whether albedo texture is used.
- **`use_normal_texture`**: Whether normal map is used.
- **`use_specular_texture`**: Whether specular map is used.
- **`use_emissive_texture`**: Whether emissive texture is used.
- **`use_occlusion_texture`**: Whether ambient occlusion is used.
- **`use_height_texture`**: Whether height map is used.
- **`use_displacement_texture`**: Whether displacement map is used.
- **`use_metallic_texture`**: Whether metallic map is used.
- **`use_roughness_texture`**: Whether roughness map is used.
- **`use_ambient_texture`**: Whether ambient texture is used.
- **`use_bump_texture`**: Whether bump map is used.
- **`use_highlight_texture`**: Whether highlight map is used.

### Flags
- **`use_depth`**: Whether depth is used for shadowing.
- **`use_lights`**: Whether lights are used.
- **`use_shadow`**: Whether shadows are used.
- **`use_transparency`**: Whether transparency is enabled.
- **`use_wireframe`**: Whether wireframe rendering is enabled.
- **`use_backface_culling`**: Whether backface culling is enabled.
- **`use_alpha_blend`**: Whether alpha blending is enabled.
- **`use_alpha_test`**: Whether alpha testing is enabled.
- **`use_alpha_to_coverage`**: Whether alpha-to-coverage is enabled.
- **`use_depth_write`**: Whether depth writing is enabled.
- **`use_stencil_write`**: Whether stencil writing is enabled.
- **`use_stencil_test`**: Whether stencil testing is enabled.
- **`use_outline`**: Whether outline rendering is enabled.
- **`use_wireframe_outline`**: Whether wireframe outline is enabled.
- **`use_lighting`**: Whether lighting is enabled.
- **`use_lighting_ambient`**: Whether ambient lighting is enabled.
- **`use_lighting_diffuse`**: Whether diffuse lighting is enabled.
- **`use_lighting_specular`**: Whether specular lighting is enabled.
- **`use_lighting_shading`**: Whether shading is enabled.
- **`use_lighting_reflection`**: Whether reflection is enabled.
- **`use_lighting_refraction`**: Whether refraction is enabled.
- **`use_lighting_sky`**: Whether sky lighting is enabled.

### Triplanar Mapping
- **`use_triplanar`**: Whether triplanar mapping is enabled.
- **`triplanar_sharpness`**: Sharpness of triplanar blending.
- **`triplanar_use_world`**: Whether triplanar is calculated in world space.

---

## Methods

### Texture Management
- **`get_texture(param)`**: Returns the texture associated with the specified `TextureParam`.
- **`set_texture(param, texture)`**: Sets the texture for the specified `TextureParam`.

### Feature and Flag Control
- **`get_feature(feature)`**: Checks if a specific feature is enabled.
- **`set_feature(feature, enable)`**: Enables or disables a specific feature.
- **`get_flag(flag)`**: Checks if a specific flag is enabled.
- **`set_flag(flag, enable)`**: Enables or disables a specific flag.

---

## Notes

### Rendering Methods
- **`vertex_color_is_srgb`** is only effective with **Forward+** and **Mobile** rendering methods. **Compatibility** mode does not apply this conversion.
- **`use_triplanar`** is only valid when using **Forward+** or **Mobile** rendering methods.

### Flags and Bitmasks
- Flags are **not** bitmaskable; each flag must be set individually. For example, you cannot enable multiple flags at once using a single call.

### Texture Parameters
- The `TextureParam` enum defines available texture slots (e.g., albedo, normal, emissive, etc.).

### SRGB Conversion
- When `vertex_color_is_srgb` is true, vertex colors are converted from sRGB to linear color space before rendering. This ensures correct color blending and lighting calculations.

---

## Example Usage
```cpp
BaseMaterial3D material;
material.set_texture(TextureParam::ALBEDO, albedoTexture);
material.set_flag(Flag::USE_LIGHTING, true);
material.set_feature(Feature::VERTEX_COLOR_USE_AS_ALBEDO, true);
```

This documentation provides a clear structure for understanding and implementing the `BaseMaterial3D` class, ensuring compatibility with various rendering methods and features.