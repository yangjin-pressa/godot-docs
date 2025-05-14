**CanvasModulate**  
**Inherits:** Node2D < CanvasItem < Node < Object  

---  

### Description  
Applies a color tint to all nodes on a canvas. Only one instance can be used per canvas, though CanvasLayer can render independently.  

---  

### Tutorials  
- 2D lights and shadows: ../tutorials/2d/2d_lights_and_shadows  

---  

### Properties  
- **color**: Color (default: Color(1, 1, 1, 1))  
  - Tint color to apply to the canvas.  

---  

### Methods  
- **set_color(value: Color)**  
  - Sets the tint color.  

- **get_color()**  
  - Returns the current tint color.  

---  

### Notes  
- This method is virtual and should be overridden for custom behavior.  
- The `color` property is a const value, meaning it does not alter instance state.