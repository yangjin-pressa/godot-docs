# InputEventMIDI

**Inherits:** InputEvent < Resource < RefCounted < Object

Represents a MIDI message from a MIDI device, such as a musical keyboard.

## Description

Stores information about messages from MIDI devices. These may include musical keyboards, synthesizers, and drum machines.

MIDI messages can be received over a 5-pin MIDI connector or USB. Godot does not detect MIDI devices by default. Use OS.open_midi_inputs() to enable detection.

Example:
```gdscript
func _ready():
    OS.open_midi_inputs()
    print(OS.get_connected_midi_inputs())

func _input(input_event):
    if input_event is InputEventMIDI:
        _print_midi_info(input_event)

func _print_midi_info(midi_event):
    print(midi_event)
    print("Channel ", midi_event.channel)
    print("Message ", midi_event.message)
    print("Pitch ", midi_event.pitch)
    print("Velocity ", midi_event.velocity)
    print("Pressure ", midi_event.pressure)
    print("Instrument ", midi_event.instrument)
```

## Tutorials
- [MIDI message status byte list](https://www.midi.org/specifications-old/item/table-2-expanded-messages-list-status-bytes)
- [General MIDI instrument list](https://en.wikipedia.org/wiki/General_MIDI#Program_change_events)
- [Piano key frequency chart](https://en.wikipedia.org/wiki/Piano_key_frequencies)

## Properties

- **channel**: int (0-15) - MIDI channel number
- **message**: MIDIMessage (0-127) - Type of MIDI message
- **pitch**: int (0-127) - Pitch index number
- **velocity**: int (0-127) - Note velocity
- **pressure**: int (0-127) - Key pressure
- **instrument**: int (0-127) - Instrument number

## Property Details

- **channel**
  - 0-15 MIDI channel number
  - Channel 9 is reserved for percussion instruments

- **message**
  - Enum values: 
    - 0 = Note Off
    - 1 = Note On
    - 2 = Polyphonic Key Pressure
    - 3 = Control Change
    - 4 = Program Change
    - 5 = Aftertouch
    - 6 = Pitch Bend

- **pitch**
  - 0-127 MIDI note number
  - Middle C = 60
  - Octaves are spaced 12 apart

- **velocity**
  - 0-127 note velocity
  - Typically 0-110 for musical keyboards

- **pressure**
  - 0-127 key pressure
  - Some devices use velocity instead

- **instrument**
  - 0-127 instrument number
  - 0 = Acoustic Grand Piano
  - List is offset by 1 (no 0 index)

## Notes
- MIDI output is not supported
- Web platform requires browser permission for MIDI access
- Note ON with 0 velocity can be treated as Note OFF
```gdscript
if event.message == MIDI_MESSAGE_NOTE_ON and event.velocity > 0:
    print("Note pressed!")
```