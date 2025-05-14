# LightmapperRD

## Inheritance
- Lightmapper  
- RefCounted  
- Object  

## Description
- **Purpose**: GPU-based lightmapper for use with LightmapGI.
- **Performance**: Faster on dedicated GPUs compared to CPU-based lightmappers.
- **Technology**: Uses compute shaders for baking lightmaps.
- **Dependencies**: No need for CUDA or OpenCL libraries.
- **Compatibility**: Only usable with RenderingDevice backend (Forward+ or Mobile renderers), not Compatibility.

## Key Notes
- LightmapperRD leverages GPU capabilities for efficient lightmap baking.
- Method definitions and documentation use terms like "virtual", "const", and "static" as per the original text.