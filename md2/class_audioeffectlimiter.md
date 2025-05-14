# AudioEffectLimiter

**Deprecated:** Use `AudioEffectHardLimiter` instead.

**Inherits:** AudioEffect → Resource → RefCounted → Object

## Description
A limiter prevents sound from exceeding a dB threshold. It uses soft clipping to reduce peaks below the threshold. Adding it to the Master bus helps prevent clipping.

## Tutorials
- [Audio buses](../tutorials/audio/audio_buses)

## Properties

- **ceiling_db** (float): Maximum allowed value in dB. Range: -20 to -0.1. Default: -0.1
- **soft_clip_db** (float): Gain applied to limited waves in dB. Range: 0 to 6. Default: 2.0
- **soft_clip_ratio** (float): Soft clipping ratio. Default: 10.0 (no description available)
- **threshold_db** (float): Activation threshold in dB. Range: -30 to 0. Default: 0.0

## Method References
- `set_ceiling_db(float)`  
- `get_ceiling_db()`  
- `set_soft_clip_db(float)`  
- `get_soft_clip_db()`  
- `set_soft_clip_ratio(float)`  
- `get_soft_clip_ratio()`  

## Notes
- Soft clipping ratio property lacks a description.  
- This class is deprecated in favor of `AudioEffectHardLimiter`.