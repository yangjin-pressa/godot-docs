**EngineDebugger Class Overview**

The `EngineDebugger` class provides methods for managing debugging, profiling, and message handling within the Godot engine. Below is a summary of its key methods and functionalities:

---

### **Key Methods**

1. **`insert_breakpoint(source, line)`**  
   - **Description**: Inserts a new breakpoint at the specified line in the given source.  
   - **Parameters**:  
     - `source`: `StringName` – The source file name.  
     - `line`: `int` – The line number in the source.  

2. **`remove_breakpoint(source, line)`**  
   - **Description**: Removes a breakpoint at the specified line in the given source.  
   - **Parameters**:  
     - `source`: `StringName` – The source file name.  
     - `line`: `int` – The line number in the source.  

3. **`is_breakpoint(source, line)`**  
   - **Description**: Checks if the specified source and line represent an existing breakpoint.  
   - **Parameters**:  
     - `source`: `StringName` – The source file name.  
     - `line`: `int` – The line number in the source.  

4. **`is_active()`**  
   - **Description**: Returns whether the debugger is currently active.  
   - **Return**: `bool` – `true` if active, `false` otherwise.  

5. **`is_skipping_breakpoints()`**  
   - **Description**: Returns whether the debugger is skipping breakpoints.  
   - **Return**: `bool` – `true` if skipping breakpoints, `false` otherwise.  

6. **`line_poll()`**  
   - **Description**: Forges a processing loop for debugger events to avoid idle issues.  

7. **`set_depth(depth)`**  
   - **Description**: Sets the current debugging depth.  
   - **Note**: **Experimental** – May change in future versions.  
   - **Parameters**:  
     - `depth`: `int` – New depth value.  

8. **`set_lines_left(lines)`**  
   - **Description**: Sets the number of debugging lines remaining.  
   - **Note**: **Experimental** – May change in future versions.  
   - **Parameters**:  
     - `lines`: `int` – New line count.  

9. **`script_debug(language, can_continue, is_error_breakpoint)`**  
   - **Description**: Triggers a debug break in script execution.  
   - **Parameters**:  
     - `language`: `ScriptLanguage` – Script language (e.g., GDScript).  
     - `can_continue`: `bool` – Whether the script can continue after the break.  
     - `is_error_breakpoint`: `bool` – Whether the break is due to an error.  

10. **`send_message(message, data)`**  
    - **Description**: Sends a custom message with associated data.  
    - **Parameters**:  
      - `message`: `String` – Message content.  
      - `data`: `Array` – Array of data to accompany the message.  

11. **`register_message_capture(name, callable)`**  
    - **Description**: Registers a message capture handler.  
    - **Note**: The callable must accept a message string and data array.  
    - **Parameters**:  
      - `name`: `StringName` – Identifier for the message (e.g., "my_message").  
      - `callable`: `Callable` – Function to handle captured messages.  

12. **`register_profiler(name, profiler)`**  
    - **Description**: Registers a profiler with the given name.  
    - **Parameters**:  
      - `name`: `StringName` – Profiler name.  
      - `profiler`: `EngineProfiler` – Profiler instance.  

13. **`unregister_message_capture(name)`**  
    - **Description**: Removes a registered message capture.  
    - **Parameters**:  
      - `name`: `StringName` – Name of the message capture to remove.  

14. **`unregister_profiler(name)`**  
    - **Description**: Removes a registered profiler.  
    - **Parameters**:  
      - `name`: `StringName` – Profiler name.  

15. **`profiler_enable(name, enable, arguments)`**  
    - **Description**: Enables or disables a profiler.  
    - **Parameters**:  
      - `name`: `StringName` – Profiler name.  
      - `enable`: `bool` – Whether to enable the profiler.  
      - `arguments`: `Array` – Arguments for the profiler's toggle method.  

16. **`profiler_add_frame_data(name, data)`**  
    - **Description**: Adds frame data to a profiler.  
    - **Parameters**:  
      - `name`: `StringName` – Profiler name.  
      - `data`: `Array` – Data to add to the profiler.  

---

### **Important Notes**

- **Experimental Methods**: `set_depth()` and `set_lines_left()` are marked as experimental and may change in future versions.  
- **Message Capture Warning**: The callable in `register_message_capture` receives messages without their prefix (unlike `EditorDebuggerPlugin._capture()`).  
- **Profiler Registration**: Use `register_profiler()` to add custom profilers, as described in `EngineProfiler` documentation.  

This class is essential for debugging, profiling, and custom message handling in Godot projects.