# PacketPeerStream

**Inherits:** PacketPeer → RefCounted → Object

## Description
A wrapper for using packets over a stream. This allows packet-based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so users should not directly interact with the wrapped StreamPeer.

**Note:** When exporting to Android, ensure the "INTERNET" permission is enabled in the export preset to allow network communication.

---

## Properties

- **input_buffer_max_size**: int = 65532  
  - Sets/get: `set_input_buffer_max_size(value: int)` / `get_input_buffer_max_size()`
  - No description available.

- **output_buffer_max_size**: int = 65532  
  - Sets/get: `set_output_buffer_max_size(value: int)` / `get_output_buffer_max_size()`
  - No description available.

- **stream_peer**: StreamPeer  
  - Sets/get: `set_stream_peer(value: StreamPeer)` / `get_stream_peer()`
  - The wrapped StreamPeer object.

---

## Key Notes
- Properties for buffer sizes are default 65532.
- The `stream_peer` property references the underlying StreamPeer.
- Descriptions for buffer size properties are missing and can be contributed.