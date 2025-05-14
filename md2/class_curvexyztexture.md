**Class:** CurveXYZTexture  
**Inherits:** Texture2D → Texture → Resource → RefCounted → Object  

---

### **Description**  
A 1D texture where red, green, and blue channels map to 3 unit curves. Simplifies saving curves as images. Use `CurveTexture` for single curves. See also `GradientTexture1D`, `GradientTexture2D`.  

---

### **Properties**  
- `curve_x`: A unit `Curve` mapped to the red channel.  
- `curve_y`: A unit `Curve` mapped to the green channel.  
- `curve_z`: A unit `Curve` mapped to the blue channel.  
- `resource_local_to_scene`: `false` (overrides Resource property).  
- `width`: 256 (default).  

---

### **Property Details**  
- **curve_x**  
  - **Setter/Getter**: `set_curve_x(value: Curve)`, `get_curve_x()`.  
  - **Note**: Must be a unit `Curve`.  

- **curve_y**  
  - **Setter/Getter**: `set_curve_y(value: Curve)`, `get_curve_y()`.  
  - **Note**: Must be a unit `Curve`.  

- **curve_z**  
  - **Setter/Getter**: `set_curve_z(value: Curve)`, `get_curve_z()`.  
  - **Note**: Must be a unit `Curve`.  

- **width**  
  - **Setter/Getter**: `set_width(value: int)`, `get_width()`.  
  - **Note**: Higher values improve detail but increase generation time/memory usage.  

---

### **Key Notes**  
- All curves must be unit curves (normalized).  
- Adjust `width` for trade-off between detail and performance.  
- Overrides `resource_local_to_scene` to `false` by default.