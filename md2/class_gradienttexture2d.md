**GradientTexture2D**  
A class for generating textures based on gradients. Inherits from unspecified base classes.  

---

**Description**  
- Creates textures using a gradient (linear or radial).  
- Supports high dynamic range (HDR) for effects like glows.  
- Related classes: `Gradient`, `Image`, `Environment`.  

---

**Properties**  
- **height** (int): Default 64. Number of vertical color samples from the gradient.  
  - `set_height()`, `get_height()`  
- **width** (int): Default 64. Number of horizontal color samples from the gradient.  
  - `set_width()`, `get_width()`  
- **repeat** (Repeat): Default 0. Controls gradient repetition (e.g., `REPEAT_NONE`, `REPEAT_LINEAR`).  
  - `set_repeat()`, `get_repeat()`  
- **use_hdr** (bool): Default false. Enables HDR support (uses `Image.FORMAT_RGBAF`).  
  - `set_use_hdr()`, `is_using_hdr()`  
- **gradient** (Gradient): The gradient used to fill the texture.  
  - `set_gradient()`, `get_gradient()`  

---

**Enumerations**  
**Fill**  
- **FILL_LINEAR**: Linear gradient.  
- **FILL_RADIAL**: Radial gradient.  

**Repeat**  
- **REPEAT_NONE**: No repetition.  
- **REPEAT_LINEAR**: Repeats linearly.  

---

**Key Features**  
- **Gradient Types**: Linear or radial.  
- **HDR Support**: Toggles between `Image.FORMAT_RGBAF` (HDR) and `Image.FORMAT_RGBA8` (LDR).  
- **Repetition**: Allows gradients to cover the entire texture.