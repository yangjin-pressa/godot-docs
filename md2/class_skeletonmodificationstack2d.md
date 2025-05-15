**SkeletonModificationStack2D**  
*Experimental class for managing modifications to a skeleton.*

---

### **Inheritance**  
- `Resource`  
- `RefCounted`  
- `Object`  

---

### **Description**  
Controls the order and strength of modifications applied to a skeleton. Crucial for full-body IK setups. Modifications are applied in the order they are added to the stack. For example, spine modifications should precede arm modifications to ensure proper hierarchy.

---

### **Properties**  
- **enabled**  
  - **Type**: `bool`  
  - **Default**: `false`  
  - **Description**: Whether the modification stack is active.  

- **modification_count**  
  - **Type**: `int`  
  - **Default**: `0`  
  - **Description**: Number of modifications in the stack.  

- **strength**  
  - **Type**: `float`  
  - **Default**: `1.0`  
  - **Description**: Overall strength multiplier for all modifications.  

---

### **Methods**  
- **add_modification(modification: SkeletonModification2D)**  
  - **Description**: Adds a modification to the stack.  

- **delete_modification(mod_idx: int)**  
  - **Description**: Removes the modification at the specified index.  

- **enable_all()**  
  - **Description**: Enables all modifications in the stack.  

- **execute()**  
  - **Description**: Applies all modifications in the stack, in order.  
  - **Note**: Order of modifications affects results. For example, spine modifications should precede arm modifications.  

- **get_is_setup()**  
  - **Description**: Returns whether the stack is ready to execute.  

- **get_modification(mod_idx: int)**  
  - **Description**: Retrieves the modification at the specified index.  

- **get_skeleton()**  
  - **Description**: Returns the associated `Skeleton2D` node.  

- **set_modification(mod_idx: int, modification: SkeletonModification2D)**  
  - **Description**: Replaces the modification at the specified index.  

- **setup()**  
  - **Description**: Initializes the stack for execution. This is usually called by `Skeleton2D`.  

---

### **Key Notes**  
- **Order matters**: Modifications are applied in the order they are added to the stack.  
- **Setup required**: `setup()` must be called by `Skeleton2D` before execution.  
- **Strength control**: The `strength` property affects all modifications uniformly.