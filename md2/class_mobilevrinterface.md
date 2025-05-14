# MobileVRInterface

## Inheritance
- `XRInterface` ← `RefCounted` ← `Object`

## Description
A generic mobile VR implementation requiring phone and VR headset specifications. Key features include:
- Eye height default of 1.85 meters
- Sensor requirements for Android (accelerometer, gravity, etc.)
- Support for VRS (View-Dependent Rendering)

## Properties

### Type: `float`
- **oversample** (default: 1.5)  
  Controls rendering resolution. Values between 1.5-2.0 balance quality and performance.

### Type: `float`
- **vrs_strength** (default: 1.0)  
  Determines VRS density map intensity. Higher values increase VRS visibility.

### Type: `float`
- **vrs_min_radius** (default: 20.0)  
  Minimum radius for full-quality rendering when using VRS. Requires specific viewport settings.

### Type: `Rect2`
- **offset_rect** (default: (0,0,1,1))  
  Defines rendering area offset. Value 1 represents full screen size.

### Type: `float`
- **eye_height** (default: 1.85)  
  Sets the vertical position for VR headsets. Adjustable for user comfort.

### Type: `float`
- **zoom** (default: 1.0)  
  Controls field of view scaling. Adjusts how much of the scene is visible.

### Type: `bool`
- **vrs_enabled** (default: false)  
  Enables/disables View-Dependent Rendering. Requires specific viewport configuration.

## Notes
- **Sensor Enablement (Android)**:  
  `ProjectSettings.input_devices/sensors/enable_accelerometer`, `ProjectSettings.input_devices/sensors/enable_gravity`, etc., must be enabled for proper functionality.

- **VRS Requirements**:  
  Mobile and Forward+ renderers only. Requires `Viewport.vrs_mode` set to `Viewport.VRS_XR`.

- **Performance Considerations**:  
  Higher oversample or VRS strength values may impact performance, especially on mobile devices.