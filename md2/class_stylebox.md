**Inheritance**  
- Inherits from: `Control`  

---

**Properties**  
- **content_margin_left**: `float`  
  - The default margin offset for the left side.  
- **content_margin_right**: `float`  
  - The default margin offset for the right side.  
- **content_margin_top**: `float`  
  - The default margin offset for the top side.  
- **content_margin_bottom**: `float`  
  - The default margin offset for the bottom side.  

---

**Methods**  

**Public Methods**  
- **draw**(`canvas_item: RID`, `rect: Rect2`)  
  - Draws this stylebox using a canvas item identified by the given `RID`.  

- **get_content_margin**(`margin: Side`)  
  - Returns the default margin of the specified `Side`.  

- **get_margin**(`margin: Side`)  
  - Returns the content margin offset for the specified `Side`.  
  - Positive values reduce size inward, unlike `Control`'s margin values.  

- **get_minimum_size**()  
  - Returns the minimum size that this stylebox can be shrunk to.  

- **get_offset**()  
  - Returns the "offset" of a stylebox as a `Vector2` (left and top margins).  

- **set_content_margin**(`margin: Side`, `offset: float`)  
  - Sets the default value of the specified `Side` to `offset` pixels.  

- **set_content_margin_all**(`offset: float`)  
  - Sets the default margin to `offset` pixels for all sides.  

**Private Methods**  
- **_draw**(`to_canvas_item: RID`, `rect: Rect2`)  
  - Virtual method to draw the stylebox. No description provided.  

- **_get_draw_rect**(`rect: Rect2`)  
  - Virtual method to calculate the drawing rectangle. No description provided.  

- **_get_minimum_size**()  
  - Virtual method to return a custom minimum size. By default, it considers content margins.  

- **_test_mask**(`point: Vector2`, `rect: Rect2`)  
  - Virtual method to test if a point is within the mask. No description provided.  

---

**Notes**  
- The `get_margin` method returns the content margin offset, which is used to adjust the stylebox's size.  
- The `_test_mask` method is used for determining if a point lies within the stylebox's mask area.  
- Private methods like `_draw` and `_get_draw_rect` are intended for subclass overriding.  
- Some methods (e.g., `_draw`, `_get_draw_rect`, `_test_mask`) lack descriptions and require user contribution for clarification.