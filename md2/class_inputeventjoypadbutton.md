**Class Name**: InputEventJoypadButton  
**Inherits**: InputEvent → Resource → RefCounted → Object  

---

### Description  
Represents a gamepad button being pressed or released.  
For analog sticks and joysticks, see `InputEventJoypadMotion`.  

---

### Tutorials  
- [Using InputEvent](../tutorials/inputs/inputevent)  

---

### Properties  
- **button_index**: `JoyButton` = `0`  
  - Button identifier (one of `JoyButton` constants).  
  - Methods: `set_button_index()`, `get_button_index()`.  

- **pressed**: `bool` = `false`  
  - Indicates if the button is pressed (`true`) or released (`false`).  
  - Methods: `set_pressed()`, `is_pressed()`.  

- **pressure**: `float` = `0.0`  
  - **Deprecated**: Never set by the engine; always `0`.  
  - Methods: `set_pressure()`, `get_pressure()`.  

---

### Notes  
- `pressure` is deprecated and unused.  
- This class is part of Godot's input system for gamepad interactions.