**EditorSpinSlider**  
A control node for numeric editing in the Godot Engine's editor. Used with the Inspector plugin to display and manipulate numerical values. The behavior of the control depends on the `step` property: if set to a non-zero value, it displays arrows for increment/decrement; otherwise, it uses a slider.

---

### **Properties**  
- **editing_integer**: `bool`  
  Determines whether the control treats the value as an integer (displays arrows) or a float (displays a slider).  
  - **Set**: `set_editing_integer(bool value)`  
  - **Get**: `is_editing_integer()`  

- **flat**: `bool`  
  Controls whether the control appears flat (no background color).  

- **focus_mode**: `int`  
  Sets the focus mode (e.g., mouse or keyboard focus).  

- **hide_slider**: `bool`  
  Hides the slider if enabled.  

- **label**: `String`  
  The text displayed next to the value.  

- **read_only**: `bool`  
  Prevents user interaction with the control.  

- **size_flags_vertical**: `int`  
  Determines vertical size constraints (e.g., fixed height).  

- **step**: `float`  
  The step value for incrementing/decrementing. Defaults to 0 (slider mode).  

- **suffix**: `String`  
  A suffix displayed after the value (e.g., "px" for pixels).  

---

### **Theme Properties**  
- **updown**: `Texture2D`  
  A single texture for both up and down buttons.  

- **updown_disabled**: `Texture2D`  
  A single texture for up/down buttons when the control is readonly or disabled.  

---

### **Signals**  
- **grabbed**: Triggered when the user clicks and drags the slider.  
- **ungrabbed**: Triggered when the user releases the slider.  
- **updown_pressed**: Triggered when the up/down buttons are pressed.  

---

### **Key Notes**  
- **Step Value**: A non-zero `step` value enables arrow-based interaction.  
- **Suffix Handling**: Suffixes are typically plural words (e.g., "percent" for "%").  
- **Theme Textures**: Custom textures for buttons can be set via the theme.  

This class provides a flexible way to interact with numerical values in the Godot editor, with customizable behavior and appearance.