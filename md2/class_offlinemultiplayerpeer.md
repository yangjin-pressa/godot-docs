**Class:** OfflineMultiplayerPeer  
**Inherits:** MultiplayerPeer → PacketPeer → RefCounted → Object  

---

### **Description**  
- Default multiplayer peer for `Node.multiplayer`  
- Acts as a server with no connected peers  
- SceneTree serves as multiplayer authority by default  
- Key behaviors:  
  - `MultiplayerAPI.is_server()` returns `true`  
  - `MultiplayerAPI.get_unique_id()` returns `MultiplayerPeer.TARGET_PEER_SERVER`  

---

### **Key Properties**  
- **Server Authority:**  
  - SceneTree manages multiplayer state  
  - No peer connections required  

---

### **Citations**  
- `MultiplayerPeer` class: [class_MultiplayerPeer](https://github.com/godotengine/godot/tree/master/doc/tools/make_rst.py)  
- `TARGET_PEER_SERVER` constant: [MultiplayerPeer.TARGET_PEER_SERVER](https://github.com/godotengine/godot/tree/master/modules/multiplayer/doc_classes/OfflineMultiplayerPeer.xml)