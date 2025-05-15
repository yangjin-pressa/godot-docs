**RibbonTrailMesh**  
A class for handling particle trails in Godot.  

---

### **Description**  
RibbonTrailMesh is used to create and manage particle trails in 3D environments. It allows for dynamic visual effects by tracking the movement of particles over time.  

---

### **Tutorials**  
- [3D Particle trails](../tutorials/3d/particles/trails)  
- [Particle systems (3D)](../tutorials/3d/particles/index)  

---

### **Properties**  
1. **curve**  
   - **Type:** Curve  
   - **Default:** 0  
   - Defines the shape of the particle trail.  

2. **section_length**  
   - **Type:** float  
   - **Default:** 0.2  
   - Controls the length of each segment in the trail.  

3. **section_radius**  
   - **Type:** float  
   - **Default:** 0.1  
   - Determines the radius of each segment.  

4. **start_offset**  
   - **Type:** Vector3  
   - **Default:** (0, 0, 0)  
   - Adjusts the starting position of the trail.  

5. **end_offset**  
   - **Type:** Vector3  
   - **Default:** (0, 0, 0)  
   - Modifies the ending position of the trail.  

6. **lifetime**  
   - **Type:** float  
   - **Default:** 1.0  
   - Sets the duration for which the trail is visible.  

7. **emission_rate**  
   - **Type:** float  
   - **Default:** 10.0  
   - Controls how many particles are emitted per second.  

---

### **Enumerations**  
- **Shape**  
  - **SHAPE_FLAT**  
    - A flat, 2D trail.  
  - **SHAPE_CROSS**  
    - A cross-shaped trail with vertical segments.  

---

### **Key Methods**  
- **set_curve(value)**  
  - Sets the trail shape.  
- **get_curve()**  
  - Retrieves the current shape.  
- **set_section_length(value)**  
  - Adjusts segment length.  
- **get_section_length()**  
  - Gets the current segment length.  
- **set_section_radius(value)**  
  - Modifies segment radius.  
- **get_section_radius()**  
  - Retrieves segment radius.  

---

This class is essential for creating dynamic, visually engaging particle effects in 3D scenes. Adjust properties to customize the trail’s appearance and behavior.