**Class: ResourceImporterOggVorbis**  
- **Inherits From**: ResourceImporter → RefCounted → Object  
- **Description**: A class for loading and managing Ogg Vorbis audio files. It provides better audio quality compared to formats like ResourceImporterMP3.  

---

### **Tutorials**  
- Example: [ResourceImporterOggVorbis Example](https://github.com/godotengine/godot-engine/tree/main/docs/en/main/classes/resource_importer_ogg_vorbis.rst)  

---

### **Properties**  
| Type     | Name           | Default | Description                                                                 |
|----------|----------------|---------|-----------------------------------------------------------------------------|
| int      | bar_beats      | 0       | Number of bars in the audio for music.                                     |
| float    | bitrate        | 128.0   | Bitrate in kbps.                                                           |
| float    | channel_ratio  | 1.0     | Ratio of channels (e.g., 2.0 for stereo).                                  |
| int      | frames         | 0       | Number of audio frames to load.                                            |
| int      | samples        | 0       | Number of audio samples to load.                                           |
| float    | sample_rate    | 44100.0 | Sampling rate in Hz.                                                       |
| bool     | use_ladspa     | false   | Whether to use LADSPA effects for audio processing.                        |

---

### **Methods**  
- **`static get_audio_format()`**:  
  - **Description**: Retrieves the audio format for Ogg Vorbis files.  
  - **Deprecated**: Use `AudioStreamOggVorbis.get_audio_format()` instead.  

- **`static get_extension()`**:  
  - **Description**: Returns the file extension (e.g., `.ogg`).  
  - **Deprecated**: Use `AudioStreamOggVorbis.get_extension()` instead.  

---

### **Property Descriptions**  
- **bar_beats**:  
  - Sets the number of bars in the audio for music.  
- **bitrate**:  
  - Controls the audio bitrate in kbps.  
- **channel_ratio**:  
  - Adjusts the channel ratio for stereo or mono output.  
- **frames**:  
  - Specifies the number of audio frames to load.  
- **samples**:  
  - Defines the number of audio samples to load.  
- **sample_rate**:  
  - Sets the sampling rate in Hz (e.g., 44100 for standard audio).  
- **use_ladspa**:  
  - Enables LADSPA effects for audio processing.  

--- 

**Notes**:  
- All methods are static and deprecated. Use `AudioStreamOggVorbis` for direct audio handling.  
- Properties are optional; default values ensure basic functionality.