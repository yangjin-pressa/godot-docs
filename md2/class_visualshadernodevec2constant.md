**Class:** VisualShaderNodeVec2Constant  
**Inherits:** VisualShaderNodeConstant → VisualShaderNode → Resource → RefCounted → Object  

---

**Description**  
A constant Vector2 used as an input node in the visual shader graph.  

---

**Properties**  
- **constant**: Vector2 = Vector2(0, 0)  
  - A Vector2 constant representing this node's state.  

---

**Methods**  
- **set_constant(value: Vector2)**  
  - Sets the constant value.  

- **get_constant()**  
  - Returns the current constant value.  

---

**Notes**  
- The `constant` property is a virtual method (can be overridden).  
- The `set_constant` and `get_constant` methods are const (no side effects).  

---

**References**  
- [Vector2](https://github.com/godotengine/godot/tree/master/doc/classes/Vector2)  
- [VisualShaderNodeConstant](https://github.com/godotengine/godot/tree/master/doc/classes/VisualShaderNodeConstant)