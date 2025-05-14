# AudioEffectDistortion

**Inherits**: AudioEffect → Resource → RefCounted → Object

Adds a distortion effect to an audio bus. Modifies waveform to create a "crunchy" or "abrasive" sound used for simulating saturated devices.

## Description
Available distortion types:
- Clip
- Tan
- Lo-fi (bit crushing)
- Overdrive
- Waveshape

## Tutorials
- [Audio buses](../tutorials/audio/audio_buses)

## Properties
- **drive**: float (0.0) - Distortion intensity (0-1)
- **keep_hf_hz**: float (16000.0) - High-pass filter cutoff (1-20000 Hz)
- **mode**: Mode (0) - Distortion type
- **post_gain**: float (0.0) - Post-effect gain (-80 to 24 dB)
- **pre_gain**: float (0.0) - Pre-effect gain (-60 to 60 dB)

## Enumerations
### Mode
- **MODE_CLIP** = 0: Cuts waveform peaks
- **MODE_ATAN** = 1: No description available
- **MODE_LOFI** = 2: Bit depth reduction emulation
- **MODE_OVERDRIVE** = 3: Warm transistor distortion (drive has no effect)
- **MODE_WAVESHAPE** = 4: Abrasive electronic sound

## Property Descriptions
- **drive**: Set/Get distortion intensity
- **keep_hf_hz**: Set/Get high-pass filter cutoff
- **mode**: Set/Get distortion type
- **post_gain**: Set/Get post-effect gain
- **pre_gain**: Set/Get pre-effect gain

Note: Missing description for MODE_ATAN - help document this enum.