The `Input` class in Godot is a core component for handling input from various sources, including keyboards, mice, joypads, and other devices. Below is a structured explanation of its key methods and their purposes:

---

### **1. Device and Sensor Management**
- **`should_ignore_device(vendor_id, product_id)`**  
  Checks if a specific input device (identified by vendor/product ID) should be ignored. This is useful for excluding devices like external controllers or gamepads that might interfere with game logic.

- **`set_gravity(value)`**, **`set_gyroscope(value)`**, **`set_magnetometer(value)`**  
  Allows manual simulation of sensor data (gravity, gyroscope, magnetometer) for debugging on platforms without hardware sensors (e.g., editor). These values are overridden by hardware sensors on Android and iOS.

---

### **2. Vibration and Haptic Feedback**
- **`start_joy_vibration(device, weak_magnitude, strong_magnitude, duration)`**, **`stop_joy_vibration(device)`**  
  Controls rumble effects on joypads. `weak_magnitude` and `strong_magnitude` set the strength of the respective motors, while `duration` defines how long the vibration lasts.

- **`vibrate_handheld(duration_ms, amplitude)`**  
  Triggers a vibration on handheld devices (e.g., smartphones). Requires the `VIBRATE` permission on Android and works on iOS (iOS 13+). On Web, amplitude cannot be adjusted.

---

### **3. Mouse and Cursor Control**
- **`warp_mouse(position)`**  
  Manually sets the mouse position to a specified coordinate. Supported on Windows, macOS, and Linux. Clamped to the window's boundaries if in confined mode.

- **`set_default_cursor_shape(shape)`**  
  Sets the default cursor shape for the viewport. Overrides the default arrow cursor. Triggers an `InputEventMouseMotion` to update the cursor immediately.

- **`set_cursor(file_path)`**  
  Loads a custom cursor image from a file. The image must be in a supported format (e.g., PNG) and size (128x128 max for web). Animated textures are not supported.

---

### **4. Input State Queries**
- **`is_key_pressed(keycode)`**, **`is_key_short_pressed(keycode)`**  
  Checks if a key is currently pressed or was pressed recently. Useful for detecting key states in real-time.

- **`is_mouse_button_pressed(button_index)`**  
  Determines if a specific mouse button (e.g., left, right) is pressed.

- **`is_joystick_connected(joystick_index)`**  
  Checks if a joystick is connected. Helps in identifying available controllers.

- **`is_device_connected(device_index)`**  
  Checks if a specific input device (keyboard, mouse, etc.) is connected.

---

### **5. Device Information**
- **`get_device_type(device_index)`**, **`get_device_name(device_index)`**  
  Retrieves the type and name of a connected input device. Useful for identifying devices in the game.

- **`get_joystick_button(joystick_index, button_index)`**, **`get_joystick_axis(joystick_index, axis_index)`**  
  Gets the current state of a joystick button or axis. Essential for detecting controller input.

---

### **6. Sensor Data Access**
- **`get_mouse_position()`**  
  Returns the current mouse position in screen coordinates.

- **`get_mouse_button_index()`**  
  Returns the index of the currently pressed mouse button (e.g., 0 for left, 1 for right).

---

### **7. Platform-Specific Notes**
- **Vibration**: Supported on Android, iOS, and Web (with limitations). Requires permissions on Android and iOS 13+.
- **Cursor Size**: On Web, maximum cursor size is 128x128. Larger images are restricted for security reasons.
- **Sensor Overrides**: Values set via `set_gravity`, `set_gyroscope`, etc., are overridden by hardware sensors on Android and iOS.

---

### **Usage Example**
```gdscript
# Vibrate a device for 1 second with moderate strength
vibrate_handheld(duration_ms=1000, amplitude=0.5)

# Set a custom cursor
set_cursor("res://custom_cursor.png")

# Check if the right mouse button is pressed
if is_mouse_button_pressed(1):
    print("Right mouse button pressed!")
```

This class is essential for creating responsive and interactive games, allowing developers to handle input from multiple sources seamlessly.