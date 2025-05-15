# ProgressBar

## Description
The `ProgressBar` class in Godot is used to display a progress bar that can be filled dynamically. It supports custom styling and can display a percentage value. For advanced customization, consider using `TextureProgressBar` instead.

---

## Properties
- **`editor_preview_indeterminate`**: `bool` (default: `false`)  
  Controls whether the progress bar appears as an indeterminate (infinite) spinner in the editor.

- **`editor_preview_indeterminate_duration`**: `float` (default: `0.0`)  
  Duration (in seconds) for the indeterminate animation.

- **`editor_preview_percentage`**: `float` (default: `0.5`)  
  Percentage value to display in the editor preview.

- **`editor_preview_smooth`**: `bool` (default: `true`)  
  Smooths the progress bar in the editor preview.

- **`maximum`**: `float` (default: `100.0`)  
  Maximum value of the progress bar.

- **`minimum`**: `float` (default: `0.0`)  
  Minimum value of the progress bar.

- **`percentage`**: `float` (default: `0.5`)  
  Current percentage value of the progress bar.

- **`show_percentage`**: `bool` (default: `true`)  
  Enables/disables the display of the percentage value.

---

## Theme Properties
- **`background`**: `StyleBox`  
  Style of the background.

- **`fill`**: `StyleBox`  
  Style of the progress (filled part of the bar).

- **`font`**: `Font`  
  Font used to draw the percentage value if `show_percentage` is `true`.

- **`font_size`**: `int`  
  Font size for the percentage value.

- **`outline_size`**: `int` (default: `0`)  
  Size of the text outline.  
  **Note**: If using a font with MSDF, its pixel range must be at least twice this value for proper outline rendering.

---

## Enumerations
### FillMode
- **`FILL_BEGIN_TO_END`**  
  Fills the bar from left to right.

- **`FILL_END_TO_BEGIN`**  
  Fills the bar from right to left.

---

## Property Descriptions
- **`editor_preview_indeterminate`**  
  **Set**: `set_editor_preview_indeterminate(value: bool)`  
  **Get**: `get_editor_preview_indeterminate() -> bool`  

- **`editor_preview_indeterminate_duration`**  
  **Set**: `set_editor_preview_indeterminate_duration(value: float)`  
  **Get**: `get_editor_preview_indeterminate_duration() -> float`  

- **`editor_preview_percentage`**  
  **Set**: `set_editor_preview_percentage(value: float)`  
  **Get**: `get_editor_preview_percentage() -> float`  

- **`editor_preview_smooth`**  
  **Set**: `set_editor_preview_smooth(value: bool)`  
  **Get**: `get_editor_preview_smooth() -> bool`  

- **`maximum`**  
  **Set**: `set_maximum(value: float)`  
  **Get**: `get_maximum() -> float`  

- **`minimum`**  
  **Set**: `set_minimum(value: float)`  
  **Get**: `get_minimum()_t -> float`  

- **`percentage`**  
  **Set**: `set_percentage(value: float)`  
  **Get**: `get_percentage() -> float`  

- **`show_percentage`**  
  **Set**: `set_show_percentage(value: bool)`  
  **Get**: `get_show_percentage() -> bool`  

---

## Notes
- The `outline_size` property is tied to MSDF font rendering. Ensure the pixel range is at least twice the outline size for correct results.