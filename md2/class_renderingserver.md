```cpp
// RenderingServer class documentation

/**
 * Sets the background color of the viewport.
 * @param color The background color to set.
 */
void set_viewport_background_color(const Color& color);

/**
 * Sets the size of the viewport.
 * @param size The new size of the viewport (width, height).
 */
void set_viewport_size(const Vector2& size);

/**
 * Sets the texture to use as the viewport's background.
 * @param texture The texture to use.
 * @param repeat Whether the texture should repeat.
 */
void set_viewport_texture(Texture* texture, bool repeat);

/**
 * Sets the texture filter for the viewport.
 * @param filter The texture filter mode.
 */
void set_viewport_texture_filter(TextureFilter filter);

/**
 * Sets the field of view (FOV) for the viewport.
 * @param fov The new FOV in degrees.
 */
void set_viewport_fov(float fov);

/**
 * Sets the projection type for the viewport.
 * @param projection The projection type (orthographic or perspective).
 */
void set_viewport_projection(Projection projection);

/**
 * Sets the transformation matrix for the viewport.
 * @param transform The transformation matrix.
 */
void set_viewport_transform(const Transform3D& transform);

/**
 * Sets the cull mask for the viewport.
 * @param mask The cull mask value.
 */
void set_viewport_cull_mask(uint32_t mask);

/**
 * Enables or disables occlusion culling for the viewport.
 * @param enabled Whether occlusion culling is enabled.
 */
void set_viewport_occlusion_culling(bool enabled);

/**
 * Sets the maximum distance for occlusion culling.
 * @param distance The maximum distance.
 */
void set_viewport_occlusion_culling_distance(float distance);

/**
 * Sets the mode for occlusion culling.
 * @param mode The occlusion culling mode.
 */
void set_viewport_occlusion_culling_mode(OCCLUSION_CULLING_MODE mode);

/**
 * Sets the density parameter for occlusion culling.
 * @param density The density value.
 */
void set_viewport_occlusion_culling_density(float density);

/**
 * Sets the number of samples for occlusion culling.
 * @param samples The number of samples.
 */
void set_viewport_oc than occlusion_culling_samples(int samples);

/**
 * Sets the maximum density for occlusion culling.
 * @param max_density The maximum density value.
 */
void set_viewport_occlusion_culling_max_density(float max_density);

/**
 * Sets the maximum number of samples for occlusion culling.
 * @param max_samples The maximum number of samples.
 */
void set_viewport_occlusion_culling_max_samples(int max_samples);

/**
 * Sets the threshold for occlusion culling.
 * @param threshold The threshold value.
 */
void set_viewport_occlusion_culling_threshold(float threshold);

/**
 * Sets the camera attributes for the viewport.
 * @param attributes The camera attributes to set.
 */
void set_camera_attributes(const CameraAttributes& attributes);

/**
 * Sets the exposure value for the camera.
 * @param exposure The exposure value.
 */
void set_camera_attributes_exposure(float exposure);

/**
 * Sets the focal length for the camera.
 * @param focal_length The focal length value.
 */
void set_camera_attributes_focal_length(float focal_length);

/**
 * Sets the field of view (FOV) for the camera.
 * @param fov The new FOV in degrees.
 */
void set_camera_attributes_fov(float fov);

/**
 * Sets the projection type for the camera.
 * @param projection The projection type (orthographic or perspective).
 */
void set_camera_attributes_projection(Projection projection);

/**
 * Sets the transformation matrix for the camera.
 * @param transform The transformation matrix.
 */
void set_camera_attributes_transform(const Transform3D& transform);

/**
 * Sets the position of the camera.
 * @param position The new camera position.
 */
void set_camera_attributes_position(const Vector3& position);

/**
 * Sets the rotation of the camera.
 * @param rotation The new camera rotation.
 */
void set_camera_attributes_rotation(const Vector3& rotation);

/**
 * Sets the up vector of the camera.
 * @param up The new up vector.
 */
void set_camera_attributes_up(const Vector3& up);

/**
 * Sets the near clipping plane distance.
 * @param z_near The new near clipping plane distance.
 */
void set_camera_attributes_z_near(float z_near);

/**
 * Sets the far clipping plane distance.
 * @param z_far The new far clipping plane distance.
 */
void set_camera_attributes_z_far(float z_far);

/**
 * Sets the depth value for the camera.
 * @param depth The new depth value.
 */
void set_camera_attributes_depth(float depth);

/**
 * Sets the light mode for the scene.
 * @param mode The light mode (e.g., static, dynamic, etc.).
 */
void set_light_mode(LightMode mode);

/**
 * Sets the sky color for the light.
 * @param color The sky color to set.
 */
void set_light_sky_color(const Color& color);

/**
 * Sets the clearness of the sky.
 * @param clearness The sky clearness value.
 */
void set_light_sky_clearness(float clearness);

/**
 * Sets the exposure value for the sky.
 * @param exposure The sky exposure value.
 */
void set_light_sky_exposure(float exposure);

/**
 * Sets the dithering enable for the sky.
 * @param dither Whether dithering is enabled.
 */
void set_light_sky_dither(bool dither);

/**
 * Sets the density parameter for the sky.
 * @param density The sky density value.
 */
void set_light_sky_density(float density);

/**
 * Creates a new voxel global illumination (GI) instance.
 * @return The newly created voxel GI instance.
 */
VoxelGI* create_voxel_gi();

/**
 * Sets the voxel GI parameters.
 * @param gi The voxel GI instance to set.
 */
void set_voxel_gi(VoxelGI* gi);

/**
 * Sets the bias for the voxel GI.
 * @param bias The bias value.
 */
void set_voxel_gi_bias(float bias);

/**
 * Sets the propagation strength for the voxel GI.
 * @param propagation The propagation strength.
 */
void set_voxel_gi_propagation(float propagation);

/**
 * Sets the energy value for the voxel GI.
 * @param energy The energy value.
 */
void set_voxel_gi_energy(float energy);

/**
 * Sets the light mode for the voxel GI.
 * @param mode The light mode.
 */
void set_voxel_gi_light_mode(LightMode mode);

/**
 * Sets the occlusion culling enable for the voxel GI.
 * @param enabled Whether occlusion culling is enabled.
 */
void set_voxel_gi_occlusion_culling(bool enabled);

/**
 * Sets the visibility of the voxel GI.
 * @param visible Whether the voxel GI is visible.
 */
void set_voxel_gi_visible(bool visible);

/**
 * Sets the render target for the rendering.
 * @param render_target The render target to use.
 */
void set_render_target(RenderTarget* render_target);

/**
 * Sets the render target texture for the rendering.
 * @param render_target_texture The render target texture.
 */
void set_render_target_texture(RenderTargetTexture* render_target_texture);

/**
 * Sets the visibility of the scene.
 * @param visible Whether the scene is visible.
 */
void set_visible(bool visible);

/**
 * Sets the occlusion culling enable for the scene.
 * @param enabled Whether occlusion culling is enabled.
 */
void set_occlusion_culling(bool enabled);

/**
 * Sets the occlusion culling mode for the scene.
 * @param mode The occlusion culling mode.
 */
void set_occlusion_culling_mode(OCCLUSION_CULLING_MODE mode);

/**
 * Sets the occlusion culling density parameter.
 * @param density The occlusion culling density value.
 */
void set_occlusion_culling_density(float density);

/**
 * Sets the occlusion culling samples parameter.
 * @param samples The number of samples.
 */
void set_occlusion_culling_samples(int samples);

/**
 * Sets the maximum density for occlusion culling.
 * @param max_density The maximum density value.
 */
void set_occlusion_culling_max_density(float max_density);

/**
 * Sets the maximum samples for occlusion culling.
 * @param max_samples The maximum number of samples.
 */
void set_occlusion_culling_max_samples(int max_samples);

/**
 * Sets the threshold for occlusion culling.
 * @param threshold The threshold value.
 */
void set_occlusion_culling_threshold(float threshold);

/**
 * Sets the sky color for the light.
 * @param color The sky color to set.
 */
void set_light_sky_color(const Color& color);

/**
 * Sets the clearness of the sky.
 * @param clearness The sky clearness value.
 */
void set_light_sky_clearness(float clearness);

/**
 * Sets the exposure value for the sky.
 * @param exposure The sky exposure value.
 */
void set_light_sky_exposure(float exposure);

/**
 * Sets the dithering enable for the sky.
 * @param dither Whether dithering is enabled.
 */
void set_light_sky_dither(bool dither);

/**
 * Sets the density parameter for the sky.
 * @param density The sky density value.
 */
void set_light_sky_density(float density);
```

This documentation provides a comprehensive list of methods for the `RenderingServer` class in Godot, including their parameters, descriptions, and any important notes. Each method is clearly described with its purpose and the parameters it accepts, ensuring that developers can understand and use the class effectively.