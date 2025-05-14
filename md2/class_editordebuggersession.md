# EditorDebuggerSession

## Description
This class cannot be directly instantiated and must be retrieved via a `EditorDebuggerPlugin`.  
Key functionality includes adding tabs to the session UI, sending messages, and toggling profilers.

## Methods
- **add_session_tab**(control: Control): Adds a control to the debug session UI. The control's node name is used as the tab title.
- **is_active**(): Returns true if the debug session is attached to a remote instance.
- **is_breaked**(): Returns true if the remote instance is in the debug loop.
- **is_debuggable**(): Returns true if the remote instance can be debugged.
- **remove_session_tab**(control: Control): Removes a control from the debug session UI.
- **send_message**(message: String, data: Array = []): Sends a message to the remote instance.
- **set_breakpoint**(path: String, line: int, enabled: bool): Enables or disables a breakpoint.
- **toggle_profiler**(profiler: String, enable: bool, data: Array = []): Toggles a profiler on the remote instance.

## Signals
- **breaked**(can_debug: bool): Emitted when the remote instance enters a break state.
- **continued**: Emitted when the remote instance exits a break state.
- **started**: Emitted when a remote instance is attached to the session.
- **stopped**: Emitted when a remote instance is detached from the session.

## Method Descriptions
- **add_session_tab**: Adds a UI control to the debugger bottom panel as a tab.
- **is_active**: Checks if the debug session is currently attached to a remote instance.
- **is_breaked**: Checks if the remote instance is in the debug loop.
- **is_debuggable**: Checks if the remote instance can be debugged.
- **remove_session_tab**: Removes a UI control from the debugger bottom panel.
- **send_message**: Sends a message to the remote instance, optionally with data.
- **set_breakpoint**: Updates a breakpoint's enabled state and reflects changes in the Editor Breakpoint Panel.
- **toggle_profiler**: Toggles a profiler on the remote instance, optionally with data.