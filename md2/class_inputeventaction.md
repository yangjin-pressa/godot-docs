**InputEventAction**  
Inherits from: `InputEvent`, `Resource`, `RefCounted`, `Object`

**Description**  
Contains a generic action. Actions are defined in the Input Map tab. This class is not emitted by the engine but is useful for manually emitting actions. To check if a physical event matches an action, use `InputEvent.is_action()` and `InputEvent.is_action_pressed()`.

**Tutorials**  
- [Using InputEvent: Actions](../tutorials/inputs/inputevent.html#actions)  
- [2D Dodge The Creeps Demo](https://example.com/2d-dodge)  
- [3D Voxel Demo](https://example.com/3d-voxel)  

**Properties**  
- **action** (`StringName`)  
  - *Description*: The action name.  
  - *Default*: `""`  
  - *Methods*: `set_action()`, `get_action()`  

- **event_index** (`int`)  
  - *Description*: The index of the event.  
  - *Default*: `0`  
  - *Methods*: `set_event_index()`, `get_event_index()`  

- **pressed** (`bool`)  
  - *Description*: Whether the action is pressed.  
  - *Default*: `false`  
  - *Methods*: `set_pressed()`, `get_pressed()`  

- **strength** (`float`)  
  - *Description*: The strength of the action.  
  - *Default*: `1.0`  
  - *Methods*: `set_strength()`, `get_strength()`  

**Note**  
This class is virtual, meaning it can be overridden in derived classes.  

**Key Concepts**  
- **Virtual Method**: Use `InputEvent.is_action()` and `InputEvent.is_action_pressed()` to determine if a physical event matches an action.  
- **Manual Emission**: The class is designed for manually emitting actions in scenarios where the engine does not handle them.  

**Related Classes**  
- [InputMap](class_InputMap)  
- [InputEvent](class_InputEvent)