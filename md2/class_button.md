Here’s a detailed breakdown of the **Button** class in Godot, covering its properties, theme-related settings, and key considerations for UI design:

---

### **Button Properties**
1. **`icon`**  
   - **Type:** `Texture2D`  
   - **Description:** Sets the default icon for the button. If not assigned, the button will not display an icon unless specified elsewhere.

2. **`text`**  
   - **Type:** `String`  
   - **Description:** The text displayed on the button. This is typically controlled via the `Label` node inside the button.

3. **`expand_icon`**  
   - **Type:** `bool`  
   - **Description:** If `true`, the icon scales with the button's size. Otherwise, it uses its default size.

4. **`h_separation`**  
   - **Type:** `int`  
   - **Description:** Horizontal spacing between the icon and text. Negative values are treated as `0`.

5. **`icon_max_width`**  
   - **Type:** `int`  
   - **Description:** Maximum allowed width for the icon. If non-zero, the icon is scaled to fit within this limit.

---

### **Theme-Related Properties**
These control the visual appearance of the button in different states (normal, hovered, pressed, etc.).

#### **StyleBox (Style Sheets)**
- **`normal`**  
  Default style for the button when not in any special state (e.g., not hovered/pressed).

- **`hover`**  
  Style applied when the mouse is over the button. Often used for visual feedback.

- **`pressed`**  
  Style for when the button is clicked. May include depressed or active states.

- **`disabled`**  
  Style for when the button is disabled (e.g., grayed out).

- **`focus`**  
  Visual effect when the button is focused (e.g., outlined or underlined). Use `StyleBoxEmpty` to disable this.

- **Mirrored Versions**  
  - **`hover_mirrored` / `pressed_mirrored`**  
    Used for right-to-left layouts to ensure consistency in UI direction.

#### **Font and Text Settings**
- **`font`**  
  The font used for the button's text. Overrides the default font in the theme.

- **`font_size`**  
  Font size for the text. Can be adjusted for different screen sizes or UI hierarchies.

- **`line_spacing`**  
  Additional vertical spacing between text lines (in pixels). Negative values are allowed for spacing adjustments.

- **`outline_size`**  
  Size of the text outline. **Note:** For MSDF fonts, ensure `msdf_pixel_range` is at least twice this value to avoid rendering issues.

#### **Constants**
- **`align_to_largest_stylebox`**  
  A boolean-like constant. If `true`, the button's size is based on the largest stylebox margins. Otherwise, it uses the current state's margins.

---

### **Key Considerations**
1. **State Transitions**  
   - Buttons use state-specific styles (e.g., `hover`, `pressed`) to provide visual feedback. Ensure these styles are distinct but cohesive.

2. **Accessibility**  
   - **Focus Visuals:** Use `focus` style boxes for keyboard/navigational feedback. Avoid `StyleBoxEmpty` unless explicitly required for design.
   - **Contrast:** Ensure text and icon colors contrast properly with background styles, especially in disabled states.

3. **Responsive Design**  
   - Use `expand_icon` and `icon_max_width` to adapt icons to different screen sizes or layouts.
   - Adjust `h_separation` for spacing consistency across devices.

4. **Right-to-Left (RTL) Support**  
   - Use mirrored styles (`hover_mirrored`, `pressed_mirrored`) to ensure buttons behave correctly in RTL layouts.

5. **MSDF Fonts**  
   - If using `outline_size` with MSDF fonts, configure `msdf_pixel_range` correctly to avoid rendering artifacts.

---

### **Example Use Case**
```gdscript
# Example: Customizing a Button's Theme
var button = Button.new()
button.add_theme_stylebox("normal", "path/to/normal.style")
button.add_theme_stylebox("hover", "path/to/hover.style")
button.add_theme_font("font", "path/to/custom_font.ttf")
button.add_theme_font_size("font_size", 16)
button.add_theme_constant("h_separation", 8)
```

---

### **Summary**
The **Button** class in Godot offers flexible control over appearance and behavior through a combination of properties and theme settings. By carefully configuring styles, fonts, and layout constants, you can create visually appealing and accessible UI elements that adapt to different user interactions and screen sizes. Always test RTL support and ensure consistent feedback for hover, press, and focus states.