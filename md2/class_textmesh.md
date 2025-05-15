**Overview**  
The `TextMesh` class in Godot is used to generate a 3D mesh based on text content. It supports properties for text positioning, alignment, spacing, and styling. Key features include handling text direction, line spacing, and language-specific shaping. The class inherits from `Node` and is a `Resource`, meaning it can be saved and loaded independently.

---

**Properties**  
1. **autofill**  
   - Type: `bool`  
   - Default: `false`  
   - Controls automatic text filling.  

2. **autofit**  
   - Type: `bool`  
   - Default: `false`  
   - Enables text to automatically adjust to container size.  

3. **autofit_horizontal**  
   - Type: `bool`  
   - Default: `false`  
   - Auto-adjusts text width to container.  

4. **autofit_vertical**  
   - Type: `bool`  
   - Default: `false`  
   - Auto-adjusts text height to container.  

5. **background**  
   - Type: `Texture`  
   - Default: `null`  
   - Sets a background texture for the text.  

6. **background_color**  
   - Type: `Color`  
   - Default: `Color(0, 0, 0, 0)`  
   - Defines the background color.  

7. **background_visible**  
   - Type: `bool`  
   - Default: `false`  
   - Controls whether the background is visible.  

8. **border_bottom**  
   - Type: `float`  
   - Default: `0`  
   - Bottom border thickness.  

9. **border_left**  
   - Type: `float`  
   - Default: `0`  
   - Left border thickness.  

10. **border_right**  
    - Type: `float`  
    - Default: `0`  
    - Right border thickness.  

11. **border_top**  
    - Type: `float`  
    - Default: `0`  
    - Top border thickness.  

12. **border_visible**  
    - Type: `bool`  
    - Default: `false`  
    - Controls border visibility.  

13. **color**  
    - Type: `Color`  
    - Default: `Color(1, 1, 1, 1)`  
    - Text color.  

14. **color_visible**  
    - Type: `bool`  
    - Default: `true`  
    - Enables text color visibility.  

15. **font**  
    - Type: `Font`  
    - Default: `null`  
    - Specifies the font used for text.  

16. **font_size**  
    - Type: `int`  
    - Default: `12`  
    - Font size in pixels.  

17. **font_visible**  
    - Type: `bool`  
    - Default: `true`  
    - Controls font visibility.  

18. **height**  
    - Type: `float`  
    - Default: `0`  
    - Text height (in pixels).  

19. **hint**  
    - Type: `String`  
    - Default: `""`  
    - Extra text hint for styling.  

20. **hint_visible**  
    - Type: `bool`  
    - Default: `false`  
    - Enables hint visibility.  

21. **horizontal_alignment**  
    - Type: `enum`  
    - Default: `LEFT`  
    - Controls text horizontal alignment (left, center, right, fill, justify).  

22. **horizontal_padding**  
    - Type: `float`  
    - Default: `0`  
    - Horizontal padding around text.  

23. **hint_alignment**  
    - Type: `enum`  
    - Default: `LEFT`  
    - Alignment for hints.  

24. **hint_padding**  
    - Type: `float`  
    - Default: `0`  
    - Vertical padding for hints.  

25. **justification**  
    - Type: `enum`  
    - Default: `LEFT`  
    - Text justification (left, center, right).  

26. **justification_flags**  
    - Type: `bitfield`  
    - Default: `163`  
    - Line fill alignment rules (e.g., text shaping).  

27. **language**  
    - Type: `String`  
    - Default: `""`  
    - Language code for text shaping (if empty, uses system locale).  

28. **line_spacing**  
    - Type: `float`  
    - Default: `0`  
    - Additional vertical spacing between lines (in pixels).  

29. **line_spacing_mode**  
    - Type: `enum`  
    - Default: `AUTO`  
    - Spacing mode (auto, fixed, percentage).  

30. **max_width**  
    - Type: `float`  
    - Default: `0`  
    - Maximum text width (in pixels).  

31. **min_width**  
    - Type: `float`  
    - Default: `0`  
    - Minimum text width (in pixels).  

32. **offset**  
    - Type: `Vector2`  
    - Default: `(0, 0)`  
    - Text drawing offset (in pixels).  

33. **outline_color**  
    - Type: `Color`  
    - Default: `Color(0, 0, 0, 0)`  
    - Outline color.  

34. **outline_enabled**  
    - Type: `bool`  
    - Default: `false`  
    - Enables text outline.  

35. **outline_offset**  
    - Type: `float`  
    - Default: `0`  
    - Outline offset distance.  

36. **padding**  
    - Type: `float`  
    - Default: `0`  
    - Padding around text.  

37. **pixel_size**  
    - Type: `float`  
    - Default: `0.01`  
    - Scale factor for pixel size in 3D.  

38. **posture**  
    - Type: `enum`  
    - Default: `NORMAL`  
    - Text posture (normal, italic, bold).  

39. **posture_visible**  
    - Type: `bool`  
    - Default: `true`  
    - Enables posture visibility.  

40. **quality**  
    - Type: `int`  
    - Default: `3`  
    - Mesh quality (0-4, higher = more detail).  

41. **radius**  
    - Type: `float`  
    - Default: `0.05`  
    - Radius for text curves.  

42. **render_mode**  
    - Type: `enum`  
    - Default: `TEXTURE`  
    - Render mode (texture, lines, wireframe).  

43. **rotation**  
    - Type: `Vector3`  
    - Default: `(0, 0, 0)`  
    - Text rotation (X, Y, Z).  

44. **shadow_color**  
    - Type: `Color`  
    - Default: `Color(0, 0, 0, 0)`  
    - Shadow color.  

45. **shadow_offset**  
    - Type: `Vector2`  
    - Default: `(0, 0)`  
    - Shadow offset (X, Y).  

46. **shadow_visible**  
    - Type: `bool`  
    - Default: `false`  
    - Enables shadow visibility.  

47. **text**  
    - Type: `String`  
    - Default: `""`  
    - Main text content.  

48. **text_halign**  
    - Type: `enum`  
    - Default: `LEFT`  
    - Horizontal alignment of text.  

49. **text_valign**  
    - Type: `enum`  
    - Default: `TOP`  
    - Vertical alignment of text.  

50. **thickness**  
    - Type: `float`  
    - Default: `0.02`  
    - Text thickness.  

51. **use_outline**  
    - Type: `bool`  
    - Default: `false`  
    - Enables outline rendering.  

52. **use_shadow**  
    - Type: `bool`  
    - Default: `false`  
    - Enables shadow rendering.  

53. **vertical_flip**  
    - Type: `bool`  
    - Default: `false`  
    - Flips text vertically.  

54. **visible**  
    - Type: `bool`  
    - Default: `true`  
    - Controls text visibility.  

55. **width**  
    - Type: `float`  
    - Default: `0`  
    - Text width (in pixels).  

---

**Important Notes**  
- **Resource Behavior**: The `TextMesh` is a `Resource`, allowing it to be saved and reloaded independently.  
- **Translation Settings**: The text does not inherit the parent node's translation settings. To position the text, use the `offset` property or adjust the node's translation manually.  
- **Font Handling**: The `font` property must be assigned a valid `Font` resource (e.g., from `FontFace` or `FontTexture`).  
- **Mesh Quality**: The `quality` property balances detail and performance (higher values use more polygons).  

This class is ideal for creating 3D text elements in games or applications requiring text rendering with mesh geometry.