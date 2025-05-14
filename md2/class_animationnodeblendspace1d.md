**AnimationNodeBlendSpace1D**  
Inherits from `AnimationNode`.  

---

### **Description**  
A blend space for animating between multiple nodes along a virtual axis. Points on the axis represent nodes, and blending interpolates between them based on a value.  

---

### **Tutorials**  
- [AnimationNode documentation](#)  
- [Blend Space Example](#)  

---

### **Properties**  
- **blend_mode**: Default value `"value"`. Label for the virtual axis.  
- **max_space**: Default `-1.0`. Upper limit for the virtual axis.  
- **min_space**: Default `1.0`. Lower limit for the virtual axis.  
- **snap**: Default `0.1`. Increment to snap to when adjusting points.  
- **sync**: Default `false`. If `true`, blended animations advance frames.  
- **value_label**: Default `"value"`. Axis label.  

---

### **Methods**  
- **add_blend_point(node, pos, at_index=-1)**: Adds a node to the virtual axis at a position.  
- **get_blend_point_count()**: Returns the number of points on the axis.  
- **get_blend_point_node(point)**: Retrieves the node at a specific index.  
- **get_blend_point_position(point)**: Gets the position of a point.  
- **remove_blend_point(point)**: Removes a point from the axis.  
- **set_blend_point_node(point, node)**: Updates the node at a specific index.  
- **set_blend_point_position(point, pos)**: Adjusts the position of a point.  

---

### **Enumerations**  
- **BLEND_MODE_INTERPOLATED**: Linear interpolation between points.  
- **BLEND_MODE_DISCRETE**: Step between points.  
- **BLEND_MODE_DISCRETE_CARRY**: Continuously carry the last value between points.  

---

### **Notes**  
- **sync**: If `false`, blending stops at `0`. If `true`, animations advance frames.  
- **snap**: Adjusts point positions when moving them on the axis.