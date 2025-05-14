# InputEventMagnifyGesture

**Inherits:** InputEventGesture < InputEventWithModifiers < InputEventFromWindow < InputEvent < Resource < RefCounted < Object

## Description
Stores the factor of a magnifying touch gesture. This is usually performed when the user pinches the touch screen and used for zooming in/out.

**Note:** On Android, this requires the project setting `project_settings/input_devices/pointing/android/enable_pan_and_scale_gestures` to be enabled.

## Tutorials
- Using InputEvent

## Properties
- factor (float) = 1.0

## Property Descriptions
**factor** (float) = 1.0
The amount (or delta) of the event. This value is closer to 1.0 the slower the gesture is performed.

## Methods
- void set_factor(value: float)
- float get_factor()