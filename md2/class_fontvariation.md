# FontVariation

**Inherits:** Font → Resource → RefCounted → Object

## Description
Provides OpenType variations, simulated bold/slant, and additional font settings. Example usage:  
```gdscript
var fv = FontVariation.new()
fv.base_font = load("res://BarlowCondensed-Regular.ttf")
fv.variation_embolden = 1.2
$Label.add_theme_font_override("font", fv)
$Label.add_theme_font_size_override("font_size", 64)
```

## Properties

- **base_font**: Font (default: Theme font)  
  Base font used for variation.  

- **variation_embolden**: float (default: 0.0)  
  Emboldens font outlines. Negative values reduce thickness.  

- **variation_face_index**: int (default: 0)  
  Active face index in font collection.  

- **variation_transform**: Transform2D (default: identity)  
  2D transform for slanting/rotating glyphs.  
  Example: Transform2D(1.0, slant, 0.0, 1.0, 0.0, 0.0)  

- **variation_opentype**: Dictionary  
  OpenType variation coordinates. Uses tags (e.g., `wght`) for axes.  
  [Tags ↔ Names](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg)

- **variation_opentype**: Dictionary  
  Font OpenType variation coordinates. [Tags ↔ Names](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg)

- **spacing_bottom**: int  
  Pixel spacing at line bottom.  

- **spacing_top**: int  
  Pixel spacing at line top.  

- **spacing_glyph**: int  
  Additional spacing between glyphs.  

- **spacing_char**: int  
  Character spacing in pixels.  

- **baseline_offset**: float  
  Adjusts baseline position.  

## Methods

- **set_spacing(spacing_type: SpacingType, value: int)**  
  Sets spacing for specific type (bottom, top, glyph, char).  

## Notes
- Emboldened fonts may have self-intersecting outlines, causing issues with MSDF and TextMesh.  
- Use `Font.get_supported_variation_list()` to check available axes.  
- [OpenType feature tags](https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags)  
- [OpenType variation tags](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg)