# EditorTranslationParserPlugin

**Inherits:** RefCounted < Object

## Description
A plugin for adding custom parsers to extract translatable strings from files (.csv, .json, etc.). Override `_parse_file()` to define parsing logic.

Key requirements:
- Return Array of PackedStringArray
- Each entry contains [msgid, msgctxt, msgid_plural, comment] (optional fields)
- Empty strings are ignored
- Extracted strings are saved to a POT file via "POT Generation" in Project Settings

Example usage:
```gdscript
@tool
extends EditorTranslationParserPlugin

func _parse_file(path):
    var ret: Array[PackedStringArray] = []
    var file = FileAccess.open(path, FileAccess.READ)
    var text = file.get_as_text()
    var split_strs = text.split(",", false)
    for s in split_strs:
        ret.append(PackedStringArray([s]))
    
    return ret

func _get_recognized_extensions():
    return ["csv"]
```

## Method Overview
- `_get_recognized_extensions()`: Returns list of file extensions this parser supports
- `_parse_file(path)`: Custom parsing logic to extract translatable strings

## Custom String Extraction Examples
```gdscript
ret.append(PackedStringArray(["Test 1", "context", "test 1 plurals", "test 1 comment"]))
ret.append(PackedStringArray(["A test without context", "", "plurals"]))
ret.append(PackedStringArray(["Only with context", "a friendly context"]))
```

## Best Practices
- For script files (GDScript/C#), use ResourceLoader.load() to access file content
- Example:
```gdscript
func _parse_file(path):
    var res = ResourceLoader.load(path, "Script")
    var text = res.source_code
    # Parsing logic
```

## Usage Instructions
1. Register plugin using `EditorPlugin.add_translation_parser_plugin()`
2. Implement custom parsing logic in `_parse_file()`
3. Define recognized file extensions in `_get_recognized_extensions()`