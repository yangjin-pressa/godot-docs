**Class Name**: ResourceImporterMP3  
**Inherits**: ResourceImporter → RefCounted → Object  

---

### Description  
Imports an MP3 audio file for playback.  
- MP3 is a lossy audio format with worse quality than Ogg Vorbis at the same bitrate.  
- Use Ogg Vorbis for most cases. Use MP3 only if no higher-quality source is available.  
- MP3 requires more CPU than WAV for decoding. Use WAV for simultaneous sound playback on low-end devices.  

---

### Tutorials  
- [Importing audio samples](../tutorials/assets_pipeline/importing_audio_samples)  

---

### Properties  
- **bar_beats**: int = 4  
- **beat_count**: int = 0  
- **bpm**: float = 0  
- **loop**: bool = false  
- **loop_offset**: float = 0  

---

### Property Descriptions  
- **bar_beats**  
  - Sets the number of bars per beat in the audio track. Relevant for interactive music.  
  - Editor for this property is available in the **Advanced Import Settings**.  

- **beat_count**  
  - Tracks the number of beats in the audio. Relevant for interactive music.  
  - Editor for this property is available in the **Advanced Import Settings**.  

- **bpm**  
  - Beats per minute of the audio. Should match the composition's BPM.  
  - Editor for this property is available in the **Advanced Import Settings**.  

- **loop**  
  - If enabled, the audio restarts from the beginning after reaching the end.  
  - Note: Looping audio in `AudioStreamPlayer` does not trigger the `finished` signal.  

- **loop_offset**  
  - Determines the start time for looping after the audio ends.  
  - Only effective if `loop` is enabled.  
  - Editor for this property is available in the **Advanced Import Settings**.  

--- 

**Note**: Properties related to interactive music (e.g., bar_beats, beat_count, bpm) are not applicable to sound effects.