# Godot WebXRInterface Guide

This guide explains how to use the `WebXRInterface` in Godot to handle WebXR (WebXR 1.1) features like VR/AR sessions, input tracking, and display settings.

## Overview

The `WebXRInterface` is a Godot class that provides access to WebXR features via the WebXR API. It's used for:

- Starting/ending WebXR sessions
- Handling input devices (controllers, touchscreens)
- Managing display settings
- Tracking user interactions

## Properties

### session_mode
```gdscript
var session_mode: String
```
- **Description**: Current session mode (e.g., "immersive-vr", "immersive-ar", "inline")
- **Set**: Use `set_session_mode()` to change the session mode
- **Get**: Use `get_session_mode()`

### required_features
```gdscript
var required_features: String
```
- **Description**: Comma-separated list of required features (e.g., "hand-tracking", "pose-tracking")
- **Set**: Use `set_required_features()` to specify required features
- **Get**: Use `get_required_features()`

### visibility_state
```gdscript
var visibility_state: String
```
- **Description**: Current visibility state of the WebXR session (e.g., "visible", "hidden")
- **Get**: Use `get_visibility_state()`

## Methods

### is_session_supported(session_mode: String)
```gdscript
func is_session_supported(session_mode: String):
    # Checks if a session mode is supported
    # Emits session_supported signal with result
```
- **Usage**: 
```gdscript
webxr.interface.is_session_supported("immersive-vr")
```

### get_input_source_tracker(input_source_id: int) → XRControllerTracker
```gdscript
func get_input_source_tracker(input_source_id: int):
    # Returns tracker for a specific input source
```
- **Usage**: 
```gdscript
var tracker = webxr.interface.get_input_source_tracker(0)
```

### get_input_source_target_ray_mode(input_source_id: int) → TargetRayMode
```gdscript
func get_input_source_target_ray_mode(input_source_id: int):
    # Returns target ray mode for input source
```
- **Usage**: 
```gdscript
var mode = webxr.interface.get_input_source_target_ray_mode(0)
```

### set_display_refresh_rate(refresh_rate: float)
```gdscript
func set_display_refresh_rate(refresh_rate: float):
    # Sets display refresh rate for HMD
```
- **Usage**: 
```gdscript
webxr.interface.set_display_refresh_rate(120)
```

## Signals

### session_started()
- **Description**: Emitted when WebXR session starts
- **Connection**: 
```gdscript
webxr.connect("session_started", self, "_on_session_started")
```

### session_stopped()
- **Description**: Emitted when WebXR session stops
- **Connection**: 
```gdscript
webxr.connect("session_stopped", self, "_on_session_stopped")
```

### display_refresh_rate_changed(refresh_rate: float)
- **Description**: Emitted when display refresh rate changes
- **Connection**: 
```gdscript
webxr.connect("display_refresh_rate_changed", self, "_on_refresh_rate_changed")
```

### input_source_changed(input_source_id: int)
- **Description**: Emitted when input source changes
- **Connection**: 
```gdscript
webxr.connect("input_source_changed", self, "_on_input_source_changed")
```

## Enum: TargetRayMode

```gdscript
enum TargetRayMode:
    "directional"
    "position"
    "projected"
```

## Example Usage

### 1. Check Session Support
```gdscript
func _ready():
    var webxr = WebXRInterface.new()
    webxr.is_session_supported("immersive-vr")
```

### 2. Handle Input Events
```gdscript
func _ready():
    var webxr = WebXRInterface.new()
    webxr.connect("select", self, "_on_select")
    webxr.connect("squeeze", self, "_on_squeeze")

func _on_select():
    print("Select event detected!")

func _on_squeeze():
    print("Squeeze event detected!")
```

### 3. Set Display Refresh Rate
```gdscript
func _ready():
    var webxr = WebXRInterface.new()
    webxr.set_display_refresh_rate(120)
```

## Tips

1. **Initialization**: Ensure the WebXR plugin is enabled in your Godot project settings.
2. **Session Mode**: Use "immersive-vr" for VR, "immersive-ar" for AR, and "inline" for 2D.
3. **Input Handling**: Use the `get_input_source_tracker()` method to get controller positions/orientations.
4. **Display Settings**: Use `get_display_refresh_rate()` to check current refresh rate.
5. **Platform Notes**: WebXR support varies by browser and device. Test on supported platforms.

## Notes

- The WebXRInterface is primarily used on platforms with WebXR support (e.g., Android, iOS, desktop).
- For VR, ensure the scene is properly set up with a perspective camera and 3D objects.
- Use the `XRPositionalTracker` and `XRControllerTracker` for accurate input tracking.
- Always handle the "session_stopped" signal to clean up resources when the session ends.

This guide provides a foundation for using WebXR in Godot. For advanced features, refer to the Godot WebXR documentation and browser-specific WebXR APIs.