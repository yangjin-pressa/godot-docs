**Light3D Class Documentation**

---

### **Properties**

#### **Light Properties**
- **light_color**: `Color`  
  The color of the light. Default: `Color(1, 1, 1, 1)`.  
  Controls the hue and intensity of the light.

- **light_temperature**: `float`  
  The temperature of the light in Kelvin. Default: `6500.0`.  
  Used to calculate correlated colors for rendering.

- **light_intensity**: `float`  
  The intensity of the light. Default: `1.0`.  
  Determines the strength of the light's effect.

- **light_range**: `float`  
  The maximum distance the light affects. Default: `0.0`.  
  Controls the area of influence.

- **light_shadow_enabled**: `bool`  
  Whether the light casts shadows. Default: `false`.  
  Enabling this adds real-time shadow rendering but has performance costs.

- **distance_fade_enabled**: `bool`  
  Whether the light fades out at a distance. Default: `false`.  
  Helps hide the light when far from the camera.

- **light_ambient**: `float`  
  Ambient light component. Default: `0.0`.  
  Adds a base level of lighting to the scene.

- **light_specular**: `float`  
  Specular light component. Default: `0.0`.  
  Controls highlights and reflections.

---

#### **Shadow Settings**
- **shadow_enabled**: `bool`  
  Whether the light casts shadows. Default: `false`.  
  Enabling this adds real-time shadow rendering but has performance costs.

- **shadow_blur**: `float`  
  Shadow edge blur amount. Default: `1.0`.  
  Reduces pixel artifacts but may impact performance.

- **shadow_caster_mask**: `int`  
  Mask for shadow-casting layers. Default: `4294967295` (all layers).  
  Only objects in specified layers cast shadows.

- **shadow_normal_bias**: `float`  
  Normal bias for shadow maps. Default: `2.0`.  
  Reduces self-shadowing artifacts.

- **shadow_opacity**: `float`  
  Shadow map opacity. Default: `1.0`.  
  Lower values make shadows more transparent.

- **shadow_reverse_cull_face**: `bool`  
  Whether to reverse backface culling for shadows. Default: `false`.  
  Useful for meshes that need shadows on both sides.

- **shadow_bias**: `float`  
  Shadow map offset. Default: `0.1`.  
  Adjusts for self-shadowing or shadow separation.

- **shadow_transmittance_bias**: `float`  
  Shadow transmittance offset. Default: `0.05`.  
  Currently no description.  

---

#### **Light Parameters**
- **Param**: `enum`  
  Enum for specifying light parameters (e.g., intensity, color, range).

---

### **Methods**

#### **get_correlated_color()**
- **Returns**: `Color`  
  Returns the color of an idealized blackbody at the current light temperature.  
  Used for calculating correlated colors in rendering.

#### **get_param(param: Param)**
- **Returns**: `float`  
  Retrieves the value of the specified parameter.  
  `param` is an enum specifying which light property to get (e.g., intensity, color).

#### **set_param(param: Param, value: float)**
- **Sets**: the value of a specified parameter.  
  `param` is an enum specifying which light property to set (e.g., intensity, color).  
  `value` is the new value for the parameter.

---

### **Notes**
- **shadow_transmittance_bias**: No description available.  
  Please contribute a description to improve the documentation.

---

This documentation outlines the properties and methods of the `Light3D` class in Godot, providing clear explanations for each attribute and function. Developers can use these properties to customize light behavior and shadows in 3D scenes.