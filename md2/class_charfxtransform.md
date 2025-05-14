**Class Name:** CharFXTransform  
**Inherits:** RefCounted  

---

### **Description**  
Used for FX transforms in the RichTextEffect system. Controls properties like color, position, and transformations for individual characters.

---

### **Tutorials**  
- [RichTextEffect Tutorial](https://docs.godotengine.org/en/latest/tutorials/2d/rich_text.html)  

---

### **Properties**  
1. **color**  
   - **Type:** Color  
   - **Default:** Color(1, 1, 1, 0)  
   - **Description:** The color of the character.  
   - **Set/Get:** `set_color(new_color)`, `get_color()`  
   - **Notes:** If set to transparent, the character is hidden.  

2. **offset**  
   - **Type:** Vector2  
   - **Default:** Vector2(0, 0)  
   - **Description:** Position offset for the character (in pixels).  
   - **Set/Get:** `set_offset(new_offset)`, `get_offset()`  

3. **transform**  
   - **Type:** Transform2D  
   - **Default:** Transform2D(1, 0, 0, 1, 0, 0)  
   - **Description:** Current transformation matrix for the glyph.  
   - **Set/Get:** `set_transform(new_transform)`, `get_transform()`  

4. **visible**  
   - **Type:** bool  
   - **Default:** true  
   - **Description:** Whether the character is visible.  
   - **Set/Get:** `set_visibility(new_visibility)`, `is_visible()`  
   - **Notes:** Hidden characters cause reflow; use `color` for transparency instead.  

5. **outline**  
   - **Type:** bool  
   - **Default:** false  
   - **Description:** Whether the FX transform is applied for outline drawing.  
   - **Set/Get:** `set_outline(new_outline)`, `is_outline()`  
   - **Notes:** Read-only; does not affect rendering.  

---

### **Other Properties**  
- **range**  
  - **Type:** Vector2i  
  - **Default:** Vector2i(0, 0)  
  - **Description:** Absolute character range in the string.  
  - **Notes:** Read-only.  

- **relative_index**  
  - **Type:** int  
  - **Default:** 0  
  - **Description:** Character offset relative to the current block.  
  - **Notes:** Read-only.  

- **glyph_index**  
  - **Type:** int  
  - **Default:** 0  
  - **Description:** Glyph index specific to the font.  
  - **Notes:** Read-only; use `TextServer` to replace glyphs.  

- **glyph_range**  
  - **Type:** Vector2i  
  - **Default:** Vector2i(0, 0)  
  - **Description:** Range of glyphs in the font.  
  - **Notes:** Read-only.  

---

### **Key Notes**  
- All properties are either read-only or can be set dynamically.  
- Transformations (e.g., rotation, scaling) are applied via `transform`.  
- Use `visible` for hiding characters, or `color` for transparency.  
- Transform2D can be overridden for animation or curve-driven effects.