# ReferenceRect

**Inherits:** Control < CanvasItem < Node < Object

A rectangle box that displays only a colored border around its rectangle. It is used to visualize the extents of a Control.

## Properties

- **border_color**: Color, default `Color(1, 0, 0, 1)`
- **border_width**: float, default `1.0`
- **editor_only**: bool, default `true`

## Property Descriptions

### border_color
Sets the border color of the **ReferenceRect**.

- `set_border_color(value: Color)`: Sets the border color.
- `get_border_color()`: Gets the border color.

### border_width
Sets the border width of the **ReferenceRect**. The border grows both inwards and outwards with respect to the rectangle box.

- `set_border_width(value: float)`: Sets the border width.
- `get_border_width()`: Gets the border width.

### editor_only
If `true`, the **ReferenceRect** will only be visible while in editor. Otherwise, **ReferenceRect** will be visible in the running project.

- `set_editor_only(value: bool)`: Sets the editor_only flag.
- `get_editor_only()`: Gets the editor_only flag.