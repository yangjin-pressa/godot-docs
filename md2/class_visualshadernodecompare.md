**Class: VisualShaderNodeCompare**  
**Inherits from:** VisualShaderNode  

---

### **Description**  
A node for performing comparisons between values.  

---

### **Properties**  
1. **condition**: `Condition` (0)  
   - Extra condition for vector types.  
   - **Set/Get**: `set_condition(value: Condition)`, `get_condition()`.  

2. **function**: `Function` (0)  
   - Comparison function.  
   - **Set/Get**: `set_function(value: Function)`, `get_function()`.  

3. **type**: `ComparisonType` (0)  
   - Type to be used in the comparison.  
   - **Set/Get**: `set_comparison_type(value: ComparisonType)`, `get_comparison_type()`.  

---

### **Enums**  

#### **ComparisonType**  
Defines the data type for comparison.  
- **CTYPE_SCALAR** (0)  
- **CTYPE_SCALAR_INT** (1)  
- **CTYPE_VECTOR_2D** (2)  
- **CTYPE_VECTOR_3D** (3)  
- **CTYPE_VECTOR_4D** (4)  

#### **Function**  
Comparison function options.  
- **FUNCTION_EQUAL** (0)  
  - Used for equality checks.  
- **FUNCTION_NOT_EQUAL** (1)  
  - Used for inequality checks.  
- **FUNCTION_LESS_THAN** (2)  
  - Used for less-than comparisons.  
- **FUNCTION_GREATER_THAN** (3)  
  - Used for greater-than comparisons.  
- **FUNCTION_LESS_THAN_EQUAL** (4)  
  - Used for less-than-or-equal comparisons.  
- **FUNCTION_GREATER_THAN_EQUAL** (5)  
  - Used for greater-than-or-equal comparisons.  
- **FUNCTION_EQUAL_ANY** (6)  
  - Used for any component matching.  
- **FUNCTION_EQUAL_ALL** (7)  
  - Used for all components matching.  

**Note**: Certain functions (e.g., LESS_THAN) are incompatible with `CTYPE_BOOLEAN` or `CTYPE_TRANSFORM`.  

#### **Condition**  
Determines if any or all components meet the condition.  
- **COND_ANY** (1)  
  - Returns true if any component satisfies the function.  
- **COND_ALL** (2)  
  - Returns true only if all components satisfy the function.  

---

### **Property Descriptions**  
- **condition**:  
  - Applies an additional condition when the type is `CTYPE_VECTOR_3D`.  

- **function**:  
  - Specifies the comparison operation (e.g., equal, less than).  

- **type**:  
  - Defines the data type (e.g., scalar, vector) for the comparison.  

--- 

**See also**:  
- `ComparisonType` for type options.  
- `Function` for function details.  
- `Condition` for condition logic.