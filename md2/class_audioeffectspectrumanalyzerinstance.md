# AudioEffectSpectrumAnalyzerInstance

**Inherits:** AudioEffectInstance < RefCounted < Object

## Description
Queryable instance of an AudioEffectSpectrumAnalyzer. Used to query magnitude of a frequency range on its host bus.

Obtain via: AudioServer.get_bus_effect_instance()

## Tutorials
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

## Methods
- **get_magnitude_for_frequency_range**(from_hz: float, to_hz: float, mode: MagnitudeMode = 1) → Vector2
  - Returns magnitude of frequencies in linear energy as Vector2 (left channel: x, right channel: y)
  - `mode` determines processing mode (see MagnitudeMode)

## Enumerations
### MagnitudeMode
- **MAGNITUDE_AVERAGE** = 0
  - Average value across frequency range
- **MAGNITUDE_MAX** = 1
  - Maximum value in frequency range