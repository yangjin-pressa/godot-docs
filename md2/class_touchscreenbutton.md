**TouchScreenButton Class**  

**Inheritance**  
- `Node2D`  
  - `CanvasItem`  
    - `Node`  
      - `Object`  

**Description**  
- A touch screen button component that supports multitouch interactions.  
- Different from the `Button` class, it is optimized for touch-based UI.  
- To enable mouse emulation for touch, set `ProjectSettings > Input > Emulate mouse with touch`.  

---

**Properties**  
- **String** `action` = `""`  
  - Action to trigger when the button is pressed.  
- **BitMap** `bitmask`  
  - Bitmask for shape rendering.  
- **bool** `passby_press` = `true`  
  - Whether signals are emitted when a finger passes over the button.  
- **Texture2D** `texture_normal`  
  - Normal state texture.  
- **Texture2D** `texture_pressed`  
  - Pressed state texture.  
- **VisibilityMode** `visibility_mode` = `0`  
  - Controls visibility on different platforms.  

---

**Methods**  
- **bool** `is_pressed()` | `const`  
  - Returns `true` if the button is currently pressed.  

---

**Signals**  
- **pressed**  
  - Emitted when the button is pressed.  
- **released**  
  - Emitted when the button is released.  

---

**Enumerations**  
- **VisibilityMode**  
  - **VISIBILITY_ALWAYS** = `0`  
    - Always visible.  
  - **VISIBILITY_TOUCHSCREEN** = `1`  
    - Visible only on touch devices.  

---

**Property Descriptions**  
- **action**  
  - Set/get method: `set_texture_normal()`, `get_texture_normal()`.  
  - Used with `InputEventAction` for event handling.  
- **passby_press**  
  - Note: "Pass-by" mode affects signal emission when the finger moves over the button.  
- **visibility_mode**  
  - See `VisibilityMode` for possible values (0: always visible, 1: touch-only).  

--- 

**Notes**  
- The `passby_press` property determines if signals are triggered on touch movement.  
- The `visibility_mode` controls platform-specific visibility behavior.