**Class: PinJoint3D**  
**Inherits:** Joint3D → Node3D → Node → Object  

---

### **Description**  
A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. Used for creating pendulums or seesaws by connecting a RigidBody3D to a StaticBody3D.  

---

### **Properties**  
- **bias**: `float` (default: 0.3)  
  Force keeping connected objects in positional relation. Higher = stronger.  
- **damping**: `float` (default: 1.0)  
  Force keeping connected objects in velocity relation. Higher = stronger.  
- **impulse_clamp**: `float` (default: 0.0)  
  Maximum impulse for this joint. Value > 0 enables clamping.  

---

### **Methods**  
- **get_param(param: Param) → float**  
  Returns the value of the specified parameter.  
- **set_param(param: Param, value: float) → void**  
  Sets the value of the specified parameter.  

---

### **Enumerations**  
**Param**  
- **PARAM_BIAS** = 0  
  Controls positional force.  
- **PARAM_DAMPING** = 1  
  Controls velocity force.  
- **PARAM_IMPULSE_CLAMP** = 2  
  Limits maximum impulse.  

---

### **Property Descriptions**  
- **bias**  
  - **set_param**: Adjusts positional force.  
  - **get_param**: Retrieves positional force.  
- **damping**  
  - **set_param**: Adjusts velocity force.  
  - **get_param**: Retrieves velocity force.  
- **impulse_clamp**  
  - **set_param**: Sets maximum impulse limit.  
  - **get_param**: Retrieves impulse limit.  

--- 

**Note:** This joint allows rotation around a single point, enabling dynamic interactions between connected physics bodies.