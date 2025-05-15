# TextureProgressBar Class Documentation

## Overview
The `TextureProgressBar` class is a specialized control that uses texture-based visuals to represent a range value. It supports layered textures for progress, over, and under elements, with custom color tints and stretch margins for nine-patch support.

---

## Properties

### Texture-related Properties
- **`texture_progress`**  
  The main texture that fills based on the node's `value` and `fill_mode`. Shows entirely when `value` reaches `max_value`.

- **`texture_over`**  
  A texture drawn over the progress bar. Useful for highlights or upper frames that hide parts of the progress texture.

- **`texture_under`**  
  The background texture for the progress bar. Represents the base appearance of the bar.

- **`texture_progress_offset`**  
  Offsets the position of the `texture_progress` texture. Useful for aligning with `texture_over`/`texture_under` textures.

### Color Tint Properties
- **`tint_progress`**  
  Multiplies the color of the `texture_progress` texture.

- **`tint_over`**  
  Multiplies the color of the `texture_over` texture.

- **`tint_under`**  
  Multiplies the color of the `texture_under` texture.

### Stretch Margin Properties
- **`stretch_margin_bottom`**  
  The height of the 9-patch top row.  
- **`stretch_margin_top`**  
  The height of the 9-patch bottom row.  
- **`stretch_margin_left`**  
  The width of the 9-patch left column.  
- **`stretch_margin_right`**  
  The width of the 9-patch right column.  

These margins control how the 9-patch textures (progress, over, under) are stretched.

---

## Methods

### `set_stretch_margin`  
Sets the stretch margin for a specific direction.  
**Parameters:**  
- `margin`: `Side` enum (e.g., `Side::TOP`, `Side::LEFT`).  
- `value`: `int` (margin size).  

### `get_stretch_margin`  
Returns the stretch margin for a specific direction.  
**Parameters:**  
- `margin`: `Side` enum (e.g., `Side::TOP`, `Side::LEFT`).  
**Returns:** `int` (margin size).

---

## Usage Notes

- **Range Integration**:  
  The `value` property is derived from a `Range` object. Adjust `min_value`, `max_value`, and `value` to control the progress bar's range.  

- **Nine-Patch Support**:  
  Use `stretch_margin_*` properties to define how textures are stretched. This is particularly useful for custom textures with borders or gradients.

- **Texture Layering**:  
  Use `texture_over` and `texture_under` to create layered effects. For example, a highlight texture on top of the progress bar.

- **Color Modulation**:  
  Adjust `tint_*` properties to change the appearance of individual textures without altering the original textures.

---

## Example

```gdscript
# Create a TextureProgressBar node
var bar = TextureProgressBar.new()

# Set textures
bar.texture_progress = load("res://progress.png")
bar.texture_over = load("res://highlight.png")
bar.texture_under = load("res://background.png")

# Set tints
bar.tint_progress = Color(1, 0, 0, 1)  # Red progress
bar.tint_over = Color(1, 1, 0, 1)      # Yellow highlight
bar.tint_under = Color(0.2, 0.2, 0.2, 1)  # Dark gray background

# Set stretch margins
bar.set_stretch_margin(Side::TOP, 10)
bar.set_stretch_margin(Side::LEFT, 5)

# Set range
bar.range = Range.new(min_value=0, max_value=100, value=50)
```

---

## Key Concepts

- **Fill Mode**: Determines how the `texture_progress` fills (e.g., left-to-right, radial, etc.).  
- **Texture Clipping**: The `texture_progress` is clipped based on the `value` and `fill_mode`.  
- **Nine-Patch System**: The stretch margins allow for flexible scaling of textures, ideal for UI elements with borders.  

This class provides a flexible way to create custom progress indicators using textures and color modulation.