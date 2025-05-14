# CubemapArray

## Inheritance Hierarchy
- **CubemapArray** extends: `ImageTextureLayered` → `TextureLayered` → `Texture` → `Resource` → `RefCounted` → `Object`

## Key Information
- **Purpose**: An array of Cubemap textures stored together with a single reference.
- **Texture Requirement**: Must contain a number of textures divisible by 6 (each face of a cube).
- **Shader Usage**: Accessed in shaders via a single texture reference, improving GPU efficiency.
- **Internal Use**: Used internally by Godot for effects like Sky (when texture_array_reflections is enabled).
- **Image Templates**: 
  - 2×3, 3×2, 1×6, 6×1 layouts available for cubemap templates.
  - Default vertical import (top layer first), or horizontal layout in import options.
- **Compatibility Note**: Not supported in Compatibility renderer due to API limitations.

## Methods
- **create_placeholder** (const) → `Resource`  
  Creates a placeholder CubemapArray instance (`PlaceholderCubemapArray`).

## Method Details
- **create_placeholder**:  
  - **Type**: `const` (no side effects, no variable modifications).  
  - **Usage**: Generates a placeholder version of the CubemapArray for temporary or default scenarios.  
  - **Link**: [PlaceholderCubemapArray](class_PlaceholderCubemapArray)

## Image Import Notes
- **Order**: X+, X-, Y+, Y-, Z+, Z- (Godot's coordinate system).  
- **Templates**:  
  - [2×3 template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_2x3.webp)  
  - [3×2 template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_3x2.webp)  
  - [1×6 template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_1x6.webp)  
  - [6×1 template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_6x1.webp)  
- **Layout Options**: Vertical (top layer first) or horizontal (left first) import settings.