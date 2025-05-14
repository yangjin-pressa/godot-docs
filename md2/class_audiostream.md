# AudioStream

## Description  
A base class for audio streams in Godot, providing common functionality for audio playback and stream management.

---

## Tutorials  
- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)  
- [Audio Stream Player Example](https://godotengine.org/asset-library/asset/2760)  

---

## Signals  
- **parameter_list_changed**: Emitted when the stream's parameter list changes.  

---

## Methods  

### **Private Methods**  
- **_get_bar_beats()**: Virtual method to return bar beats for the stream.  
- **_get_stream_name()**: Virtual method to customize the stream's name.  
- **_has_loop()**: Virtual method to return whether the stream has a loop.  
- **_instantiate_playback()**: Virtual method to create a new `AudioStreamPlayback` instance.  
- **_is_monophonic()**: Virtual method to determine if the stream supports single-channel playback.  

### **Public Methods**  
- **can_be_sampled()**: Experimental. Returns if the stream can be sampled (only static streams).  
- **generate_sample()**: Experimental. Generates an `AudioSample` based on the current stream.  
- **get_length()**: Returns the length of the audio stream in seconds.  
- **instantiate_playback()**: Returns a newly created `AudioStreamPlayback` instance.  
- **is_meta_stream()**: Returns `true` if the stream is a collection of other streams.  
- **is_monophonic()**: Returns `true` if the stream supports single-channel playback.  

---

## Notes  
- **Virtual Methods**: Should be overridden by subclasses to customize behavior.  
- **Const Methods**: Do not modify instance variables.  
- **Experimental Methods**: `can_be_sampled()` and `generate_sample()` may change or be removed in future versions.