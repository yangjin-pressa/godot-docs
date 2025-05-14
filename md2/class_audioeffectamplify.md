# AudioEffectAmplify

**Inherits:** AudioEffect < Resource < RefCounted < Object

Adds an amplifying audio effect to an audio bus.

## Description

Increases or decreases the volume being routed through the audio bus.

## Tutorials

- Audio buses (https://godotengine.org/documentation/ tutorials/audio/audio_buses.html)

## Properties

- **volume_db**: float = 0.0  
  Amount of amplification in decibels. Positive values make the sound louder, negative values make it quieter. Value can range from -80 to 24.

- **volume_linear**: float  
  Amount of amplification as a linear value.

## Property Descriptions

### volume_db
- **set_volume_db**(value: float): void  
- **get_volume_db**(): float  

### volume_linear
- **set_volume_linear**(value: float): void  
- **get_volume_linear**(): float  

**Note:** This member modifies volume_db for convenience. The returned value is equivalent to the result of @GlobalScope.db_to_linear() on volume_db. Setting this member is equivalent to setting volume_db to the result of @GlobalScope.linear_to_db() on a value.