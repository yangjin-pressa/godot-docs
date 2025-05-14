# AudioEffectCompressor

## Inheritance
- Inherits from: `AudioEffect` → `Resource` → `RefCounted` → `Object`

## Description
A dynamic range compressor reduces sound levels when amplitude exceeds a threshold, smoothing dynamics and increasing overall volume. Common uses include:
- Master bus compression (preferred over limiter)
- Voice channels for balanced sound
- Sidechaining (e.g., music/SFX level control)
- Transient accentuation via attack adjustment

## Tutorials
- [Audio buses](../tutorials/audio/audio_buses)

## Properties
- **attack_us**: float = 20.0  
  Compressor reaction time (microseconds). Range: 20–2000
- **gain**: float = 0.0  
  Output signal gain. Range: -∞ to +∞
- **mix**: float = 1.0  
  Signal blend (0 = dry, 1 = wet). Range: 0–1
- **ratio**: float = 4.0  
  Compression intensity. Range: 1–48
- **release_ms**: float = 250.0  
  Recovery time after threshold is met (milliseconds). Range: 20–2000
- **sidechain**: StringName = ""  
  Audio bus for sidechain threshold detection
- **threshold**: float = 0.0  
  Compression trigger level. Range: -60–0

## Method References
- `set_attack_us(value: float)`, `get_attack_us()`
- `set_gain(value: float)`, `get_gain()`
- `set_mix(value: float)`, `get_mix()`
- `set_ratio(value: float)`, `get_ratio()`
- `set_release_ms(value: float)`, `get_release_ms()`
- `set_sidechain(value: StringName)`, `get_sidechain()`
- `set_threshold(value: float)`, `get_threshold()`