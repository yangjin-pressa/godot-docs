PhysicsServer2DManager  
Inherits: Object  

Description:  
- A singleton for managing PhysicsServer2D implementations.  
- Note: It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.  

Methods:  
- register_server(name: String, create_callback: Callable)  
  - Register a PhysicsServer2D implementation by passing a name and a Callable that returns a PhysicsServer2D object.  

- set_default_server(name: String, priority: int)  
  - Set the default PhysicsServer2D implementation to the one identified by name, if priority is greater than the priority of the current default implementation.  

Key notes:  
- This class is a singleton.  
- The priority parameter determines the default server selection.  
- Methods are used during startup, not at runtime.