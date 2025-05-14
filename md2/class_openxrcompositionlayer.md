# OpenXRCompositionLayer Documentation

## Properties

### alpha_mode
**Type:** `int`  
**Description:** Controls how the alpha channel is handled for the composition layer.  
**Notes:**  
- `0`: Transparent (alpha is ignored).  
- `1`: Opaque (alpha is used for blending).  
- Default value: `1`.

---

### android_surface_size
**Type:** `Vector2`  
**Description:** Dimensions of the Android surface used for the composition layer.  
**Notes:**  
- Only applicable if `use_android_surface` is enabled.  
- The surface is created during an active OpenXR session.

---

### use_android_surface
**Type:** `bool`  
**Description:** Enables or disables the use of an Android surface for the composition layer.  
**Notes:**  
- Only works in Android builds.  
- The surface is created during an active OpenXR session.

---

### layer_viewport
**Type:** `Vector4`  
**Description:** Defines the viewport for the composition layer.  
**Notes:**  
- Specifies the screen coordinates (x, y, width, height) in normalized device coordinates (NDC).

---

### enable_depth
**Type:** `bool`  
**Description:** Enables or disables depth testing for the composition layer.  
**Notes:**  
- Default: `true`.

---

### enable_stencil
**Type:** `bool`  
**Description:** Enables or disables stencil testing for the composition layer.  
**Notes:**  
- Default: `true`.

---

### enable_blending
**Type:** `bool`  
**Description:** Enables or disables blending for the composition layer.  
**Notes:**  
- Default: `true`.

---

### enable_culling
**Type:** `bool`  
**Description:** Enables or disables culling for the composition layer.  
**Notes:**  
- Default: `true`.

---

### enable_scissor_test
**Type:** `bool`  
**Description:** Enables or disables the scissor test for the composition layer.  
**Notes:**  
- Default: `true`.

---

## Swapchain State Properties

These properties control the OpenGL ES settings for the swapchain state.

### red_swizzle
**Type:** `Swizzle`  
**Description:** Specifies how the red channel is swizzled.  
**Notes:**  
- Default: `0` (no swizzle).  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### green_swizzle
**Type:** `Swizzle`  
**Description:** Specifies how the green channel is swizzled.  
**Notes:**  
- Default: `0` (no swizzle).  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### blue_swizzle
**Type:** `Swizzle`  
**Description:** Specifies how the blue channel is swizzled.  
**Notes:**  
- Default: `0` (no swizzle).  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### alpha_swizzle
**Type:** `Swizzle`  
**Description:** Specifies how the alpha channel is swizzled.  
**Notes:**  
- Default: `0` (no swizzle).  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### mag_filter
**Type:** `Filter`  
**Description:** Specifies the magnification filter for the swapchain.  
**Notes:**  
- Default: `1` (linear).  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### min_filter
**Type:** `Filter`  
**Description:** Specifies the minification filter for the swapchain.  
**Notes:**  
- Default: `1` (linear).  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### mipmap_mode
**Type:** `MipmapMode`  
**Description:** Specifies the mipmap mode for the swapchain.  
**Notes:**  
- Default: `2` (nearest).  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### max_anisotropy
**Type:** `float`  
**Description:** Specifies the maximum anisotropy for the swapchain.  
**Notes:**  
- Default: `1.0`.  
- Only applicable if the device supports the XR_FB_swapchain_update extension.

### horizontal_wrap
**Type:** `Wrap`  
**Description:** Specifies the horizontal wrap mode for the swapchain.  
**Notes:**  
- Default: `0` (clamp).  
- Only applicable if the device supports the XR_FB_swap_to_depth extension.

### vertical_wrap
**Type:** `Wrap`  
**Description:** Specifies the vertical wrap mode for the swapchain.  
**Notes:**  
- Default: `0` (clamp).  
- Only applicable if the device supports the XR_FB_swap_to_depth extension.

---

## Methods

### get_android_surface
**Return Type:** `JavaObject`  
**Description:** Returns an `android.view.Surface` object if `use_android_surface` is enabled.  
**Notes:**  
- The surface is only created during an active OpenXR session.  
- Returns `null` if not enabled or if the session is not active.

---

### intersects_ray
**Return Type:** `Vector2`  
**Description:** Calculates the UV coordinates where a ray intersects the composition layer.  
**Parameters:**  
- `origin`: Ray origin in global space.  
- `direction`: Ray direction in global space.  
**Notes:**  
- Returns `(-1.0, -1.0)` if no intersection is found.  
- Requires the composition layer to be visible and active.

---

### is_natively_supported
**Return Type:** `bool`  
**Description:** Checks if the OpenXR runtime natively supports the composition layer type.  
**Notes:**  
- Only returns accurate results after the OpenXR session has started.  
- May not be reliable if the session is not active.

---

## Notes

- **Active Session Requirement:** Methods like `get_android_surface` and `is_natively_supported` require an active OpenXR session.  
- **Android-Specific:** The `use_android_surface` property is only valid in Android builds.  
- **Swapchain Settings:** Swapchain state properties (e.g., `mag_filter`, `min_filter`) are only applicable if the device supports the XR_FB_swapchain_update extension.  
- **Viewport Management:** The `layer_viewport` property defines the area of the screen used for rendering.  
- **Depth/Stencil/Blending:** Enabled by default, but can be disabled for performance optimization.  

This documentation provides a comprehensive overview of the `OpenXRCompositionLayer` class, including its properties, methods, and usage notes. Developers should ensure that dependencies (e.g., active session, Android support) are met before using these features.