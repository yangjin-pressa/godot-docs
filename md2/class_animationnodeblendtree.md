**AnimationNodeBlendTree**  
A class representing a sub-tree of other animation nodes, used by `AnimationTree`.  

---

### **Description**  
- A sub-tree of other animation nodes.  
- Used by `AnimationTree` to manage complex animation logic.  

---

### **Tutorials**  
- Link to tutorials (example: [Tutorials](#)).  

---

### **Properties**  
- **graph_offset**: A value that offsets the position of sub-animations.  

---

### **Methods**  
- **get_node(name: StringName)**  
  Returns the sub animation node with the specified name.  

- **get_node_list()**  
  Returns a list of names of all sub animation nodes.  

- **get_node_position(name: StringName)**  
  Returns the position of the sub animation node with the specified name.  

- **has_node(name: StringName)**  
  Returns `true` if a sub animation node with the specified name exists.  

- **remove_node(name: StringName)**  
  Removes a sub animation node.  

- **rename_node(name: StringName, new_name: StringName)**  
  Changes the name of a sub animation node.  

- **set_node_position(name: Stringity, position: Vector2)**  
  Modifies the position of a sub animation node.  

---

### **Signals**  
- **node_signal**: Emitted when a node is added or removed.  

---

### **Constants**  
- **NOT_SET**: A constant value for when a node is not set.  

--- 

This summary preserves the original structure and terminology without markdown, focusing on key details and functionality.