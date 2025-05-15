# PhysicalSkyMaterial

## Inheritance
- **Material**  
  - **Resource**  
    - **RefCounted**  
      - **Object**

## Description
A material defining a sky for a `Sky` resource using the Preetham analytic daylight model. Offers more realistic skies than `ProceduralSkyMaterial` but is slower and less flexible. Only supports one sun; its color, energy, and direction are derived from the first `DirectionalLight3D` in the scene tree.

---

## Properties

- **energy_multiplier** (float) = 1.0  
  Sky's overall brightness multiplier. Higher values increase sky brightness.

- **ground_color** (Color) = Color(0.1, 0.07, 0.034, 1)  
  Modulates the color on the bottom half of the sky to represent the ground.

- **mie_coefficient** (float) = 0.005  
  Strength of Mie scattering (light scattering from larger particles like water). Influences whitish colors around the sun and horizon.

- **mie_color** (Color) = Color(0.69, 0.729, 0.812, 1)  
  Color of Mie scattering effect. Adjusts for alien-like planetary atmospheres.

- **mie_eccentricity** (float) = 0.8  
  Direction of Mie scattering. 1 = light passes straight forward; -1 = light scatters backward.

- **night_sky** (Texture2D)  
  Texture for the night sky. May be visible during the day if bright enough.

- **rayleigh_coefficient** (float) = 2.0  
  Strength of Rayleigh scattering (light scattering from small particles). Responsible for the blue sky.

- **rayleigh_color** (Color) = Color(0.3, 0.405, 0.6, 1)  
  Color of Rayleigh scattering. Adjusts for alien-like planetary atmospheres (e.g., red for Mars).

- **sun_disk_scale** (float) = 1.0  
  Size of the sun disk. Default based on Sol's perceived size from Earth.

- **turbidity** (float) = 10.0  
  Thickness of the atmosphere. Higher values create foggy atmospheres; lower values result in clearer skies.

- **use_debanding** (bool) = true  
  Enables debanding, which adds noise to reduce color banding in the sky.

---

## Notes
- Properties with default values are listed with their values.  
- `night_sky` has no default value and requires explicit assignment.  
- Mie and Rayleigh scattering properties influence atmospheric appearance and color.  
- `use_debanding` adds noise to mitigate smooth color transitions in the sky.