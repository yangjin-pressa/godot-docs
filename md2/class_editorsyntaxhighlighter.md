# EditorSyntaxHighlighter

**Inherits:** SyntaxHighlighter < Resource < RefCounted < Object  
**Inherited By:** GDScriptSyntaxHighlighter  

## Description  
Base class for SyntaxHighlighter used by ScriptEditor.  
- Add to a script: `ScriptEditorBase.add_syntax_highlighter()`  
- Register for all scripts: `ScriptEditor.register_syntax_highlighter()`  

## Methods  
- **_get_name**()  
  - **Type:** String  
  - **Notes:** Virtual, const. Return the syntax highlighter name.  

- **_get_supported_languages**()  
  - **Type:** PackedStringArray  
  - **Notes:** Virtual, const. Return supported language names.  

## Key Notes  
- These methods are virtual (overrideable) and const (no side effects).  
- Used to define syntax highlighting behavior for specific languages.