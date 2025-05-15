**Class:** VisualShaderNodeIntFunc  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  

**Description**  
A scalar integer function node for the visual shader graph. Accepts an integer input and applies a function from the `Function` enum.  

---

**Properties**  
- `function`: `Function` (default: 2)  
  - The function to apply to the scalar input. See the `Function` enum for options.  

---

**Enumerations**  
**Function**  
- **FUNC_ABS** = 0  
  - Returns absolute value. Equivalent to `abs(x)` in Godot Shader Language.  
- **FUNC_NEGATE** = 1  
  - Negates the input. Equivalent to `-(x)`.  
- **FUNC_SIGN** = 2  
  - Extracts the sign. Equivalent to `sign(x)`.  
- **FUNC_BITWISE_NOT** = 3  
  - Applies bitwise NOT. Equivalent to `~a`.  
- **FUNC_MAX** = 4  
  - Represents the size of the `Function` enum.  

---

**Property Descriptions**  
**function**  
- **set_function**(value: Function): void  
- **get_function**(): Function  
  - Sets/gets the function to apply to the scalar input.  

---

**Notes**  
- The function is applied to the scalar input port.  
- Functions translate directly to Godot Shader Language operations.  
- `FUNC_MAX` indicates the number of valid function types.