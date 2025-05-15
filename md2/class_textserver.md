# Godot TextServer Documentation

The `TextServer` class in Godot provides functionalities for text rendering, language processing, and Unicode manipulation. It supports various text-related operations, including character breaking, case conversion, and glyph manipulation.

---

## Core Methods

### `text_server_get_version()`
**Description**: Returns the version of the TextServer.

**Return Value**: A string representing the version.

---

### `text_server_init()`
**Description**: Initializes the TextServer. This is only called once during the engine's startup.

**Return Value**: `void`

---

### `text_server_set_language(language)`
**Description**: Sets the language for the TextServer. This is used for language-specific text processing.

**Parameters**:
- `language`: A string representing the language code (e.g., "en", "fr").

**Return Value**: A boolean indicating success.

**Note**: If the server doesn't support the specified language, it returns `false`.

---

### `text_server_get_languages()`
**Description**: Returns a list of supported languages by the TextServer.

**Return Value**: A `PackedStringArray` containing language codes.

---

## Shaped Text Methods

These methods work on `shaped` text buffers, which are pre-shaped text data structures optimized for rendering.

### `shaped_text_get_characters(shaped)`
**Description**: Returns the characters in a shaped text buffer.

**Parameters**:
- `shaped`: A `RID` representing the shaped text buffer.

**Return Value**: A `PackedStringArray` containing the characters.

---

### `shaped_text_get_glyphs(shaped, offset=0, count=-1)`
**Description**: Returns the glyphs in a shaped text buffer.

**Parameters**:
- `shaped`: A `RID` representing the shaped text buffer.
- `offset`: Start index for glyphs (default: 0).
- `count`: Number of glyphs to return (default: -1, which means all).

**Return Value**: A `PackedInt32Array` containing glyph indices.

---

### `shaped_text_get_glyph_info(shaped, index)`
**Description**: Returns detailed information about a specific glyph.

**Parameters**:
- `shaped`: A `RID` representing the shaped text buffer.
- `index`: Index of the glyph.

**Return Value**: A `PackedVector3Array` containing glyph information (e.g., position, advance, etc.).

---

### `shity_text_get_outline(shaped, glyph_index, linear=true)`
**Description**: Returns the outline of a specific glyph.

**Parameters**:
- `shaped`: A `RID` representing the shaped text buffer.
- `glyph_index`: Index of the glyph.
- `linear`: Boolean to determine if the outline is linear or cubic Bezier (default: true).

**Return Value**: A `PackedVector2Array` containing the outline points.

---

### `shaped_text_get_kerning(shaped, first, second)`
**Description**: Returns the kerning value between two glyphs.

**Parameters**:
- `shaped`: A `RID` representing the shaped text buffer.
- `first`: Index of the first glyph.
- `second`: Index of the second glyph.

**Return Value**: A float representing the kerning value.

---

### `shaped_text_get_advances(shaped)`
**Description**: Returns the advance (width) of each glyph.

**Parameters**:
- `shaped`: A `RID` representing the shaped text buffer.

**Return Value**: A `PackedVector2Array` containing glyph advances.

---

### `shaped_text_get_text(shaped)`
**Description**: Returns the original text string of the shaped buffer.

**Return Value**: A string.

---

### `shaped_text_get_bbox(shaped)`
**Description**: Returns the bounding box of the text.

**Return Value**: A `Rect2` containing the text's bounding box.

---

### `shaped_text_get_width(shaped)`
**Description**: Returns the total width of the text.

**Return Value**: A float representing the total width.

---

### `shaped_text_get_line_info(shaped)`
**Description**: Returns information about each line in the text.

**Return Value**: A `PackedVector2Array` containing line information (e.g., start and end positions).

---

### `shaped_text_get_line_count(shaped)`
**Description**: Returns the number of lines in the text.

**Return Value**: An integer representing the number of lines.

---

### `shaped_text_get_line_widths(shaped)`
**Description**: Returns the width of each line.

**Return Value**: A `PackedVector2Array` containing line widths.

---

### `shaped_text_get_line_heights(shaped)`
**Description**: Returns the height of each line.

**Return Value**: A `PackedVector2Array` containing line heights.

---

## Text Processing Methods

### `text_server_get_languages()`
**Description**: Returns a list of supported languages by the TextServer.

**Return Value**: A `PackedStringArray` containing language codes.

---

### `text_server_get_language()`
**Description**: Returns the current language setting of the TextServer.

**Return Value**: A string representing the current language.

---

## Unicode and Text Manipulation

### `string_get_character_breaks(text)`
**Description**: Returns boundaries for composite characters in a string.

**Parameters**:
- `text`: A string.

**Return Value**: A `PackedInt32Array` containing character boundaries.

**Example**:
```godot
var breaks = text_server.string_get_character_breaks("Hello, world!");
```

---

### `string_get_word_breaks(text)`
**Description**: Returns word break positions in a string.

**Parameters**:
- `text`: A string.

**Return Value**: A `PackedInt32Array` containing word break positions.

**Example**:
```godot
var breaks = text_server.string_get_word_breaks("Hello world!");
```

---

### `string_to_lower(text)`
**Description**: Converts a string to lowercase.

**Parameters**:
- `text`: A string.

**Return Value**: A string in lowercase.

**Example**:
```godot
var lower = text_server.string_to_lower("Hello");
```

---

### `string_to_upper(text)`
**Description**: Converts a string to uppercase.

**Parameters**:
- `text`: A string.

**Return Value**: A string in uppercase.

**Example**:
```godot
var upper = text_server.string_to_upper("hello");
```

---

### `string_to_title(text)`
**Description**: Converts a string to title case.

**Parameters**:
- `text`: A string.

**Return Value**: A string in title case.

**Example**:
```godot
var title = text_server.string_to_title("hello world");
```

---

### `strip_diacritics(text)`
**Description**: Removes diacritics (accents) from a string.

**Parameters**:
- `text`: A string.

**Return Value**: A string without diacritics.

**Example**:
```godot
var clean = text_server.strip_diacritics("café");
```

---

## Security & Spoof Check

### `spoof_check(text)`
**Description**: Checks if a string is likely to be a spoof (e.g., a misleading or fake string).

**Parameters**:
- `text`: A string.

**Return Value**: A boolean indicating whether the text is a spoof.

**Example**:
```godot
var is_spoof = text_server.spoof_check("Hello, world!");
```

---

## Utility Methods

### `tag_to_name(tag)`
**Description**: Converts an OpenType tag to a readable name.

**Parameters**:
- `tag`: A string representing an OpenType tag (e.g., "C2SC", "Kern").

**Return Value**: A string representing the tag's name.

**Example**:
```godot
var name = text_server.tag_to_name("C2SC");
```

---

## Notes and Best Practices

1. **Shaped Text**: Methods like `shaped_text_get_characters` and `shaped_text_get_glyphs` require the text buffer to be shaped first. The TextServer automatically shapes the text when necessary.
2. **Language Support**: Methods like `text_server_set_language` and `string_get_word_breaks` rely on the TextServer's language capabilities.
3. **Unicode Handling**: Methods like `strip_diacritics` and `string_get_character_breaks` are essential for working with Unicode characters.

This documentation provides a comprehensive overview of the `TextServer` class in Godot, covering all methods and their use cases. Developers should refer to this guide for text rendering, language processing, and Unicode manipulation in Godot projects.