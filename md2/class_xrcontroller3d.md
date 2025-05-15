**XRController3D**  
Inherits from: `XRBaseController`  

**Description**  
- Linked by ID to manage multiple instances.  
- Position is automatically updated by `XRServer`.  
- Input names are defined by `XRInterface`.  

**Tutorials**  
- [XRInterface Documentation](https://example.com/xrinterface)  

**Methods**  
- `get_float(name: str) → float`: Returns a float value for the input with the given name.  
- `get_int(name: str) → int`: Returns an integer value for the input with the given name.  
- `get_string(name: str) → str`: Returns a string value for the input with the given name.  
- `get_bool(name: str) → bool`: Returns a boolean value for the input with the given name.  

**Signals**  
- `button_pressed(name: str)`: Emitted when a button is pressed, with the button's name.  
- `axis_moved(name: str, value: float)`: Emitted when an axis moves, with the axis name and value.  
- `trigger_pressed(name: str)`: Emitted when a trigger is pressed, with the trigger's name.  

**Method Details**  
- **get_float**: Returns a float value for the input with the given name. The name is defined by `XRInterface`.  
- **get_int**: Returns an integer value for the input with the given name. The name is defined by `XRInterface`.  
- **get_string**: Returns a string value for the input with the given name. The name is defined by `XRInterface`.  
- **get_bool**: Returns a boolean value for the input with the given name. The name is defined by `XRInterface`.  

**Key Notes**  
- The position of the controller is managed by `XRServer`.  
- Input names are determined by the `XRInterface` class.