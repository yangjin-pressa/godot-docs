# EditorToaster

**Inherits:** HBoxContainer → BoxContainer → Container → Control → CanvasItem → Node → Object

## Description
Manages toast notifications within the editor, ensuring timely and informative alerts are presented to users.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using `EditorInterface.get_editor_toaster()`.

## Methods
- **push_toast** (message: String, severity: Severity = 0, tooltip: String = "")  
  Pushes a toast notification to the editor for display.

## Enumerations
### Severity
- **SEVERITY_INFO** = 0  
  Toast displays with INFO severity.
- **SEVERITY_WARNING** = 1  
  Toast displays with WARNING severity and corresponding color.
- **SEVERITY_ERROR** = 2  
  Toast displays with ERROR severity and corresponding color.

## Method Descriptions
- **push_toast**  
  A void method that takes a message, severity, and tooltip. The severity defaults to 0 (INFO).  
  - **virtual**: Method should typically be overridden by the user.  
  - **const**: No side effects; does not modify instance variables.