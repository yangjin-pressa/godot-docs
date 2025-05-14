# AudioEffectEQ

**Inherits:** AudioEffect < Resource < RefCounted < Object  
**Inherited By:** AudioEffectEQ10, AudioEffectEQ21, AudioEffectEQ6  

Base class for audio equalizers. Provides control over frequencies. Useful for compensating audio deficiencies, adjusting mixes for different playback devices, or modifying master buses.  

## Tutorials  
Audio buses (tutorial)  

## Methods  
- `get_band_count()`: Returns the number of bands of the equalizer.  
- `get_band_gain_db(band_idx)`: Returns the band's gain at the specified index, in dB.  
- `set_band_gain_db(band_idx, volume_db)`: Sets the band's gain at the specified index, in dB.  

## Key Functionality  
- Adjusts audio frequency bands for customization.  
- Supports dynamic gain modification for specific band indices.  
- Used in scenarios like mastering mixes or adapting audio for mobile speakers.