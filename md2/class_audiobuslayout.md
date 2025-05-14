# AudioBusLayout

**Inherits:** Resource < RefCounted < Object

## Description
Stores position, muting, solo, bypass, effects, effect position, volume, and connections between buses. See AudioServer for usage.

## Properties
- **bus**: int - Index of the bus (0-based). Values: 0 to maximum bus count.
- **mute**: bool - Mute state (true/false).
- **solo**: bool - Solo state (true/false).
- **bypass**: bool - Bypass state (true/false).
- **volume**: float - Volume (0.0 to 1.0).
- **effect_volume**: float - Effect volume (0.0 to 1.0).
- **effect_bus**: int - Effect bus index (0-based).
- **effect_position**: int - Effect position (0 to maximum effect count).

## Methods
- **set_bus(int bus)**: Sets the bus index.
- **get_bus()**: Gets the current bus index.
- **set_mute(bool mute)**: Mutes the bus.
- **get_mute()**: Gets mute state.
- **set_solo(bool solo)**: Sets solo state.
- **get_solo()**: Gets solo state.
- **set_bypass(bool bypass)**: Sets bypass state.
- **get_bypass()**: Gets bypass state.
- **set_volume(float volume)**: Sets volume.
- **get_volume()**: Gets volume.
- **set_effect_volume(float volume)**: Sets effect volume.
- **get_effect_volume()**: Gets effect volume.
- **set_effect_bus(int bus)**: Sets effect bus.
- **get_effect_bus()**: Gets effect bus.
- **set_effect_position(int position)**: Sets effect position.
- **get_effect_position()**: Gets effect position.

## Constants
- **MAX_BUSES**: int - Maximum number of buses (32).
- **MAX_EFFECTS**: int - Maximum number of effects (32).

## Operators
- **==**: Compares two AudioBusLayout instances.
- **!=**: Compares for inequality.

## Bitfields
- **FLAGS**: Bitfield - Flags for advanced configurations. Values: 
  - `FLAG_DISABLED` (0x01)
  - `FLAG_ACTIVE` (0x02)
  - `FLAG_PAN` (0x04)