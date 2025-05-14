# Cubemap

**Inherits:** `ImageTextureLayered` → `TextureLayered` → `Texture` → `Resource` → `RefCounted` → `Object`

## Description
- A cubemap consists of 6 square textures arranged in layers (X+, X-, Y+, Y-, Z+, Z-).
- Commonly used for reflections in 3D rendering (e.g., `ReflectionProbe`).
- Efficient alternative to other reflection methods.
- Typically used as a uniform in custom shaders.

## Methods
- **`create_placeholder()`**  
  Creates a placeholder version of this resource (`PlaceholderCubemap`).

## Key Details
- **Image order:** X+, X-, Y+, Y-, Z+, Z- (Y+ is "up", Z- is "forward").
- **Templates:**  
  - [2×3 cubemap](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_2x3.webp)  
  - [3×2 cubemap](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_3x2.webp)  
  - [1×6 cubemap](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_1x6.webp)  
  - [6×1 cubemap](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_6x1.webp)  

## Shader Code Example
```glsl
shader_type sky;

uniform samplerCube source_panorama : filter_linear, source_color, hint_default_black;
uniform float exposure : hint_range(0, 128) = 1.0;

void sky() {
    vec3 eyedir = vec3(EYEDIR.x, EYEDIR.y, EYEDIR.z);
    COLOR = texture(source_panorama, eyedir).rgb * exposure;
}
```

## Notes
- Godot does **not** support cubemaps in `PanoramaSkyMaterial`.  
  Convert to `ShaderMaterial` and replace shader code as shown.  
- Alternatively, use [this tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html) to convert cubemaps to equirectangular maps.