# Performance Class in Godot

The `Performance` class in Godot provides tools for monitoring and tracking performance metrics, both built-in and custom. It allows developers to track things like frame rate, memory usage, and custom metrics defined by the user.

---

## **Built-in Monitors**

Godot provides several built-in performance metrics, which can be accessed using the `Monitor` enum. These include:

- **TIME_FPS**: Current frame rate (FPS).
- **MEMORY_USAGE**: Memory usage in bytes.
- **MEMORY_ALLOCS**: Number of memory allocations.
- **MEMORY_ALLOCS_BYTES**: Total bytes allocated.
- **MEMORY_MALLOC_BYTES**: Bytes allocated via `malloc`.
- **MEMORY_STACK_BYTES**: Bytes used by the stack.
- **MEMORY_HEAP_BYTES**: Bytes used by the heap.
- **TIME_PROCESSING**: Time spent processing the scene.
- **TIME_PHYSICS**: Time spent in physics simulation.
- **TIME_SIGNALS**: Time spent in signal emission.
- **TIME_IDLE**: Time spent in idle state.
- **TIME_SCRIPTS**: Time spent in script execution.
- **TIME_DRAW**: Time spent in rendering.
- **TIME_OTHER**: Other time spent.
- **TIME_TOTAL**: Total time since game start.
- **TIME_LAST**: Time of the last frame.
- **MEMORY_LIVE`: Number of live objects.
- **MEMORY_ALLOCATED**: Total allocated memory.
- **MEMORY_RELEASED**: Total released memory.
- **MEMORY_FRAGMENTED**: Memory fragmentation percentage.
- **MEMORY_MAX**: Maximum memory used.
- **MONITOR_MAX**: Total number of monitors (59).

### **Method: `get_monitor(Monitor)`**
Retrieves the value of a built-in monitor. Example:

```gdscript
print(Performance.get_monitor(Performance.TIME_FPS)) # Prints FPS
```

---

## **Custom Monitors**

Custom monitors allow developers to track custom metrics, such as the number of NPCs, texture load times, or any other data relevant to their game.

### **Method: `add_custom_monitor(id, callable, arguments = [])`**
Adds a custom monitor. The `id` can be structured with categories (e.g., `"Game/NumberOfNPCs"`). The `callable` is a function that returns the value for this monitor.

**Example in GDScript:**
```gdscript
func _ready():
    var monitor_value = Callable(self, "get_monitor_value")

    Performance.add_custom_monitor("Game/NumberOfNPCs", monitor_value)
    Performance.add_custom_monitor("Custom/MyMonitor", monitor_value)
```

**Example in C#:**
```csharp
public override void _Ready()
{
    var monitorValue = new Callable(this, MethodName.GetMonitorValue);

    Performance.AddCustomMonitor("Game/NumberOfNPCs", monitorValue);
}
```

**Requirements for `callable`:**
- Must return a zero or positive integer or float.
- Can accept arguments from the `arguments` array.

---

## **Monitor Management**

### **Method: `get_custom_monitor(id)`**
Retrieves the value of a custom monitor by its `id`. If the `id` doesn’t exist, it throws an error.

### **Method: `get_custom_monitor_names()`**
Returns an array of all active custom monitor names.

### **Method: `has_custom_monitor(id)`**
Checks if a custom monitor with the given `id` exists.

### **Method: `remove_custom_monitor(id)`**
Removes a custom monitor by its `id`. If the `id` doesn’t exist, it throws an error.

---

## **Monitor Modification Time**

### **Method: `get_monitor_modification_time()`**
Returns the last time (in microseconds) a custom monitor was added or removed. This is useful for tracking when monitors were last updated.

---

## **Key Notes**

- **Categories in `id`:** Use slashes (`/`) to structure categories (e.g., `"Game/Stats/Score"`). The default category is `"Custom"`.
- **Uniqueness:** Each `id` must be unique, even if it shares a name with another monitor in a different category.
- **Callable Callbacks:** The `callable` is invoked when the monitor is accessed (e.g., via `get_custom_monitor()`).

---

## **Example Use Cases**

1. **Tracking FPS:**
   ```gdscript
   print(Performance.get_monitor(Performance.TIME_FPS))
   ```

2. **Custom Metric: NPC Count:**
   ```gdscript
   func get_monitor_value():
       return randi() % 25
   ```

3. **Memory Usage:**
   ```gdscript
   print(Performance.get_monitor(Performance.MEMORY_USAGE))
   ```

---

## **Summary**

The `Performance` class is a powerful tool for debugging and optimizing Godot games. It provides both built-in and custom metrics, allowing developers to track performance at a granular level. By leveraging custom monitors, developers can create tailored performance tracking systems that fit their specific game needs.