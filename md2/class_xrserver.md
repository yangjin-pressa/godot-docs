The `XRServer` class in Godot is essential for managing spatial tracking and interface registration in AR/VR applications. Below is a structured overview of its key components, usage, and best practices:

---

### **Key Properties**
1. **`world_origin`**  
   - **Type**: `Transform3D`  
   - **Description**: The origin of the tracking space in the virtual world. This is managed by the `XROrigin3D` node and is critical for aligning the game world with real-world coordinates.  

2. **`world_scale`**  
   - **Type**: `float`  
   - **Description**: Scales the game world relative to the real world. Defaults to 1.0, where 1 game unit = 1 meter. Adjust this if your platform uses different units.

---

### **Signals**
- **`on_reference_frame_changed`**  
  - **Triggered**: When the reference frame (from `center_on_hmd`) is updated.  
  - **Usage**: Connect to this signal to update game logic or UI when the tracking alignment changes.

---

### **Methods**
1. **`add_interface(interface: XRInterface)`**  
   - **Purpose**: Register an `XRInterface` (e.g., AR/VR platform support).  
   - **Usage**: Use this to initialize platforms like OpenVR or Android AR.

2. **`remove_interface(interface: XRInterface)`**  
   - **Purpose**: Remove an interface.  
   - **Usage**: Unregister platforms when they are no longer needed.

3. **`center_on_hmd(rotation_mode: RotationMode, keep_height: bool)`**  
   - **Purpose**: Align the tracking origin to the HMD's current position and orientation.  
   - **Important**: Call this after the game has stabilized (e.g., after a few seconds) to ensure accurate tracking.  
   - **Parameters**:  
     - `rotation_mode`: Use `RotationMode` to control alignment (e.g., `RotationMode.ALIGN_TO_HMD`).  
     - `keep_height`: Maintain vertical position relative to the HMD.

4. **`clear_reference_frame()`**  
   - **Purpose**: Reset the reference frame set by `center_on_hmd`.  
   - **Usage**: Realign tracking after recalibration or if drift is detected.

5. **`get_hmd_transform()`**  
   - **Purpose**: Retrieve the HMD's transformation (position and orientation).  
   - **Usage**: Use this to track the HMD's position in the virtual world.

6. **`get_reference_frame()`**  
   - **Purpose**: Return the current reference frame transform (internal use).  
   - **Usage**: Exposed for GDExtension integration.

7. **`get_interfaces()`**  
   - **Purpose**: Return a list of available interfaces (e.g., platform-specific capabilities).  
   - **Usage**: Check for supported platforms before initializing.

8. **`get_tracker(tracker_name: StringName)`**  
   - **Purpose**: Retrieve a tracker by name.  
   - **Usage**: Access specific spatial trackers (e.g., for physical objects).

9. **`get_trackers(tracker_types: int)`**  
   - **Purpose**: Return a dictionary of trackers for specific types (e.g., `TrackerType.POSITIONAL`).  
   - **Usage**: Filter trackers by type for custom logic.

---

### **Best Practices**
1. **Initialize Interfaces**:  
   - Use `get_interfaces()` to check for available platforms (e.g., OpenVR, Android AR).  
   - Initialize the first compatible interface for your project.

2. **Track Calibration**:  
   - Call `center_on_hmd()` after the game has stabilized (e.g., after 2-3 seconds).  
   - Use `clear_reference_frame()` if recalibration is needed.

3. **Trackers Management**:  
   - Register trackers with `add_tracker()` for physical objects (e.g., AR anchors).  
   - Ensure trackers are properly removed when no longer needed.

4. **World Alignment**:  
   - Adjust `world_scale` based on the platform's real-world units.  
   - Use `world_origin` to fine-tune the tracking origin if needed.

5. **Signal Handling**:  
   - Connect to `on_reference_frame_changed` to update game logic when the tracking reference frame changes.

---

### **Example Usage**
```gdscript
# Check available interfaces
var interfaces = get_interfaces()
for interface in interfaces:
    if interface.name == "OpenVR":
        # Initialize OpenVR interface
        var openvr = interface
        break

# Add a positional tracker
var tracker = XRTracker.new()
tracker.name = "MyTracker"
add_tracker(tracker)

# Center tracking on HMD
center_on_hmd(RotationMode.ALIGN_TO_HMD, true)

# Connect to reference frame change signal
connect("on_reference_frame_changed", self, "_onReferenceFrameChanged")

# Callback for reference frame change
func _onReferenceFrameChanged():
    var new_frame = get_reference_frame()
    print("New reference frame:", new_frame)
```

---

### **Notes**
- The `XRServer` is tightly integrated with `XROrigin3D`, which handles the world origin and scale.  
- Ensure that your project's tracking system is properly configured for the target platform (e.g., OpenXR, VrView, etc.).  
- Test calibration and tracking stability in different environments to avoid drift or misalignment.  

By leveraging these methods and properties, developers can create robust AR/VR applications that accurately map the real world to the virtual environment.