# AudioStreamPlaylist

**Inherits**: AudioStream < Resource < RefCounted < Object

## Properties
- **fade_time**: float = 0.3
- **loop**: bool = true
- **shuffle**: bool = false
- **stream_count**: int = 0

## Constants
- **MAX_STREAMS** = 64

## Property Descriptions
- **fade_time**: Fade time between streams. Streams should have extra audio for smooth transitions.
- **loop**: If true, the playlist loops; otherwise, it ends when the last stream finishes.
- **shuffle**: If true, the playlist shuffles streams on each playback start or loop.
- **stream_count**: Number of streams in the playlist.

## Methods
- **get_bpm**(): Returns the BPM of the playlist (varies by current clip).
- **get_list_stream**(stream_index: int): Returns the stream at the specified index.
- **set_list_stream**(stream_index: int, audio_stream: AudioStream): Sets the stream at the specified index.

## Method Descriptions
- **get_bpm**: Retrieves the current BPM of the playlist.
- **get_list_stream**: Accesses the stream at a specific position in the playlist.
- **set_list_stream**: Replaces the stream at a specific position in the playlist.