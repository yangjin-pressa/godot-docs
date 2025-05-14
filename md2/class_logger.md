# Logger

## Inheritance
- RefCounted → Object

## Description
Custom logger to receive messages from the internal error/warning stream. Loggers are registered via [OS.add_logger()](class_OS_method_add_logger).

## Methods
- **_log_error** (function: String, file: String, line: int, code: String, rationale: String, editor_notify: bool, error_type: int, script_backtraces: Array[ScriptBacktrace])  
- **_log_message** (message: String, error: bool)

## Enumerations
### ErrorType
- **ERROR_TYPE_ERROR** = 0  
  The message received is an error.
- **ERROR_TYPE_WARNING** = 1  
  The message received is a warning.
- **ERROR_TYPE_SCRIPT** = 2  
  The message received is a script error.
- **ERROR_TYPE_SHADER** = 3  
  The message received is a shader error.

## Method Descriptions
### _log_error
Called when an error is logged. Parameters include the source location, error details, and type.  
- **Note**: script_backtraces contains only stack frames in editor/debug builds by default.  
- **Warning**: This function may be called from multiple threads; thread safety requires manual locking.  
- **Note**: script_backtraces lacks captured variables due to performance constraints.

### _log_message
Called when a message is logged. The `error` parameter indicates if the message should go to stderr.  
- **Warning**: This function may be called from multiple threads; thread safety requires manual locking.

## Key Notes
- Method overrides are required for functionality.
- Thread safety: Manual locking is necessary for thread-safe implementations.