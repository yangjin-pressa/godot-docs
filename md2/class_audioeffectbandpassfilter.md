# AudioEffectBandPassFilter

**Inherits:**  
- AudioEffectFilter  
  - AudioEffect  
    - Resource  
      - RefCounted  
        - Object  

## Description  
Attenuates frequencies within a range around the `AudioEffectFilter.cutoff_hz` property, while cutting frequencies outside this band.

## Tutorials  
- [Audio buses](../tutorials/audio/audio_buses)

## Key Concepts  
- **virtual**: (This method should typically be overridden by the user to have any effect.)  
- **const**: (This method has no side effects. It doesn't modify any of the instance's member variables.)  
- **vararg**: (This method accepts any number of arguments after the ones described here.)  
- **constructor**: (This method is used to construct a type.)  
- **static**: (This method doesn't need an instance to be called, so it can be called directly using the class name.)  
- **operator**: (This method describes a valid operator to use with this type as left-hand operand.)  
- **bitfield**: (This value is an integer composed as a bitmask of the following flags.)  
- **void**: (No return value.)  

## References  
- [AudioEffectFilter.cutoff_hz](#AudioEffectFilter.cutoff_hz)