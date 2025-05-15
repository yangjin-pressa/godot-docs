**VisualShaderNodeIntParameter**

**Inheritance Hierarchy:**
- `VisualShaderNodeIntParameter`
  - Inherits from: `VisualShaderNodeParameter` → `VisualShaderNode` → `Resource` → `RefCounted` → `Object`

**Description:**
A node for handling integer parameters in shaders, allowing customization of value ranges. Supports properties like min, max, and step for value constraints.

---

**Properties:**
- **default_value**  
  Type: `int`  
  Default: `0`  
  Methods:  
  - `void set_default_value(int value)`  
  - `int get_default_value() const`  
  *Note: This method should typically be overridden by the user to have any effect.*

- **min**  
  Type: `int`  
  Default: `0`  
  Methods:  
  - `void set_min(int value)`  
  - `int get_min() const`  
  *Applies only if hint is HINT_RANGE or HINT_RANGE_STEP.*

- **max**  
  Type: `int`  
  Default: `0`  
  Methods:  
  - `void set_max(int value)`  
  - `int get_max() const`  
  *Applies only if hint is HINT_RANGE or HINT_RANGE_STEP.*

- **step**  
  Type: `int`  
  Default: `1`  
  Methods:  
  - `void set_step(int value)`  
  - `int get_step() const`  
  *Applies only if hint is HINT_RANGE_STEP.*

- **enum**  
  Type: `int`  
  Default: `0`  
  Methods:  
  - `void set_enum(int value)`  
  - `int get_enum() const`  

- **enum_hint**  
  Type: `int`  
  Default: `0`  
  Methods:  
  - `void set_enum_hint(int value)`  
  - `int get_enum_hint() const`  

---

**Enumerations:**
- **HINT_NONE**  
  Value: `0`  
  Description: No constraints on value.

- **HINT_RANGE**  
  Value: `1`  
  Description: Value is constrained between min and max.

- **HINT_RANGE_STEP**  
  Value: `2`  
  Description: Value must be a multiple of the step.

---

**Method Descriptions:**
- **_validate()**  
  *const*  
  Description: Validates the parameter's current value against constraints (min, max, step).

- **_set_value(int value)**  
  *virtual*  
  Description: Sets the parameter's value. Overrides the default implementation to enforce constraints.

- **_get_value() const**  
  *virtual*  
  Description: Returns the parameter's current value.

---

**Notes:**
- `enum` and `enum_hint` are used for enum-based parameter definitions.
- `PackedStringArray` is copied when modified, so changes are not persistent across instances.