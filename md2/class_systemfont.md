**SystemFont Class Overview**  
The `SystemFont` class in Godot represents a system font, allowing access to system-installed fonts for rendering text. It provides properties to control font characteristics, hinting, subpixel positioning, and rendering options.

---

### **Key Properties**  

1. **font_weight**  
   - **Type**: `int`  
   - **Default**: `400`  
   - **Description**: Preferred font weight (boldness). Range: 100–999. `400` = normal, `700` = bold.  

2. **font_stretch**  
   - **Type**: `int`  
   - **Default**: `100` (50% of normal width)  
   - **Description**: Preferred font stretch percentage (50%–200%).  

3. **hinting**  
   - **Type**: `Hinting` (enum)  
   - **Default**: `1` (normal hinting)  
   - **Description**: Font hinting mode (e.g., `HINTING_NORMAL`, `HINTING_NONE`).  

4. **subpixel_positioning**  
   - **Type**: `SubpixelPositioning` (enum)  
   - **Default**: `1` (auto)  
   - **Description**: Subpixel positioning mode for smoother text rendering. Use `SUBPIXEL_POSITIONING_AUTO` for automatic handling.  

5. **keep_rounding_remainders**  
   - **Type**: `bool`  
   - **Default**: `true`  
   - **Description**: Accumulates rounding remainders for uniform glyph distribution (no effect if subpixel positioning is enabled).  

6. **modulate_color_glyphs**  
   - **Type**: `bool`  
   - **Default**: `false`  
   - **Description**: Applies color modulation to colored glyphs instead of monochrome ones.  

7. **msdf_pixel_range**  
   - **Type**: `int`  
   - **Default**: `16`  
   - **Description**: Range for MSDF textures. Minimum value ensures outline sizes up to `8` render correctly.  

8. **msdf_size**  
   - **Type**: `int`  
   - **Default**: `48`  
   - **Description**: Source font size for MSDF textures. Larger values improve precision but increase memory usage.  

9. **multichannel_signed_distance_field**  
   - **Type**: `bool`  
   - **Default**: `false`  
   - **Description**: Renders all glyph sizes using a single multichannel MSDF texture.  

10. **generate_mipmaps**  
    - **Type**: `bool`  
    - **Default**: `false`  
    - **Description**: Generates mipmaps for font textures to improve performance on different scales.  

11. **force_autohinter**  
    - **Type**: `bool`  
    - **Default**: `false`  
    - **Description**: Prioritizes auto-hinting over font-specific hinting.  

12. **allow_lazy_load**  
    - **Type**: `bool`  
    - **Default**: `true`  
    - **Description**: Loads font data on demand (lazy loading).  

---

### **Deprecated Property**  
- **oversampling**  
  - **Type**: `float`  
  - **Default**: `2.0`  
  - **Note**: Deprecated. Use `oversampling` parameter in `draw_*` methods instead. This property does nothing.  

---

### **Important Notes**  
- **System Font Access**: This class allows access to system fonts for rendering, but availability depends on the platform.  
- **MSDF Settings**: For MSDF textures, ensure `msdf_pixel_range` is at least twice the largest font outline size.  
- **Subpixel Positioning**: Enables smoother text rendering but increases memory and rasterization cost.  
- **Lazy Loading**: `allow_lazy_load` can reduce initial resource usage but may delay rendering.  

This summary covers the core properties, their purposes, and relevant notes for using the `SystemFont` class effectively.