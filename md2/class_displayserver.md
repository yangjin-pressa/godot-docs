# DisplayServer Window Methods Documentation

Below is a comprehensive documentation of the `DisplayServer` window-related methods, including their parameters, descriptions, notes, and platform-specific behaviors.

---

## `window_set_title(title: String, window_id: int = 0)`
**Description:**  
Sets the title of the given window to `title`.  
**Parameters:**  
- `title`: The new window title.  
- `window_id`: The ID of the window to update (default is 0).  

**Notes:**  
- It's recommended to use the `Window.title` property instead.  
- Avoid changing the title frequently (e.g., every frame) to prevent performance issues on certain window managers.  

---

## `window_set_position(position: Vector2i, window_id: int = 0)`
**Description:**  
Sets the position of the given window to `position`.  
**Parameters:**  
- `position`: The new window position.  
- `window_id`: The ID of the window to update (default is 0).  

**Notes:**  
- On Linux (Wayland), this method is a no-op.  
- It's recommended to use the `Window.position` property instead.  

---

## `window_set_size(size: Vector2i, window_id: int = 0)`
**Description:**  
Sets the size of the given window to `size`.  
**Parameters:**  
- `size`: The new window size.  
- `window_id`: The ID of the window to update (default is 0).  

**Notes:**  
- It's recommended to use the `Window.size` property instead.  

---

## `window_start_drag(window_id: int = 0)`
**Description:**  
Starts an interactive drag operation on the window with the given `window_id`, using the current mouse position.  
**Parameters:**  
- `window_id`: The ID of the window to drag (default is 0).  

**Notes:**  
- This method is implemented on Linux (X11/Wayland), macOS, and Windows.  
- Allows the window to participate in system features like space switching and tiling.  

---

## `window_start_resize(edge: WindowResizeEdge, window_id: int = 0)`
**Description:**  
Starts an interactive resize operation on the window with the given `window_id`, using the current mouse position.  
**Parameters:**  
- `edge`: The edge to start resizing (e.g., top, bottom, left, right).  
- `window_id`: The ID of the window to resize (default is 0).  

**Notes:**  
- This method is implemented on Linux (X11/Wayland), macOS, and Windows.  

---

## `window_set_vsync_mode(vsync_mode: VSyncMode, window_id: int = 0)`
**Description:**  
Sets the V-Sync mode of the given window.  
**Parameters:**  
- `vsync_mode`: The desired V-Sync mode (e.g., enabled, disabled, or a hybrid mode).  
- `window_id`: The ID of the window to update (default is 0).  

**Notes:**  
- Supported modes: `VSYNC_ENABLED`, `VSYNC_DISABLED`, or `VSYNC_UNKNOWN`.  
- Modes other than `VSYNC_ENABLED` are only supported in Forward+ and Mobile rendering methods.  
- Fallbacks to `VSYNC_ENABLED` if the desired mode isn't supported.  

---

## `window_set_transient(window_id: int, parent_window_id: int)`
**Description:**  
Sets the transient parent for a window. Transient windows are destroyed when their parent is closed.  
**Parameters:**  
- `window_id`: The ID of the window to set as transient.  
- `parent_window_id`: The ID of the parent window.  

**Notes:**  
- It's recommended to use the `Window.transient` property instead.  
- Transient windows cannot enter full-screen mode.  

---

## `window_set_popup_safe_rect(window: int, rect: Rect2i)`
**Description:**  
Sets the bounding box of control or menu item that opened a popup window. Clicking this area won't close the popup.  
**Parameters:**  
- `window`: The ID of the window.  
- `rect`: The safe area rectangle in screen coordinates.  

---

## `window_set_rect_changed_callback(callback: Callable, window_id: int = 0)`
**Description:**  
Sets a callback to trigger when the window's size or position changes.  
**Parameters:**  
- `callback`: The function to call on rect change.  
- `window_id`: The ID of the window (default is 0).  

**Note:**  
- Warning: Overriding default implementations can introduce bugs.  

---

## `window_set_window_event_callback(callback: Callable, window_id: int = 0)`
**Description:**  
Sets a callback for window events (e.g., focus, close).  
**Parameters:**  
- `callback`: The function to call on window events.  
- `window_id`: The ID of the window (default is 0).  

**Note:**  
- Warning: Overriding default implementations can introduce bugs.  

---

## `window_set_transient(window_id: int, parent_window_id: int)`
**Description:**  
Sets the transient parent for a window. Transient windows are destroyed when their parent is closed.  
**Parameters:**  
- `window_id`: The ID of the window to set as transient.  
- `parent_window_id`: The ID of the parent window.  

**Notes:**  
- Transient windows cannot enter full-screen mode.  

---

## `window_set_popup_safe_rect(window: int, rect: Rect2i)`
**Description:**  
Sets the bounding box of control or menu item that opened a popup window. Clicking this area won't close the popup.  
**Parameters:**  
- `window`: The ID of the window.  
- `rect`: The safe area rectangle in screen coordinates.  

---

## `window_set_rect_changed_callback(callback: Callable, window_id: int = 0)`
**Description:**  
Sets a callback to trigger when the window's size or position changes.  
**Parameters:**  
- `callback`: The function to call on rect change.  
- `window_id`: The ID of the window (default is 0).  

**Note:**  
- Warning: Overriding default implementations can introduce bugs.  

---

## `window_set_window_event_callback(callback: Callable, window_id: int = 0)`
**Description:**  
Sets a callback for window events (e.g., focus, close).  
**Parameters:**  
- `callback`: The function to call on window events.  
- `window_id`: The ID of the window (default is 0).  

**Note:**  
- Warning: Overriding default implementations can introduce bugs.  

---

## Platform-Specific Notes
- **Wayland:** `window_set_position` is a no-op.  
- **VSync Modes:** Use `VSYNC_ENABLED` for compatibility.  
- **Transient Windows:** Behavior may vary across platforms.  

---

This documentation ensures developers understand the purpose, parameters, and limitations of each method, while encouraging the use of properties for better performance and readability.