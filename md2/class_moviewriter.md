# MovieWriter

**Inherits:** Object

## Description
Godot supports non-real-time video recording with perfect frame pacing. Two built-in encoders are available:

1. **AVI (MJPEG):**  
   - File extension: `.avi`  
   - Features: Lossy compression, medium file size, fast encoding  
   - Limitation: No transparency, max file size 4GB  
   - Quality adjustable in ProjectSettings  

2. **PNG Sequence (WAV audio):**  
   - File extension: `.png`  
   - Features: Lossless compression, large file size, slow encoding  
   - Limitation: No transparency, requires external tool for web playback  

Custom encoders can be created by extending MovieWriter (recommended for GDExtension).  

**Editor Usage**:  
- Set default path in `ProjectSettings.editor/movie_writer/movie_file`  
- Add `movie_file` metadata to root node for scene-specific paths  
- Enable Movie Maker mode via the editor's video reel icon  
- Recording stops when engine quits (not on Ctrl+C termination)  

**Note**: Avoid using MovieWriter for end-user recording; use OBS Studio or FFmpeg instead.  

---

## Methods

- **_get_audio_mix_rate()** → int (Hz)  
  Returns audio sample rate (default: 48000 Hz).  

- **_get_audio_speaker_mode()** → SpeakerMode  
  Returns audio output mode (default: stereo).  

- **_handles_file(path: String)** → bool  
  Determines if this writer supports a file path. Example:  
  ```gdscript
  func _handles_file(path):
      return path.get_extension().to_lower() == "mkv"
  ```  

- **_write_begin(movie_size: Vector2i, fps: int, base_path: String)** → Error  
  Called before recording starts.  

- **_write_end()**  
  Called when recording finishes (engine quits).  

- **_write_frame(frame_image: Image, audio_frame_block: const void*)** → Error  
  Writes a frame to the output.  

- **add_writer(writer: MovieWriter)**  
  Adds a custom writer to the engine. Must be called early in initialization.  

---

## Notes
- AVI output is limited to 4GB file size.  
- PNG sequence requires external tools for web playback.  
- _write_end() is not called on Ctrl+C termination.  
- Custom writers must override _handles_file() to support specific extensions.