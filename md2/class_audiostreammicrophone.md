# AudioStreamMicrophone

**Inherits:** AudioStream < Resource < RefCounted < Object

## Description
Plays real-time audio input data. When used in an AudioStreamPlayer node, it can be combined with AudioEffectCapture for processing or saving.

**Note:** ProjectSettings.audio/driver/enable_input must be set to true for audio input to work. See that setting's description for permissions and OS privacy caveats.

## Tutorials
- Recording with microphone: ../tutorials/audio/recording_with_microphone
- Audio Mic Record Demo: https://github.com/godotengine/godot-demo-projects/tree/master/audio/mic_record

## Key Concepts
- virtual: This method should typically be overridden by the user to have any effect.
- const: This method has no side effects. It doesn't modify any of the instance's member variables.
- vararg: This method accepts any number of arguments after the ones described here.
- constructor: This method is used to construct a type.
- static: This method doesn't need an instance to be called, so it can be called directly using the class name.
- operator: This method describes a valid operator to use with this type as left-hand operand.
- bitfield: This value is an integer composed as a bitmask of the following flags.
- void: No return value.