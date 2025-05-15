**Class: Shortcut**  
Inherits: `Resource` → `RefCounted` → `Object`  

---

### **Description**  
Shortcuts bind input events (e.g., hotkeys) to actions. A single shortcut can contain multiple `InputEvent` instances, enabling multi-input triggers.  

---

### **Properties**  
- **events**: `Array` (default: `[]`)  
  - Stores `InputEvent` instances. May include `InputEventKey`, `InputEventAction`, etc.  

---

### **Methods**  
- **get_as_text()** → `String` (const)  
  - Returns the first valid `InputEvent` as a string.  

- **has_valid_event()** → `bool` (const)  
  - Checks if `events` contains a valid `InputEvent`.  

- **matches_event(event: `InputEvent`)** → `bool` (const)  
  - Determines if any `InputEvent` in `events` matches the provided `event` (using `InputEvent.is_match()`).  

---

### **Key Notes**  
- Methods are `const` (no side effects) and typically overrideable.  
- `events` can include any `InputEvent` type, not limited to `InputEventKey`.