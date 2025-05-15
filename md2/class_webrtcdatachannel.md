**WebRTCDataChannel Class**  
- **Inherits from**: PacketPeer → RefCounted → Object  
- **Inherited by**: WebRTCDataChannelExtension  

---

### Class Overview  
- **Note**: Currently no detailed description available. Help update the class reference: [contributing one](doc_updating_the_class_reference).  

---

### Properties  
- **write_mode**  
  - **Type**: WriteMode  
  - **Value**: 1  
  - **Description**: Determines whether data is transferred as text or binary.  

---

### Methods  
- **close()**  
  - **Return**: void  
  - **Description**: Closes the channel.  

- **get_buffered_amount()**  
  - **Return**: int  
  - **Description**: Returns the current buffered amount.  

- **get_ready_state()**  
  - **Return**: ChannelState  
  - **Description**: Returns the current state of the channel.  

- **is_negotiated()**  
  - **Return**: bool  
  - **Description**: Returns true if the channel was created with out-of-band configuration.  

- **is_ordered()**  
  - **Return**: bool  
  - **Description**: Returns true if ordering is enabled (default).  

- **poll()**  
  - **Return**: Error  
  - **Description**: Reserved, not used currently.  

- **was_string_packet()**  
  - **Return**: bool  
  - **Description**: Returns true if the last received packet was transferred as text.  

---

### Enumerations  
#### WriteMode  
- **0**: Text  
- **1**: Binary  

#### ChannelState  
- **0**: Closed  
- **1**: Opening  
- **2**: Negotiating  
- **3**: Connected  
- **4**: Failed  
- **5**: Ended  

---

### Notes  
- The `write_mode` property defines the data transfer format.  
- The `poll()` method is reserved but not currently used.  
- The `was_string_packet()` method checks the last received packet's format.