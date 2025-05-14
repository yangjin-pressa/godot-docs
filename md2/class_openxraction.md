# OpenXRAction

**Inherits:** Resource ← RefCounted ← Object

## Description
An OpenXR action used for inputs (buttons, joysticks, triggers) and outputs (haptics). Actions are bound to device paths, not individual devices. The resource name registers the action.

## Properties
- **action_type**: ActionType (default: 1)
- **localized_name**: String (default: "")
- **toplevel_paths**: PackedStringArray (default: empty)

## Enumerations
### ActionType
- **OPENXR_ACTION_BOOL** = 0  
  Boolean value
- **OPENXR_ACTION_FLOAT** = 1  
  Float value between 0.0 and 1.0
- **OPENXR_ACTION_VECTOR2** = 2  
  Vector2 value for trackpads/joysticks
- **OPENXR_ACTION_POSE** = 3  
  (No description available)

## Property Descriptions
### action_type
- **set_action_type**(value: ActionType): void
- **get_action_type**(): ActionType
  Type of action (boolean, float, vector2, pose)

### localized_name
- **set_localized_name**(value: String): void
- **get_localized_name**(): String
  Localized description of the action

### toplevel_paths
- **set_toplevel_paths**(value: PackedStringArray): void
- **get_toplevel_paths**(): PackedStringArray
  Paths to devices this action can be bound to
  (Note: Returns a copy; changes to the array do not affect the original)

## Notes
- Action name is used to register with OpenXR
- Use [OpenXR specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-reserved) for path details