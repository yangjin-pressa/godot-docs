# ResourceImporterImageFont

**Inherits:** ResourceImporter → RefCounted → Object

Imports a bitmap font where all glyphs have the same width and height.

## Description
This image-based workflow can be easier to use than ResourceImporterBMFont, but requires all glyphs to have the same width and height. Glyph advances and drawing offsets can be customized. Best suited for fixed-width fonts.

See also: ResourceImporterDynamicFont

## Tutorials
- [Bitmap fonts - Using fonts](../tutorials/ui/gui_using_fonts.html#bitmap-fonts)

## Properties
- **ascent**: int = 0 (Font ascent, pixels above baseline)
- **character_margin**: Rect2i = Rect2i(0, 0, 0, 0) (Margin around glyphs)
- **character_ranges**: PackedStringArray = [] (Character ranges to import)
- **columns**: int = 1 (Number of columns in font image)
- **compress**: bool = true (Lossless compression)
- **descent**: int = 0 (Font descent, pixels below baseline)
- **fallbacks**: Array = [] (Fallback font list)
- **image_margin**: Rect2i = Rect2i(0, 0, 0, 0) (Image border margin)
- **kerning_pairs**: PackedStringArray = [] (Kerning pair adjustments)
- **rows**: int = 1 (Number of rows in font image)
- **scaling_mode**: int = 2 (Font scaling mode)

## Property Descriptions
- **ascent**: Font ascent (pixels above baseline). 0 uses half character height.
- **character_margin**: Adjust spacing if glyph guides are present.
- **character_ranges**: Define character ranges (e.g., "0-127" for ASCII). Ranges can include advance/x/y offsets.
- **columns**: Number of columns in font image.
- **compress**: Enable lossless compression.
- **descent**: Font descent (pixels below baseline). 0 uses half character height.
- **fallbacks**: List of fallback fonts (first in list is tried first).
- **image_margin**: Cut border margin from image.
- **kerning_pairs**: Adjust spacing between character pairs (e.g., "ab cd -3" for "ac", "ad", "bc", "bd").
- **rows**: Number of rows in font image.
- **scaling_mode**: Font scaling mode (value 2 is default).

## Notes
- PackedStringArray returns a copy; changes don't affect original.
- character_ranges must not exceed columns × rows.