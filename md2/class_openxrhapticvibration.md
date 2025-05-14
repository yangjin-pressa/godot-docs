# OpenXRHapticVibration

**Inherits:** `OpenXRHapticBase < Resource < RefCounted < Object`

Vibration haptic feedback.

## Description
This haptic feedback resource defines a vibration-based pulse triggered via OpenXR action maps.

## Properties
- **amplitude**: `float` (default: `1.0`)  
- **duration**: `int` (default: `-1`)  
- **frequency**: `float` (default: `0.0`)  

## Property Descriptions

### amplitude
- **Type**: `float`  
- **Default**: `1.0`  
- **Range**: `0.0` to `1.0`  
- **Methods**:  
  - `set_amplitude(value: float)`  
  - `get_amplitude()`

### duration
- **Type**: `int`  
- **Default**: `-1`  
- **Description**: Pulse duration in nanoseconds. `-1` uses runtime default.  
- **Methods**:  
  - `set_duration(value: int)`  
  - `get_duration()`

### frequency
- **Type**: `float`  
- **Default**: `0.0`  
- **Description**: Pulse frequency in Hz. `0.0` lets the runtime choose.  
- **Methods**:  
  - `set_frequency(value: float)`  
  - `get_frequency()`