**ENetMultiplayerPeer Class**  
- **Inherits**: MultiplayerPeer → PacketPeer → RefCounted → Object  

---

### **Description**  
- A class for networking using the ENet library.  
- Supports creating servers, clients, and mesh networks.  
- Uses ENetConnection for managing peer connections.  

---

### **Tutorials**  
- [High-level multiplayer networking](../tutorials/networking/high_level_multiplayer)  
- [ENet API Documentation](http://enet.bespin.org/usergroup0.html)  

---

### **Properties**  
- **host**: `ENetConnection`  
  - The underlying ENet connection object.  

---

### **Methods**  
#### **create_client**  
- **Parameters**:  
  - `address`: Peer IP address.  
  - `port`: Port number.  
  - `max_clients`: Maximum clients (default 32).  
  - `max_channels`: Maximum channels (default 0).  
  - `in_bandwidth`: Inbound bandwidth limit.  
  - `out_bandwidth`: Outbound bandwidth limit.  
- **Returns**: `Error`  
- **Description**: Creates a client connection to a server.  

#### **create_server**  
- **Parameters**:  
  - `port`: Port number.  
  - `max_clients`: Maximum clients (default 32).  
  - `max_channels`: Maximum channels (default 0).  
  - `in_bandwidth`: Inbound bandwidth limit.  
  - `out_bandwidth`: Outbound bandwidth limit.  
- **Returns**: `Error`  
- **Description**: Creates a server that listens for connections.  

#### **set_bind_ip**  
- **Parameters**:  
  - `ip`: IP address (e.g., "192.168.1.1").  
- **Description**: Sets the IP address for a server to bind to.  

#### **get_peer**  
- **Parameters**:  
  - `id`: Peer ID.  
- **Returns**: `ENetPacketPeer`  
- **Description**: Returns the packet peer associated with the given ID.  

#### **add_mesh_peer**  
- **Description**: Adds a mesh peer manually (requires manual setup with ENetConnection).  

---

### **Notes**  
- **UDP**: ENet uses UDP for low-latency communication.  
- **UPNP**: For public access, use UPNP to map ports.  
- **Mesh Networking**: Allows advanced control over connections and load distribution.  

--- 

**Key Features**  
- Supports both server/client modes.  
- Enables mesh networking for custom peer management.  
- Bandswidth limits for traffic control.