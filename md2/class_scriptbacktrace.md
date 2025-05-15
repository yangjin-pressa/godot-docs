# ScriptBacktrace

## Description
A class representing a script backtrace, capturing information about the execution stack of a script. This includes stack frames, local variables, global variables, and member variables.

## Methods

- **format(indentation)**: Formats the backtrace into a readable string with specified indentation.
- **get_language_name()**: Returns the name of the script language (e.g., GDScript).
- **is_empty()**: Returns true if the backtrace contains no stack frames.
- **get_global_variable_name(index)**: Returns the name of a global variable at the specified index.
- **get_global_variable_value(index)**: Returns the value of a global variable at the specified index.
- **get_local_variable_name(frame_index, variable_index)**: Returns the name of a local variable in a specific stack frame.
- **get_local_variable_value(frame_index, variable_index)**: Returns the value of a local variable in a specific stack frame.
- **get_member_variable_name(frame_index, variable_index)**: Returns the name of a member variable in a specific stack frame.
- **get_member_variable_value(frame_index, variable_index)**: Returns the value of a member variable in a specific stack frame.
- **get_local_variable_count(frame_index)**: Returns the number of local variables in a specific stack frame.
- **get_member_variable_count(frame_index)**: Returns the number of member variables in a specific stack frame.
- **get_global_variable_count()**: Returns the number of global variables (if included).

## Key Notes
- **Global/Local Variables**: The values returned for variables (especially in GDScript) include object references, which may prevent deallocation. Avoid storing these values if memory management is critical.
- **Include Variables**: The presence of variables (local, global, member) depends on the `include_variables` parameter used when capturing the backtrace.
- **Empty Backtrace**: `is_empty()` checks if the backtrace contains no stack frames.
- **Language Detection**: `get_language_name()` identifies the script language (e.g., GDScript, JavaScript).