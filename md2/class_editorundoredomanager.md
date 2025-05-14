The `EditorUndoRedoManager` class in Godot is a critical component for managing undo and redo operations within the editor. It allows developers to control how changes are tracked, merged, and reverted, ensuring robust and flexible editing workflows. Below is a structured breakdown of the class's functionality, implementation details, and use cases.

---

### **Key Features and Implementation Overview**

#### **1. History Management**
- **Multiple Histories**: The manager supports multiple undo/redo histories, each associated with a unique ID. These include:
  - **Scene-based Histories**: For each opened scene (tab).
  - **Global History**: For operations not tied to a specific scene (e.g., resource changes).
  - **Special Cases**: `INVALID_HISTORY` (clears all), `GLOBAL_HISTORY`, and `SCENE_TABS`.

- **History ID Mapping**:
  - `id > 0`: Maps to scene tabs (but not their order).
  - `id <= 0`: Special meanings (e.g., `INVALID_HISTORY` or `GLOBAL_HISTORY`).

- **Accessing Histories**: The `get_history_undo_redo(id)` method retrieves the `UndoRedo` instance for a given ID, allowing direct manipulation of undo/redo operations.

---

#### **2. Action Creation and Execution**
- **`create_action(name, merge_mode, custom_context, backward_undo_ops)`**:
  - **Purpose**: Starts a new action with a custom name and merge mode.
  - **Parameters**:
    - `name`: Identifier for the action.
    - `merge_mode`: Determines how actions are merged (e.g., `MergeMode::Merge`, `MergeMode::Replace`).
    - `custom_context`: Overrides automatic history deduction (e.g., for nested resources).
    - `backward_undo_ops`: Controls the order of undo operations (forward vs. backward).

- **`add_do_method(object, method)`**:
  - **Purpose**: Adds a method to the current action that will be executed when the action is committed.
  - **Usage**: Typically used with `create_action` to define the "do" operations.

- **`add_undo_method(object, method)`**:
  - **Purpose**: Adds a method to reverse the "do" operations when the action is undone.

- **`commit_action(execute=true)`**:
  - **Purpose**: Finalizes the action. If `execute` is true, it runs the "do" methods/properties.
  - **Use Case**: Commit changes to the scene or resource tree, triggering undo/redo operations.

---

#### **3. History Deduction and Overrides**
- **`get_object_history_id(object)`**:
  - **Purpose**: Deduces the appropriate history ID based on the object's type.
  - **Examples**:
    - **Node**: Uses the scene's history (e.g., `scene_root`).
    - **Resource**: Uses the global history (id = -99).

- **`force_fixed_history()`**:
  - **Purpose**: Forces the next operation to use the current action's history instead of deducing it from the object.
  - **Use Case**: When the object's history cannot be determined (e.g., nested resources with placeholder paths).

---

#### **4. Clearing and Marking Histories**
- **`clear_history(id=-99, increase_version=true)`**:
  - **Parameters**:
    - `id`: History ID to clear. `INVALID_HISTORY` clears all.
    - `increase_version`: Marks the history as unsaved (useful for un-saved scenes).
  - **Note**: For marking a scene as unsaved without clearing history, use `EditorInterface.mark_scene_as_unsaved()`.

---

#### **5. State Checking**
- **`is_committing_action()`**:
  - **Purpose**: Returns `true` if the manager is currently committing an action.
  - **Use Case**: Ensures that actions are not being modified during commit.

---

### **Example Usage**

```cpp
// Example: Committing a node addition to a scene
EditorUndoRedoManager* undo_redo = EditorInterface.get_editor_undo_redo();
undo_redo->create_action("Add Node", MergeMode::Merge, nullptr, false);

// Add "do" method (create node)
undo_redo->add_do_method(scene_root, "add_child", node);

// Add "undo" method (remove node)
undo_redo->add_undo_method(scene_root, "remove_child", node);

// Commit the action
undo_redo->commit_action(true);
```

---

### **Key Considerations**
- **Merge Modes**: Carefully choose `MergeMode` to avoid conflicts (e.g., merging similar operations vs. replacing the current action).
- **Custom Context**: Use `custom_context` for complex objects where automatic history deduction fails.
- **Memory Management**: Ensure that references (e.g., nodes) are valid during the action's lifetime to avoid crashes.
- **Performance**: Avoid excessive action creation for small, frequent changes to maintain efficiency.

---

### **Conclusion**

The `EditorUndoRedoManager` is a powerful tool for managing complex editing workflows in Godot. By leveraging its methods, developers can ensure that changes are tracked, merged, and reverted accurately, providing a seamless user experience. Understanding its mechanics allows for efficient implementation of custom undo/redo logic tailored to specific projects.