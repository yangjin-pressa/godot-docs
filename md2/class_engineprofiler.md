# EngineProfiler

**Inherits:** RefCounted < Object

Base class for creating custom profilers.

## Description
This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

See EngineDebugger and EditorDebuggerPlugin for more information.

## Methods

- **_add_frame**: Called when data is added to profiler using `EngineDebugger.profiler_add_frame_data()`.  
  **Parameters**: `data` (Array)

- **_tick**: Called once every engine iteration when the profiler is active with information about the current frame. All time values are in seconds. Lower values represent faster processing times and are therefore considered better.  
  **Parameters**: `frame_time` (float), `process_time` (float), `physics_time` (float), `physics_frame_time` (float)

- **_toggle**: Called when the profiler is enabled/disabled, along with a set of `options`.  
  **Parameters**: `enable` (bool), `options` (Array)

## Notes
- These methods are virtual and should typically be overridden by the user to have any effect.