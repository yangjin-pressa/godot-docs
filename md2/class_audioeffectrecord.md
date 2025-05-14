# AudioEffectRecord

## Inheritance
- Inherits from: AudioEffect → Resource → RefCounted → Object

## Description
Records sound from an audio bus into an AudioStreamWAV. 
- When applied to the "Master" bus, captures all audio output.
- Encodes recordings with specified format (8-bit, 16-bit, or compressed).
- Can be used with AudioStreamMicrophone for microphone input.
- Requires `ProjectSettings.audio/driver/enable_input` to be set to true.

## Tutorials
- [Recording with microphone](../tutorials/audio/recording_with_microphone)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)

## Properties
- **Format**: format = 1
  - Specifies the recording format. See Format enum for options.

## Methods
- **get_recording()** (const)
  - Returns the recorded AudioStreamWAV.

- **is_recording_active()** (const)
  - Returns whether the recording is active.

- **set_recording_active(record: bool)**
  - Activates or deactivates recording. Restarting clears previous recordings.

## Key Notes
- Audio input requires `ProjectSettings.audio/driver/enable_input` to be enabled.
- Format options: 8-bit, 16-bit, or compressed.