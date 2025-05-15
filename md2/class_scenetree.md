Here's a detailed explanation of the methods in the `SceneTree` class, including their purpose, parameters, and relevant notes:

---

### **`change_scene(path: String, position: Vector2)`**
**Description:**  
Changes the current scene to a new scene specified by the given path. The new scene's root node is positioned relative to the current scene's root.

**Parameters:**
- `path`: The path to the new scene file (e.g., `"res://scene.tscn"`).
- `position`: The position (in world coordinates) of the new scene's root node.

**Notes:**  
- This method replaces the current scene with the new one. If the new scene is not found, it may fail.
- Useful for dynamically loading scenes from a file.

---

### **`change_scene_to(path: String, position: Vector2)`**
**Description:**  
Similar to `change_scene`, but may allow for more specific control over the scene transition (e.g., transitions, animations, or custom behavior).

**Parameters:**
- `path`: The path to the new scene.
- `position`: The position of the new scene's root node.

**Notes:**  
- The exact behavior depends on the implementation. In Godot, this method is not directly available, but the equivalent is `change_scene`.

---

### **`change_scene_with(...)`**
**Description:**  
A hypothetical method for changing scenes with additional parameters (e.g., scene arguments, custom parameters, or animations).

**Parameters:**  
Not explicitly listed, but may include:
- Scene path.
- Position.
- Additional scene-specific parameters.

**Notes:**  
- This method is likely a placeholder or variation of `change_scene` with extended functionality.

---

### **`clear()`**
**Description:**  
Removes all nodes from the scene tree, effectively resetting the scene to an empty state.

**Parameters:**  
None.

**Notes:**  
- Clears the current scene's root node and any children, but does not unload the scene itself.

---

### **`current_scene` (Property)**
**Description:**  
Returns the current scene being loaded and active in the `SceneTree`.

**Return Type:**  
A `PackedScene` object representing the current scene.

**Notes:**  
- This property is read-only and reflects the scene currently loaded via `load_scene()` or `change_scene()`.

---

### **`reload_current_scene()`**
**Description:**  
Reloads the currently active scene, re-applying any changes made to the scene file.

**Parameters:**  
None.

**Notes:**  
- Useful for re-loading a scene after modifying its resource file (e.g., changing a texture or script).

---

### **`queue_delete(obj: Node)`**
**Description:**  
Queues the specified node for deletion at the end of the current frame.

**Parameters:**
- `obj`: The node to delete.

**Notes:**  
- Similar to `Node.queue_free()`, but this method is specific to the `SceneTree` class.
- Deletes the node from the scene hierarchy but does not immediately remove it from memory.

---

### **`quit()`**
**Description:**  
Exits the application, terminating the game or app.

**Parameters:**  
None.

**Notes:**  
- On iOS, this method may not work as expected (e.g., the app may not close). Use the Home button instead for termination.

---

### **`unload_current_scene()`**
**Description:**  
Unloads the current scene, freeing its resources (e.g., textures, sounds, etc.).

**Parameters:**  
None.

**Notes:**  
- This method is useful for releasing memory or resources when a scene is no longer needed.
- Does not remove the scene from the `SceneTree` property but frees its memory.

---

### **`notify_group(group: String, notification: int)`**
**Description:**  
Notifies all nodes in the specified group of a given notification.

**Parameters:**
- `group`: The name of the group (e.g., `"Player"`, `"Enemy"`, etc.).
- `notification`: A notification type (e.g., `NOTIFICATION_ENTER_TREE`, `NOTIFICATION_EXIT_TREE`).

**Notes:**  
- This method is used to broadcast events to all nodes in a group.
- Efficient for managing node behavior in groups.

---

### **`notify_group_flags(group: String, notification: int, flags: int)`**
**Description:**  
Sends a notification to nodes in a group with optional flags for behavior customization.

**Parameters:**
- `group`: Group name.
- `notification`: Notification type.
- `flags`: Flags to customize behavior (e.g., `NOTIFY_FLAG_LOCAL`, `NOTIFY_FLAG_RECURSIVE`).

**Notes:**  
- Flags control how the notification is processed (e.g., whether it's recursive or affects only local nodes).

---

### **`set_group(group: String, property: String, value: Variant)`**
**Description:**  
Sets a specific property of all nodes in the specified group.

**Parameters:**
- `group`: Group name.
- `property`: Property name (e.g., `"position"`, `"visible"`).
- `value`: New value for the property.

**Notes:**  
- Useful for batch updates to nodes in a group (e.g., disabling all nodes in a group).

---

### **`set_group_flags(group: String, property: String, value: Variant, flags: int)`**
**Description:**  
Sets a property of nodes in a group with optional flags for behavior customization.

**Parameters:**
- `group`: Group name.
- `property`: Property name.
- `value`: New value.
- `flags`: Flags to customize behavior.

**Notes:**  
- Similar to `set_group`, but with flags for more control.

---

### **`set_multiplayer(config: MultiplayerConfig)`**
**Description:**  
Configures the multiplayer settings for the current scene.

**Parameters:**
- `config`: A `MultiplayerConfig` object containing settings like connection type, port, etc.

**Notes:**  
- This method sets up the scene for multiplayer functionality, suchity for networked gameplay.

---

### **`is_accessibility_enabled()`**
**Description:**  
Checks if accessibility features are enabled for the current scene.

**Return Type:**  
A `bool` indicating whether accessibility is enabled.

**Notes:**  
- Accessibility features may include larger text, high contrast, or other UI adjustments.

---

### **`is_accessibility_supported()`**
**Description:**  
Checks if the current platform supports accessibility features.

**Return Type:**  
A `bool` indicating whether the OS supports accessibility.

**Notes:**  
- This is useful for determining if UI adjustments for accessibility are necessary.

---

### **Key Concepts**
- **Scene Tree:** The `SceneTree` class manages the hierarchy of nodes in a scene, allowing for dynamic scene loading and control.
- **Groups:** Nodes can be grouped for efficient batch operations (e.g., changing properties, sending notifications).
- **Multiplayer:** The `set_multiplayer()` method enables networked gameplay by configuring the scene for multiplayer.
- **Accessibility:** The `is_accessibility_` methods help adapt scenes to user needs.

This comprehensive list covers the core functionality of the `SceneTree` class, including scene management, node manipulation, and platform-specific features.