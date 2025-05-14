# CSGCombiner3D

**Inherits:**  
- CSGShape3D  
- GeometryInstance3D  
- VisualInstance3D  
- Node3D  
- Node  
- Object  

---

## Description  
- Combines multiple CSG modifiers into a single structured operation.  
- Encapsulates results of CSG operations from child nodes.  
- Allows sequential operations on separate shape groups.  
- **Note:** CSG nodes are for prototyping, not gameplay. High CPU cost compared to MeshInstance3D.  

---

## Tutorials  
- [Prototyping levels with CSG](../tutorials/3d/csg_tools)  

---

## Method Notes  
- **virtual**: Methods typically overridden by users.  
- **const**: Methods with no side effects.  
- **vararg**: Methods accepting variable arguments.  
- **static**: Methods callable without instance.  
- **operator**: Valid operators for this type.  
- **bitfield**: Integer bitmask for flags.  
- **void**: No return value.  

---

## Key Features  
- Organizes complex shape arrangements.  
- Supports nested CSG operations.  
- Efficient for level design, not real-time performance.