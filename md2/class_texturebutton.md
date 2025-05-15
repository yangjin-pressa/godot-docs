# TextureButton

## Overview
A texture-based button that supports visual states (normal, hover, pressed, disabled, focused). Inherits from BaseButton and uses sprite textures instead of theme resources.

## Key Features
- Faster creation than theme-based buttons
- Supports 6 texture states: normal, hover, pressed, disabled, focused, click mask
- 5 stretching modes for texture scaling
- Support for flipped textures (horizontal/vertical)
- Texture size ignore option

## Tutorials
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

## Properties
- **flip_h**: bool (default false) - Flip texture horizontally
- **flip_v**: bool (default false) - Flip texture vertically
- **ignore_texture_size**: bool (default false) - Whether to ignore texture dimensions
- **texture_click_mask**: Bitmap - Click detection mask (white = clickable area)
- **texture_disabled**: Texture2D - Disabled state texture
- **texture_focused**: Texture2D - Focus overlay texture
- **texture_hover**: Texture2D - Hover state texture
- **texture_normal**: Texture2D - Default state texture
- **texture_pressed**: Texture2D - Pressed state texture

## Stretching Modes
- **STRETCH_KEEP_CENTER**: Keep center aligned
- **STRETCH_KEEP_SIZE**: Maintain original size
- **STRETCH_KEEP_ASPECT**: Maintain aspect ratio
- **STRETCH_FILL**: Fill space with distortion
- **STRETCH_CENTER**: Center-aligned scaling

## State Priority
1. Normal state (texture_normal)
2. Hover state (texture_hover)
3. Pressed state (texture_pressed)
4. Disabled state (texture_disabled)
5. Focus state (texture_focused)

## Important Notes
- Must set texture_normal for visible display; other states will fall back to normal
- Focus state overlay (texture_focused) should be semi-transparent for visibility
- Click mask (texture_click_mask) defines interactive areas for non-rectangular buttons
- Texture sizes should match the button's dimensions for proper scaling

## Usage Example
```gdscript
var button = TextureButton.new()
button.texture_normal = load("res://button_normal.png")
button.texture_hover = load("res://button_hover.png")
button.texture_pressed = load("res://button_pressed.png")
button.texture_disabled = load("res://button_disabled.png")
button.texture_focused = load("res://button_focus.png")
```