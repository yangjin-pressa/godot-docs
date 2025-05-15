**Class:** VisualShaderNodeFloatFunc  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  

---

### **Description**  
Applies a scalar floating-point function to an input value (x). The function determines how the input is transformed.  

---

### **Properties**  
- **function**: Specifies the function to apply. Default: `FUNC_SATURATE` (value 13).  
  - **Set**: `set_function(value: Function)`  
  - **Get**: `get_function()`  

---

### **Functions (Enum)**  
List of available functions with descriptions:  

- **FUNC_SIN** (0): Sine of input.  
- **FUNC_COS** (1): Cosine of input.  
- **FUNC_TAN** (2): Tangent of input.  
- **FUNC_SATURATE** (13): Clamps input to [0, 1].  
- **FUNC_ABS** (17): Absolute value.  
- **FUNC_LOG** (26): Natural logarithm.  
- **FUNC_EXP** (27): Exponential.  
- **FUNC_MAX** (32): Enum size (32 entries).  

*(Example: `FUNC_SIN` → `sin(x)`; `FUNC_LOG` → `log(x)`)*  

---

### **Key Functions**  
- **FUNC_DEGREES**: Convert radians to degrees.  
- **FUNC_RADIANS**: Convert degrees to radians.  
- **FUNC_RECIPROCAL**: `1 / x`.  
- **FUNC_TRUNC**: Truncate decimal part.  
- **FUNC_ROUNDEVEN**: Round to nearest even integer.  

---

### **Function Mapping**  
Each enum value corresponds to a mathematical operation, as shown in the property description. Use `get_function()` to retrieve the current function.