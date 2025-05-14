Here's a structured guide to the **Godot ColorPicker** node, covering its properties, methods, and customizability. This helps you understand how to use and extend the node in your Godot project.

---

### **1. Properties**
These are the core settings that control the behavior and appearance of the color picker.

#### **Boolean Flags**
- **`can_focus`**: Enables keyboard/controller focus for navigation.
- **`can_select_color`**: Allows users to select colors via the picker.
- **`is_custom`**: Indicates if the color picker is custom (e.g., used in a custom UI).

#### **Size and Position**
- **`size`**: The overall size of the color picker.
- **`min_size`**: Minimum size for the color picker.
- **`offset`**: Offset from the parent node's position.

#### **Color Picker Settings**
- **`color`**: The currently selected color.
- **`color_hue`**: Hue value of the selected color.
- **`color_saturation`**: Saturation value.
- **`color_value`**: Value (brightness) of the selected color.

#### **Picker Shape**
- **`picker_shape`**: Controls the shape of the color picker (circle, square, wheel, etc.).

---

### **2. Methods**
These are the functions you can call to interact with the color picker.

#### **`get_selected_color()`**
- **Return Type**: `Color`  
- **Description**: Returns the currently selected color.  
- **Note**: This method is virtual and should be overridden if you need a custom implementation.

#### **`set_selected_color(color: Color)`**
- **Parameters**: `color: Color`  
- **Description**: Sets the selected color and updates the UI.

#### **`get_selected_color_hue()`**
- **Return Type**: `float`  
- **Description**: Returns the hue value of the selected color.

#### **`set_selected_color_hue(hue: float)`**
- **Parameters**: `hue: float`  
- **Description**: Sets the hue value of the selected color.

#### **`get_selected_color_saturation()`**
- **Return Type**: `float`  
- **Description**: Returns the saturation value of the selected color.

#### **`set_selected_color_saturation(saturation: float)`**
- **Parameters**: `saturation: float`  
- **Description**: Sets the saturation value of the selected color.

#### **`get_selected_color_value()`**
- **Return Type**: `float`  
- **Description**: Returns the value (brightness) of the selected color.

#### **`set_selected_color_value(value: float)`**
- **Parameters**: `value: float`  
- **Description**: Sets the value (brightness) of the selected color.

---

### **3. Themes (Customization)**
These allow you to customize the appearance of the color picker. Themes are typically set via the **Theme Editor** in Godot.

#### **Icons**
- **`add_preset`**: Icon for the "Add Preset" button.  
- **`bar_arrow`**: Texture for the arrow grabber.  
- **`color_hue`**: Texture for the hue slider.  
- **`expanded_arrow`**: Icon for the preset dropdown when expanded.  
- **`folded_arrow`**: Icon for the preset dropdown when folded.  
- **`menu_option`**: Icon for preset menu options.  
- **`overbright_indicator`**: Indicator for colors outside the 0-1 range.  
- **`picker_cursor`**: Cursor for the selected color.  
- **`picker_cursor_bg`**: Background for the picker cursor.  
- **`sample_bg`**: Background for the color preview.  
- **`sample_revert`**: Icon for the "revert" button.  
- **`screen_picker`**: Icon for the screen color picker.  
- **`shape_circle`**: Icon for circular picker shapes.  
- **`shape_rect`**: Icon for rectangular picker shapes.  
- **`shape_rect_wheel`**: Icon for rectangular wheel picker shapes.  

#### **Styles (Focus and Visuals)**
- **`picker_focus_circle`**: StyleBox for the focus effect on the circular part of the picker.  
- **`picker_focus_rectangle`**: StyleBox for the focus effect on the rectangular part of the picker.  
- **`sample_focus`**: StyleBox for the focus effect on the sample area.  

**Note**: Use partially transparent StyleBoxes for focus effects to ensure the picker shape remains visible. Avoid using `StyleBoxEmpty` for accessibility reasons.

---

### **4. Key Considerations**
- **Accessibility**: Ensure the color picker is navigable via keyboard/controller. Use focus styles (`picker_focus_circle`, `picker_focus_rectangle`, `sample_focus`) to indicate interaction areas.
- **Customization**: Replace icons and styles with your own textures or StyleBoxes to match your UI theme.
- **Color Range**: The `overbright_indicator` helps users know if a color is outside the 0-1 range.
- **Theming**: Use the **Theme Editor** to assign textures and styles to the color picker. For example, set `picker_cursor` to a custom cursor image.

---

### **5. Example Usage**
```gdscript
# Get the color picker from the scene
var color_picker = get_node("ColorPicker")

# Set a selected color
color_picker.set_selected_color(Color.from_hsv(0.5, 0.7, 0.8))

# Get the current color
var selected_color = color_picker.get_selected_color()
print("Selected color:", selected_color)

# Customize the picker shape
color_picker.picker_shape = ColorPicker.PICKER_SHAPE_CIRCLE
```

---

### **6. Extensibility**
- Override `get_selected_color()` if you need to implement a custom color selection logic.
- Add custom buttons or menus using the `add_preset` icon and `menu_option` theme to allow saving colors to a list.

---

This guide covers the essential properties, methods, and customization options for the Godot ColorPicker node. Use it to build a rich, interactive color picker in your projects!