# OpenXRDpadBindingModifier

## Inheritance
- `OpenXRIPBindingModifier`  
  - `OpenXRBindingModifier`  
    - `Resource`  
      - `RefCounted`  
        - `Object`

## Description
The DPad binding modifier converts an axis input to a dpad output, emulating a DPad. New input paths for each dpad direction are added to the interaction profile. When bound to actions, the DPad emulation is activated. **Do not combine dpad inputs with normal inputs in the same action set** for the same control, as this causes an error when submitting bindings to OpenXR.

[Reference](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_dpad_binding)

## Properties
- **action_set**: `OpenXRActionSet` (default: empty)  
- **center_region**: `float` (default: 0.1)  
- **input_path**: `String` (default: "")  
- **is_sticky**: `bool` (default: false)  
- **off_haptic**: `OpenXRHapticBase`  
- **on_haptic**: `OpenXRHapticBase`  
- **threshold**: `float` (default: 0.6)  
- **threshold_released**: `float` (default: 0.4)  
- **wedge_angle**: `float` (default: 1.5708)  

## Property Descriptions
- **action_set**  
  Action set for which this dpad binding modifier is active.  

- **center_region**  
  Center region in which the dpad's center position returns `true`.  

- **input_path**  
  Input path for this dpad binding modifier.  

- **is_sticky**  
  If `false`, the dpad zone becomes `true` when entering a new zone. If `true`, it remains `true` even if overlapping with another zone.  

- **off_haptic**  
  Haptic pulse emitted when the user releases the input.  

- **on_haptic**  
  Haptic pulse emitted when the user presses the input.  

- **threshold**  
  Input value must be ≥ this value for the dpad in a direction to become `true`. Stays `true` until input falls below `threshold_released`.  

- **threshold_released**  
  Input value must be < this value for the dpad output to become `false`.  

- **wedge_angle**  
  Angle of each wedge identifying the 4 directions of the emulated dpad.