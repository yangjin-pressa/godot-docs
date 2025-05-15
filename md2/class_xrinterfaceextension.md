# XRInterfaceExtension Documentation

The `XRInterfaceExtension` class provides a framework for handling extended reality (XR) features in Godot, such as VR, AR, or mixed reality. It includes methods for initializing the interface, managing render targets, applying lens distortion, enabling haptic feedback, and controlling play areas. Below is a detailed documentation of the class and its methods.

---

## Public Methods

### `add_blit`
**Description**  
Blits the render results to the screen, optionally applying lens distortion. This method is called during the `_commit_views` phase of the rendering pipeline.

**Parameters**  
- `render_target`: The render target to blit from.  
- `src_rect`: The source rectangle within the render target.  
- `dst_rect`: The destination rectangle on the screen.  
- `use_layer`: Whether to use a specific layer (e.g., for stereo rendering).  
- `layer`: The layer number (e.g., for双眼 rendering).  
- `apply_lens_distortion`: Whether to apply lens distortion for VR headsets.  
- `eye_center`: The center of the eye for stereo rendering.  
- `k1`, `k2`: Lens distortion coefficients (e.g., for barrel distortion).  
- `upscale`: Scaling factor for the render target.  
- `aspect_ratio`: The aspect ratio for the render target.  

**Usage Notes**  
This method is intended for post-processing effects, overlays, or custom rendering. It should only be called during `_commit_views` to ensure compatibility with the rendering pipeline.

---

### `get_color_texture`
**Description**  
Returns the RID of the color texture buffer for the current frame. This buffer contains the main color data rendered by the interface.

**Returns**  
A `RID` representing the color texture.

**Usage Notes**  
This method is useful for accessing the color buffer directly for post-processing or custom rendering.

---

### `get_depth_texture`
**Description**  
Returns the RID of the depth texture buffer for the current frame. This buffer is used for depth calculations, shadow mapping, and other depth-based effects.

**Returns**  
A `RID` representing the depth texture.

**Usage Notes**  
This method provides access to the depth buffer, which is essential for applications requiring 3D spatial awareness.

---

### `get_render_target_texture`
**Description**  
Returns the RID of a texture associated with a specific render target. This method allows users to access custom render targets defined during the rendering pipeline.

**Parameters**  
- `render_target`: The render target for which the texture is requested.

**Returns**  
A `RID` representing the texture for the specified render target.

**Usage Notes**  
This method is useful for applications that require custom rendering targets, suchity for post-processing or multi-pass rendering.

---

## Private Methods

### `_initialize`
**Description**  
Initializes the XR interface. This method checks for hardware support, sets up necessary resources, and prepares the interface for use.

**Returns**  
`bool`: `true` if initialization is successful, `false` otherwise.

**Usage Notes**  
This method is called internally during the startup of the XR interface and is critical for ensuring the interface is ready for rendering and interaction.

---

### `_is_initialized`
**Description**  
Checks whether the XR interface is currently initialized. This method is a helper for determining the state of the interface.

**Returns**  
`bool`: `true` if the interface is initialized, `false` otherwise.

**Usage Notes**  
This method is used internally to ensure operations are only performed on an initialized interface.

---

### `_post_draw_viewport`
**Description**  
Called after the XR viewport is drawn. This method handles post-processing effects or other operations that need to occur after the main rendering pass.

**Usage Notes**  
This is used for tasks like applying screen effects, post-processing passes, or saving rendered frames.

---

### `_pre_draw_viewport`
**Description**  
Called before the XR viewport is drawn. This method determines whether the viewport should be rendered and prepares any necessary resources.

**Returns**  
`bool`: `true` if the viewport should be rendered, `false` otherwise.

**Usage Notes**  
This is critical for managing rendering states, such as pausing rendering when the user removes the headset.

---

### `_pre_render`
**Description**  
Called before the main rendering pass. This method is used to sync tracking data, prepare the environment, or perform setup tasks before rendering.

**Usage Notes**  
This is a critical step for ensuring accurate tracking and rendering in VR/AR environments.

---

### `_process`
**Description**  
Called before the physics and game processing steps. This method is used to update trackers, handle input, or perform any setup tasks required before the game loop begins.

**Usage Notes**  
This method is essential for maintaining accurate tracking and user interaction in real-time applications.

---

### `_trigger_haptic_pulse`
**Description**  
Triggers a haptic pulse on a specific tracker. This method is used to provide tactile feedback to the user, such as vibrations or force feedback.

**Parameters**  
- `action_name`: The name of the haptic action (e.g., "vibrate").  
- `tracker_name`: The name of the tracker (e.g., "left_hand").  
- `frequency`: The frequency of the haptic pulse (in Hz).  
- `amplitude`: The amplitude of the haptic pulse (e.g., strength of the vibration).  

**Usage Notes**  
This method is used by developers to implement haptic feedback in VR/AR applications, such as vibration feedback for interactions.

---

## Play Area Management

### `set_play_area_mode`
**Description**  
Sets the play area mode for the XR interface. This determines how the environment is rendered and interacts with the user.

**Parameters**  
- `mode`: The desired play area mode (e.g., "infinite", "bounded").

**Returns**  
`bool`: `true` if the mode is set successfully, `false` otherwise.

**Usage Notes**  
This method is used to configure the play area for applications requiring different spatial layouts.

---

### `supports_play_area_mode`
**Description**  
Checks whether a specific play area mode is supported by the XR interface.

**Parameters**  
- `mode`: The play area mode to check.

**Returns**  
`bool`: `true` if the mode is supported, `false` otherwise.

**Usage Notes**  
This method helps developers determine if a specific play area configuration is available.

---

## Anchor Detection

### `_set_anchor_detection_is_enabled`
**Description**  
Enables or disables anchor detection on the XR interface. Anchors are used to track spatial positions in the environment.

**Parameters**  
- `enabled`: A boolean indicating whether anchor detection is enabled.

**Usage Notes**  
This method is internal and is used to configure the interface's ability to track and maintain anchors in the environment.

---

## Summary

The `XRInterfaceExtension` class provides a comprehensive set of methods for managing XR features in Godot, including rendering, haptic feedback, play area management, and custom rendering targets. Developers should use these methods to build immersive VR/AR applications with accurate tracking, rendering, and user interaction.