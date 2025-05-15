# TextServerDummy

**Inherits:** TextServerExtension < TextServer < RefCounted < Object

A dummy text server that cannot render text or manage fonts. Used to free memory when text rendering is unnecessary, or for performance testing in complex GUIs.

## Description

A non-functional text server interface for memory optimization and performance benchmarking. It is always available at the start of a project.

### Access Method
```gdscript
var dummy_text_server = TextServerManager.find_interface("Dummy")
if dummy_text_server != null:
    TextServerManager.set_primary_interface(dummy_text_server)
    # Remove unused text servers
    for i in TextServerManager.get_interface_count():
        var text_server = TextServerManager.get_interface(i)
        if text_server != dummy_text_server:
            TextServerManager.remove_interface(text_server)
```

### Command Line Usage
Use `--text-driver Dummy` to force the "Dummy" text server on a project.

**Key Features:**
- No rendering capabilities
- Memory-efficient placeholder
- Performance testing tool
- Always available at project start
- Can be configured via command line argument