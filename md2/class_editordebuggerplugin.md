**EditorDebuggerPlugin**  
A base class for implementing custom debugger plugins in Godot.  

---

### **Description**  
- **Purpose**: Provides a framework for creating debugger plugins that interact with the editor.  
- **Usage**:  
  - Add to the editor via `EditorPlugin.add_debugger_plugin()`.  
  - The plugin's `_setup_session()` method is called for each `EditorDebuggerSession`.  
- **Session Management**:  
  - Use `get_session(id)` to retrieve a session by ID.  
  - Use `get_sessions()` to get an array of available sessions.  

---

### **Code Examples**  
**Editor Side**  
```gdscript
class_name EditorDebuggerPlugin
extends EditorDebuggerPlugin:

    func _setup_session(session_id):
        # Create UI or logic for the session
        pass

    func _capture_message(message):
        # Process incoming messages
        pass
```

**Game Side**  
```gdscript
# Example of using EngineDebugger in a game
var debugger = EngineDebugger()
debugger.add_message("Debug info")
```

---

### **Key Methods**  
| Method | Parameters | Return Type | Notes |
|-------|------------|-------------|-------|
| `_breakpoint_set_in_tree` | `session_id: int` | `void` | Virtual method to handle breakpoint setting. |
| `_breakpoints_cleared_in_tree` | `session_id: int` | `void` | Virtual method to handle clearing breakpoints. |
| `_capture` | `message: String` | `bool` | Processes messages; returns `true` if handled. |
| `_has_capture` | `message: String` | `bool` | Checks if a message should be captured. |
| `_setup_session` | `session_id: int` | `void` | Virtual method to initialize a session. |
| `get_session` | `id: int` | `EditorDebuggerSession` | Returns the session with the given ID. |
| `get_sessions` | - | `Array[EditorDebuggerSession]` | Returns all active sessions. |

---

### **Method Descriptions**  
- **`_setup_session(session_id: int)`:**  
  Called when a new `EditorDebuggerSession` is created. Use this to initialize UI or logic for the session.  

- **`get_session(id: int)`:**  
  Retrieves a specific `EditorDebuggerSession` by its ID.  

- **`get_sessions()`:**  
  Returns a list of all `EditorDebuggerSession` instances. Note that sessions in the list may be inactive.  

- **`_capture(message: String)`:**  
  Processes a message. Return `true` if the message is handled by this plugin.  

- **`_has_capture(message: String)`:**  
  Determines if a message should be captured by this plugin.  

---

### **Important Notes**  
- **Session State**: Check `EditorDebuggerSession.is_active()` to verify if a session is active.  
- **Output Log**: The Output Log may not display messages from this plugin if it is not properly configured.  
- **Virtual Methods**: Most methods are `virtual` and should be overridden to add custom behavior.  

--- 

This class is essential for extending Godot's debugging capabilities, allowing developers to create custom tools for inspecting or modifying game state.