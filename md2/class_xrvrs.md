# XRVRS

**Inherits:** Object

## Description

Helper class for XR interfaces that generates VRS textures to speed up rendering.

---

## Properties

- **vrs_min_radius**: float = 20.0  
  Minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.

- **vrs_render_region**: Rect2i = Rect2i(0, 0, 0, 0)  
  Render region that the VRS texture will be scaled to when generated.

- **vrs_strength**: float = 1.0  
  Strength used to calculate the VRS density map. Higher values make VRS more noticeable.

---

## Methods

- **make_vrs_texture**(target_size: Vector2, eye_foci: PackedVector2Array) → RID  
  Generates the VRS texture based on a render target size adjusted by VRS tile size. For each eye focal point, a layer is created. Focal points are in NDC coordinates. The result is cached; repeated calls with identical parameters return the cached RID.

---

## Property Descriptions

**vrs_min_radius**  
- Set: void set_vrs_min_radius(value: float)  
- Get: float get_vrs_min_radius()

**vrs_render_region**  
- Set: void set_vrs_render_region(value: Rect2i)  
- Get: Rect2i get_vrs_render_region()

**vrs_strength**  
- Set: void set_vrs_strength(value: float)  
- Get: float get_vrs_strength()