# FoldableContainer Class Overview

A versatile container node that supports folding and expanding, with customizable appearance and interactive controls.

## Key Features
- Folding/Expanding functionality
- Customizable visual appearance
- Title bar controls management
- Theme-based styling for different states
- Keyboard/controller navigation support

## Signals
- `folded`: Emitted when container is folded
- `folded_pressed`: Emitted when folded state is pressed

## Properties
### Core Properties
- `collapsed`: Boolean (true when folded)
- `font`: Font resource (title text font)
- `font_size`: Integer (title text size)
- `font_color`: Color (title text color when expanded)
- `collapsed_font_color`: Color (title text color when collapsed)
- `font_outline_color`: Color (title text outline color)
- `outline_size`: Integer (title text outline size)
- `h_separation`: Integer (horizontal separation between icon and text)

### Icon Properties
- `expanded_arrow`: Texture2D (expanded state icon)
- `expanded_arrow_mirrored`: Texture2D (expanded state icon for right-to-left layouts)
- `folded_arrow`: Texture2D (collapsed state icon for left-to-right layouts)
- `folded_arrow_mirrored`: Texture2D (collapsed state icon for right-to-left layouts)

### Title Bar Controls
- `title_bar_controls`: Array of Control nodes (additional elements in title bar)

## Theme Properties
These define the visual appearance for different states and components:

### Color Theme Properties
- `font_color`: Title text color when expanded
- `hover_font_color`: Title text color when hovered
- `collapsed_font_color`: Title text color when collapsed
- `font_outline_color`: Title text outline color

### Background Theme Properties
- `panel`: Default container background
- `title_panel`: Title background when expanded
- `title_collapsed_panel`: Title background when collapsed
- `title_hover_panel`: Title background when hovered
- `title_collapsed_hover_panel`: Title background when collapsed and hovered
- `focus`: Focus indicator style

### Layout Constants
- `h_separation`: Horizontal spacing between icon and text
- `outline_size`: Title text outline size

## Usage Notes
1. **Focus Style**: The `focus` style is displayed over the base style. Use a partially transparent StyleBox for better visibility. Avoid using StyleBoxEmpty for accessibility reasons.
2. **Icon Direction**: Use mirrored icons for right-to-left layouts.
3. **Theme Customization**: Override theme properties in the editor or via code to customize appearance.
4. **Title Bar Controls**: Add/remove controls using `add_title_bar_control()` and `remove_title_bar_control()`.

## Example Usage
```gdscript
# FoldableContainer example
var container = FoldableContainer.new()
container.font = preload("res://fonts/arial.ttf")
container.font_size = 16
container.font_color = Color(0.1, 0.5, 0.9)
container.fold()
```

This class provides a flexible way to create interactive containers with custom visual styles and layout options, suitable for various UI/UX implementations in Godot.