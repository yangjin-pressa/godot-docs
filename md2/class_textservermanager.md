# TextServerManager

**Inherits:** Object

A singleton for managing TextServer implementations.

## Description
TextServerManager is the API backend for loading, enumerating, and switching TextServer instances.  
**Note:** Switching text server at runtime invalidates all fonts and text buffers. Ensure all controls, fonts, and themes are unloaded before doing so.

## Methods
- **add_interface** (interface: TextServer): Registers a TextServer interface.
- **find_interface** (name: String): Finds an interface by its name.
- **get_interface** (idx: int): Returns the interface at the given index.
- **get_interface_count** (): Returns the number of registered interfaces.
- **get_interfaces** (): Returns a list of available interfaces with their index and name.
- **get_primary_interface** (): Returns the currently active TextServer interface.
- **remove_interface** (interface: TextServer): Removes an interface. Free all fonts and shaped text caches before removal.
- **set_primary_interface** (index: TextServer): Sets the primary TextServer interface.

## Signals
- **interface_added** (interface_name: StringName): Emitted when a new interface is added.
- **interface_removed** (interface_name: StringName): Emitted when an interface is removed.

## Method Descriptions
- **add_interface**: Registers a TextServer interface.
- **find_interface**: Finds an interface by its name.
- **get_interface**: Returns the interface at the specified index.
- **get_interface_count**: Returns the total number of registered interfaces.
- **get_interfaces**: Returns a list of available interfaces with their index and name.
- **get_primary_interface**: Returns the currently active TextServer interface.
- **remove_interface**: Removes an interface; ensure all fonts and caches are freed first.
- **set_primary_interface**: Sets the primary TextServer interface.