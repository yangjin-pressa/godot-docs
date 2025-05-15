# XRPositionalTracker

## Description
XRPositionalTracker is a class that represents a tracker for positional data in a 3D space. It is used in conjunction with other classes like XRInterface to provide tracking capabilities in a 3D environment.

## Tutorials
- [XRInterface](https://godotengine.org/documentation/) for tracking interactions.

## Properties
- **hand**: `TrackerHand` = `0`  
  Defines which hand this tracker relates to.
- **profile**: `String` = `""`  
  The profile associated with this tracker, interface dependent but will indicate the type of controller being tracked.

## Methods
- **get_input**(name: `StringName`) → `Variant` |const  
  **Deprecated**: Use through [XRControllerTracker](https://godotengine.org/documentation/).  
  Returns an input for this tracker. It can return a boolean, float, or Vector2 value depending on whether the input is a button, trigger, or thumbstick/thumbpad.

- **get_pose**(name: `StringName`) → `XRPose` |const  
  Returns the current XRPose state object for the bound `name` pose.

- **has_pose**(name: `StringName`) → `bool` |const  
  Returns `true` if the tracker is available and is currently tracking the bound `name` pose.

- **invalidate_pose**(name: `StringName`)  
  Marks this pose as invalid, allowing users to decide if trackers need to be hidden if we lose tracking or remain at their last known position.

- **set_input**(name: `StringName`, value: `Variant`)  
  **Deprecated**: Use through [XRControllerTracker](https://godotengine.org/documentation/).  
  Changes the value for the given input. This method is called by an XRInterface implementation and should not be used directly.

- **set_pose**(name: `StringName`, transform: `Transform3D`, linear_velocity: `Vector3`, angular_velocity: `Vector3`, tracking_confidence: `TrackingConfidence`)  
  Sets the transform, linear velocity, angular velocity, and tracking confidence for the given pose. This method is called by an XRInterface implementation and should not be used directly.

## Signals
- **button_pressed**  
  Emitted when a button is pressed.

- **trigger_pressed**  
  Emitted when a trigger is pressed.

- **thumbstick_pressed**  
  Emitted when a thumbstick is pressed.

## Enumerations
### TrackerHand
- **0**: Hand is not specified.
- **1**: Tracker is for the left hand.
- **2**: Tracker is for the right hand.

## Property Descriptions
- **hand**  
  Type: `TrackerHand`  
  Default: `0`  
  Set/get: `set_tracker_hand`, `get_tracker_hand`  
  Defines which hand this tracker relates to.

- **profile**  
  Type: `String`  
  Default: `""`  
  Set/get: `set_tracker_profile`, `get_tracker_profile`  
  The profile associated with this tracker, interface dependent but will indicate the type of controller being tracked.

## Method Descriptions
- **get_input**  
  **Deprecated**: Use through [XRControllerTracker](https://godotengine.org/documentation/).  
  Returns an input for this tracker. It can return a boolean, float, or Vector2 value depending on whether the input is a button, trigger, or thumbstick/thumbpad.

- **get_pose**  
  Returns the current XRPose state object for the bound `name` pose.

- **has_pose**  
  Returns `true` if the tracker is available and is currently tracking the bound `name` pose.

- **invalidate_pose**  
  Marks this pose as invalid, allowing users to decide if trackers need to be hidden if we lose tracking or remain at their last known position.

- **set_input**  
  **Deprecated**: Use through [XRControllerTracker](https://godotengine.org/documentation/).  
  Changes the value for the given input. This method is called by an XRInterface implementation and should not be used directly.

- **set_pose**  
  Sets the transform, linear velocity, angular velocity, and tracking confidence for the given pose. This method is called by an XRInterface implementation and should not be used directly.