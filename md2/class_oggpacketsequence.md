# OggPacketSequence

**Inherits:** Resource → RefCounted → Object

A sequence of Ogg packets.

## Description
A sequence of Ogg packets.

## Properties
- **granule_positions**: PackedInt64Array = PackedInt64Array()  
  Contains the granule positions for each page in this packet sequence.  
  Note: The returned array is *copied* and any changes to it will not update the original property value. See PackedInt64Array for more details.

- **packet_data**: Array[Array] = []  
  Contains the raw packets that make up this OggPacketSequence.

- **sampling_rate**: float = 0.0  
  Holds sample rate information about this sequence. Must be set by another class that actually understands the codec.

## Methods
- **get_length() const**: float  
  The length of this stream, in seconds.

## Property Descriptions
### granule_positions
- **set_packet_granule_positions(value: PackedInt64Array)**: void  
- **get_packet_granule_positions()**: PackedInt64Array  

### packet_data
- **set_packet_data(value: Array[Array])**: void  
- **get_packet_data()**: Array[Array]  

### sampling_rate
- **set_sampling_rate(value: float)**: void  
- **get_sampling_rate()**: float  

## Notes
- granule_positions is a copy-on-write array. Modifications to the returned array do not affect the original property.
- packet_data stores raw Ogg packets as an array of byte arrays.
- sampling_rate must be set by a codec class, not this class itself.