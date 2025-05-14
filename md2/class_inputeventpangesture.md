**Class: InputEventPanGesture**  
**Inherits:**  
- `InputEventGesture`  
  - `InputEventWithModifiers`  
    - `InputEventFromWindow`  
      - `InputEvent`  
        - `Resource`  
          - `RefCounted`  
            - `Object`  

---

### **Description**  
Stores information about pan gestures. A pan gesture is performed when the user swipes the touch screen with two fingers. Typically used for panning/scrolling.  

**Note:** On Android, requires the project setting `ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures` to be enabled.  

---

### **Tutorials**  
- [Using InputEvent](../tutorials/inputs/inputevent)  

---

### **Properties**  
- **delta**: `Vector2` (default: `Vector2(0, 0)`)  
  - Represents panning amount since last pan event.  

---

### **Methods**  
- `set_delta(value: Vector2): void`  
  - Sets the delta value.  

- `get_delta(): Vector2`  
  - Retrieves the delta value.  

---

### **References**  
- [Android setting documentation](https://godotengine.org/standalone/classes/class_ProjectSettings_property_input_devices_pointing_android_enable_pan_and_scale_gestures)