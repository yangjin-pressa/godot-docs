**Class Name and Inheritance**  
- **SceneReplicationConfig**: Inherits from `Resource` → `RefCounted` → `Object`.

---

**Enumerations**  
- **ReplicationMode**:  
  - **NEVER**: Synchronization is disabled.  
  - **ALWAYS**: Synchronization is enabled continuously.  
  - **ON_CHANGE**: Synchronization occurs only when changes are detected.  

---

**Methods**  
- **add_property(path: NodePath, index: int)**:  
  Adds a property to the synchronization configuration.  
  **Note**: See [MultiplayerSynchronizer](class_MultiplayerSynchronizer) for more information.  

- **property_get_replication_mode(path: NodePath)**:  
  Returns the synchronization mode for a property.  
  **See**: [ReplicationMode](enum_SceneReplicationConfig_ReplicationMode).  

- **property_set_replication_mode(path: NodePath, mode: ReplicationMode)**:  
  Sets the synchronization mode for a property.  

- **property_set_spawn(path: NodePath, enabled: bool)**:  
  Enables or disables synchronization on spawn for a property.  

- **property_set_sync(path: NodePath, enabled: bool)**:  
  **Deprecated**: Use `property_set_replication_mode` with `ALWAYS` instead.  
  Sets whether a property is synchronized on process.  

- **property_set_watch(path: NodePath, enabled: bool)**:  
  **Deprecated**: Use `property_set_replication_mode` with `ON_CHANGE` instead.  
  Sets whether a property is reliably synchronized on changes.  

- **remove_property(path: NodePath)**:  
  Removes a property from the configuration.  

- **property_get_sync(path: NodePath)**:  
  **Deprecated**: Use `property_get_replication_mode` instead.  
  Returns whether a property is synchronized on process.  

- **property_get_watch(path: NodePath)**:  
  **Deprecated**: Use `property_get_replication_mode` instead.  
  Returns whether a property is reliably synchronized on changes.  

- **property_get_spawn(path: NodePath)**:  
  Returns whether a property is synchronized on spawn.  

- **property_get_sync(path: NodePath)**:  
  **Deprecated**: Use `property_get_replication_mode` instead.  

- **property_get_watch(path: NodePath)**:  
  **Deprecated**: Use `property_get_replication_mode` instead.  

--- 

**Key Notes**  
- **ReplicationMode** defines how properties are synchronized during gameplay.  
- **DEPRECATED** methods should be replaced with the `ReplicationMode`-based approach.