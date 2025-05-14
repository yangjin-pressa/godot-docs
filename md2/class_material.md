# Material

## Overview
Virtual base class for applying visual properties to an object, such as color and roughness.

---

## Key Concepts
- **Inherits**: Resource → RefCounted → Object
- **Inherited By**: 
  - BaseMaterial3D
  - CanvasItemMaterial
  - FogMaterial
  - PanoramaSkyMaterial
  - ParticleProcessMaterial
  - PhysicalSkyMaterial
  - PlaceholderMaterial
  - ProceduralSkyMaterial
  - ShaderMaterial

---

## Core Features
- Used for coloring and shading geometry
- All VisualInstance3D nodes use a Material
- Can be extended to create custom materials

---

## Tutorials
- [3D Material Testers Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

---

## Properties
- **next_pass**: Material (Sets material for next render pass)
- **render_priority**: int (Determines rendering order)

---

## Constants
- **RENDER_PRIORITY_MAX**: 127 (Maximum value for render_priority)
- **RENDER_PRIORITY_MIN**: -128 (Minimum value for render_priority)

---

## Methods
### Private Methods
- `_can_do_next_pass()`: Virtual const (Determines if next_pass is visible in editor)
- `_can_use_render_priority()`: Virtual const (Determines if render_priority is visible in editor)
- `_get_shader_mode()`: Virtual const (Returns shader mode for editor tools)
- `_get_shader_rid()`: Virtual const (Returns shader RID for editor tools)

### Public Methods
- `create_placeholder()`: Const (Creates placeholder material)
- `inspect_native_shader_code()`: (Available in editor; displays native shader code)

---

## Property Details
### next_pass
- **Set**: set_next_pass(Material)
- **Get**: get_next_pass()
- **Note**: Only applies to StandardMaterial3D and Spatial ShaderMaterial

### render_priority
- **Set**: set_render_priority(int)
- **Get**: get_render_priority()
- **Note**: Only applies to StandardMaterial3D and Spatial ShaderMaterial

---

## Notes
- Render priority affects sorting of objects but not transparent/opaque sorting
- next_pass materials may not render immediately after the source material
- Shader code inspection is only available in the editor