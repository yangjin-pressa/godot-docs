# AudioStreamWAV

## Overview
A class for handling WAV audio streams, supporting various audio formats and properties.

---

## Description
This class provides functionality for loading, manipulating, and saving WAV audio data. It supports different audio formats, sample rates, and stereo capabilities.

---

## Tutorials
- [Loading and playing WAV files](#method-load_from_file)

---

## Properties

| Property         | Type          | Default Value | Description |
|------------------|---------------|----------------|-------------|
| data             | PackedByteArray | -              | Audio data buffer |
| format           | Format       | 0              | Audio format type |
| loop_begin       | int          | 0              | Loop start point in samples |
| loop_end         | int          | 0              | Loop end point in samples |
| loop_mode        | LoopMode     | 0              | Loop mode type |
| mix_rate         | int          | 44100          | Sample rate for mixing |
| stereo           | bool         | false          | Whether audio is stereo |

---

## Methods

### `load_from_buffer(stream_data: PackedByteArray, options: Dictionary = {}) -> AudioStreamWAV`
- **Description**: Creates a new `AudioStreamWAV` instance from a buffer containing WAV data.
- **Parameters**:
  - `stream_data`: The buffer with WAV data.
  - `options`: Dictionary of properties matching `ResourceImporterWAV` settings.

### `load_from_file(path: String, options: Dictionary = {}) -> AudioStreamWAV`
- **Description**: Creates a new `AudioStreamWAV` instance from a WAV file.
- **Example**:
  ```gdscript
  @onready var audio_player = $AudioStreamPlayer

  func _ready():
      get_window().files_dropped.connect(_on_files_dropped)

  func _on_files_dropped(files):
      if files[0].get_extension() == "wav":
          audio_player.stream = AudioStreamWAV.load_from_file(files[0], {
                  "force/max_rate": true,
                  "force/max_rate_hz": 11025
              })
          audio_player.play()
  ```

### `save_to_wav(path: String) -> Error`
- **Description**: Saves the `AudioStreamWAV` as a WAV file. IMA ADPCM and QOA formats cannot be saved.
- **Note**: Automatically appends `.wav` if the path doesn't have it.

---

## Enumerations

### Format
- **WAV**: Standard WAV format.
- **IMA**: IMA ADPCM format.
- **QOA**: Quite OK Audio format.

### LoopMode
- **0**: No loop.
- **1**: Loop from start to end.
- **2**: Loop from loop_begin to loop_end.

---

## Property Descriptions

- **data**: A `PackedByteArray` containing the audio data. Changes to this property will update the stream.
- **format**: Specifies the audio format (WAV, IMA, QOA).
- **loop_begin**: The starting sample index for looping.
- **loop_end**: The ending sample index for looping.
- **loop_mode**: Determines how looping is performed.
- **mix_rate**: Sample rate for audio output (e.g., 44100 Hz is standard).
- **stereo**: Boolean indicating whether the audio is stereo.

---

## Notes
- **Sample Rate**: Common rates include 11025, 16000, 22050, 32000, 44100, and 48000 Hz. Higher rates require more storage but improve quality.
- **File Format**: Only WAV files are supported for loading and saving.