# AudioListener3D

**Inherits:** Node3D < Node < Object

Overrides the location sounds are heard from.

## Description

Once added to the scene tree and enabled using `make_current()`, this node will override the location sounds are heard from. This can be used to listen from a location different from the Camera3D.

## Methods

- **clear_current()**: Disables the listener to use the current camera's listener instead.
- **get_listener_transform()** → Transform3D: Returns the listener's global orthonormalized Transform3D.
- **is_current()** → bool: Returns `true` if the listener was made current using `make_current()`, `false` otherwise.
- **make_current()**: Enables the listener. This will override the current camera's listener.

**Note:** There may be more than one AudioListener3D marked as "current" in the scene tree, but only the one that was made current last will be used.