**Class Name:** VisualShaderNodeUIntOp  
**Inherits:** VisualShaderNode < Resource < RefCounted < Object  

---  

**Description**  
Applies an operator to two unsigned integer inputs: `a` and `b`.  

---  

**Properties**  
- **operator**: `Operator` (default: 0)  
  - Specifies the operation to apply to inputs `a` and `b`.  

---  

**Enumerations**  
**Operator**  
- **OP_ADD** = 0  
  - Sums two numbers using `a + b`.  
- **OP_SUB** = 1  
  - Subtracts two numbers using `a - b`.  
- **OP_MUL** = 2  
  - Multiplies two numbers using `a * b`.  
- **OP_DIV** = 3  
  - Divides two numbers using `a / b`.  
- **OP_MOD** = 4  
  - Calculates the remainder of two numbers using `a % b`.  
- **OP_MAX** = 5  
  - Returns the greater of two numbers. Translates to `max(a, b)`.  
- **OP_MIN** = 6  
  - Returns the lesser of two numbers. Translates to `max(a, b)`.  
- **OP_BITWISE_AND** = 7  
  - Returns the result of bitwise `AND` operation. Translates to `a & b`.  
- **OP_BITWISE_OR** = 8  
  - Returns the result of bitwise `OR` operation. Translates to `a | b`.  
- **OP_BITWISE_XOR** = 9  
  - Returns the result of bitwise `XOR` operation. Translates to `a ^ b`.  
- **OP_BITWISE_LEFT_SHIFT** = 10  
  - Returns the result of bitwise left shift operation. Translates to `a << b`.  
- **OP_BITWISE_RIGHT_SHIFT** = 11  
  - Returns the result of bitwise right shift operation. Translates to `a >> b`.  
- **OP_ENUM_SIZE** = 12  
  - Represents the size of the `Operator` enum.  

---  

**Property Descriptions**  
**operator**  
- **Type:** `Operator`  
- **Default Value:** 0  
- **Methods:**  
  - `set_operator(value: Operator)`  
  - `get_operator()`  
- **Note:** This method should typically be overridden by the user to have any effect.