**NoiseTexture2D**  
A class for generating noise textures in Godot, using a Noise resource.  

---

### **Description**  
This class generates textures based on a Noise resource. Example usage:  
```  
var texture = NoiseTexture2D()  
texture.width = 1024  
texture.height = 768  
texture.noise = Noise()  
texture.generate()  
```  

---

### **Properties**  
- **width**: Integer, default 512. Width of the generated texture.  
- **height**: Integer, default 512. Height of the generated texture.  
- **noise**: Noise instance. The Noise resource used to generate the texture.  
- **invert**: Boolean, default false. Invert the noise texture (white becomes black).  
- **normalize**: Boolean, default true. Normalize the noise output to 0.0–1.0.  
- **seamless**: Boolean, default false. Generate seamless noise textures.  
- **seamless_blend_skirt**: Float, default 0.1. Controls seamless blending quality.  
- **as_normalized**: Boolean, default true. Use normalized noise for consistent results.  

---

### **Property Details**  
- **width**  
  - **Set/Get**: `set_width(value)`, `get_width()`  
  - **Description**: Sets the width of the texture.  

- **height**  
  - **Set/Get**: `set_height(value)`, `get_height()`  
  - **Description**: Sets the height of the texture.  

- **noise**  
  - **Set/Get**: `set_noise(value)`, `get_noise()`  
  - **Description**: Assigns the Noise resource to generate the texture.  

- **invert**  
  - **Set/Get**: `set_invert(value)`, `get_invert()`  
  - **Description**: Inverts the texture colors.  

- **normalize**  
  - **Set/Get**: `set_normalize(value)`, `get_normalize()`  
  - **Description**: Ensures noise is normalized to 0.0–1.0.  

- **seamless**  
  - **Set/Get**: `set_seamless(value)`, `get_seamless()`  
  - **Description**: Generates seamless noise textures (may take longer).  

- **seamless_blend_skirt**  
  - **Set/Get**: `set_seamless_blend_skirt(value)`, `get_seamless_blend_skirt()`  
  - **Description**: Controls blending distance for seamless textures.  

- **as_normalized**  
  - **Set/Get**: `set_as_normalized(value)`, `get_as_normalized()`  
  - **Description**: Ensures output is normalized for consistency.  

---

### **Important Notes**  
1. **Seamless Noise**:  
   - Seamless textures may take longer to generate and have lower contrast.  
   - Increase `seamless_blend_skirt` for better blending when using smaller dimensions.  

2. **Normalization**:  
   - Disabling normalization can affect contrast and allow non-repeating noise.  

3. **FastNoiseLite**:  
   - The default implementation uses FastNoiseLite for seamless generation.  

4. **Texture Generation**:  
   - The `generate()` method must be called to apply settings to the texture.  

--- 

This class provides flexibility for creating procedural textures using noise algorithms.