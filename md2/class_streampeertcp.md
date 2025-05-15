**StreamPeerTCP**  
*Inherits:* StreamPeer → RefCounted → Object  

---

### Description  
A stream peer that handles TCP connections. This object can be used to connect to TCP servers, or also is returned by a TCP server.  

**Note:** When exporting to Android, ensure the "INTERNET" permission is enabled in the export preset. Otherwise, network communication will be blocked.  

---

### Methods  
- **bind**(port: int, host: String = "*") → Error  
  Binds the TCP socket to the specified local address.  

- **connect_to_host**(host: String, port: int) → Error  
  Connects to the specified host:port. Returns OK on success.  

- **disconnect_from_host**()  
  Disconnects from the host.  

- **get_connected_host**() → String  
  Returns the IP address of the connected peer.  

- **get_connected_port**() → int  
  Returns the port of the connected peer.  

- **get_local_port**() → int  
  Returns the local port to which the peer is bound.  

- **get_status**() → Status  
  Returns the connection status (e.g., CONNECTING, CONNECTED).  

- **poll**() → Error  
  Updates the socket state.  

- **set_no_delay**(enabled: bool)  
  Controls packet sending behavior (Nagle's algorithm).  

---

### Enumerations  
**Status**  
- **STATUS_NONE** = 0  
  Initial state (disconnected).  
- **STATUS_CONNECTING** = 1  
  Connecting to a host.  
- **STATUS_CONNECTED** = 2  
  Successfully connected.  
- **STATUS_ERROR** = 3  
  Connection failed.  

---

### Notes  
- **Android**: Requires "INTERNET" permission for network operations.  
- **set_no_delay**: Enabling this sends packets immediately (default is disabled for large data transfers).  
- **bind**: Used for NAT punchthrough or forcing source interface.