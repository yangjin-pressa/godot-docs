**Class Name**: OpenXRAnalogThresholdModifier  
**Inherits**: OpenXRActionBindingModifier → OpenXRBindingModifier → Resource → RefCounted → Object  

---

### **Description**  
Modifies a float input to a boolean input with specified thresholds.  
See [XR_VALVE_analog_threshold](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VALVE_analog_threshold) for details.  

---

### **Properties**  
- **off_haptic**: OpenXRHapticBase (default: none)  
- **off_threshold**: float (default: 0.4)  
- **on_haptic**: OpenXRHapticBase (default: none)  
- **on_threshold**: float (default: 0.6)  

---

### **Property Descriptions**  
- **off_haptic**  
  - Sets/gets the haptic pulse emitted when the input is released.  

- **off_threshold**  
  - When input value falls below this threshold, output becomes `false`.  

- **on_haptic**  
  - Sets/gets the haptic pulse emitted when the input is pressed.  

- **on_threshold**  
  - When input value is ≥ this threshold, output becomes `true`. Stays `true` until input falls below `off_threshold`.  

---

### **Methods**  
- **set_off_haptic(value: OpenXRHapticBase)**  
  - Sets the haptic pulse for release.  

- **get_off_haptic()**  
  - Retrieves the haptic pulse for release.  

- **set_off_threshold(value: float)**  
  - Sets the threshold for outputting `false`.  

- **get_off_threshold()**  
  - Retrieves the threshold for outputting `false`.  

- **set_on_haptic(value: OpenXRHapticBase)**  
  - Sets the haptic pulse for input pressure.  

- **get_on_haptic()**  
  - Retrieves the haptic pulse for input pressure.  

- **set_on_threshold(value: float)**  
  - Sets the threshold for outputting `true`.  

- **get_on_threshold()**  
  - Retrieves the threshold for outputting `true`.