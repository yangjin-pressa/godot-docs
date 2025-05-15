**Class: WorldBoundaryShape2D**  
**Inherits:** Shape2D → Resource → RefCounted → Object  

---

### **Description**  
A 2D world boundary shape used for physics collision. Acts as an infinite straight line that enforces physics bodies to stay on one side of the line. The normal defines the "above" direction.  

---

### **Properties**  
- **distance**  
  - Type: `float`  
  - Default: `0.0`  
  - Description: Distance from the origin to the line, measured along the normal. Absolute distance is `abs(distance) / normal.length()`.  

- **normal**  
  - Type: `Vector2`  
  - Default: `Vector2(0, -1)`  
  - Description: Line's normal vector (unit vector). Direction indicates the non-colliding half-plane.  

---

### **Methods**  
- **set_distance(value: float)**  
  - Sets the distance property.  

- **get_distance()**  
  - Retrieves the distance property.  

- **set_normal(value: Vector2)**  
  - Sets the normal property.  

- **get_normal()**  
  - Retrieves the normal property.  

---

### **Notes**  
- The line equation `ax + by = d` corresponds to `distance` as `d`, with `(a, b)` from the normal.  
- The normal can be any length (non-zero) but is typically a unit vector.  
- This shape is used for constraints like endless floors or barriers.  

---  

**Citations**  
- [distance](#class_WorldBoundaryShape2D_property_distance)  
- [normal](#class_WorldBoundaryShape2D_property_normal)