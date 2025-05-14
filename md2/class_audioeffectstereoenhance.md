# AudioEffectStereoEnhance

**Inherits:** AudioEffect < Resource < RefCounted < Object

## Description
An audio effect that can be used to adjust the intensity of stereo panning.

## Tutorials
- Audio buses: ../tutorials/audio/audio_buses

## Properties
- pan_pullout: float = 1.0
- surround: float = 0.0
- time_pullout_ms: float = 0.0

## Property Descriptions

**pan_pullout**  
- set_pan_pullout(value: float)  
- get_pan_pullout()  
Amplifies the difference between stereo channels, increasing or decreasing existing panning. A value of 0.0 will downmix stereo to mono. Does not affect a mono signal.

**surround**  
- set_surround(value: float)  
- get_surround()  
Widens sound stage through phase shifting in conjunction with time_pullout_ms. Just pans sound to the left channel if time_pullout_ms is 0.

**time_pullout_ms**  
- set_time_pullout(value: float)  
- get_time_pullout()  
Widens sound stage through phase shifting in conjunction with surround. Just delays the right channel if surround is 0.