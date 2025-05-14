# JavaScriptBridge

## Overview
- **Inherits**: Object
- **Purpose**: Singleton connecting Godot engine to browser JavaScript context for Web export
- **Key Feature**: Enables interaction with browser APIs and embedded pages
- **Security Note**: Can be disabled at build-time for enhanced security (default: enabled)

## Key Features
- **Web Export Only**: Available only in Web export builds
- **Singleton Usage**: Accessed via `JavaScriptBridge.instance`
- **JavaScript Integration**: Provides access to browser's JavaScript environment

## Methods

### create_callback
- **Returns**: JavaScriptObject
- **Parameters**: Callable
- **Description**: Creates a JavaScript callback reference. Callback must accept a single Array argument (JavaScript arguments object converted to array)

### create_object
- **Returns**: Variant
- **Parameters**: String, ... (vararg)
- **Description**: Creates JavaScript object using new constructor. First parameter must be a valid window property

### download_buffer
- **Returns**: void
- **Parameters**: PackedByteArray, String, String (mime type)
- **Description**: Triggers file download. Note: May be blocked by browsers if not called from user interaction

### eval
- **Returns**: Variant
- **Parameters**: String, bool (use_global_context)
- **Description**: Executes JavaScript code. Use_global_context determines execution context

### force_fs_sync
- **Returns**: void
- **Description**: Forces file system synchronization. Useful for modules that can't use FileAccess

### get_interface
- **Returns**: JavaScriptObject
- **Parameters**: String
- **Description**: Returns JavaScript object interface. Callback must accept single Array argument

### is_js_buffer
- **Returns**: bool
- **Parameters**: JavaScriptObject
- **Description**: Checks if object is ArrayBuffer, DataView, or typed array

### js_buffer_to_packed_byte_array
- **Returns**: PackedByteArray
- **Parameters**: JavaScriptObject
- **Description**: Converts JavaScript buffer to PackedByteArray

### pwa_needs_update
- **Returns**: bool (const)
- **Description**: Checks if progressive web app needs update (relevant for PWA exports)

### pwa_update
- **Returns**: Error
- **Description**: Forces PWA update. Reloads all browser tabs. Requires pwa_needs_update to be true

## Signals
- **pwa_update_available**: Emits when PWA update is detected but not yet activated

## Important Notes
1. **Callback Requirements**: Callback functions must accept exactly one Array argument
2. **Security**: Disable singleton in project settings for production builds
3. **Browser Restrictions**: download_buffer may be blocked by browsers unless called from user interaction
4. **PWA Specific**: pwa_needs_update and pwa_update only relevant for Progressive Web App exports
5. **Typed Arrays**: is_js_buffer checks for ArrayBuffer, DataView, or typed arrays

## Related Concepts
- JavaScriptObject: Used for all JavaScript interactions
- PackedByteArray: Used for data conversion between JavaScript and Godot
- ArrayBuffer/DataView: Special types checked by is_js_buffer