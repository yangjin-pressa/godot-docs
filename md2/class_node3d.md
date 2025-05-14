Here's a structured overview of the **`Node3D`** class methods in Godot 4, along with their purposes, parameters, and key considerations:

---

### **Core Transformations and Positioning**
1. **`hide()` / `show()`**  
   - **Purpose**: Control visibility of the node.  
   - **`hide()`**: Equivalent to setting `visible = false`.  
   - **`show()`**: Equivalent to setting `visible = true`.  
   - **Use Case**: Toggle visibility of 3D objects in the scene.

2. **`translate()` / `translate_object_local()`**  
   - **Purpose**: Move the node's position.  
   - **`translate()`**: Adds offset to the **local** position (relative to the node).  
   - **`translate_object_local()`**: Same as `translate()`, but preferred for future compatibility.  
   - **Note**: `translate()` is **not** in parent space by default. Use `position += offset` for parent-space translation.

3. **`scale_object_local()`**  
   - **Purpose**: Scale the node's basis (local space).  
   - **Parameters**: `scale` (a `Vector3`).  
   - **Use Case**: Adjust size of a node relative to its own local axes.

4. **`to_global()` / `to_local()`**  
   - **Purpose**: Convert points between local and global space.  
   - **`to_global(local_point)`**: Converts a local point to global coordinates.  
   - **`to_local(global_point)`**: Converts a global point to local coordinates.  
   - **Use Case**: For raycasting, collision detection, or UI interactions in 3D space.

---

### **Transform Notifications**
5. **`set_notify_transform()` / `set_notify_local_transform()`**  
   - **Purpose**: Enable/disable notifications when transforms change.  
   - **`set_notify_transform(enable)`**: Triggers `NOTIFICATION_TRANSFORM_CHANGED` when `global_transform` changes.  
   - **`set_notify_local_transform(enable)`**: Triggers `NOTIFICATION_LOCAL_TRANSFORM_CHANGED` when `transform` changes.  
   - **Use Case**: Ensure nodes respond to changes in their hierarchy or parent transformations.

6. **`set_ignore_transform_notification(enabled)`**  
   - **Purpose**: Temporarily suppress transform notifications.  
   - **Use Case**: Prevent infinite recursion when handling notifications (e.g., during custom logic).

---

### **Scaling and Orthonormalization**
7. **`set_disable_scale(disable)` / `is_scale_disabled()`**  
   - **Purpose**: Control whether `global_transform` is automatically orthonormalized.  
   - **`set_disable_scale(true)`**: Prevents distortion; enforces `scale = Vector3.ONE`.  
   - **Use Case**: Ensure objects remain axis-aligned when scaled.

8. **`orthonormalize()`**  
   - **Purpose**: Orthonormalize the node's transformation (rotates to align with parent).  
   - **Use Case**: Fix orientation issues when moving objects in 3D space.

---

### **Editor-Specific Features**
9. **`update_gizmos()`**  
   - **Purpose**: Update editor gizmos (e.g., move/rotate tools) attached to the node.  
   - **Use Case**: Only works in the editor; ensures gizmos reflect the node's current state.

10. **`set_subgizmo_selection(gizmo, id, transform)`**  
    - **Purpose**: Select a subgizmo in the editor and set its transformation.  
    - **Use Case**: Custom editor tools for fine-grained node manipulation.

---

### **Transform Reset and Identity**
11. **`set_identity()`**  
    - **Purpose**: Resets the node's transform to identity (no rotation, scale, or translation).  
    - **Use Case**: Reset a node's position and rotation for repositioning.

---

### **Key Notes**
- **Local vs Global**:  
  - Local transformations are relative to the node's own coordinate system.  
  - Global transformations are relative to the scene's root.  
  - Use `to_global()` and `to_local()` to convert between them.

- **Editor vs Game Mode**:  
  - Methods like `update_gizmos()` and `set_subgizmo_selection()` are **only valid in the editor**.  
  - Avoid relying on them in runtime code.

- **Performance**:  
  - Avoid frequent calls to `set_notify_transform()`/`set_notify_local_transform()` unless necessary.  
  - Use `set_ignore_transform_notification()` to prevent recursion.

---

### **Example Use Cases**
- **Simple Movement**:
  ```gdscript
  node3d.translate(Vector3(1, 0, 0))  # Move right in local space
  ```

- **Orthonormalize for Alignment**:
  ```gdscript
  node3d.orthonormalize()
  ```

- **Disable Distortion**:
  ```gdscript
  node3d.set_disable_scale(true)
  ```

- **Editor Gizmo Setup**:
  ```gdscript
  node3d.set_subgizmo_selection(editor_gizmo, 0, Transform3D.IDENTITY)
  ```

---

This summary covers the essential methods for manipulating 3D nodes in Godot, including core transformations, editor tools, and best practices for handling 3D space.