**InputEventKey Class**  
*Inherits from:* InputEvent → InputEventWithModifiers  

---

### **Overview**  
Represents a keyboard input event with modifier keys. Used to track key presses, releases, and modifiers like Shift, Alt, etc. Key properties include the physical keyboard location, location, and Unicode character.  

---

### **Key Features**  
- **Event Comparison Priority**: Properties are compared in the order: `unicode`, `physical_keycode`, `keycode`, `location`.  
- **Modifier Support**: Combines base key with modifier keys (e.g., Shift + A).  
- **Unicode Handling**: Unicode values are adjusted for modifiers (e.g., Shift + 'a' → 'A').  

---

### **Properties**  

| Property           | Type    | Default | Description                                                                 |
|-------------------|---------|---------|-----------------------------------------------------------------------------|
| `unicode`         | `int`   | `0`     | Unicode character code (shifted by modifiers).                            |
| `pressed`         | `bool`  | `false` | Indicates if the key is pressed (`true`) or released (`false`).            |
| `location`        | `KeyLocation` | `0` | Key location (e.g., left/ right Shift, Alt).                               |
| `physical_keycode`| `Key`   | `0`     | Physical keyboard position (e.g., US QWERTY layout).                      |
| `keycode`         | `Key`   | `0`     | Logical key (e.g., 'A', 'Shift').                                          |
| `key_label`       | `String`| `""`    | Localized key label (e.g., "A", "Shift").                                 |

---

### **Methods**  

- **`as_text_key_label()`**  
  Returns a string representation of `key_label` and modifiers.  

- **`as_text_keycode()`**  
  Returns a string representation of `keycode` and modifiers.  

- **`as_text_location()`**  
  Returns a string for `location` (e.g., "Left", "Right"). Returns empty if unspecified.  

- **`as_text_physical_keycode()`**  
  Returns a string for `physical_keycode` and modifiers.  

- **`get_key_label_with_modifiers()`**  
  Returns localized key label with modifiers (e.g., "Shift + A").  

- **`get_keycode_with_modifiers()`**  
  Returns logical key with modifiers (e.g., "A" with Shift).  

- **`get_physical_keycode_with_modifiers()`**  
  Returns physical key with modifiers (e.g., "Left Shift + A").  

---

### **Code Example**  
To map `physical_keycode` to a human-readable name:  

```gdscript
# GDScript
func _input(event):
    if event is InputEventKey:
        var keycode = DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
        print(OS.get_keycode_string(keycode))
```

```csharp
public override void _Input(InputEvent @event)
{
    if (@event is InputEventKey inputEventKey)
    {
        var keycode = DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
        GD.Print(OS.GetKeycodeString(keycode));
    }
}
```

---

### **Notes**  
- **Unicode Limitations**: Unicode values may not represent complex scripts unless IME is active.  
- **Modifier Behavior**: Methods like `get_key_label_with_modifiers()` combine base key and modifiers (e.g., Shift + A → "Shift + A").  

--- 

This class is essential for handling keyboard input with modifiers in Godot, enabling precise key state tracking and user input analysis.