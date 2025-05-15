**Timer Class Documentation**  

**Description**  
- A countdown timer that emits a "timeout" signal when it ends.  
- Can be started manually or automatically (via `start()` or `autostart` property).  
- The editor allows connecting the signal via the Node dock.  
- Note: Use `SceneTree.create_timer()` for one-shot timers instead of the node.  

**Tutorials**  
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)  

**Properties**  
- **autostart**: `bool` (default: `false`) — Starts the timer automatically when added to a scene.  
- **ignore_time_scale**: `bool` (default: `false`) — Ignores `Engine.time_scale` when calculating timing.  
- **one_shot**: `bool` (default: `false`) — Triggers the "timeout" signal only once.  
- **wait_time**: `float` (default: `1.0`) — Time required for the timer to end (in seconds).  

**Methods**  
- **is_stopped()**: Returns `true` if the timer is stopped or hasn’t started.  
- **start(time_sec=-1)**: Starts or resets the timer. If `time_sec > 0`, sets `wait_time` to this value.  
- **stop()**: Stops the timer immediately.  

**Signals**  
- **timeout**: Emitted when the timer ends.  

**Enumerations**  
- **TimerProcessCallback**:  
  - **TIMER_PROCESS_PHYSICS**: Processes the timer once per physics frame.  
  - **TIMER_PROCESS**: Processes the timer once per process frame.  

**Property Descriptions**  
- **autostart**: Controls automatic startup.  
- **ignore_time_scale**: Affects timing calculations.  
- **one_shot**: Determines if the signal is triggered once.  
- **wait_time**: Sets the duration before the timer ends.  

**Method Descriptions**  
- **is_stopped()**: Checks if the timer is stopped.  
- **start()**: Initializes or resets the timer with optional duration.  
- **stop()**: Halts the timer immediately.  

**Notes**  
- Timers process once per physics or process frame (based on `process_callback`).  
- Short timers (`< 0.05s`) may be inconsistent due to frame rate.  
- `time_left` is read-only and reflects `wait_time`.  
- `wait_time` can be adjusted dynamically via `start()`.