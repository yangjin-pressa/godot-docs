# OpenXRAPIExtension Class

## Overview
The `OpenXRAPIExtension` class provides a comprehensive set of methods for interacting with the OpenXR API, enabling advanced 3D rendering, spatial tracking, and environment blending in Godot. This class acts as a bridge between Godot's rendering pipeline and the OpenXR framework, allowing developers to configure spatial reference spaces, manage render regions, handle velocity textures, and perform pose transformations.

---

## Key Features
- **Spatial Reference Space Management**: Set and retrieve custom play spaces for 3D positioning.
- **Render Region Control**: Define custom render regions for optimized rendering.
- **Velocity Textures**: Manage velocity and depth textures for motion tracking.
- **Pose Transformations**: Convert OpenXR poses to Godot's `Transform3D` format.
- **Extension Registration**: Register/unregister custom extensions for frame info, composition layers, and projection views.
- **Environment Blending**: Emulate alpha blending for specific rendering modes.
- **Debugging Tools**: Set object names for debug output and handle XR result codes.

---

## Methods

### 1. **Play Space Management**
```godot
void set_custom_play_space(const void* space)
```
Sets the reference space used by OpenXR to the provided `XrSpace` (cast to a `void*` pointer).

```godot
void get_custom_play_space(void* out_space)
```
Retrieves the current custom play space as a `void*` pointer.

---

### 2. **Render Region Control**
```godot
void set_render_region(const Rect2i& render_region)
```
Sets the render region to override the default render target's rect.

```godot
void get_render_region(Rect2i& out_region)
```
Retrieves the current render region.

---

### 3. **Velocity Textures**
```godot
void set_velocity_depth_texture(const RID& render_target)
```
Sets the render target for the velocity depth texture.

```godot
void set_velocity_texture(const RID& render_target)
```
Sets the render target for the velocity texture.

```godot
void set_velocity_target_size(const Vector2i& target_size)
```
Sets the target size for velocity and velocity depth textures.

---

### 4. **Pose Transformations**
```godot
Transform3D transform_from_pose(const void* pose)
```
Converts an `XrPosef` structure into a `Transform3D` for 3D space transformations.

---

### 5. **Extension Registration**
```godot
void register_composition_layer_provider(const Ref<OpenXRExtensionWrapper>& extension)
```
Registers an extension as a composition layer provider for custom layer handling.

```godot
void register_frame_info_extension(const Ref<OpenXRExtensionWrapper>& extension)
```
Registers an extension to modify frame info via virtual methods.

```godot
void register_projection_views_extension(const Ref<OpenXRExtensionWrapper>& extension)
```
Registers an extension to provide additional data structures for projections.

```godot
void unregister_composition_layer_provider(const Ref<OpenXRExtensionWrapper>& extension)
```
Unregisters an extension as a composition layer provider.

```godot
void unregister_frame_info_extension(const Ref<OpenXRExtensionWrapper>& extension)
```
Unregisters an extension modifying frame info.

```godot
void unregister_projection_views_extension(const Ref<OpenXRExtensionWrapper>& extension)
```
Unregisters an extension as a projection views provider.

---

### 6. **Environment Blending**
```godot
void set_emulate_environment_blend_mode_alpha_blend(bool enabled)
```
Enables/disables an extension for emulating alpha blending in the environment.

---

### 7. **Object Debugging**
```godot
void set_object_name(int object_type, int object_handle, const String& object_name)
```
Sets the name of an OpenXR object for debug output. `object_type` must be a valid `XrObjectType`, and `object_handle` must be a valid OpenXR handle.

---

### 8. **XR Result Handling**
```godot
bool xr_result(int result, const String& format, const Array& args)
```
Checks if an `XrResult` (cast to an integer) is successful. Returns `false` on failure and prints the error message with additional context.

---

## Notes
- **Virtual Methods**: Methods like `xr_result` are virtual and should be overridden by subclasses for custom behavior.
- **Const Methods**: Methods like `get_custom_play_space` are const and do not modify the instance.
- **Internal Usage**: Some methods (e.g., `set_custom_play_space`) are internal and not meant for direct user interaction.
- **OpenXR Dependency**: This class relies on the OpenXR API and requires proper initialization in the engine.

---

## Example Usage
```godot
// Set a custom play space
void set_custom_play_space(const void* space) {
    // Assume 'space' is a valid XrSpace pointer
    // This is used to define a reference frame for 3D positioning
}

// Convert an XrPosef to Godot's Transform3D
Transform3D transform = transform_from_pose(pose_pointer);
```

---

This class is essential for developing immersive 3D applications with OpenXR, enabling precise control over spatial tracking, rendering, and environment interactions.