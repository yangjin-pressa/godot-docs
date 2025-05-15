# Sky Class Overview

## Class Hierarchy
- `Sky` inherits from `Resource` → `RefCounted` → `Object`

## Core Functionality
- Uses a `Material` to render 3D environment background and emitted light
- Updates reflection/radiance cubemaps for environmental lighting

## Key Properties

- **ProcessMode** = 0 (default)
- **RadianceSize** = 3 (256×256 pixels)
- **SkyMaterial** = (default material)

## Enumerations

### RadianceSize
- **RADIANCE_SIZE_32** = 0 (32×32)
- **RADIANCE_SIZE_64** = 1 (64×64)
- **RADIANCE_SIZE_128** = 2 (128×128)
- **RADIANCE_SIZE_256** = 3 (256×256)
- **RADIANCE_SIZE_512** = 4 (512×512)
- **RADIANCE_SIZE_1024** = 5 (1024×1024)
- **RADIANCE_SIZE_2048** = 6 (2048×2048)
- **RADIANCE_SIZE_MAX** = 7 (maximum enum value)

### ProcessMode
- **PROCESS_MODE_AUTOMATIC** = 0 (auto-select based on shader)
- **PROCESS_MODE_QUALITY** = 1 (high-quality sampling)
- **PROCESS_MODE_INCREMENTAL** = 2 (multi-frame updates)
- **PROCESS_MODE_REALTIME** = 3 (fast filtering)

## Property Descriptions

### ProcessMode
- Controls radiance map generation method
- Affects quality vs performance tradeoff
- Default: QUALITY mode

### RadianceSize
- Determines cubemap resolution
- Larger values = more detailed lighting
- Note: High values (≥512) may cause hardware issues

### SkyMaterial
- Used for background rendering
- Options: PanoramaSkyMaterial, ProceduralSkyMaterial, PhysicalSkyMaterial, or custom ShaderMaterial

## Important Notes
- FAST FILTERING (REALTIME mode) requires 256×256 cubemaps
- QUALITY mode uses importance sampling for better lighting
- INCREMENTAL mode updates over multiple frames for smooth transitions
- High-quality settings may require hardware with sufficient VRAM

## Performance Considerations
- QUALITY mode is computationally intensive
- REALTIME mode is faster but less accurate
- RADIANCE_SIZE_256 is recommended for FAST FILTERING
- High-end hardware recommended for larger radiance sizes