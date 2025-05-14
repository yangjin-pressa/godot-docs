# PacketPeer

## Inheritance
- **Inherits**: RefCounted < Object  
- **Inherited By**:  
  - ENetPacketPeer  
  - MultiplayerPeer  
  - PacketPeerDTLS  
  - PacketPeerExtension  
  - PacketPeerStream  
  - PacketPeerUDP  
  - WebRTCDataChannel  
  - WebSocketPeer  

## Description
Abstract base class for packet-based protocols (e.g., UDP). Provides APIs for sending/receiving packets as raw data or variables, simplifying data transfer without manual byte encoding or network ordering concerns.  

**Note**: On Android, ensure the "INTERNET" permission is enabled in the export preset to allow network communication.

## Properties
- **encode_buffer_max_size**: `int` = 8388608  
  - **Description**: Maximum buffer size for encoding `Variant` objects. Increasing this value allows larger memory allocations. If a `Variant` exceeds this size, `put_var()` will error with `ERR_OUT_OF_MEMORY`.

## Methods
- **get_available_packet_count()** → `int`  
  - **Description**: Returns the number of packets in the ring buffer.  

- **get_packet()** → `PackedByteArray`  
  - **Description**: Retrieves a raw packet.  

- **get_packet_error()** → `Error`  
  - **Description**: Returns the error state of the last received packet (via `get_packet()` or `get_var()`).  

- **get_var([allow_objects: bool = false])** → `Variant`  
  - **Description**: Retrieves a `Variant`. If `allow_objects` is true, object decoding is permitted.  
  - **Warning**: Deserialized objects may execute code. Avoid this if the data source is untrusted.  

- **put_packet(buffer: PackedByteArray)** → `Error`  
  - **Description**: Sends a raw packet.  

- **put_var(var: Variant, [full_objects: bool = false])** → `Error`  
  - **Description**: Sends a `Variant` as a packet. If `full_objects` is true, object encoding is allowed (may include code).  

## Notes
- **Security Warning**: Deserialization of untrusted data may lead to remote code execution.  
- **Android Requirement**: Enable "INTERNET" permission for network operations.