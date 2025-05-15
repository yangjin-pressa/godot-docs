**ProceduralSkyMaterial**  
*Inherits from Node2D*  

---

### **Description**  
A procedural sky material that simulates a sky and horizon with customizable colors, textures, and lighting. It supports features like texture overlays, sun positioning, and debanding to reduce color banding in smooth gradients.

---

### **Properties**  

#### **sky_cover**  
**Type:** `Texture2D`  
**Description:**  
The sky cover texture to use. This texture must use an equirectangular projection. The texture's colors are added to the existing sky color, multiplied by `sky_energy_multiplier` and `sky_cover_modulate`. Suitable for displaying stars at night or clouds during the day.

#### **sky_cover_modulate**  
**Type:** `Color`  
**Description:**  
The tint to apply to the `sky_cover` texture. Adjusts the sky cover's colors or opacity independently of the sky energy. Only effective if a texture is defined in `sky_cover`.

#### **sky_energy_multiplier**  
**Type:** `float`  
**Description:**  
Multiplier for sky color. A higher value makes the sky brighter. Influences the intensity of the sky color when combined with the `sky_cover` texture.

#### **sky_curve**  
**Type:** `float`  
**Description:**  
Controls how quickly the `sky_horizon_color` fades into the `sky_top_color`. A lower value creates a more gradual transition.

#### **sky_top_color**  
**Type:** `Color`  
**Description:**  
Color of the sky at the top. Blends with `sky_horizon_color` to create the upper part of the sky gradient.

#### **sky_horizon_color**  
**Type:** `Color`  
**Description:**  
Color of the sky at the horizon. Blends with `sky_top_color` to create the lower part of the sky gradient.

#### **sun_angle_max**  
**Type:** `float`  
**Description:**  
Distance from the center of the sun where it fades out completely. Defines the edge of the sun's disk in the sky.

#### **sun_curve**  
**Type:** `float`  
**Description:**  
Controls how quickly the sun fades away between the edge of the sun disk and `sun_angle_max`. A lower value creates a more gradual fade.

#### **use_debanding**  
**Type:** `bool`  
**Description:**  
If `true`, enables debanding. Adds noise to reduce banding caused by smooth color transitions in the sky. Default is `true`.

---

### **Key Features**  
- **Texture Overlay:** Supports custom textures for stars, clouds, or other sky effects.  
- **Sun Positioning:** Uses `sun_angle_max` and `sun_curve` to simulate sun placement.  
- **Color Gradients:** Customizable sky and ground colors with smooth blending.  
- **Lighting Control:** Adjusts brightness via energy multipliers and texture modulation.  

This material is ideal for creating dynamic skies in 3D scenes, with flexibility for weather, time of day, or custom visual effects.