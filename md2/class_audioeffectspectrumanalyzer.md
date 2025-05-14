# AudioEffectSpectrumAnalyzer

**Inherits:** AudioEffect → Resource → RefCounted → Object

Audio effect for real-time audio visualizations. Does not affect sound output.

## Description
- Used for real-time audio visualizations
- Configures AudioEffectSpectrumAnalyzerInstance for analysis
- Instance obtained via AudioServer.get_bus_effect_instance()
- See also: AudioStreamGenerator for procedural sound generation

## Tutorials
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

## Properties
- **buffer_length**: float (default 2.0)  
  Buffer duration in seconds (higher values require more memory)
- **fft_size**: FFTSize (default 2)  
  FFT buffer size: 256 (lowest latency), 512, 1024, 2048, 4096 (highest stability)
- **tap_back_pos**: float (default 0.01)  
  (No description available)

## Enumerations
**FFTSize**
- FFT_SIZE_256 (0) → 256 samples (lowest latency)
- FFT_SIZE_512 (1) → 512 samples (low latency)
- FFT_SIZE_1024 (2) → 1024 samples (compromise)
- FFT_SIZE_2048 (3) → 2048 samples (high latency)
- FFT_SIZE_4096 (4) → 4096 samples (most stable)
- FFT_SIZE_MAX (5) → Enum size indicator

## Property Methods
- **set_buffer_length(value: float)** → void  
- **get_buffer_length()** → float  
- **set_fft_size(value: FFTSize)** → void  
- **get_fft_size()** → FFTSize  
- **set_tap_back_pos(value: float)** → void  
- **get_tap_back_pos()** → float