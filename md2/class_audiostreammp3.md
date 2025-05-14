# AudioStreamMP3

## Inheritance
- AudioStreamMP3 inherits from AudioStream → Resource → RefCounted → Object

## Description
MP3 audio stream driver. See [data](#class_AudioStreamMP3_property_data) if you want to load an MP3 file at run-time.

**Note:** This class can optionally support legacy MP1 and MP2 formats if the engine is compiled with `minimp3_extra_formats=yes`.

---

## Properties

| Type | Name | Default | Description |
|------|------|---------|-------------|
| int | bar_beats | 4 |  |
| int | beat_count | 0 |  |
| float | bpm | 0.0 |  |
| PackedByteArray | data | PackedByteArray() | Contains the audio data in bytes. |
| bool | loop | false | If true, the stream will automatically loop when it reaches the end. |
| float | loop_offset | 0.0 | Time in seconds at which the stream starts after being looped. |

---

## Methods

- **load_from_buffer**(stream_data: PackedByteArray) → AudioStreamMP3: Creates an instance from a buffer containing MP3 data.
- **load_from_file**(path: String) → AudioStreamMP3: Creates an instance from an MP3 file path.

---

## Property Descriptions

### bar_beats
- **set_bar_beats**(value: int): 
- **get_bar_beats**():

There is currently no description for this property.

### beat_count
- **set_beat_count**(value: int): 
- **get_beat_count**():

There is currently no description for this property.

### bpm
- **set_bpm**(value: float): 
- **get_bpm**():

There is currently no description for this property.

### data
- **set_data**(value: PackedByteArray): 
- **get_data**():

Contains the audio data in bytes.

**Example:**
```gdscript
func load_mp3(path):
    var file = FileAccess.open(path, FileAccess.READ)
    var sound = AudioStreamMP3.new()
    sound.data = file.get_buffer(file.get_length())
    return sound
```

**Note:** The returned array is *copied* and any changes to it will not affect the original.

### loop
- **set_loop**(value: bool): 
- **get_loop**():

There is currently no description for this property.

### loop_offset
- **set_loop_offset**(value: float): 
- **get_loop_offset**():

There is currently no description for this property.

---

## Notes
- The `data` property is crucial for loading MP3 files. It stores the raw audio data.