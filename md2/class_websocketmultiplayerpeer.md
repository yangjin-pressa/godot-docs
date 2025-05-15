# WebSocketMultiplayerPeer

## Inheritance Hierarchy
- `MultiplayerPeer`  
  - `PacketPeer`  
    - `RefCounted`  
      - `Object`

## Description
Base class for WebSocket server and client, enabling use with the `MultiplayerAPI`.  
**Note:** For Android exports, ensure the `INTERNET` permission is set in the export preset to avoid network blocking.

---

## Properties

- **handshake_headers**: `PackedStringArray` (default: empty)  
  Extra headers for WebSocket handshake. See `WebSocketPeer.handshake_headers` for details.  
  *Note: Returns a copy; changes to the array do not affect the original.*

- **handshake_timeout**: `float` (default: 3.0)  
  Maximum time peers can remain connecting before being dropped.

- **inbound_buffer_size**: `int` (default: 65535)  
  Buffer size for incoming data from peers. See `WebSocketPeer.inbound_buffer_size`.

- **max_queued_packets**: `int` (default: 4096)  
  Maximum packets queued for peers. See `WebSocketPeer.max_queued_packets`.

- **outbound_buffer_size**: `int` (default: 65535)  
  Buffer size for outgoing data to peers. See `WebSocketPeer.outbound_buffer_size`.

- **supported_protocols**: `PackedStringArray` (default: empty)  
  Supported WebSocket sub-protocols. See `WebSocketPeer.supported_protocols`.  
  *Note: Returns a copy; changes to the array do not affect the original.*

---

## Methods

- **create_client(url: String, tls_client_options: TLSOptions = null)** → `Error`  
  Creates a WebSocket client connecting to `url`.  
  *Note: URL should include `ws://` or `wss://` for clarity. TLS options can customize CA trust or disable CN verification.*

- **create_server(port: int, bind_address: String = "*", tls_server_options: TLSOptions = null)** → `Error`  
  Listens on `port` with optional `bind_address` and TLS settings. See `TLSOptions.server()` for TLS configuration.

- **get_peer(peer_id: int)** → `WebSocketPeer` (const)  
  Returns the `WebSocketPeer` associated with `peer_id`.

- **get_peer_address(id: int)** → `String` (const)  
  Returns the IP address of the peer with ID `id`.

- **get_peer_port(id: int)** → `int` (const)  
  Returns the remote port of the peer with ID `id`.

---

## Notes
- **Android:** Always include `INTERNET` permission in export settings.
- **TLS Options:** Use `TLSOptions.client()` or `TLSOptions.client_unsafe()` for custom TLS behavior.
- **URL Scheme:** Prefer `ws://` or `wss://` for URL parameters.