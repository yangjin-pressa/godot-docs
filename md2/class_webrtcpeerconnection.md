The `WebRTCPeerConnection` class in Godot is used to handle WebRTC (Web Real-Time Communication) connections, enabling features like video, audio, and data channels between peers. Below is a structured explanation of its key components, methods, and usage flow:

---

### **Key Concepts**
- **WebRTC**: A protocol for real-time communication (RTC) between peers, supporting media streams and data channels.
- **SDP**: Session Description Protocol, used to describe media sessions (offers and answers).
- **ICE**: Internet Candidate Exchange, used to facilitate connectivity between peers.
- **Data Channels**: Allow application-level data transmission between peers.

---

### **Core Methods**

#### 1. **Initialize Peer Connection**
```gdscript
var err = peer_connection.initialize({
    "iceServers": [
        {"urls": ["stun:stun.example.com:3478"]},
        {"urls": ["turn:turn.example.com:3478"], "username": "user", "credential": "pass"}
    ]
})
```
- **Purpose**: Configure the peer connection with ICE servers (STUN/TURN).
- **Parameters**: A dictionary with `iceServers` to define STUN/TURN servers.

---

#### 2. **Create Data Channel**
```gdscript
var channel = peer_connection.create_data_channel("my-channel", {
    "negotiated": true,
    "id": 1,
    "maxRetransmits": 3
})
```
- **Purpose**: Create a data channel for application data.
- **Parameters**: 
  - `label`: Channel name.
  - `options`: Configurable parameters like `negotiated` (out-of-band negotiation), `id`, `maxRetransmits`, and `protocol`.

---

#### 3. **Create Offer**
```gdscript
var err = peer_connection.create_offer()
```
- **Purpose**: Generate an SDP offer for the peer to exchange with the other end.
- **Precondition**: At least one data channel must be created before calling this method.

---

#### 4. **Set Local Description**
```gdscript
var err = peer_connection.set_local_description("offer", "SDP_OFFER")
```
- **Purpose**: Set the local peer's SDP description (offer) after generating the offer.
- **Signal**: Triggers `session_description_created` once ready.

---

#### 5. **Set Remote Description**
```gdscript
var err = peer_connection.set_remote_description("answer", "SDP_ANSWER")
```
- **Purpose**: Set the remote peer's SDP description (answer) received from the other end.
- **Signal**: Triggers `ice_candidate_created` for ICE candidates.

---

### **Key Signals**
- **`session_description_created`**: Emitted when the local SDP (offer/answer) is ready to be sent.
- **`ice_candidate_created`**: Emitted when ICE candidates are generated for the connection.
- **`data_channel_received`**: Emitted when the other peer creates a data channel.

---

### **State and Utility Methods**
- **`get_connection_state()`**: Returns the current connection state (e.g., `STATE_NEW`, `STATE_CONNECTED`).
- **`get_signaling_state()`**: Returns the signaling state (e.g., `SIGNALING_NEEDED`, `SIGNALING_READY`).
- **`poll()`**: Continuously processes WebRTC events (e.g., ICE candidates, data packets).

---

### **Usage Flow**
1. **Initialize** the peer connection with ICE servers.
2. **Create data channels** (with negotiated options if needed).
3. **Generate an offer** using `create_offer()`.
4. **Set the local description** with the offer.
5. **Send the offer** to the remote peer.
6. **Receive the remote peer's answer** via signaling (e.g., WebSocket).
7. **Set the remote description** with the answer.
8. **Exchange ICE candidates** as they are generated.
9. **Use data channels** to send/receive application data.

---

### **Important Notes**
- **Negotiated Channels**: Use `negotiated: true` for channels that are established out-of-band (e.g., both peers set the same ID).
- **Polling**: Call `poll()` frequently (e.g., in `Node._process()`) to ensure WebRTC events are processed.
- **Error Handling**: Check for errors when setting descriptions or creating channels.

---

### **Example Workflow**
```gdscript
var peer_connection = WebRTCPeerConnection.new()
peer_connection.initialize({
    "iceServers": [
        {"urls": ["stun:stun.example.com:3478"]}
    ]
})

var channel = peer_connection.create_data_channel("my-channel", {
    "negotiated": true,
    "id": 1
})

peer_connection.create_offer().then {
    var err = peer_connection.set_local_description("offer", "SDP_OFFER")
    if err == OK {
        # Send SDP offer to remote peer
    }
}
```

---

This class is fundamental for implementing real-time communication in Godot, leveraging WebRTC's capabilities for media and data exchange. Proper configuration of ICE servers and handling of signaling events are critical for reliable peer connections.