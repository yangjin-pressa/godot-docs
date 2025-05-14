**CanvasItemMaterial Class**  
*Inherits from: `Material`*

---

### **Description**  
Use a `ShaderMaterial` to more fully customize a material's interactions with a `CanvasItem`. This class provides properties for managing animation and sprite sheet behavior in 2D nodes like `GPUParticles2D` and `CPUParticles2D`.

---

### **Properties**  
| Enum/Property | Type | Default | Description |
|---------------|------|---------|-------------|
| **BlendMode** | Enum | - | Controls how the material blends with other elements. |
| **LightMode** | Enum | - | Determines how light interacts with the material. |
| **particles_animation** | `bool` | `false` | Enables animation features for particles. |
| **particles_anim_speed_max** | `float` | - | Maximum animation speed for particles. |
| **particles_anim_speed_min** | `float` | - | Minimum animation speed for particles. |
| **particles_anim_speed** | `float` | - | Animation speed for particles. |

---

### **Enumerations**  

#### **BlendMode**  
- **`BLEND_MODE_OPAQUE`** (0): No transparency.  
- **`BLEND_MODE_ADDITIVE`** (1): Adds colors without overwriting.  
- **`BLEND_MODE_SUBTRACTIVE`** (2): Subtracts colors.  
- **`BLEND_MODE_MULTIPLY`** (3): Multiplies colors.  
- **`BLEND_MODE_SCREEN`** (4): Screens colors.  
- **`BLEND_MODE_MODULATE`** (5): Modulates colors.  
- **`BLENDity`** (6): Mixes colors based on alpha.  
- **`BLEND_MODE_PREMULTIPLIED`** (7): Uses pre-multiplied colors.  

#### **LightMode**  
- **`LIGHT_MODE_NONE`** (0): No light interaction.  
- **`LIGHT_MODE_1PASS`** (1): Basic lighting.  
- **`LIGHT_MODE_2PASS`** (2): Advanced lighting.  
- **`LIGHT_MODE_SHADER`** (3): Uses a shader for lighting.  

---

### **Property Descriptions**  

- **particles_animation** (bool):  
  If `true`, enables animation features for particles. Requires `particles_anim_speed_max` to be set.  

- **particles_anim_speed_max** (float):  
  Maximum speed for animation.  

- **particles_anim_speed_min** (float):  
  Minimum speed for animation.  

- **particles_anim_speed** (float):  
  Animation speed.  

- **particles_animation** (bool):  
  This property has no effect on non-particle nodes.  

---

### **Notes**  
- `particles_animation` and related properties only affect `GPUParticles2D` and `CPUParticles2D`.  
- Animation speed must be positive for visible effects.  
- Blend and Light modes determine how the material interacts with the scene.