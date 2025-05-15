# SyntaxHighlighter

## Inheritance
- **Resource** < **RefCounted** < **Object**

## Inherited By
- CodeHighlighter
- EditorSyntaxHighlighter

## Description
Base class for syntax highlighters. Provides syntax highlighting data to a TextEdit. The associated TextEdit will call into the SyntaxHighlighter on an as-needed basis.

**Note:** A SyntaxHighlighter instance should not be used across multiple TextEdit nodes.

---

## Methods

### _clear_highlighting_cache (virtual)
Clears local caches for syntax highlighting data.

### _get_line_syntax_highlighting (virtual, const)
Returns syntax highlighting data for a line. If not cached, calculates it.

**Example:**
```json
{
    0: {
        "color": Color(1, 0, 0)
    },
    5: {
        "color": Color(0, 1, 0)
    }
}
```

### _update_cache (virtual)
Updates local caches for syntax highlighting data.

### clear_highlighting_cache
Calls _clear_highlighting_cache to clear cached data.

### get_line_syntax_highlighting (line: int)
Returns syntax highlighting data for a line. If not cached, calls _get_line_syntax_highlighting.

### get_text_edit
Returns the associated TextEdit node.

### update_cache
Clears and updates the SyntaxHighlighter caches. Override _update_cache for custom behavior.

**Note:** This method is automatically called when the TextEdit updates.

---

## Key Details
- SyntaxHighlighter provides syntax data to TextEdit.
- Private methods (_clear, _get, _update) handle internal caching.
- Public methods (clear, get_line, get_text) expose functionality for external use.
- The class is designed for single TextEdit usage to avoid conflicts.