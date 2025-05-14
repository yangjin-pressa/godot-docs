**ConeTwistJoint3D**  
A joint that allows rotational movement in a cone-shaped area.  

---

### **Description**  
A joint that allows rotational movement in a cone-shaped area. This joint enables objects to rotate around an axis while restricting rotation to a specific angular range.  

---

### **Properties**  
- **bias**: `float`  
  A float value representing the bias parameter for the joint. Default: `0.3`.  
- **twist_span**: `float`  
  A float value defining the maximum allowable twist angle. Default: `3.14159`.  

**Other properties** (linked to methods):  
- **bias**: `float`  
- **twist_span**: `float`  

---

### **Methods**  
- **get_param(param: Param)** → `float`  
  Returns the value of the specified parameter.  
- **set_param(param: Param, value: float)** → `void`  
  Sets the value of the specified parameter.  

---

### **Enumerations**  
**Param**  
- **BIAS**: `0`  
  Represents the bias parameter for the joint.  
- **TWIST_SPAN**: `1`  
  Represents the twist span parameter for the joint.  

---

### **Property Descriptions**  
- **bias**:  
  A float value that controls the joint's bias parameter. Used to adjust the stiffness of the joint's constraints.  

- **twist_span**:  
  A float value that defines the maximum allowable twist angle. If below `0.05`, the joint becomes locked.  

---

### **Method Descriptions**  
- **get_param(param: Param)**:  
  Retrieves the current value of the specified parameter.  

- **set_param(param: Param, value: float)**:  
  Updates the value of the specified parameter.  

--- 

**Note**: All properties and methods are interconnected through the `Param` enum, which defines valid parameters for the joint.