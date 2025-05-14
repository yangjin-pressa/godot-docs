# AudioServer Class Documentation

## Overview
The `AudioServer` class manages audio buses, effects, and other audio-related operations in a Godot project. It provides methods to control audio parameters, apply effects, manage bus layouts, and interact with the audio driver.

---

## Key Methods

### Buses Management
- **`add_bus`**  
  Adds a new audio bus to the list.  
  **Parameters**:  
  - `bus_layout`: `AudioBusLayout` – The layout of the new bus.  
  - `name`: `String` – The name of the new bus.  

- **`remove_bus`**  
  Removes a bus by its index.  
  **Parameters**:  
  - `index`: `int` – Index of the bus to remove.  

- **`move_bus`**  
  Moves a bus from one index to another.  
  **Parameters**:  
  - `index`: `int` – Current index of the bus.  
  - `to_index`: `int` – Target index for the bus.  

- **`set_bus_name`**  
  Sets the name of a bus.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `name`: `String` – New name for the bus.  

- **`set_bus_mute`**  
  Mutes or unmutes a bus.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `enable`: `bool` – `true` to mute, `false` to unmute.  

- **`set_bus_solo`**  
  Sets a bus to solo mode.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `enable`: `bool` – `true` to enable solo mode.  

- **`set_bus_volume_db`**  
  Sets the volume of a bus in decibels.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `volume_db`: `float` – Volume in decibels.  

- **`set_bus_volume_linear`**  
  Sets the volume of a bus as a linear value.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `volume_linear`: `float` – Volume as a linear value.  
  **Note**: Equivalent to converting the linear value to decibels and using `set_bus_volume_db`.

- **`set_bus_layout`**  
  Sets the layout for all buses.  
  **Parameters**:  
  - `bus_layout`: `AudioBusLayout` – New layout configuration.  

---

### Effects Management
- **`add_bus_effect`**  
  Adds an effect to a bus.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `effect`: `AudioEffect` – Effect to add.  

- **`remove_bus_effect`**  
  Removes an effect from a bus.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `effect_idx`: `int` – Index of the effect to remove.  

- **`set_bus_effect_enabled`**  
  Enables or disables an effect on a bus.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `effect_idx`: `int` – Index of the effect.  
  - `enabled`: `bool` – `true` to enable, `false` to disable.  

- **`swap_bus_effects`**  
  Swaps two effects in a bus.  
  **Parameters**:  
  - `bus_idx`: `int` – Index of the bus.  
  - `effect_idx`: `int` – Index of the first effect.  
  - `by_effect_idx`: `int` – Index of the second effect.  

---

### Audio Driver Control
- **`lock`**  
  Locks the audio driver's main loop.  
  **Note**: Must be followed by a call to `unlock()`.  

- **`unlock`**  
  Unlocks the audio driver's main loop.  

---

### Stream Registration
- **`register_stream_as_sample`**  
  Registers a stream as a sample to avoid re-registration.  
  **Note**: May cause lag spikes; best used during asset loading.  

- **`set_enable_tagging_used_audio_streams`**  
  Enables or disables tagging of used audio streams.  
  **Note**: Enabled by default in the editor for previews.  

---

### Important Notes
- **Experimental Methods**:  
  Methods like `register_stream_as_sample` and `set_enable_tagging_used_audio_streams` may change in future versions.  

- **Index Management**:  
  Indices in methods like `move_bus` and `remove_bus` are based on the current list of buses.  

- **Layout Overwrite**:  
  `set_bus_layout` replaces the current layout configuration.  

- **Locking**:  
  Always `unlock()` after calling `lock()` to avoid blocking the audio driver.  

---

## Example Usage
```gdscript
# Example: Set bus volume in decibels
audio_server.set_bus_volume_db(0, -12.0)

# Example: Swap two effects in a bus
audio_server.swap_bus_effects(0, 0, 1)

# Example: Lock and unlock audio driver
audio_server.lock()
# ... perform operations ...
audio_server.unlock()
```

This documentation provides a comprehensive guide to using the `AudioServer` class in Godot for managing audio buses, effects, and driver interactions.