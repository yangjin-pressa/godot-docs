# AudioEffectCapture

**Inherits:** AudioEffect → Resource → RefCounted → Object

## Description
AudioEffectCapture is an AudioEffect that copies all audio frames from the attached audio effect bus into its internal ring buffer. Application code should consume these frames via `get_buffer()`. When capturing from a microphone, the format is stereo 32-bit float PCM. Unlike AudioEffectRecord, this class returns raw audio samples, not an AudioStream.

## Tutorials
- [Audio buses tutorial](audio_buses)

## Properties
- **buffer_length** (float) = 0.1  
  The length of the internal ring buffer in seconds. Setting this has no effect if the buffer is already initialized.

## Methods
- **can_get_buffer**(int frames) → bool  
  Returns true if at least `frames` number of audio frames are available.

- **clear_buffer**()  
  Clears the internal buffer. **Note:** Calling this during capture may cause data loss.

- **get_buffer**(int frames) → PackedVector2Array  
  Returns a PackedVector2Array containing the audio samples. The samples are stereo 32-bit float PCM values in the range [-1, 1].

- **get_buffer_length_frames**() → int  
  Returns the total size of the internal buffer in audio frames.

- **get_discarded_frames**() → int  
  Returns the number of audio frames discarded due to buffer overflow.

- **get_frames_available**() → int  
  Returns the number of audio frames currently available in the buffer.

- **get_pushed_frames**() → int  
  Returns the number of audio frames that have been added to the buffer.