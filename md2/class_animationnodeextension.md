# AnimationNodeExtension

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** AnimationNode → Resource → RefCounted → Object

Base class for extending AnimationRootNode from GDScript, C#, or C++.

## Description
AnimationNodeExtension exposes the APIs of AnimationRootNode to allow users to extend it from GDScript, C#, or C++. This class is not meant to be used directly, but to be extended by other classes. It is used to create custom nodes for the AnimationTree system.

## Methods

- **_process_animation_node** (playback_info: PackedFloat64Array, test_only: bool) → PackedFloat32Array (virtual)
  - A version of the AnimationNode._process() method meant to be overridden by custom nodes. Returns a PackedFloat32Array with processed animation data.
  - playback_info contains playback time, delta, start and end times, seek status, loop flag, and blend weight.
  - Returns a PackedFloat32Array with animation length, time position, delta, loop mode, end flag, and infinite flag.

- **get_remaining_time** (node_info: PackedFloat32Array, break_loop: bool) → float (static)
  - Returns the animation's remaining time. For looping animations, returns remaining time only if break_loop is true; otherwise returns a large integer.

- **is_looping** (node_info: PackedFloat32Array) → bool (static)
  - Returns true if the animation for the given node_info is looping.

## Inheritance Hierarchy
- AnimationNodeExtension
  - AnimationNode
    - Resource
      - RefCounted
        - Object

## Key Attributes
- **Experimental**: May be changed or removed in future versions.
- **Extends**: AnimationRootNode for custom node creation in AnimationTree.
- **Usage**: Extend this class to create custom animation nodes in GDScript, C#, or C++.