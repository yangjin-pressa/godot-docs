# PacketPeerDTLS

## Inheritance
- Inherits from: `PacketPeer` → `RefCounted` → `Object`

## Description
Represents a DTLS peer connection. Used to connect to a DTLS server and returned by `DTLSServer.take_connection()`. 

**Note:** Enable the `INTERNET` permission in Android export settings to avoid network blocks.

**Warning:** TLS certificate revocation and pinning are not supported. Revoked certificates are accepted if otherwise valid.

---

## Methods

- **connect_to_peer**  
  Connects using a `PacketPeerUDP` (must be connected). Optionally specifies `TLSOptions` for validation.  
  **Parameters:**  
  - `packet_peer`: `PacketPeerUDP`  
  - `hostname`: `String`  
  - `client_options`: `TLSOptions` (optional)  

- **disconnect_from_peer**  
  Terminates the DTLS session.

- **get_status**  
  Returns the connection status.  
  **Returns:** `Status` (see enum for values)

- **poll**  
  Checks for incoming packets. Call frequently to maintain connection.

---

## Enumerations

### Status
- **STATUS_DISCONNECTED** = 0  
  Connection is disconnected.

- **STATUS_HANDSHAKING** = 1  
  Performing handshake with remote peer.

- **STATUS_CONNECTED** = 2  
  Connected to a remote peer.

- **STATUS_ERROR** = 3  
  Generic error state.

- **STATUS_ERROR_HOSTNAME_MISMATCH** = 4  
  DTLS certificate domain mismatch.