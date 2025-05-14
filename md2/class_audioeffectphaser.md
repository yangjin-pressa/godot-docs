# AudioEffectPhaser

## Inheritance
- **AudioEffect**  
  - **Resource**  
    - **RefCounted**  
      - **Object**

## Description
Combines phase-shifted signals with the original signal. The movement of the phase-shifted signals is controlled using a low-frequency oscillator.

## Tutorials
- [Audio buses](../tutorials/audio/audio_buses)

## Properties
- **depth**: float = 1.0  
  - Determines how high the filter frequencies sweep. Low value affects bass, high value affects treble. Range: 0.1–4.0.  
  - Methods: `set_depth(value: float)`, `get_depth()`

- **feedback**: float = 0.7  
  - Output percent of modified sound. Range: 0.1–0.9.  
  - Methods: `set_feedback(value: float)`, `get_feedback()`

- **range_max_hz**: float = 1600.0  
  - Maximum frequency affected by LFO modulations. Range: 10–10000.  
  - Methods: `set_range_max_hz(value: float)`, `get_range_max_hz()`

- **range_min_hz**: float = 440.0  
  - Minimum frequency affected by LFO modulations. Range: 10–10000.  
  - Methods: `set_range_min_hz(value: float)`, `get_range_min_hz()`

- **rate_hz**: float = 0.5  
  - Adjusts the rate in Hz for effect sweeping.  
  - Methods: `set_rate_hz(value: float)`, `get_rate_hz()`

## Key Concepts
- **Phaser Effect**: Modulates audio signals using phase-shifted copies.  
- **LFO (Low-Frequency Oscillator)**: Controls the movement of phase-shifted signals.  
- **Parameter Range**: Values for properties are constrained to specific ranges for optimal performance.