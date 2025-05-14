**MultiplayerSynchronizer**  
A class for synchronizing game properties between clients in a multiplayer environment.  

---

### **Description**  
- Synchronizes properties from the server (authority) to clients.  
- Manages visibility of replicated properties via `set_visibility_for()`, `add_visibility_filter()`, and `update_visibility()`.  
- Works with `MultiplayerSpawner` to spawn/despawn nodes based on synchronizer visibility.  
- **Note**: Certain properties (e.g., custom types) are not supported for synchronization.  

---

### **Properties**  
- **delta_interval**: `float` (default: 0.0)  
  - Time interval between delta updates (e.g., for partial state sync).  

- **public_visibility**: `bool` (default: true)  
  - Whether synchronization is visible to all peers by default.  

- **replication_config**: `SceneReplicationConfig`  
  - Defines which properties to synchronize.  

- **root_path**: `NodePath` (default: `NodePath("..")`)  
  - Relative path for replicated properties.  

- **visibility_update_mode**: `VisibilityUpdateMode` (default: 0)  
  - When to update visibility filters (e.g., on every frame, on network event).  

---

### **Methods**  
- **add_visibility_filter(filter: Callable)**  
  - Adds a function to determine which peers are visible.  

- **get_visibility_for(peer: int) -> bool**  
  - Checks if a specific peer is visible.  

- **remove_visibility_filter(filter: Callable)**  
  - Removes a previously added visibility filter.  

- **set_visibility_for(peer: int, visible: bool)**  
  - Sets visibility for a specific peer.  

- **update_visibility(for_peer: int = 0)**  
  - Applies visibility filters to peers (default: all peers).  

---

### **Signals**  
- **delta**: Emits when delta sync data is ready.  
- **replication**: Emits when replication data is ready.  
- **visibility**: Emits when visibility changes.  

---

### **Enumerations**  
- **VisibilityUpdateMode**  
  - **0**: Update on every frame.  
  - **1**: Update on network event.  
  - **2**: Update on visibility change.  

---

### **Key Notes**  
- Synchronization is relative to the node specified by `root_path`.  
- Use `replication_config` to define which properties to sync.  
- `public_visibility` and filters allow fine-grained control over visibility.  
- Delta and always replication modes are determined by `replication_interval` and `replication_config`.