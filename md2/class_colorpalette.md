# ColorPalette

**Inherits:** Resource < RefCounted < Object

A resource class for managing a palette of colors, which can be loaded and saved using ColorPicker.

## Description
- Stores and manages a collection of colors.
- Useful for creating themes, designing user interfaces, or managing game assets.
- ColorPicker can use ColorPalette without additional code.

## Properties
- **colors**: PackedColorArray() (default)

## Property Descriptions
- **colors**: A PackedColorArray containing the colors in the palette.  
  - `get_colors()` returns a copy of the array; changes to the returned array do not update the original property value.

## Methods
- `set_colors(value: PackedColorArray)`: Sets the colors in the palette.
- `get_colors()`: Returns a copy of the colors array.