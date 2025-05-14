The Decal class in Godot is used to create and manage decals, which are 2D textures applied to surfaces in a 3D scene. Below is a structured summary of its key components:

### **Properties**
1. **Textures**:
   - **texture_albedo**: The base color texture for the decal.
   - **texture_emission**: The emission color texture (e.g., glowing effects).
   - **texture_normal**: Per-pixel normal map for detail.
   - **texture_orm**: Combines ambient occlusion, roughness, and metallic data.
   - **texture_ao**: Ambient occlusion texture (if applicable).

2. **Rendering Parameters**:
   - **albedo_mix**: Blends albedo and emission colors (0.0 = only albedo, 1.0 = only emission).
   - **upper_fade**: Fade curve based on distance from the AABB center (positive values only).
   - **lower_fade**: Similar to upper_fade but for the opposite direction.
   - **cull_mode**: Controls culling behavior (e.g., back face culling).
   - **cull_box**: A bounding box to define the decal's visibility range.
   - **cull_box_margin**: Margin around the cull box for visibility.
   - **cull_box_rotation**: Rotation of the cull box.
   - **cull_box_offset**: Offset from the cull box center.
   - **cull_box_scale**: Scaling of the cull box.
   - **cull_box_visible**: Whether the cull box is visible.
   - **cull_box_visible_texture**: Whether the cull box is visible with the texture.
   - **cull_box_visible_texture_offset**: Offset for the texture in the cull box.
   - **cull_box_visible_texture_scale**: Scaling for the texture in the cull box.

3. **Visibility and Culling**:
   - **layers**: Layers the decal is rendered on.
   - **layer_mask**: Mask for which layers the decal is visible.
   - **render_priority**: Priority for rendering the decal.
   - **render_depth**: Depth for the decal.
   - **render_queue**: Queue for rendering the decal.
   - **render_mode**: Rendering mode (e.g., opaque, transparent, etc.).

4. **Texture Settings**:
   - **filter**: Global filter mode for all decal textures (set in ProjectSettings).
   - **wrap**: Texture wrapping mode (e.g., clamp, repeat).

### **Methods**
1. **get_texture(type: DecalTexture)**:
   - Retrieves a texture by type (e.g., `DECAL_TEXTURE_ALBEDO`).
   - Example: `decal.get_texture(Decal.TEXTURE_ALBEDO)`.

2. **set_texture(type: DecalTexture, texture: Texture2D)**:
   - Sets a texture by type.
   - Example: `decal.set_texture(Decal.TEXTURE_ALBEDO, albedo_texture)`.

### **Key Notes**
- **Texture Requirements**: A decal requires at least one of `texture_albedo` or `texture_emission` to be visible. Other textures (normal, ORM) are optional but can add detail.
- **Global Filter Mode**: All decal textures use the same filter mode set in `ProjectSettings`.
- **Cull Box**: Used for efficiently rendering decals only where they are needed, reducing draw calls.
- **Copying Textures**: Use `get_texture` and `set_texture` to copy textures between decals, e.g., for batch creation.

### **Example Use Cases**
- **Basic Decal**: Use `texture_albedo` and `texture_emission` for a colored, emissive decal.
- **Normal Map**: Apply `texture_normal` for bump mapping, combined with `texture_albedo`.
- **ORM-Only Decal**: Use `texture_orm` with `albedo_mix = 0.0` and a placeholder `texture_albedo`.

This class provides flexible control over decal appearance, visibility, and performance, making it ideal for effects like graffiti, UI overlays, or environmental effects.