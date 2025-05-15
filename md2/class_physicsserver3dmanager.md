**Class: PhysicsServer3DManager**  
**Inherits:** Object  

---

### **Description**  
A singleton for managing PhysicsServer3D implementations.  
- **Note:** Cannot switch physics servers at runtime. Used only during startup.  

---

### **Methods**  
- **register_server(name: String, create_callback: Callable)**  
  Registers a PhysicsServer3D implementation by name and a callback that creates the server.  

- **set_default_server(name: String, priority: int)**  
  Sets the default PhysicsServer3D implementation if the provided priority is higher than the current default.  

---

### **Key Details**  
- **singleton**  
- **used for:** registering and setting default PhysicsServer3D implementations  
- **runtime limitations:** no dynamic switching of physics servers allowed  

---

### **References**  
- String (class)  
- Callable (class)  
- PhysicsServer3D (class)  
- Object (class)  

--- 

**Note:** All method parameters and functionality are defined in the Godot engine source code.