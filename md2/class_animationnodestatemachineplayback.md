# AnimationNodeStateMachinePlayback

## Inheritance
- `Resource` → `RefCounted` → `Object`

## Description
Controls state machines created with `AnimationNodeStateMachine`. Access via:  
`$AnimationTree.get("parameters/playback")`

## Tutorials
- [Using AnimationTree](../tutorials/animation/animation_tree)

## Properties
- `resource_local_to_scene`: `true` (overrides `Resource` property)

## Methods
- **get_current_length()** → `float`: Returns current state length  
- **get_current_node()** → `StringName`: Returns current animation state  
- **get_current_play_position()** → `float`: Returns playback position in current state  
- **get_fading_from_node()** → `StringName`: Returns starting state of fading animation  
- **get_travel_path()** → `Array<StringName>`: Returns travel path via A\* algorithm  
- **is_playing()** → `bool`: Returns true if animation is playing  
- **next()**: Transitions to next state in travel path  
- **start(node: StringName, reset: bool = true)**: Starts playing specified animation (reset to beginning if `reset` is true)  
- **stop()**: Stops current animation  
- **travel(to_node: StringName, reset_on_teleport: bool = true)**: Transitions to target state via shortest path. If path fails, plays from start. Reset on teleport if specified.

## Notes
- Cross-fade: current state changes immediately after fade begins.  
- Multiple animations may exist within a single state.  
- Fading from node indicates the starting state of a cross-fade.  
- Travel path is computed internally by A\* algorithm.