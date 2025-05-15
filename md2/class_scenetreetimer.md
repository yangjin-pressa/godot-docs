# SceneTreeTimer

**Inherits:** RefCounted < Object

One-shot timer managed by the scene tree. Emits `timeout` signal when complete.

## Description
- Used for one-shot delays
- Automatically dereferenced after time elapses
- Can be kept in reference to persist
- Processes after node methods in current frame
- See: SceneTree.create_timer()

## Properties
- **time_left** (float): Time remaining in seconds
  - Set: set_time_left(value: float)
  - Get: get_time_left()

## Signals
- **timeout** (): Emitted when timer reaches 0

## Notes
- Timer processing order:
  - Node._process() called before timer
  - Physics processing: if process_in_physics is true, Node._physics_process() called before timer

## Related
- [RefCounted](class_RefCounted)
- [SceneTree.create_timer()](class_SceneTree_method_create_timer)
- [Timer](class_Timer)