# WebSocketPeer Class Documentation

A class representing a WebSocket connection in a network application, providing methods to connect, send data, and manage the connection state.

---

## Constants

### `STATE_CLOSED`
The connection has been closed.  
**Value**: `State.CLOSED`

### `STATE_CLOSING`
The connection is in the process of being closed.  
**Value**: `State.CLOSING`

### `STATE_OPEN`
The connection is open and ready for data transmission.  
**Value**: `State.OPEN`

---

## Methods

### `connect_to_url(url: String, tls_client_options: TLSOptions = null)`
**Description**: Connects to a URL using WebSocket.  
**Parameters**:  
- `url`: The URL to connect to (e.g., "ws://example.com/").  
- `tls_client_options`: Optional TLS options for secure connections (e.g., `wss://`).  
**Return Value**: `Error` indicating success or failure.  
**Notes**:  
- This method is non-blocking. Use `poll()` regularly to check the connection state.  
- For Web exports, use `wss://` to avoid mixed content warnings.  
- TLS certificate validation is done against the hostname when using `wss://`.

**Example**:  
```val error = WebSocketPeer.connect_to_url("wss://example.com")
if (error == OK) {
    // Connection successful
}
```

---

### `get_close_code() -> int | const`
**Description**: Returns the close code from the last WebSocket close frame.  
**Return Value**: The close code (e.g., `1000` for normal closure) or `-1` if the connection was not cleanly closed.  
**Note**: Only call this when `get_ready_state()` returns `STATE_CLOSED`.

---

### `get_close_reason() -> String | const`
**Description**: Returns the close reason string from the last WebSocket close frame.  
**Return Value**: The close reason string or an empty string if not available.  
**Note**: Only call this when `get_ready_state()` returns `STATE_CLOSED`.

---

### `get_connected_host() -> String | const`
**Description**: Returns the IP address of the connected peer.  
**Return Value**: The connected host address.  
**Note**: Not available in Web exports.

---

### `get_connected_port() -> int | const`
**Description**: Returns the remote port of the connected peer.  
**Return Value**: The connected port number.  
**Note**: Not available in Web exports.

---

### `get_current_outbound_buffered_amount() -> int | const`
**Description**: Returns the amount of data in the outbound buffer.  
**Return Value**: The current buffered data size.  
**Note**: Web exports use `WebSocket.bufferedAmount`, while other platforms use an internal buffer.

---

### `get_ready_state() -> State | const`
**Description**: Returns the current state of the WebSocket connection.  
**Return Value**: The state (e.g., `STATE_OPEN`, `STATE_CLOSED`).  
**See**: `State` enum for possible values.

---

### `get_requested_url() -> String | const`
**Description**: Returns the URL requested by the peer.  
**Return Value**: The URL from `connect_to_url()` or the HTTP headers when acting as a server.  
**Example**:  
```val url = WebSocketPeer.get_requested_url()
```

---

### `get_selected_protocol() -> String | const`
**Description**: Returns the selected WebSocket sub-protocol.  
**Return Value**: The sub-protocol or an empty string if not selected.  
**Example**:  
```val protocol = WebSocketPeer.get_selected_protocol()
```

---

### `poll()`
**Description**: Updates the connection state and processes incoming data.  
**Note**: Call this regularly (e.g., in a loop) to maintain a clean connection state.  
**Example**:  
```while (WebSocketPeer.poll() == OK) {
    // Process data
}
```

---

### `send(message: PackedByteArray, write_mode: WriteMode = 1) -> Error`
**Description**: Sends binary data using the specified write mode.  
**Parameters**:  
- `message`: The binary data to send.  
- `write_mode`: `1` for binary mode (default), `0` for text mode.  
**Return Value**: `Error` indicating success or failure.  
**Note**: Prefer `send_text()` for text-based APIs.

---

### `send_text(message: String) -> Error`
**Description**: Sends text data using WebSocket text mode.  
**Parameters**:  
- `message`: The text message to send.  
**Return Value**: `Error` indicating success or failure.  
**Note**: Use this for third-party text APIs (e.g., JSON).  
**Example**:  
```val error = WebSocketPeer.send_text("Hello, world!")
```

---

### `set_no_delay(enabled: bool)`
**Description**: Disables Nagle's algorithm on the underlying TCP socket.  
**Parameters**:  
- `enabled`: `true` to disable Nagle's algorithm (default), `false` to enable.  
**Note**: Not available in Web exports.  
**Example**:  
```WebSocketPeer.set_no_delay(true)
```

---

### `was_string_packet() -> bool | const`
**Description**: Checks if the last received packet was text.  
**Return Value**: `true` if the last packet was text.  
**Note**: See `WriteMode` for context.  
**Example**:  
```val wasText = WebSocketPeer.was_string_packet()
```

---

## Notes

1. **Web Export Limitations**:  
   - Methods like `get_connected_host()` and `set_no_delay()` are not available in Web exports.  
   - Use `wss://` for secure connections to avoid mixed content warnings.

2. **TLS Options**:  
   - Customize TLS settings with `TLSOptions` (e.g., `client_unsafe()` to bypass certificate checks).

3. **Connection State**:  
   - Poll regularly with `poll()` to check the state using `get_ready_state()`.  
   - A clean close requires waiting until `STATE_CLOSED` is reached.

4. **Close Handling**:  
   - Use `get_close_code()` and `get_close_reason()` only after `STATE_CLOSED` is confirmed.

5. **Performance**:  
   - Use `set_no_delay(true)` for low-latency applications.

---

## Enums

### `State`
- `CLOSED`: Connection closed.  
- `CLOSING`: Connection being closed.  
- `OPEN`: Connection open.  

### `WriteMode`
- `0`: Text mode.  
- `1`: Binary mode (default).  

---

This documentation covers all methods, constants, and platform-specific considerations for the `WebSocketPeer` class. Use it to build robust WebSocket clients and servers.