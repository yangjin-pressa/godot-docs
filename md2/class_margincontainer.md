# MarginContainer

**Inherits:** `Container` → `Control` → `CanvasItem` → `Node` → `Object`

## Description
A container that keeps a margin around its child controls. The margins are added around all children, not around each individual one. To control the margins, use the `margin_*` theme properties.

**Note:** The margin sizes are theme overrides, not normal properties. Example code to change them:
```gdscript
# This code sample assumes the current script is extending MarginContainer.
var margin_value = 100
add_theme_constant_override("margin_top", margin_value)
add_theme_constant_override("margin_left", margin_value)
add_theme_constant_override("margin_bottom", margin_value)
add_theme_constant_override("margin_right", margin_value)
```

```csharp
// This code sample assumes the current script is extending MarginContainer.
int marginValue = 100;
AddThemeConstantOverride("margin_top", marginValue);
AddThemeConstantOverride("margin_left", marginValue);
AddThemeConstantOverride("margin_bottom", marginValue);
AddThemeConstantOverride("margin_right", marginValue);
```

## Tutorials
- [Using Containers](../tutorials/ui/gui_containers)

## Theme Properties
- `margin_bottom`: `int` (0)
- `margin_left`: `int` (0)
- `margin_right`: `int` (0)
- `margin_top`: `int` (0)

## Theme Property Descriptions
- **margin_bottom**: Offsets towards the inside direct children of the container by this amount of pixels from the bottom.
- **margin_left**: Offsets towards the inside direct children of the container by this amount of pixels from the left.
- **margin_right**: Offsets towards the inside direct children of the container by this amount of pixels from the right.
- **margin_top**: Offsets towards the inside direct children of the container by this amount of pixels from the top.