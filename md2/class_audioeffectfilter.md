**Class Name:** AudioEffectFilter  
**Inherits:** AudioEffect < Resource < RefCounted < Object  

**Inherited By:**  
- AudioEffectBandLimitFilter  
- AudioEffectBandPassFilter  
- AudioEffectHighPassFilter  
- AudioEffectHighShelfFilter  
- AudioEffectLowPassFilter  
- AudioEffectLowShelfFilter  
- AudioEffectNotchFilter  

**Description:**  
Allows frequencies other than the `cutoff_hz` to pass.  

**Tutorials:**  
- Audio buses: [../tutorials/audio/audio_buses](../tutorials/audio/audio_buses)  

**Properties:**  
- **cutoff_hz**: float = 2000.0  
- **db**: FilterDB = 0  
- **gain**: float = 1.0  
- **resonance**: float = 0.5  

**Enumerations:**  
- **FilterDB**  
  - FILTER_6DB = 0  
  - FILTER_12DB = 1  
  - FILTER_18DB = 2  
  - FILTER_24DB = 3  

**Property Descriptions:**  
- **cutoff_hz**  
  - Type: float  
  - Default: 2000.0  
  - Description: Threshold frequency for the filter, in Hz.  
  - Methods:  
    - set_cutoff(value: float)  
    - get_cutoff()  

- **db**  
  - Type: FilterDB  
  - Default: 0  
  - Description: Steepness of the cutoff curve in dB per octave.  
  - Methods:  
    - set_db(value: FilterDB)  
    - get_db()  

- **gain**  
  - Type: float  
  - Default: 1.0  
  - Description: Gain amount of the frequencies after the filter.  
  - Methods:  
    - set_gain(value: float)  
    - get_gain()  

- **resonance**  
  - Type: float  
  - Default: 0.5  
  - Description: Amount of boost in the frequency range near the cutoff frequency.  
  - Methods:  
    - set_resonance(value: float)  
    - get_resonance()