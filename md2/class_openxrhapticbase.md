# OpenXRHapticBase

## Header: OpenXRHapticBase

**Inherits:** Resource < RefCounted < Object

**Inherited By:** OpenXRHapticVibration

## Description

This is a base class for haptic feedback resources.

## Key Features

- Base class for haptic feedback resources
- Inherits from Resource, RefCounted, and Object
- Provides foundation for vibration and haptic functionality
- Contains methods for haptic feedback control

## Class Hierarchy

- **OpenXRHapticBase**
  - Inherits from: Resource
    - Inherits from: RefCounted
      - Inherits from: Object

## Method Definitions

- `void set_vibration_enabled(bool enabled)`: Enables or disables vibration
- `void set_vibration_intensity(float intensity)`: Sets vibration intensity
- `void set_vibration_frequency(float frequency)`: Sets vibration frequency
- `void set_vibration_pattern(Ref<OpenXRHapticPattern> pattern)`: Sets vibration pattern

## Related Classes

- Resource class
- RefCounted class
- Object class
- OpenXRHapticVibration class

## Notes

- This class provides the fundamental interface for haptic feedback systems
- Derived classes implement specific haptic functionality
- Methods should be overridden by subclasses for custom behavior

## References

- Godot engine source code: https://github.com/godotengine/godot/tree/master/modules/openxr/doc_classes/OpenXRHapticBase.xml