**Gradient Class**  
Inherits from `Resource` → `RefCounted` → `Object`.  

---

### **Description**  
- Defines a color transition using colored points and interpolation.  
- Similar to `Curve`, but supports color values instead of numerical data.  

---

### **Properties**  
1. **colors**  
   - **Type**: `PackedColorArray`  
   - **Default**: `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)`  
   - **Note**: Setting this updates all colors at once. Use `set_color()` for individual changes.  

2. **offsets**  
   - **Type**: `PackedFloat32Array`  
   - **Default**: `PackedFloat32Array(0, 1)`  
   - **Note**: Setting this updates all offsets at once. Use `set_offset()` for individual changes.  

3. **interpolation_mode**  
   - **Type**: `InterpolationMode`  
   - **Default**: `GRADIENT_INTERPOLATE_LINEAR`  
   - **Note**: Controls interpolation method (e.g., linear, constant, etc.).  

4. **interpolation_color_space**  
   - **Type**: `ColorSpace`  
   - **Default**: `COLOR_SPACE_SRGB`  
   - **Note**: Determines the color space for interpolation.  

---

### **Enumerations**  
#### **InterpolationMode**  
- **GRADIENT_INTERPOLATE_LINEAR**: Linear interpolation between points.  
- **GRADIENT_INTERPOLATE_CONSTANT**: Uses the first or last point for all values (e.g., for gradients with only two colors).  

#### **ColorSpace**  
- **COLOR_SPACE_SRGB**: Standard sRGB color space.  
- **COLOR_SPACE_HSL**: HSL color space (less common, but supports hue shifts).  

---

### **Methods**  
1. **add_point(offset: float, color: Color)**  
   - Adds a new color with the specified offset to the gradient.  

2. **get_color(point: int)**  
   - Returns the color at the specified index.  

3. **get_offset(point: int)**  
   - Returns the offset for the color at the specified index.  

4. **get_point_count()**  
   - Returns the total number of colors in the gradient.  

5. **remove_point(point: int)**  
   - Removes the color at the specified index.  

6. **reverse()**  
   - Reverses the gradient, mirroring points around the middle.  
   - **Note**: May produce unexpected results with `GRADIENT_INTERPOLATE_CONSTANT`.  

7. **sample(offset: float)**  
   - Returns the interpolated color at the specified offset.  

---

### **Key Notes**  
- **Color Space**: `COLOR_SPACE_HSL` supports hue shifts, while `COLOR_SPACE_SRGB` is standard for most use cases.  
- **Interpolation**: `GRADIENT_INTERPOLATE_CONSTANT` uses the first or last color for the entire gradient.  
- **Reverse**: Mirrors the gradient, which may not work as expected with constant interpolation.  

---

### **References**  
- [Oklab](https://en.wikipedia.org/wiki/Oklab_color_space) (mentioned in ColorSpace enum).