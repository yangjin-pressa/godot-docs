# AnimationNodeTimeSeek

**Inherits:** AnimationNode → Resource → RefCounted → Object

A time-seeking animation node used in AnimationTree. It allows seeking to a specific timestamp in an animation graph.

---

## Description

This node can trigger a seek operation on child animations. It can play an animation from the start or a specific timestamp. After setting the time, the node automatically enters sleep mode on the next frame by setting `seek_request` to -1.0.

---

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree)

---

## Properties

- **explicit_elapse**: bool = true  
  If true, processes like root motion and discrete key calculation are performed between seeks.

---

## Method Reference

- `set_explicit_elapse(value: bool)`  
- `is_explicit_elapse()`  

---

## Code Examples

```gdscript
# Play child animation from the start.
animation_tree.set("parameters/TimeSeek/seek_request", 0.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 0.0

# Play child animation from 12 second timestamp.
animation_tree.set("parameters/TimeSeek/seek_request", 12.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 12.0
```

```csharp
// Play child animation from the start.
animationTree.Set("parameters/TimeSeek/seek_request", 0.0);

// Play child animation from 12 second timestamp.
animationTree.Set("parameters/TimeSeek/seek_request", 12.0);
```