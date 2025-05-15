**Class: VisualShaderNodeCubemap**  
**Inherits:** VisualShaderNode → Resource → RefCounted → Object  

---

### **Description**  
Translated to `texture(cubemap, vec3)` in the shader language. Returns a color vector and alpha channel as scalar.  

---

### **Properties**  
- **cube_map**:  
  - Type: TextureLayered  
  - Description: Cubemap texture to sample when using `SOURCE_TEXTURE`.  
  - Methods:  
    - `set_cube_map(value: TextureLayered)`  
    - `get_cube_map()`  

- **source**:  
  - Type: Source  
  - Default: `0`  
  - Description: Defines the source for sampling.  
  - Methods:  
    - `set_source(value: Source)`  
    - `get_source()`  

- **texture_type**:  
  - Type: TextureType  
  - Default: `0`  
  - Description: Defines the data type of the source texture.  
  - Methods:  
    - `set_texture_type(value: TextureType)`  
    - `get_texture_type()`  

---

### **Enumerations**  

#### **Source**  
- `SOURCE_TEXTURE` = 0  
  - Uses the cubemap set via `cube_map`.  
- `SOURCE_PORT` = 1  
  - Uses the samplerCube port.  
- `SOURCE_MAX` = 2  
  - Represents the size of the Source enum.  

#### **TextureType**  
- `TYPE_DATA` = 0  
  - No hints added to the uniform declaration.  
- `TYPE_COLOR` = 1  
  - Adds `source_color` hint for sRGB to linear conversion.  
- `TYPE_NORMAL_MAP` = 2  
  - Adds `hint_normal` hint for normal map usage.  
- `TYPE_MAX` = 3  
  - Represents the size of the TextureType enum.  

---

### **Key Notes**  
- The node samples a cubemap texture based on the selected source (`SOURCE_TEXTURE` or `SOURCE_PORT`).  
- The `texture_type` property influences how the texture is interpreted in the shader.