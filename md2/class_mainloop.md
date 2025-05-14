# MainLoop

## Overview
Abstract base class for Godot projects' game loop. Inherited by SceneTree, which is the default implementation. A MainLoop must be provided to the OS at startup, or the application exits.

---

## Key Features

- **Inherits**: Object
- **Inherited By**: SceneTree
- **Default Implementation**: SceneTree
- **Custom Usage**: Can be replaced with a custom MainLoop subclass via command line or project settings

---

## Methods

- **_initialize()**: Called during initialization
- **_finalize()**: Called before program exit
- **_physics_process(delta)**: Physics frame processing
- **_process(delta)**: Process frame processing

---

## Signals

- **on_request_permissions_result(permission, granted)**: Emitted when user responds to permission requests

---

## Constants

- **NOTIFICATION_OS_MEMORY_WARNING** = 2009: Memory warning notification (iOS)
- **NOTIFICATION_TRANSLATION_CHANGED** = 2010: Translation change notification
- **NOTIFICATION_WM_ABOUT** = 2011: About information request (macOS)
- **NOTIFICATION_CRASH** = 2012: Crash warning (desktop platforms)
- **NOTIFICATION_OS_IME_UPDATE** = 2013: IME update notification (macOS)
- **NOTIFICATION_APPLICATION_RESUMED** = 2014: App resumed
- **NOTIFICATION_APPLICATION_PAUSED** = 2015: App paused
- **NOTIFICATION_APPLICATION_FOCUS_IN** = 2016: App focus in
- **NOTIFICATION_APPLICATION_FOCUS_OUT** = 2017: App focus out
- **NOTIFICATION_TEXT_SERVER_CHANGED** = 2018: Text server change

---

## Method Descriptions

- **_finalize()**: Cleanup operations before program exit
- **_initialize()**: Initialization setup
- **_physics_process(delta)**: Physics frame logic (returns true to end loop)
- **_process(delta)**: Main game logic (returns true to end loop)

---

## Example Implementation

### GDScript
```gdscript
class_name CustomMainLoop
extends MainLoop

var time_elapsed = 0

func _initialize():
    print("Initialized:")
    print("  Starting time: %s" % str(time_elapsed))

func _process(delta):
    time_elapsed += delta
    return Input.get_mouse_button_mask() != 0 || Input.is_key_pressed(KEY_ESCAPE)
```

### C#
```csharp
using Godot;

[GlobalClass]
public partial class CustomMainLoop : MainLoop
{
    private double _timeElapsed = 0;

    public override void _Initialize()
    {
        GD.Print("Initialized:");
        GD.Print("  Starting time: %s", _timeElapsed);
    }

    public override bool _Process(float delta)
    {
        _timeElapsed += delta;
        return Input.GetMouseButtonDown() || Input.IsKeyPressed(KEY_ESCAPE);
    }
}
```

---

## Important Notes

- **Delta Handling**: Avoid using delta for real-time measurements; use Time singleton instead.
- **Performance**: Delta may be inaccurate at lower frame rates.
- **Platform Specifics**: Constants like OS_MEMORY_WARNING are platform-specific.