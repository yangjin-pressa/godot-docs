# AudioEffectInstance

## Inheritance
- **Inherits:** [RefCounted](#) < [Object](#)
- **Inherited By:** [AudioEffectSpectrumAnalyzerInstance](#)

---

## Description
An audio effect instance manipulates the audio it receives for a given effect. This instance is automatically created by an [AudioEffect](#) when it is added to a bus, and should usually not be created directly. If necessary, it can be fetched at run-time with [AudioServer.get_bus_effect_instance](#).

### Tutorials
- [Audio buses](../tutorials/audio/audio_buses)

---

## Methods

1. **_process**  
   - **Parameters:**  
     - src_buffer: const void*  
     - dst_buffer: AudioFrame*  
     - frame_count: int  
   - **Virtual:** Yes  
   - **Note:** Not useful to override in GDScript or C#. Only GDExtension can use this.

2. **_process_silence**  
   - **Returns:** bool  
   - **Virtual:** Yes  
   - **Const:** Yes  
   - **Note:** Return true to force always call _process(), even if the bus is muted.

---

## Method Descriptions

### _process
Called by [AudioServer](#) to process this effect. When _process_silence() is not overridden or returns false, this method is called only when the bus is active.

### _process_silence
Override this method to customize the processing behavior of this effect instance. Return true to force always call _process(), even if the bus is muted or cannot be heard.