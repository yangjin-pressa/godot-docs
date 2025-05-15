# RDPipelineMultisampleState

**Inherits**: RefCounted < Object

Pipeline multisample state used by RenderingDevice.

## Description
Controls multisample/supersample antialiasing for RenderingDevice rendering.

## Properties

- **enable_alpha_to_coverage**: bool = false  
  Enables alpha to coverage for multisample antialiasing.

- **enable_alpha_to_one**: bool = false  
  Forces alpha to 0.0 or 1.0 for hard edges. Requires enable_alpha_to_coverage to be true.

- **enable_sample_shading**: bool = false  
  Enables per-sample shading for higher quality antialiasing. Has high performance cost.

- **min_sample_shading**: float = 0.0  
  Multiplier for sample count to determine samples per fragment. Effective only when enable_sample_shading is true.

- **sample_count**: TextureSamples = 0  
  Number of MSAA/SSAA samples. Higher values improve antialiasing but reduce performance.

- **sample_masks**: Array[int] = []  
  Sample mask array for sample masking. See Vulkan documentation for details.

## Method Descriptions

### enable_alpha_to_coverage
- **set_enable_alpha_to_coverage**(value: bool)  
- **get_enable_alpha_to_coverage**()

### enable_alpha_to_one
- **set_enable_alpha_to_one**(value: bool)  
- **get_enable_alpha_to_one**()

### enable_sample_shading
- **set_enable_sample_shading**(value: bool)  
- **get_enable_sample_shading**()

### min_sample_shading
- **set_min_sample_shading**(value: float)  
- **get_min_sample_shading**()

### sample_count
- **set_sample_count**(value: TextureSamples)  
- **get_sample_count**()

### sample_masks
- **set_sample_masks**(value: Array[int])  
- **get_sample_masks**()

## Notes
- Sample shading (enable_sample_shading) requires Vulkan 1.3 or later.
- Sample masks are used for per-sample control in Vulkan.