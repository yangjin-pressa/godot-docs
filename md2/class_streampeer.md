# StreamPeer Class Documentation

The `StreamPeer` class in a game engine (e.g., Godot) is used to handle network communication, allowing data to be sent and received over a network connection. This class provides methods to transmit various data types, including integers, floats, strings, and custom objects, as well as to manage larger data transfers efficiently.

---

## Overview

The `StreamPeer` class is part of the networking system, enabling communication between peers (players or servers) in a multiplayer game. It supports both sending and receiving data, with methods to handle primitive types, strings, and custom objects. The class also includes functionality for managing large data transfers through partial sends.

---

## Methods

### `put_int16(value: int) -> void`
**Description**: Sends a 16-bit signed integer over the network.
**Parameters**:
- `value`: The integer to send.
**Return Type**: `void`
**Note**: This method is used for sending small integer values efficiently.

---

### `put_int32(value: int) -> void`
**Description**: Sends a 32-bit signed integer over the network.
**Parameters**:
- `value`: The integer to send.
**Return Type**: `void`
**Note**: For larger integer values, this method is more appropriate than `put_int16`.

---

### `put_int64(value: int) -> void`
**Description**: Sends a 64-bit signed integer over the network.
**Parameters**:
- `value`: The integer to send.
**Return Type**: `void`
**Note**: Used for very large integer values.

---

### `put_float(value: float) -> void`
**Description**: Sends a 32-bit floating-point number over the network.
**Parameters**:
- `value`: The float to send.
**Return Type**: `void`
**Note**: This is the standard format for transmitting real numbers.

---

### `put_string(value: str) -> void`
**Description**: Sends a string over the network. The string is prefixed with its length in bytes.
**Parameters**:
- `value`: The string to send.
**Return Type**: `void`
**Note**: This method includes the string's length in the payload. For direct sending without length prefixes, use `put_data()`.

---

### `put_utf8_string(value: str) -> void`
**Description**: Sends a UTF-8 encoded string over the network. The string is prefixed with its length in bytes.
**Parameters**:
- `value`: The UTF-8 string to send.
**Return Type**: `void`
**Note**: Similar to `put_string`, but for UTF-8 encoding, ensuring compatibility with internationalization.

---

### `put_data(value: PackedByteArray) -> void`
**Description**: Sends raw binary data over the network.
**Parameters**:
- `value`: The binary data to send as a `PackedByteArray`.
**Return Type**: `void`
**Note**: This method is useful for sending arbitrary binary data without length prefixes. Use this for direct transmission of serialized objects or custom data formats.

---

### `put_partial_data(value: PackedByteArray) -> (Error, int)`
**Description**: Sends a chunk of data over the network. If the data cannot be fully sent immediately, it returns the error and the number of bytes actually sent.
**Parameters**:
- `value`: The binary data to send as a `PackedByteArray`.
**Return Type**: `Error, int`
**Note**: Returns two values: an `Error` code and the number of bytes sent. This method is useful for handling large data transfers in chunks.

---

### `get_int16() -> int`
**Description**: Receives a 16-bit signed integer from the network.
**Return Type**: `int`
**Note**: Returns the received integer.

---

### `get_int32() -> int`
**Description**: Receives a 32-bit signed integer from the network.
**Return Type**: `int`
**Note**: Used for receiving larger integer values.

---

### `get_int64() -> int`
**Description**: Receives a 64-bit signed integer from the network.
**Return Type**: `int`
**Note**: For receiving very large integers.

---

### `get_float() -> float`
**Description**: Receives a 32-bit floating-point number from the network.
**Return Type**: `float`
**Note**: Standard for receiving real numbers.

---

### `get_string() -> str`
**Description**: Receives a string from the network, including its length prefix.
**Return Type**: `str`
**Note**: The string is decoded using the same encoding as sent (ASCII by default).

---

### `get_utf8_string() -> str`
**Description**: Receives a UTF-8 encoded string from the network.
**Return Type**: `str`
**Note**: Ensures proper decoding of international characters.

---

### `get_data() -> PackedByteArray`
**Description**: Receives raw binary data from the network.
**Return Type**: `PackedByteArray`
**Note**: Returns the received binary data as a `PackedByteArray`.

---

### `get_error() -> Error`
**Description**: Checks for the last network error.
**Return Type**: `Error`
**Note**: Use this to detect transmission failures or disconnections.

---

## Important Notes

1. **Security Warning**:  
   The `get_var()` method can deserialize objects from untrusted sources, which may lead to security vulnerabilities (e.g., remote code execution). Always validate or sanitize data from untrusted peers before deserializing.

2. **String Transmission**:  
   Use `put_string()` or `put_utf8_string()` when sending strings, as they include the length prefix. For direct binary transmission, use `put_data()`.

3. **Partial Data Handling**:  
   The `put_partial_data()` method is ideal for managing large transfers or when the network connection is unstable. It returns the error and bytes sent, allowing for error recovery.

4. **Compatibility**:  
   Ensure all peers use the same data encoding (e.g., ASCII vs. UTF-8) to avoid data corruption during transmission.

---

## Example Usage

```gdscript
# Example: Sending a string and an integer
var peer = StreamPeer()
peer.connect("data_sent", some_callback)  # Connect to a peer

peer.put_string("Hello, world!")
peer.put_int32(12345)

# Receive data
var received_string = peer.get_string()
var received_int = peer.get_int32()
```

---

## Conclusion

The `StreamPeer` class provides a flexible and efficient way to handle network communication in a game engine. By using the appropriate methods for data types and considering the nuances of string and binary transmission, developers can build robust multiplayer experiences. Always handle errors and ensure data integrity, especially when dealing with untrusted data.