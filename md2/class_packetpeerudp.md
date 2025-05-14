**PacketPeerUDP**

**Inheritance**
- Inherits from `PacketPeer`

**Overview**
PacketPeerUDP is a class for handling UDP packet communication in Godot, allowing sending and receiving packets with custom addresses and ports.

---

### **Description**
This class provides functionality for UDP-based network communication. It includes methods to bind to an address, send packets, and wait for incoming packets.

**Example: Sending a Packet**
```gdscript
socket = PacketPeerUDP.new()
# Server
socket.set_dest_address("127.0.0.1", 789)
socket.put_packet("Time to stop".to_ascii_buffer())

# Client
while socket.wait() == OK:
    var data = socket.get_packet().get_string_from_ascii()
    if data == "Time to stop":
        return
```

**Example: Receiving a Packet**
```gdscript
socket = PacketPeerUDP.new()
socket.bind("0.0.0.0", 789)
while true:
    if socket.wait() == OK:
        var data = socket.get_packet().get_string_from_ascii()
        print("Received:", data)
```

---

### **Methods**

#### **bind(host: String, port: int) → Error**
- **Description**: Binds the socket to a local address and port, allowing packet reception.
- **Notes**: Must be called before using `wait()`.

#### **set_dest_address(host: String, port: int) → Error**
- **Description**: Sets the destination address and port for sending packets.
- **Notes**: Requires `set_broadcast_enabled()` to be enabled for broadcast addresses.

#### **wait() → Error**
- **Description**: Waits for a packet to arrive on the bound address.
- **Notes**: Cannot be interrupted once called. Use a "death pill" packet to exit loops.

#### **get_packet() → Packet**
- **Description**: Retrieves the last received packet.
- **Returns**: A `Packet` object containing the data.

#### **get_var() → Variant**
- **Description**: Retrieves the last received variable (e.g., a simple value).
- **Returns**: The value from the last received packet.

#### **get_packet_port() → int**
- **Description**: Returns the port of the remote peer that sent the last packet.

#### **get_packet_ip() → String**
- **Description**: Returns the IP of the remote peer that sent the last packet.

#### **is_bound() → bool**
- **Description**: Checks if the socket is bound to an address and can receive packets.

#### **is_connected() → bool**
- **Description**: Returns true if the UDP socket is connected to a remote address.

#### **set_broadcast_enabled(enabled: bool)**
- **Description**: Enables or disables sending of broadcast packets.
- **Notes**: Required for broadcast addresses like `255.255.255.255`.

#### **join_multicast_group(multicast_address: String, interface_name: String) → Error**
- **Description**: Joins a multicast group using a specified network interface.
- **Notes**: Some Android devices may require `CHANGE_WIFI_MULTICAST_STATE` permission.

#### **leave_multicast_group(multicast_address: String, interface_name: String) → Error**
- **Description**: Leaves a multicast group using a specified network interface.

---

### **Notes**
- **Android Permissions**: 
  - `CHANGE_WIFI_MULTICAST_STATE` is required for multicast.
  - Broadcast packets may also require this permission.
- **Wait() Limitation**: Cannot be interrupted. Use a termination packet to exit loops.
- **Broadcast**: Requires `set_broadcast_enabled()` to be enabled.

This class provides flexible UDP communication capabilities, suitable for networking tasks requiring packet customization.