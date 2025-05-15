# StreamPeerExtension

**Inherits:** StreamPeer → RefCounted → Object  

---

## Methods

- **_get_available_bytes**  
  - Return type: int  
  - Notes: Virtual, const  

- **_get_data**  
  - Return type: Error  
  - Parameters:  
    - r_buffer: uint8_t*  
    - r_bytes: int  
    - r_received: int32_t*  
  - Notes: Virtual  

- **_get_partial_data**  
  - Return type: Error  
  - Parameters:  
    - r_buffer: uint8_t*  
    - r_bytes: int  
    - r_received: int32_t*  
  - Notes: Virtual  

- **_put_data**  
  - Return type: Error  
  - Parameters:  
    - p_data: const uint8_t*  
    - p_bytes: int  
    - r_sent: int32_t*  
  - Notes: Virtual  

- **_put_partial_data**  
  - Return type: Error  
  - Parameters:  
    - p_data: const uint8_t*  
    - p_bytes: int  
    - r_sent: int32_t*  
  - Notes: Virtual  

---

## Notes  
All methods lack descriptions. Contribute descriptions for:  
[contributing one](doc_updating_the_class_reference)  

---

## Key Flags  
- Virtual: Methods require user override for functionality  
- Const: Methods do not modify instance data