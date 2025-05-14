The `Camera2D` class in Godot is used to manage 2D camera behavior, including positioning, zooming, dragging, and limiting movement. Below is a structured summary of its key components:

---

### **Properties**
1. **Position**  
   - **Type**: `Vector2`  
   - **Description**: The camera's position in global coordinates.  
   - **Related Methods**: `set_position()`, `get_position()`.  

2. **Zoom**  
   - **Type**: `Vector2`  
   - **Description**: Zoom scaling for the viewport (e.g., `Vector2(2, 2)` doubles the size).  
   - **Note**: Fonts and rasterized text may appear blurry if zoomed; use MSDF fonts for crispness.  

3. **Drag Margins**  
   - **Type**: `float` (per `Side` enum: `TOP`, `BOTTOM`, `LEFT`, `RIGHT`).  
   - **Description**: Margins for drag interaction (e.g., `drag_bottom_margin`).  
   - **Related Methods**: `set_drag_margin()`, `get_drag_margin()`.  

4. **Limits**  
   - **Type**: `int` (per `Side`).  
   - **Description**: Camera movement boundaries (e.g., `limit_bottom`).  
   - **Related Methods**: `set_limit()`, `get_limit()`.  

5. **Smoothing**  
   - **Type**: `bool` (for `position_smoothing_enabled`).  
   - **Description**: Whether the camera position is smoothed over time.  
   - **Note**: `reset_smoothing()` forces immediate position update.  

6. **Tracking**  
   - **Type**: `Node2D` (tracked node).  
   - **Description**: Aligns the camera to the tracked node's position.  
   - **Method**: `align()`.  

7. **Active Camera**  
   - **Type**: `bool` (via `enabled`).  
   - **Description**: Determines if the camera is active.  
   - **Method**: `make_current()` sets it as the active camera.  

---

### **Methods**
1. **`align()`**  
   - **Description**: Aligns the camera to the tracked node's position.  

2. **`force_update_scroll()`**  
   - **Description**: Forces the camera to update its scroll position immediately.  

3. **`get_screen_center_position()`**  
   - **Description**: Returns the center of the viewport in global coordinates.  
   - **Note**: This may differ from the camera's target position.  

4. **`get_target_position()`**  
   - **Description**: Returns the camera's target position (affected by drag/smoothing).  
   - **Note**: Not the same as `Node2D.global_position`.  

5. **`is_current()`**  
   - **Description**: Checks if this camera is the active one.  

6. **`reset_smoothing()`**  
   - **Description**: Sets the camera's position to its smoothing target immediately.  

7. **`set_drag_margin()`**  
   - **Description**: Sets margins for drag interaction.  

8. **`set_limit()`**  
   - **Description**: Sets boundaries for camera movement.  

9. **`make_current()`**  
   - **Description**: Forces the camera to become active.  

---

### **Key Notes**
- **Zoom and Fonts**:  
  Zoom affects the viewport scale but does not influence `FontFile.oversampling`. Use MSDF fonts for clear text at different zoom levels.  

- **Target vs. Screen Center**:  
  The camera's target position (`get_target_position()`) includes drag/smoothing adjustments, while the screen center (`get_screen_center_position()`) reflects the current viewport.  

- **Drag Interaction**:  
  Drag margins control how much of the viewport is "clickable" for panning.  

- **Smoothing Behavior**:  
  When `position_smoothing_enabled` is `true`, the camera moves smoothly toward its target position.  

---

This class is essential for creating interactive 2D views, with flexibility for tracking, zooming, and user-driven movement.