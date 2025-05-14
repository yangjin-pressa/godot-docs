The `BaseButton` class serves as a foundational implementation for interactive button components, handling mouse input, visual states, and shortcut behavior. Below is a structured summary of its key components and functionality:

---

### **Core Properties**
1. **`button_mask`**  
   - **Type**: Bitfield of mouse buttons (e.g., `MOUSE_BUTTON_MASK_LEFT`, `MOUSE_BUTTON_MASK_RIGHT`).  
   - **Purpose**: Defines which mouse buttons trigger the button's actions.  
   - **Example**: `MOUSE_BUTTON_MASK_LEFT | MOUSE_BUTTON_MASK_RIGHT` allows both left and right clicks.

2. **`button_pressed`**  
   - **Type**: Boolean.  
   - **Purpose**: Indicates whether the button is currently pressed (or toggled if `toggle_mode` is enabled).  
   - **Note**: Setting this directly emits the `toggled` signal unless `set_pressed_no_signal()` is used.

3. **`disabled`**  
   - **Type**: Boolean.  
   - **Purpose**: Prevents interaction (clicking/toggling) if `true`.

4. **`keep_pressed_outside`**  
   - **Type**: Boolean.  
   - **Purpose**: Keeps the button visually pressed even when the mouse moves outside the button area.

5. **`toggle_mode`**  
   - **Type**: Boolean.  
   - **Purpose**: Enables toggle behavior (switching between pressed and unpressed states on click).

6. **`shortcut`**  
   - **Type**: `Shortcut` object.  
   - **Purpose**: Assigns a keyboard shortcut to the button.

7. **`shortcut_feedback`**  
   - **Type**: Boolean.  
   - **Purpose**: Enables visual feedback (e.g., highlighting) when the shortcut is activated.

8. **`shortcut_in_tooltip`**  
   - **Type**: Boolean.  
   - **Purpose**: Adds shortcut information to the button's tooltip.

---

### **Key Methods**
1. **`_pressed()` (virtual)**  
   - **Purpose**: Called when the button is pressed. Subclasses can override this for custom behavior.  
   - **Note**: Use `_toggled()` instead if toggle mode is active.

2. **`_toggled(bool toggled_on)` (virtual)**  
   - **Purpose**: Called when the button is toggled (only if `toggle_mode` is true).  
   - **Note**: Subclasses can override this for toggle-specific logic.

3. **`get_draw_mode()` (const)**  
   - **Purpose**: Returns the visual state (`DrawMode`) for rendering the button.  
   - **Example**: Returns `DRAW_MODE_PRESSED` if the button is pressed.

4. **`is_hovered()` (const)**  
   - **Purpose**: Returns `true` if the mouse is over the button.

5. **`set_pressed_no_signal(bool pressed)`**  
   - **Purpose**: Changes the button's pressed state **without** emitting the `toggled` signal.  
   - **Use Case**: Useful for initializing the button state without triggering events.

---

### **Important Notes**
- **Signal Handling**:  
  - Changing `button_pressed` emits the `toggled` signal. Use `set_pressed_no_signal()` to avoid this.  
  - The `keep_pressed_outside` property affects visual appearance but not signal emission.

- **Shortcut Behavior**:  
  - `shortcut_feedback` controls visual feedback for shortcut activation.  
  - `shortcut_in_tooltip` adds shortcut info to the tooltip (unless the tooltip is customized).

- **Toggle Mode**:  
  - When `toggle_mode` is true, the button flips between pressed and unpressed states on click.  
  - Pressing the button while it's in toggle mode updates `button_pressed`.

---

### **Usage Example**
```cpp
BaseButton* button = new BaseButton();
button->set_toggle_mode(true);  // Enable toggle behavior
button->set_button_mask(MOUSE_BUTTON_MASK_LEFT);  // Respond to left clicks
button->set_shortcut(Shortcut("Ctrl+C"));  // Assign shortcut
button->set_shortcut_feedback(true);  // Show visual feedback
```

---

### **Inheritance and Overrides**
- Subclasses should override `_pressed()` and `_toggled()` to define custom behavior for button interactions.  
- The `get_draw_mode()` method helps determine how to render the button visually based on its state.

This class provides a flexible foundation for buttons that require configurable input handling, visual states, and shortcut functionality.