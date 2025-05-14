# CompositorEffect

**Experimental:** The implementation may change as more of the rendering internals are exposed over time.

**Inherits:** Resource → RefCounted → Object

This resource allows for creating a custom rendering effect. It defines a callback for inserting additional passes during the rendering pipeline.

---

## Description
- **Purpose:** Custom rendering effect applied to Viewports via Environment.
- **Key Features:**
  - Callback called during rendering at specific pipeline stages.
  - Runs on the rendering thread.
  - Abstract base class; must be extended for implementation.

---

## Tutorials
- [The Compositor](#) (tutorial)

---

## Properties
- **access_resolved_color**: bool  
  Triggers color buffer resolve before effect if MSAA is enabled.
- **access_resolved_depth**: bool  
  Triggers depth buffer resolve before effect if MSAA is enabled.
- **needs_motion_vectors**: bool  
  Requires motion vectors during opaque render state.
- **needs_normal_roughness**: bool  
  Requires normal/roughness data during depth pre-pass (Forward+ only).
- **needs_separate_specular**: bool  
  Requires specular buffer for post-effect combination (Forward+ only).

---

## Method
- **_render_callback(effect_callback_type: int, render_data: RenderData)**  
  Virtual method for custom rendering.  
  - `effect_callback_type` must match the specified effect callback type.  
  - `render_data` contains rendering state but is only valid during rendering.

---

## Enum: EffectCallbackType
- **0**: Pre-Forward (before forward pass)
- **1**: Forward (during forward pass)
- **2**: Post-Forward (after forward pass)
- **3**: Pre-Shadow (before shadow pass)
- **4**: Shadow (during shadow pass)
- **5**: Post-Shadow (after shadow pass)
- **6**: Post-All (after all passes)

---

## Notes
1. **Motion vectors**: Access via `render_scene_buffers.get_velocity_texture()`.
2. **Normal/roughness buffer**: Use `normal_roughness_compatibility()` conversion function (see [GitHub link](https://github.com/godotengine/godot/blob/da5f39889f155658cef7f7ec3cc1abb94e17d815/servers/rendering/renderer_rd/shaders/forward_clustered/scene_forward_clustered_inc.glsl#L334-L341)).