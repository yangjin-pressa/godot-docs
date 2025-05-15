# RenderSceneBuffersConfiguration

**Inherits:** RefCounted < Object

## Description
Configuration object used to setup a RenderSceneBuffers object. Created and populated by the render engine on a viewport change.

## Properties
- **anisotropic_filtering_level**: ViewportAnisotropicFiltering = 2  
  Level of the anisotropic filter.

- **fsr_sharpness**: float = 0.0  
  FSR Sharpness applicable if FSR upscaling is used.

- **internal_size**: Vector2i = Vector2i(0, 0)  
  The size of the 3D render buffer used for rendering.

- **msaa_3d**: ViewportMSAA = 0  
  The MSAA mode we're using for 3D rendering.

- **render_target**: RID = RID()  
  The render target associated with these buffer.

- **scaling_3d_mode**: ViewportScaling3DMode = 255  
  The requested scaling mode with which we upscale/downscale if internal_size and target_size are not equal.

- **screen_space_aa**: ViewportScreenSpaceAA = 0  
  The requested screen space AA applied in post processing.

- **target_size**: Vector2i = Vector2i(0, 0)  
  The target (upscale) size if scaling is used.

- **texture_mipmap_bias**: float = 0.0  
  Bias applied to mipmaps.

- **view_count**: int = 1  
  The number of views we're rendering.

## Methods
- **set_anisotropic_filtering_level(value: ViewportAnisotropicFiltering)**  
- **get_anisotropic_filtering_level()**: ViewportAnisotropicFiltering

- **set_fsr_sharpness(value: float)**  
- **get_fsr_sharpness()**: float

- **set_internal_size(value: Vector2i)**  
- **get_internal_size()**: Vector2i

- **set_msaa_3d(value: ViewportMSAA)**  
- **get_msaa_3d()**: ViewportMSAA

- **set_render_target(value: RID)**  
- **get_render_target()**: RID

- **set_scaling_3d_mode(value: ViewportScaling3DMode)**  
- **get_scaling_3d_mode()**: ViewportScaling3DMode

- **set_screen_space_aa(value: ViewportScreenSpaceAA)**  
- **get_screen_space_aa()**: ViewportScreenSpaceAA

- **set_target_size(value: Vector2i)**  
- **get_target_size()**: Vector2i

- **set_texture_mipmap_bias(value: float)**  
- **get_texture_mipmap_bias()**: float

- **set_view_count(value: int)**  
- **get_view_count()**: int