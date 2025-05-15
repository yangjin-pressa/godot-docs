### UDPServer Class Overview  
The **UDPServer** class in Godot handles UDP communication, allowing a server to listen for packets and manage connections. Key features include:  
- Listening on a specific port.  
- Handling incoming packets and managing pending connections.  
- Closing the server and associated resources.  

---

### **Description**  
- **Purpose**: Acts as a UDP server to receive packets and manage connections.  
- **Key Functionality**:  
  - Listens on a specified port.  
  - Processes packets and determines if they are known or new connections.  
  - Limits pending connections via `max_pending_connections`.  
- **Example Use**:  
  - Use with `PacketPeerUDP` to bind and handle data.  
  - Example: `PacketPeerUDP.bind()` to specify a bind address.  

---

### **Properties**  
- **`max_pending_connections`** (int)  
  - **Value**: `16` (default).  
  - **Description**: Maximum number of pending connections the server can handle.  

---

### **Methods**  
1. **`get_local_port()`** (int)  
   - **Description**: Returns the port the server is listening on.  

2. **`is_connection_available()`** (bool)  
   - **Description**: Checks if a new connection is available (i.e., a packet from an unknown address/port).  

3. **`listen(port: int, bind_address: String = "*")`** (Error)  
   - **Description**: Starts the server, listening on the specified port and bind address.  

4. **`poll()`** (Error)  
   - **Description**: Processes incoming packets, delivering known packets to `PacketPeerUDP` and adding unknown packets as pending connections.  

5. **`stop()`** (void)  
   - **Description**: Stops the server, closing the UDP socket and disconnecting all connected peers.  

6. **`take_connection()`** (PacketPeerUDP)  
   - **Description**: Retrieves the first pending connection (if available). Returns `null` if none.  

---

### **Example Code**  
#### **GDScript**  
```gdscript
var server = UDPServer.new()
server.listen(12345)
while true:
    if server.is_connection_available():
        var peer = server.take_connection()
        peer.connect_to_host("192.168.1.1", 54321)
    server.poll()
```

#### **C++**  
```cpp
UDP_Server* server = new UDP_Server();
server->listen(12345);
while (true) {
    if (server->is_connection_available()) {
        UDP_Peer* peer = server->take_connection();
        peer->connect_to_host("192.168.1.1", 54321);
    }
    server->poll();
}
```

---

### **Key Notes**  
- **Pending Connections**: New connections (from unknown addresses) are added to the queue, managed via `is_connection_available()` and `take_connection()`.  
- **Resource Management**: Use `stop()` to cleanly close the server and release resources.  
- **Performance**: Call `poll()` regularly (e.g., in a game loop) to process packets.