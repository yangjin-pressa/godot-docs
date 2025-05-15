**Class:** WebRTCPeerConnectionExtension  
**Inherits:** WebRTCPeerConnection → RefCounted → Object  

---

**Methods:**  

- **_add_ice_candidate**  
  - Parameters: p_sdp_mid_name (String), p_sdp_mline_index (int), p_sdp_name (String)  
  - Return: Error  
  - Note: Virtual method (override recommended)  

- **_close**  
  - Parameters: None  
  - Return: void  
  - Note: Virtual method (override recommended)  

- **_create_data_channel**  
  - Parameters: p_label (String), p_config (Dictionary)  
  - Return: WebRTCDataChannel  
  - Note: Virtual method (override recommended)  

- **_create_offer**  
  - Parameters: None  
  - Return: Error  
  - Note: Virtual method (override recommended)  

- **_get_connection_state**  
  - Parameters: None  
  - Return: ConnectionState  
  - Note: Const method (no side effects)  

- **_get_gathering_state**  
  - Parameters: None  
  - Return: GatheringState  
  - Note: Const method (no side effects)  

- **_get_signaling_state**  
  - Parameters: None  
  - Return: SignalingState  
  - Note: Const method (no side effects)  

- **_initialize**  
  - Parameters: p_config (Dictionary)  
  - Return: Error  
  - Note: Virtual method (override recommended)  

- **_poll**  
  - Parameters: None  
  - Return: Error  
  - Note: Virtual method (override recommended)  

- **_set_local_description**  
  - Parameters: p_type (String), p_sdp (String)  
  - Return: Error  
  - Note: Virtual method (override recommended)  

- **_set_remote_description**  
  - Parameters: p_type (String), p_sdp (String)  
  - Return: Error  
  - Note: Virtual method (override recommended)  

---

**Notes:**  
- The class and all methods lack descriptions. Contributions are needed to document them.  
- All methods marked as virtual require user implementation for functionality.  
- Const methods (e.g., _get_connection_state) do not modify instance variables.