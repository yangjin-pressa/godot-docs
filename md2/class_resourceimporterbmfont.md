# ResourceImporterBMFont

**Inherits:** ResourceImporter < RefCounted < Object

Imports a bitmap font in the BMFont (.fnt) format.

## Description
The BMFont format is a format created by the [BMFont](https://www.angelcode.com/products/bmfont/) program. Many BMFont-compatible programs also exist, like [BMGlyph](https://www.bmglyph.com/).

Compared to [ResourceImporterImageFont](class_ResourceImporterImageFont.html), ResourceImporterBMFont supports bitmap fonts with varying glyph widths/heights.

See also [ResourceImporterDynamicFont](class_ResourceImporterDynamicFont.html).

## Tutorials
- [Bitmap fonts - Using fonts](../tutorials/ui/gui_using_fonts.html#bitmap-fonts)

## Properties
- **compress**: bool = true  
  If true, uses lossless compression for the resulting font.

- **fallbacks**: Array = []  
  List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.

- **scaling_mode**: int = 2  
  Font scaling mode.

## Notes
- This class is used for importing bitmap fonts in the BMFont format.
- The scaling mode determines how the font is scaled during import.