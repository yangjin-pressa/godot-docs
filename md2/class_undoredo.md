# Godot Engine UndoRedo Class Documentation

The `UndoRedo` class in the Godot Engine provides a way to manage undo/redo operations for user actions, such as editing scene nodes or modifying properties. This documentation explains the class's properties, methods, and usage examples.

---

## **Properties**

### `max_history_size`
- **Type**: `int`
- **Description**: The maximum number of steps that can be stored in the history. If this limit is exceeded, the oldest steps are removed.
- **Note**: This is a constant and cannot be modified after the class is initialized.

### `version`
- **Type**: `int`
- **Description**: A read-only integer that represents the current version of the undo/redo history. It increments each time a new action is committed.
- **Usage**: Useful for checking if changes have occurred since a saved state.

---

## **Methods**

### `clear_history(increase_version: bool = true)`
- **Description**: Clears the undo/redo history and associated references.
- **Parameters**:
  - `increase_version`: If `true`, the version number is incremented when the history is cleared. If `false`, the version number remains unchanged.
- **Usage**: Reset the history without affecting the version number if needed.

### `commit_action(execute: bool = true)`
- **Description**: Commits the current action. If `execute` is `true`, the "do" methods/properties are executed; otherwise, they are recorded but not executed.
- **Usage**: Always call this after adding all "do" and "undo" operations to finalize the action.

### `create_action(name: String, merge_mode: int = 0, backward_undo_ops: bool = false)`
- **Description**: Creates a new action. Subsequent calls to `add_do_method()`, `add_undo_method()`, etc., are added to this action.
- **Parameters**:
  - `name`: The name of the action.
  - `merge_mode`: Determines how actions are merged (see `MergeMode`).
  - `backward_undo_ops`: If `true`, undo operations are ordered in reverse (last added first undone).
- **Usage**: Must be called before adding operations and followed by `commit_action()`.

### `end_force_keep_in_merge_ends()`
- **Description**: Stops marking operations as to be processed even if the action gets merged with another in `MERGE_ENDS` mode.
- **Usage**: Used with `start_force_keep_in_merge_ends()` to control merging behavior.

### `get_action_name(id: int) -> String`
- **Description**: Retrieves the name of an action by its index.
- **Parameters**:
  - `id`: The index of the action in the history.

### `get_current_action() -> int`
- **Description**: Returns the index of the current action.
- **Usage**: Useful for tracking which action is being processed.

### `get_current_action_name() -> String`
- **Description**: Returns the name of the current action. Equivalent to `get_action_name(get_current_action())`.
- **Usage**: A convenience method to get the current action's name.

### `get_history_count() -> int`
- **Description**: Returns the number of elements in the history.
- **Usage**: Check the size of the undo/redo history.

### `get_version() -> int`
- **Description**: Returns the current version number.
- **Usage**: For version checking or saving states.

### `has_redo() -> bool`
- **Description**: Returns `true` if a "redo" action is available.
- **Usage**: Check if there are steps to redo.

### `has_undo() -> bool`
- **Description**: Returns `true` if an "undo" action is available.
- **Usage**: Check if there are steps to undo.

### `is_committing_action() -> bool`
- **Description**: Returns `true` if the `UndoRedo` is currently committing an action (e.g., running "do" methods).
- **Usage**: For internal state checks.

### `redo() -> bool`
- **Description**: Redoes the last action.
- **Return**: `true` if the redo was successful.
- **Usage**: After an undo, to revert the last change.

### `start_force_keep_in_merge_ends()`
- **Description**: Marks the next "do" and "undo" operations to be processed even if the action gets merged with another in `MERGE_ENDS` mode.
- **Usage**: Use this in conjunction with `end_force_keep_in_merge_ends()`.

### `undo() -> bool`
- **Description**: Undoes the last action.
- **Return**: `true` if the undo was successful.
- **Usage**: To revert the last change.

---

## **Examples**

### **Basic Usage**
```gdscript
var undo_redo = UndoRedo.new()

# Start a new action
undo_redo.create_action("Adjust Position", MergeMode.MERGE_ENDS, false)

# Add do operations
undo_redo.add_do_method("set_position", Vector2(10, 20))

# Add undo operations
undo_redo.add_undo_method("set_position", Vector2(0, 0))

# Commit the action
undo_redo.commit_action(true)

# Undo the last action
if undo_redo.has_undo():
    if undo_redo.undo():
        print("Undo successful.")
```

### **Merge Mode Example**
```gdscript
var undo_redo = UndoRedo.new()

# Start action 1
undo_redo.create_action("Move Object", MergeMode.MERGE_ENDS, false)
undo_redo.add_do_method("set_position", Vector2(10, 20))
undo_redo.add_undo_method("set_position", Vector2(0, 0))
undo_redo.commit_action(true)

# Start action 2 (merges with previous)
undo_redo.create_action("Move Object", MergeMode.MERGE_ENDS, false)
undo_redo.add_do_method("set_position", Vector2(20, 30))
undo_redo.add_undo_method("set_position", Vector2(10, 20))
undo_redo.commit_action(true)

# Now, undoing will revert the last action (second move)
if undo_redo.has_undo():
    if undo_redo.undo():
        print("Undo of second action successful.")
```

---

## **Important Notes**
- Call `create_action()` before adding operations, and `commit_action()` after.
- Use `MergeMode.MERGE_ENDS` to merge actions with the same name, avoiding redundant steps.
- `get_version()` is useful for state tracking in editors or save/load systems.
- `max_history_size` ensures the history doesn't grow infinitely.

This class is integral to creating intuitive UIs and tools that allow users to undo/redo changes in real-time, enhancing the user experience in Godot projects.