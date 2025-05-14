**CanvasTexture**  
- **Inherits**: `Texture2D` → `Texture` → `Resource` → `Object`  

---

### **Description**  
CanvasTexture is an alternative to `ImageTexture`, allowing normal and specular maps for use with `CanvasItem` nodes.  
- **Note**: Cannot be used in 3D environments.  
- **See this page**: http://wiki.polycount.com/wiki/Normal_Map_Technical_Details#Common_Swizzle_Coordinates  

---

### **Tutorials**  
- [2D Lights and Shadows](https://godotengine.org/documentation/tutorials/)

---

### **Properties**  
- **diffuse_texture**: `Texture2D` (default: none)  
  - Main texture for rendering.  

- **normal_texture**: `Texture2D`  
  - Normal map for lighting. Only affects rendering if `Light2D` is present.  

- **resource_local_to_scene**: `bool` (default: false)  
  - Overrides the `Resource`'s `local_to_scene` setting.  

- **specular_color**: `Color` (default: (1, 1, 1, 1))  
  - Multiplier for specular reflection intensity.  

- **specular_shininess**: `float` (default: 1.0)  
  - Exponent for specular highlights. Higher values create sharper highlights.  

- **specular_texture**: `Texture2D`  
  - Specular map for controlling highlight intensity. Use grayscale or colored maps.  

- **texture_filter**: `TextureFilter` (default: `TextureFilter.LINEAR`)  
  - Filtering mode for rendering.  

- **texture_repeat**: `TextureRepeat` (default: `TextureRepeat.NONE`)  
  - Repeat mode for tiling textures.  

---

### **Method Definitions**  
- **set_diffuse_texture(value: Texture2D)**  
- **get_diffuse_texture()**  
- **set_normal_texture(value: Texture2D)**  
- **get_normal_texture()**  
- **set_resource_local_to_scene(value: bool)**  
- **get_resource_local_to_scene()**  
- **set_specular_color(value: Color)**  
- **get_specular_color()**  
- **set_specular_shininess(value: float)**  
- **get_specular_shininess()**  
- **set_specular_texture(value: Texture2D)**  
- **get_specular_texture()**  
- **set_texture_filter(value: TextureFilter)**  
- **get_texture_filter()**  
- **set_texture_repeat(value: TextureRepeat)**  
- **get_texture_repeat()**  

---

### **Notes**  
- **Normal Maps**: The normal map uses swizzle coordinates (e.g., `R`, `A`, `G`, `B`) for lighting calculations.  
- **3D Limitation**: CanvasTexture is not compatible with 3D environments. Use `Texture` or `ImageTexture` for 3D lighting.