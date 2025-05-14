# PanoramaSkyMaterial

## Inheritance
- **Material**
  - **Resource**
    - **RefCounted**
      - **Object**

## Description
A material used to render a background in a `Sky` node, typically with an HDR panorama texture. This class supports equirectangular sky maps instead of cubemaps.

**Supported formats**: Radiance HDR (.hdr), OpenEXR (.exr).  
**Tool for conversion**: [Convert cubemap to panorama](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html)

## Properties
- **energy_multiplier**: `float` (default: `1.0`)  
  Adjust overall sky brightness. Higher values increase sky brightness.

- **filter**: `bool` (default: `true`)  
  Enable or disable texture filtering for the background.

- **panorama**: `Texture2D`  
  The equirectangular sky map texture applied to the material.

## Method Descriptions
- **set_energy_multiplier(value: float)**  
  Sets the brightness multiplier for the sky.

- **get_energy_multiplier()**  
  Retrieves the current brightness multiplier.

- **set_filtering_enabled(value: bool)**  
  Enables or disables texture filtering.

- **is_filtering_enabled()**  
  Checks if texture filtering is enabled.

- **set_panorama(value: Texture2D)**  
  Assigns a new texture to the material.

- **get_panorama()**  
  Returns the current texture.