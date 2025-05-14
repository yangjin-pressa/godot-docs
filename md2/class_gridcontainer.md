**Class: GridContainer**  
**Inherits:** `Container` → `Control` → `CanvasItem` → `Node` → `Object`  

---

### **Description**  
A container that arranges its child controls in a grid layout.  
- Columns are specified by the `columns` property.  
- Rows are determined by the number of child controls.  
- The grid layout is preserved for all container sizes.  
- **Note:** Only child nodes inheriting from `Control` are supported.  

---

### **Tutorials**  
- [Using Containers](../tutorials/ui/gui_containers)  
- [Operating System Testing Demo](https://godotengine.org/asset-library/asset/2789)  

---

### **Properties**  
- **columns** (int) = 1  
  - Sets the number of columns in the grid.  
  - Modifying this value reorders child controls to fit the new layout.  

---

### **Theme Properties**  
- **h_separation** (int) = 4  
  - Horizontal separation between child nodes.  
- **v_separation** (int) = 4  
  - Vertical separation between child nodes.  

---

### **Methods**  
- **set_columns(value: int)**  
  - Sets the number of columns.  
- **get_columns()**  
  - Returns the current number of columns.  

---

### **Key Notes**  
- GridContainer only works with `Control`-derived child nodes.  
- Layout is maintained regardless of container size.  
- Theme constants define spacing between child nodes.