# AudioStreamSynchronized

**Inherits:** AudioStream < Resource < RefCounted < Object

Stream that can be fitted with sub-streams, which will be played in-sync.

## Description
A stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.

## Properties
- **stream_count**: int = 0

## Methods
- **get_sync_stream(stream_index: int)** → AudioStream (const)
  - Get one of the synchronized streams, by index.
- **get_sync_stream_volume(stream_index: int)** → float (const)
  - Get the volume of one of the synchronized streams, by index.
- **set_sync_stream(stream_index: int, audio_stream: AudioStream)**
  - Set one of the synchronized streams, by index.
- **set_sync_stream_volume(stream_index: int, volume_db: float)**
  - Set the volume of one of the synchronized streams, by index.

## Constants
- **MAX_STREAMS** = 32

## Property Descriptions
- **stream_count**: int = 0
  - Set the total amount of streams that will be played back synchronized.
  - *set_stream_count(value: int)*
  - *get_stream_count()*

## Method Descriptions
- **get_sync_stream(stream_index: int)** → AudioStream (const)
  - Get one of the synchronized streams, by index.
- **get_sync_stream_volume(stream_index: int)** → float (const)
  - Get the volume of one of the synchronized streams, by index.
- **set_sync_stream(stream_index: int, audio_stream: AudioStream)**
  - Set one of the synchronized streams, by index.
- **set_sync_stream_volume(stream_index: int, volume_db: float)**
  - Set the volume of one of the synchronized streams, by index.