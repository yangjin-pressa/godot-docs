# ResourceImporterWAV

## Overview
Imports WAV audio files for playback. Inherits from ResourceImporter, RefCounted, and Object.

## Key Features
- **Uncompressed format**: Higher quality than Ogg Vorbis/MP3, low CPU cost for decoding
- **Default compression**: Lossy Quite OK Audio (can be changed via compress/mode property)

## Tutorial
- [Importing audio samples](../tutorials/assets_pipeline/importing_audio_samples)

## Properties

### General Settings
- **compress/mode**: 2 (default)  
  Compression type: 0=PCM (uncompressed), 1=IMA ADPCM, 2=Quite OK Audio

### Editing Options
- **edit/loop_begin**: 0  
- **edit/loop_end**: -1 (uses end of file)  
- **edit/loop_mode**: 0 (default)  
  Loop modes: 0=Disable, 1=Forward, 2=Ping-Pong, 3=Backward, 4=From WAV metadata

- **edit/normalize**: false  
  Normalize audio volume to 0 dB

- **edit/trim**: false  
  Trim silent beginning/end (-50 dB threshold)

### Conversion Options
- **force/8_bit**: false  
  Force 8-bit quantization (reduces quality)

- **force/max_rate**: false  
  Limit sample rate (effective only when enabled)

- **force/max_rate_hz**: 44100 Hz  
  Maximum sample rate to enforce

- **force/mono**: false  
  Convert stereo to mono (reduces file size by 50%)

## Notes
- WAV files use 16-bit float format by default
- Normalization makes audio louder based on original peak volume
- Trimming uses 500-sample fade-in/fade-out to avoid pops
- IMA ADPCM: low memory usage but no seeking support
- Looping in AudioStreamPlayer doesn't trigger finished signal for looping audio

## Related
- [Quite OK Audio](https://qoaformat.org/) compression format