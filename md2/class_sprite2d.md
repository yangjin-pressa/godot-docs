**Sprite2D Class**

---

### **Description**
A Node2D that draws a Texture2D. It supports properties for sprite sheets, region cutting, and offset adjustments.

---

### **Tutorials**
- [Example: Detecting clicks on a Sprite2D](#example)

---

### **Properties**
- **`region_enabled`**  
  Type: `bool`  
  Default: `false`  
  Description: If `true`, the texture is cut from a larger atlas texture. Use `region_rect` to define the region.

- **`region_filter_clip_enabled`**  
  Type: `bool`  
  Default: `false`  
  Description: If `true`, the area outside `region_rect` is clipped to avoid texture bleeding. Requires `region_enabled` to be `true`.

- **`region_rect`**  
  Type: `Rect2`  
  Default: `Rect2(0, 0, 0, 0)`  
  Description: The region of the atlas texture to display. Requires `region_enabled` to be `true`.

- **`texture`**  
  Type: `Texture2D`  
  Description: The texture to draw. If `null`, the sprite is invisible.

- **`offset`**  
  Type: `Vector2`  
  Default: `Vector2(0, 0)`  
  Description: The texture's drawing offset.

- **`centered`**  
  Type: `bool`  
  Default: `false`  
  Description: If `true`, the texture is drawn centered on the node.

- **`hframes`**  
  Type: `int`  
  Default: `1`  
  Description: Number of columns in the sprite sheet. Adjusts `frame` to maintain the same visual frame.

- **`vframes`**  
  Type: `int`  
  Default: `1`  
  Description: Number of rows in the sprite sheet. Adjusts `frame` to maintain the same visual frame.

- **`frame`**  
  Type: `int`  
  Default: `0`  
  Description: The frame to display from the sprite sheet. Adjusts automatically when `hframes` or `vframes` change.

- **`frame_rect`**  
  Type: `Rect2`  
  Default: `Rect2(0, 0, 0, 0)`  
  Description: The frame's position and size in the sprite sheet. Overrides `frame` if set.

- **`frame_offset`**  
  Type: `Vector2`  
  Default: `Vector2(0, 0)`  
  Description: Offset for the frame within the sprite sheet.

---

### **Methods**
- **`get_rect()`**  
  Type: `Rect2`  
  Description: Returns the Sprite2D's boundary in local coordinates.  
  **Example:**  
  ```gdscript
  func _input(event):
      if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
          if get_rect().has_point(to_local(event.position)):
              print("A click!")
  ```
  ```csharp
  public override void _Input(InputEvent @event)
  {
      if (@event is InputEventMouseButton inputEventMouse)
      {
          if (inputEventMouse.Pressed && inputEventMouse.ButtonIndex == MouseButton.Left)
          {
              if (GetRect().HasPoint(ToLocal(inputEventMouse.Position)))
              {
                  GD.Print("A click!");
              }
          }
      }
  }
  ```

- **`is_pixel_opaque(pos: Vector2)`**  
  Type: `bool`  
  Description: Returns `true` if the pixel at `pos` is opaque. Returns `false` if texture is `null` or position is invalid.

---

### **Signals**
- **`texture_changed`**  
  Triggered when the `texture` property changes.

- **`region_changed`**  
  Triggered when `region_enabled` or `region_rect` changes.

---

### **Notes**
- The `frame` property depends on `hframes` and `vframes`. If they change, `frame` is adjusted to maintain the same visual frame.
- The `is_pixel_opaque` method returns `false` if the texture is `null` or the position is invalid.