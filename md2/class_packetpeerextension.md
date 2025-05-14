**Class: PacketPeerExtension**  
**Inherits:** `PacketPeer` → `RefCounted` → `Object`  

---

### **Methods**  
- **_get_available_packet_count**  
  - **Return Type:** `int`  
  - **Note:** Virtual, const.  

- **_get_max_packet_size**  
  - **Return Type:** `int`  
  - **Note:** Virtual, const.  

- **_get_packet**  
  - **Return Type:** `Error`  
  - **Parameters:**  
    - `r_buffer`: `const uint8_t**`  
    - `r_buffer_size`: `int32_t*`  
  - **Note:** Virtual.  

- **_put_packet**  
  - **Return Type:** `Error`  
  - **Parameters:**  
    - `p_buffer`: `const uint8_t*`  
    - `p_buffer_size`: `int`  
  - **Note:** Virtual.  

---

### **Method Descriptions**  
All methods currently lack descriptions. Please contribute descriptions for:  
- `_get_available_packet_count`  
- `_get_max_packet_size`  
- `_get_packet`  
- `_put_packet`  

---

### **Notes**  
- Methods marked as virtual require overriding by users for functionality.  
- Const methods do not modify instance variables.  
- Placeholder descriptions prompt contributors to update the class reference.