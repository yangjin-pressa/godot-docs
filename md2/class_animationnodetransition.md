# AnimationNodeTransition

**Inherits:** AnimationNodeSync < AnimationNode < Resource < RefCounted < Object

A transition within an AnimationTree connecting two AnimationNode instances.

## Description
Simple state machine for cases which don't require a more advanced AnimationNodeStateMachine. Animations can be connected to the inputs and transition times can be specified.

After setting the request and changing the animation playback, the transition node automatically clears the request on the next process frame by setting its transition_request value to empty.

Note: When using a cross-fade, current_state and current_index change to the next state immediately after the cross-fade begins.

```gdscript
# Play child animation connected to "state_2" port.
animation_tree.set("parameters/Transition/transition_request", "state_2")
# Alternative syntax (same result as above).
animation_tree["parameters/Transition/transition_request"] = "state_2"
```

```gdscript
# Get current state name (read-only).
animation_tree.get("parameters/Transition/current_state")
# Alternative syntax (same result as above).
animation_tree["parameters/Transition/current_state"]
```

```gdscript
# Get current state index (read-only).
animation_tree.get("parameters/Transition/current_index")
# Alternative syntax (same result as above).
animation_tree["parameters/Transition/current_index"]
```

```csharp
// Play child animation connected to "state_2" port.
animationTree.Set("parameters/Transition/transition_request", "state_2");
```

```csharp
// Get current state name (read-only).
animationTree.Get("parameters/Transition/current_state");
```

```csharp
// Get current state index (read-only).
animationTree.Get("parameters/Transition/current_index");
```

## Tutorials
- Using AnimationTree
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties
- bool allow_transition_to_self = false
- int input_count = 0
- Curve xfade_curve
- float xfade_time = 0.0

## Methods
- bool is_input_loop_broken_at_end(input: int)
- bool is_input_reset(input: int)
- bool is_input_set_as_auto_advance(input: int)
- void set_input_as_auto_advance(input: int, enable: bool)
- void set_input_break_loop_at_end(input: int, enable: bool)
- void set_input_reset(input: int, enable: bool)

## Property Descriptions
**allow_transition_to_self** (bool)
- set_allow_transition_to_self(value: bool)
- is_allow_transition_to_self()

If true, allows transition to the self state. When the reset option is enabled in input, the animation is restarted. If false, nothing happens on the transition to the self state.

**input_count** (int)
- set_input_count(value: int)
- get_input_count()

The number of enabled input ports for this animation node.

**xfade_curve** (Curve)
- No default value.

**xfade_time** (float)
- Default value: 0.0

## Method Descriptions
**is_input_loop_broken_at_end(input: int)** (const)
- Returns whether the animation breaks the loop at the end of the loop cycle for transition.

**is_input_reset(input: int)** (const)
- Returns whether the animation restarts when the animation transitions from the other animation.

**is_input_set_as_auto_advance(input: int)** (const)
- Returns true if auto-advance is enabled for the given input index.

**set_input_as_auto_advance(input: int, enable: bool)**
- Enables or disables auto-advance for the given input index. If enabled, state changes to the next input after playing the animation once. If enabled for the last input state, it loops to the first.

**set_input_break_loop_at_end(input: int, enable: bool)**
- If true, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.

**set_input_reset(input: int, enable: bool)**
- If true, the destination animation is restarted when the animation transitions.