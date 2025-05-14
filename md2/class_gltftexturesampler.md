# GLTFTextureSampler

**Inherits:** Resource < RefCounted < Object

Represents a glTF texture sampler

## Description

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.

## Tutorials

- Runtime file loading and saving

## Properties

- **mag_filter**: int = 9729  
  - set_mag_filter(value: int)  
  - get_mag_filter()  
  - Texture's magnification filter, used when texture appears larger on screen than the source image.

- **min_filter**: int = 9987  
  - set_min_filter(value: int)  
  - get_min_filter()  
  - Texture's minification filter, used when the texture appears smaller on screen than the source image.

- **wrap_s**: int = 10497  
  - set_wrap_s(value: int)  
  - get_wrap_s()  
  - Wrapping mode to use for S-axis (horizontal) texture coordinates.

- **wrap_t**: int = 10497  
  - set_wrap_t(value: int)  
  - get_wrap_t()  
  - Wrapping mode to use for T-axis (vertical) texture coordinates.