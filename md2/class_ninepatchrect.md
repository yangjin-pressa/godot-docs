**NinePatchRect Overview**  
A class for rendering textures with a 9-slice layout, allowing customizable margins for corners and edges.  

---

### **Key Features**  
- **Texture-based rendering**: Uses a `Texture2D` for visual output.  
- **9-slice margins**: Adjustable margins for corners and edges.  
- **Region sampling**: Defines a rectangular area of the texture to use.  

---

### **Properties**  
- **AxisStretchMode**: axis_stretch_horizontal = 0  
- **AxisStretchMode**: axis_stretch_vertical = 0  
- **bool**: draw_center = true  
- **int**: patch_margin_bottom = 0  
- **int**: patch_margin_left = 0  
- **int**: patch_margin_right = 0  
- **int**: patch_margin_top = 0  
- **Rect2**: region_rect = Rect2(0, 0, 0, 0)  
- **Texture2D**: texture = (default value)  

---

### **Methods**  
- **get_patch_margin (Side)**: Returns the margin size on the specified side.  
- **set_patch_margin (Side, int)**: Sets the margin size on the specified side.  

---

### **Signals**  
- **texture_changed**: Triggered when the texture resource changes.  

---

### **Enumerations**  
- **AxisStretchMode**: Defines stretching behavior for axes.  

---

### **Usage Notes**  
- **Margins**: Set individual margins for non-uniform borders.  
- **Region Rect**: Use to define a specific area of the texture.  
- **Stretch Mode**: Controls how the texture is stretched in different directions.  

--- 

This class is ideal for creating resizable UI elements with fixed corners and scalable edges.