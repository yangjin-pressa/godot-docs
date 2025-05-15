# Thread

## Overview
A unit of execution in a process. Enables concurrent method execution on Object instances. Synchronization via Mutex or Semaphore is recommended for shared data.

## Key Concepts
- **Thread Safety**: Ensure no locks are held, no semaphore waits, and call `wait_to_finish()` before destruction
- **Priority Levels**:
  - PRIORITY_LOW (0)
  - PRIORITY_NORMAL (1)
  - PRIORITY_HIGH (2)

## Core Methods

### Thread Management
- `get_id()`: Returns unique thread identifier (empty if thread not started or finished)
- `is_alive()`: Checks if thread is currently executing
- `is_started()`: Indicates if thread has been started
- `wait_to_finish()`: Waits for thread completion, returns callable output

### Thread Control
- `start(callable, priority=1)`: Initiates new thread with specified function
  - Returns OK on success, ERR_CANT_CREATE on failure
- `set_thread_safety_checks_enabled(enabled)`: Enables/disables thread safety checks (default: enabled)

## Thread Safety Notes
- Safety checks in Node methods are enabled by default
- Disabling checks requires user responsibility for thread safety
- Applies to WorkerThreadPool tasks but not Node group processing

## Related Resources
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

## Reference
- [Using multiple threads tutorial](../tutorials/performance/using_multiple_threads)
- [Thread-safe APIs tutorial](../tutorials/performance/thread_safe_apis)