# JavaClassWrapper

**Inherits:** Object

## Overview
A singleton class for accessing the Java Native Interface (JNI) in Android builds. Provides methods to interact with Java classes and handle exceptions from JNI calls.

## Key Functions
- **Wrap Java classes**: Convert Java class names to Godot-compatible JavaClass objects
- **Exception handling**: Retrieve exceptions from JNI calls
- **Platform restriction**: Only works on Android platforms

## Example Usage
```gdscript
var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

var datetime = LocalDateTime.now()
var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

print(datetime.format(formatter))
```

## Method Descriptions

### `get_exception()`
- **Returns**: JavaObject (or null if no exception)
- **Note**: Only functional on Android platforms. Returns null on other platforms.

### `wrap(name: String) -> JavaClass`
- **Parameters**: name (String) - Java class name (use $ for nested classes)
- **Returns**: JavaClass object for the specified Java class
- **Note**: Only functional on Android. Returns empty JavaClass on other platforms.

## Important Notes
- Always check `get_exception()` after JNI calls to handle potential errors
- Nested classes should use `$` instead of `.` in class names
- This class is not available on platforms other than Android