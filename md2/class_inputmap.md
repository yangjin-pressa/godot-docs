# InputMap

**Inherits:** Object

## Description
Manages all InputEventAction. Can be created/modified via Project Settings or code. See Node._input().

## Tutorials
- [Using InputEvent: InputMap](../tutorials/inputs/inputevent.html#inputmap)

## Methods
- **action_add_event** (action: StringName, event: InputEvent)  
  Adds an event to an action.

- **action_erase_event** (action: StringName, event: InputEvent)  
  Removes an event from an action.

- **action_erase_events** (action: StringName)  
  Removes all events from an action.

- **action_get_deadzone** (action: StringName) → float  
  Returns deadzone value for an action.

- **action_get_events** (action: StringName) → Array<InputEvent>  
  Returns events associated with an action.  
  **Note:** In the editor, returns editor action events. Use ProjectSettings for project input binds.

- **action_has_event** (action: StringName, event: InputEvent) → bool  
  Checks if an action has a specific event.

- **action_set_deadzone** (action: StringName, deadzone: float)  
  Sets deadzone value for an action.

- **add_action** (action: StringName, deadzone: float)  
  Creates an action with a configurable deadzone.

- **erase_action** (action: StringName)  
  Removes an action from the InputMap.

- **event_is_action** (event: InputEvent, action: StringName, exact_match: bool) → bool  
  Checks if an event is part of an existing action. Ignores modifiers if the event is not pressed.

- **get_action_description** (action: StringName) → String  
  Returns the human-readable description of an action.

- **get_actions** () → Array<StringName>  
  Returns all actions in the InputMap.

- **has_action** (action: StringName) → bool  
  Checks if the InputMap has a registered action.

- **load_from_project_settings** ()  
  Clears all InputEventAction and loads from ProjectSettings.

## Notes
- The `event_is_action` method ignores keyboard modifiers for unpressed events.  
- Use `action_has_event` for exact matching behavior.  
- The `load_from_project_settings` method resets the InputMap to project settings.