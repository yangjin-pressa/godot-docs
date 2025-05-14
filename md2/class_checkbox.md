**CheckBox Class**  

**Description**  
- A widget for interactive elements, inheriting from `Button`.  
- Overrides `BaseButton` properties and includes theme-based visual settings.  
- See also [BaseButton](class_BaseButton).  

**Properties**  
- **alignment**: `HorizontalAlignment` (overrides Button's alignment).  
- **toggle_mode**: `bool` (overrides BaseButton's toggle_mode, default true).  

**Theme Properties**  
- **checkbox_checked_color**: `Color` (Color(1,1,1,1)), description: color of checked icon when pressed.  
- **checkbox_checked_texture**: `Texture` (default null), description: texture for checked state.  
- **checkbox_hover_color**: `Color` (default Color(1,1,1,0.2)), description: color for hover state.  
- **checkbox_pressed_color**: `Color` (default Color(1,1,1,0.5)), description: color for pressed state.  
- **checkbox_unchecked_color**: `Color` (default Color(1,1,1,0.2)), description: color for unchecked state.  

**Theme Property Descriptions**  
- **checkbox_checked_color**: Specifies the color of the checkbox when checked.  
- **checkbox_checked_texture**: Sets the texture for the checked state.  
- **checkbox_hover_color**: Determines the color during hover interaction.  
- **checkbox_pressed_color**: Defines the color when the checkbox is pressed.  
- **checkbox_unchecked_color**: Controls the color for the unchecked state.  

**Notes**  
- `toggle_mode` enables/disables state switching (default true).  
- Theme properties allow customization of visual feedback for user interaction.