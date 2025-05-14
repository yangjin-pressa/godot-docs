**Class Name**: NoiseTexture3D  
**Inheritance**: Not explicitly stated in the provided text.  

---

### **Description**  
NoiseTexture3D uses the **Noise** class for generating textures. It is threaded, meaning operations are performed asynchronously. Example code to create and use the class:  
```  
var texture = NoiseTexture3D.new()  
texture.noise = FastNoiseLite.new()  
await texture.changed  
var data = texture.get_data()  
```  

---

### **Properties**  

1. **width** (int, default 64)  
   - **Description**: Width of the generated texture (in pixels).  
   - **Methods**: `set_width(value)`  

2. **height** (int, default 64)  
   - **Description**: Height of the generated texture (in pixels).  
   - **Methods**: `set_height(value)`  

3. **seamless_blend_skirt** (float, default 0.0)  
   - **Description**: Used for seamless texture generation. Determines the distance over which seams are blended. High values reduce detail and contrast.  
   - **Methods**: `set_seamless_blend_skirt(value)`  

4. **seamless** (bool, default false)  
   - **Description**: Enables seamless texture generation.  
   - **Methods**: `set_seamless(value)`  

5. **noise** (Noise, default null)  
   - **Description**: Reference to the Noise instance used for generating the texture.  
   - **Methods**: `set_noise(value)`  

---

### **Notes**  
- **Seamless Textures**: The `seamless` property controls whether the texture is seamless. For optimal results, ensure `seamless_blend_skirt` is adjusted appropriately.  
- **Thread Safety**: The class is designed for concurrent use, but `await texture.changed` is required to trigger updates.  
- **Source Code**: The class is implemented in `NoiseTexture3D.cpp` and `NoiseTexture3D.hpp`.  

---

### **Citations**  
- **Noise**: A class used for generating procedural textures.  
- **FastNoiseLite**: A library for noise generation.  
- **Texture**: Base class for texture handling in Godot.