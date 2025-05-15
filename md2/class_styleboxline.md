# StyleBoxLine

**Inherits:** StyleBox < Resource < RefCounted < Object

## Description
A StyleBox that displays a single line of a given color and thickness. The line can be either horizontal or vertical. Useful for separators.

## Properties
- **color**: Color(0, 0, 0, 1) - The line's color.
- **grow_begin**: 1.0 - Pixels the line extends before bounds. Negative values start inside bounds.
- **grow_end**: 1.0 - Pixels the line extends past bounds. Negative values end inside bounds.
- **thickness**: 1 - Line thickness in pixels.
- **vertical**: false - If true, the line is vertical.

## Property Descriptions
### color
- **set_color** (value: Color) - Sets the line's color.
- **get_color** () - Returns the line's color.

### grow_begin
- **set_grow_begin** (value: float) - Sets pixels the line extends before bounds.
- **get_grow_begin** () - Returns pixels the line extends before bounds.

### grow_end
- **set_grow_end** (value: float) - Sets pixels the line extends past bounds.
- **get_grow_end** () - Returns pixels the line extends past bounds.

### thickness
- **set_thickness** (value: int) - Sets line thickness.
- **get_thickness** () - Returns line thickness.

### vertical
- **set_vertical** (value: bool) - Sets line orientation (vertical/horizontal).
- **is_vertical** () - Checks if line is vertical.