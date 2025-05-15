**Class RDSamplerState**

- **anisotropy_max**: `float`, default `1e+20`  
  The maximum anisotropy level for this sampler. A higher value can improve texture quality but may increase performance costs.  
  - `set_anisotropy_max`: Sets the anisotropy level.  
  - `get_anisotropy_max`: Gets the anisotropy level.

- **mag_filter**: `SamplerFilter`, default `0`  
  The filtering method to use when magnifying textures.  
  - `set_mag_filter`: Sets the magnification filter.  
  - `get_mag_filter`: Gets the magnification filter.

- **min_filter**: `SamplerFilter`, default `0`  
  The filtering method to use when minimizing textures.  
  - `set_min_filter`: Sets the minification filter.  
  - `get_min_filter`: Gets the minification filter.

- **mip_filter**: `SamplerFilter`, default `0`  
  The filtering method to use when mip-mapping textures.  
  - `set_mip_filter`: Sets the mip-map filter.  
  - `get_mip_filter`: Gets the mip-map filter.

- **max_lod**: `float`, default `1e+20`  
  The maximum level of detail (LOD) that can be used for this sampler. A higher value can improve texture quality but may increase performance costs.  
  - `set_max_lod`: Sets the maximum level of detail.  
  - `get_max_lod`: Gets the maximum level of detail.

- **min_lod**: `float`, default `0.0`  
  The minimum level of detail (LOD) that can be used for this sampler. A lower value can improve texture quality at lower resolutions but may cause aliasing.  
  - `set_min_lod`: Sets the minimum level of detail.  
  - `get_min_lod`: Gets the minimum level of detail.

- **repeat_u**: `SamplerRepeatMode`, default `2`  
  The repeat mode for the U coordinate. This determines how the texture is repeated when it is sampled beyond the texture's boundaries.  
  - `set_repeat_u`: Sets the repeat mode for the U coordinate.  
  - `get_repeat_u`: Gets the repeat mode for the U coordinate.

- **repeat_v**: `SamplerRepeatMode`, default `2`  
  The repeat mode for the V coordinate. This determines how the texture is repeated when it is sampled beyond the texture's boundaries.  
  - `set_repeat_v`: Sets the repeat mode for the V coordinate.  
  - `get_repeat_v`: Gets the repeat mode for the V coordinate.

- **repeat_w**: `SamplerRepeatMode`, default `2`  
  The repeat mode for the W coordinate. This determines how the texture is repeated when it is sampled beyond the texture's boundaries. Only effective for 3D samplers.  
  - `set_repeat_w`: Sets the repeat mode for the W coordinate.  
  - `get_repeat_w`: Gets the repeat mode for the W coordinate.

- **unnormalized_uvw**: `bool`, default `false`  
  Whether the U, V, and W coordinates are normalized. If enabled, the coordinates are interpreted as values between 0 and 1; if disabled, they are interpreted as offsets from the texture's base address. This mode is useful for certain types of textures and rendering techniques.  
  - `set_unnormalized_uvw`: Sets the normalization mode for the U, V, and W coordinates.  
  - `get_unnormalized_uvw`: Gets the normalization mode for the U, V, and W coordinates.

- **use_anisotropy**: `bool`, default `false`  
  Whether to enable anisotropic filtering for this sampler. Anisotropic filtering improves texture quality when sampling at an angle, but may increase performance costs.  
  - `set_use_anisotropy`: Enables or disables anisotropic filtering.  
  - `get_use_anisotropy`: Gets the current state of anisotropic filtering.