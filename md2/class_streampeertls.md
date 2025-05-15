# StreamPeerTLS

**Inherits:** StreamPeer → RefCounted → Object

A stream peer that handles TLS connections.

## Description
A stream peer that handles TLS connections. This object can be used to connect to a TLS server or accept a single TLS client connection.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Tutorials
- [TLS certificates](../tutorials/networking/ssl_certificates)

## Methods
- `accept_stream(stream: StreamPeer, server_options: TLSOptions)`: Returns an error code. Accepts a peer connection as a server using the given `server_options`.
- `connect_to_stream(stream: StreamPeer, common_name: String, client_options: TLSOptions = null)`: Returns an error code. Connects to a peer using an underlying `StreamPeer` `stream` and verifies the remote certificate is correctly signed for the given `common_name`.
- `disconnect_from_stream()`: Disconnects from host.
- `get_status()`: Returns the status of the connection (e.g., disconnected, handshaking, connected, error).
- `get_stream()`: Returns the underlying `StreamPeer` connection.
- `poll()`: Poll the connection to check for incoming bytes.

## Enumerations
### Status
- **STATUS_DISCONNECTED**: 0. A status representing a disconnected connection.
- **STATUS_HANDSHAKING**: 1. A status during handshaking.
- **STATUS_CONNECTED**: 2. A status representing a connected connection.
- **STATUS_ERROR**: 3. A status representing an error state.
- **STATUS_ERROR_HOSTNAME_MISMATCH**: 4. An error status for hostname mismatch in TLS certificate.

## Method Descriptions
- `accept_stream()`: Accepts a peer connection as a server using the given `server_options`.
- `connect_to_stream()`: Connects to a peer using an underlying `StreamPeer` and verifies the remote certificate.
- `disconnect_from_stream()`: Disconnects from the host.
- `get_status()`: Returns the current connection status.
- `get_stream()`: Returns the underlying `StreamPeer` connection.
- `poll()`: Polls the connection for incoming data.