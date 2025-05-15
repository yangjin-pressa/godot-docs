**Class:** VisualShaderNodeGroupBase  
**Inherits from:** VisualShaderNode  

---

### **Description**  
A base class for managing input and output ports in a shader node. Provides methods to add, remove, and configure ports, including checking their existence, validity, and retrieving their details.

---

### **Methods**  

1. **add_input_port(id: int, type: int, name: str)**  
   - **Returns:** `void`  
   - **Description:** Adds a new input port with specified ID, type, and name.  

2. **add_output_port(id: int, type: int, name: str)**  
   - **Returns:** `void`  
   - **Description:** Adds a new output port with specified ID, type, and name.  

3. **get_free_input_port_id()**  
   - **Returns:** `int`  
   - **Description:** Returns a free input port ID for use with `add_input_port()`.  

4. **get_free_output_port_id()**  
   - **Returns:** `int`  
   - **Description:** Returns a free output port ID for use with `add_output_port()`.  

5. **get_input_port_count()**  
   - **Returns:** `int`  
   - **Description:** Returns the number of input ports in use. Alternative to `get_free_input_port_id()`.  

6. **get_outputs()**  
   - **Returns:** `String`  
   - **Description:** Returns a colon-separated string of output ports in format `id,type,name;`.  

7. **get_input_port_count()**  
   - **Returns:** `int`  
   - **Description:** Returns the number of output ports in use. Alternative to `get_free_output_port_id()`.  

8. **get_inputs()**  
   - **Returns:** `String`  
   - **Description:** Returns a colon-separated string of input ports in format `id,type,name;`.  

9. **has_input_port(id: int)**  
   - **Returns:** `bool`  
   - **Description:** Checks if the specified input port exists.  

10. **has_output_port(id: int)**  
    - **Returns:** `bool`  
    - **Description:** Checks if the specified output port exists.  

11. **is_valid_port_name(name: String)**  
    - **Returns:** `bool`  
    - **Description:** Validates if the port name is unique and valid within the shader.  

12. **remove_input_port(id: int)**  
    - **Returns:** `void`  
    - **Description:** Removes the specified input port.  

13. **remove_output_port(id: int)**  
    - **Returns:** `void`  
    - **Description:** Removes the specified output port.  

14. **set_input_port_name(id: int, name: String)**  
    - **Returns:** `void`  
    - **Description:** Renames the specified input port.  

15. **set_input_port_type(id: int, type: int)**  
    - **Returns:** `void`  
    - **Description:** Sets the type of the specified input port.  

16. **set_outputs(name: String)**  
    - **Returns:** `void`  
    - **Description:** Defines all output ports from a colon-separated string `id,type,name;`.  

17. **set_output_port_name(id: int, name: String)**  
    - **Returns:** `void`  
    - **Description:** Renames the specified output port.  

18. **set_output_port_type(id: int, type: int)**  
    - **Returns:** `void`  
    - **Description:** Sets the type of the specified output port.  

19. **set_inputs(name: String)**  
    - **Returns:** `void`  
    - **Description:** Defines all input ports from a colon-separated string `id,type,name;`.  

---

### **Notes**  
- **const**: Methods like `get_inputs()` have no side effects and do not modify the object.  
- **virtual**: Methods like `add_input_port()` should typically be overridden in derived classes.  
- **PortType**: Refer to the `PortType` enum for valid type values.  
- **String Formatting**: Methods like `get_inputs()` return a string in `id,type,name;` format for easy parsing.