# WorkerThreadPool

**Inherits:** Object

A singleton that manages worker threads for offloading tasks.

---

## Description

Workers allocate threads at startup to handle tasks. This allows multithreading without manually creating threads. Tasks can be regular (single-threaded) or group (multi-threaded). Group tasks execute a callable multiple times, useful for processing large datasets.

Example:
```gdscript
var enemies = []
func process_enemy_ai(enemy_index):
    var processed_enemy = enemies[enemy_index]
    # Expensive logic...

func _process(delta):
    var task_id = WorkerThreadPool.add_group_task(process_enemy_ai, enemies.size())
    WorkerThreadPool.wait_for_group_task_completion(task_id)
```

Note: Ensuring array elements remain constant during execution is critical.

---

## Tutorials
- [Using multiple threads](../tutorials/performance/using_multiple_threads)
- [Thread-safe APIs](../tutorials/performance/thread_safe_apis)

---

## Methods

### add_group_task
**Returns:** int  
**Parameters:**
- action: Callable
- elements: int
- tasks_needed: int = -1
- high_priority: bool = false
- description: String = ""

Adds a group task to be executed by worker threads. The callable is called multiple times with increasing parameters.

**Warning:** Must wait for completion to clean up resources.

### add_task
**Returns:** int  
**Parameters:**
- action: Callable
- high_priority: bool = false
- description: String = ""

Adds a single task to a worker thread.

**Warning:** Must wait for completion to clean up resources.

### get_group_processed_element_count
**Returns:** int  
**Parameter:** group_id: int

Returns how many times a group task's callable has been executed.

**Note:** Only counts completed executions.

### is_group_task_completed
**Returns:** bool  
**Parameter:** group_id: int

Checks if a group task is completed.

**Note:** Use only between task creation and completion.

### is_task_completed
**Returns:** bool  
**Parameter:** task_id: int

Checks if a task is completed.

**Note:** Use only between task creation and completion.

### wait_for_group_task_completion
**Parameter:** group_id: int

Pauses execution until a group task completes.

### wait_for_task_completion
**Returns:** Error  
**Parameter:** task_id: int

Pauses execution until a task completes.

**Returns:**
- OK: Task completed
- ERR_INVALID_PARAMETER: Task doesn't exist
- ERR_BUSY: Potential deadlock (advanced case)

---

## Key Notes
- WorkerThreadPool is a singleton.
- Group tasks distribute work across threads, while single tasks use one thread.
- Always wait for task completion to ensure proper resource cleanup.
- Performance impact depends on task complexity and parallelism.