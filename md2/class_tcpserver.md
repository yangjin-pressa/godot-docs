# TCPServer

**Inherits:** RefCounted < Object

A TCP server that listens to connections on a port and returns a StreamPeerTCP when an incoming connection is detected.

## Description
- Listens on a specified port and binds to an IP address.
- Returns a StreamPeerTCP object when a connection is established.
- **Android Note:** Enable "INTERNET" permission in the export preset for network communication.

## Methods

- **get_local_port()** → int  
  Returns the local port the server is using.

- **is_connection_available()** → bool  
  Returns true if a connection is ready to be accepted.

- **is_listening()** → bool  
  Returns true if the server is actively listening for connections.

- **listen(port: int, bind_address: String = "*")** → Error  
  Starts listening on the specified port and address.  
  - "*": Listen on all available addresses (IPv4/IPv6).  
  - "0.0.0.0": Listen on all IPv4 addresses.  
  - "::": Listen on all IPv6 addresses.  
  - Specific IP: Listen only on the specified interface.

- **stop()**  
  Stops the server from listening for new connections.

- **take_connection()** → StreamPeerTCP  
  Returns a StreamPeerTCP object if a connection is available.

## Key Notes
- Use `stop()` to halt the server.
- `take_connection()` returns a connection if one is available.
- The `bind_address` parameter determines which network interface the server listens on.