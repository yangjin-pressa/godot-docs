# RenderSceneBuffersExtension

**Inherits**: RenderSceneBuffers ← RefCounted ← Object

## Description
This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

## Methods
- **_configure(config: RenderSceneBuffersConfiguration)**  
  Virtual method. Implement in GDExtension to handle (re)sizing of a viewport.

- **_set_anisotropic_filtering_level(anisotropic_filtering_level: int)**  
  Virtual method. Implement in GDExtension to change the anisotropic filtering level.

- **_set_fsr_sharpness(fsr_sharpness: float)**  
  Virtual method. Implement in GDExtension to record a new FSR sharpness value.

- **_set_texture_mipmap_bias(texture_mipmap_bias: float)**  
  Virtual method. Implement in GDExtension to change the texture mipmap bias.

- **_set_use_debanding(use_debanding: bool)**  
  Virtual method. Implement in GDExtension to react to the debanding flag changing.

## Notes
All methods are virtual and require implementation in GDExtension to function. Parameters are passed as specified, and each method's purpose is tied to configuration or state modification of rendering buffers.