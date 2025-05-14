# AudioEffectHardLimiter

**Inherits:** AudioEffect < Resource < RefCounted < Object

## Description
A limiter prevents sound from exceeding a dB threshold. Hard limiters apply gain reduction when peaks cross the threshold, preserving waveform and preventing clipping. Adding this in the Master bus is recommended to avoid sudden volume peaks and distortion.

## Tutorials
- [Audio buses](../tutorials/audio/audio_buses)

## Properties
- **ceiling_db**: float = -0.3  
  Maximum allowed dB. Default prevents inter-sample peaks (ISP) from exceeding 0 dB, avoiding distortion on older hardware.

- **pre_gain_db**: float = 0.0  
  Gain to apply before limiting. Adjusts input level before compression.

- **release**: float = 0.1  
  Time (in seconds) for gain reduction to fully release after a peak.

## Property Descriptions
**ceiling_db**  
- `set_ceiling_db(value: float)`  
- `get_ceiling_db()`  
  Sets/gets the maximum allowed dB value for the waveform.

**pre_gain_db**  
- `set_pre_gain_db(value: float)`  
- `get_pre_gain_db()`  
  Adjusts the input gain level before limiting.

**release**  
- `set_release(value: float)`  
- `get_release()`  
  Controls how quickly the gain reduction fades after a peak.