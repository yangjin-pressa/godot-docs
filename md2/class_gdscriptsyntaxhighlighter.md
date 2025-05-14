**Class: GDScriptSyntaxHighlighter**  
**Inherits:** EditorSyntaxHighlighter → SyntaxHighlighter → Resource → RefCounted → Object  

---

### **Description**  
- **Note:** This class is intended for editor plugins due to its reliance on editor settings.  
- **Usage Example:**  
  ```gdscript
  var code_preview = TextEdit.new()
  var highlighter = GDScriptSyntaxHighlighter.new()
  code_preview.syntax_highlighter = highlighter
  ```  
  ```csharp
  var codePreview = new TextEdit();
  var highlighter = new GDScriptSyntaxHighlighter();
  codePreview.SyntaxHighlighter = highlighter;
  ```  

---

### **Key Features**  
- **Purpose:** Enables syntax highlighting for GDScript in text editors like `TextEdit` and `CodeEdit`.  
- **Dependencies:** Requires access to editor settings and resources.  

---

### **Inheritance Hierarchy**  
- EditorSyntaxHighlighter  
  - SyntaxHighlighter  
    - Resource  
      - RefCounted  
        - Object  

---

### **Method Notes**  
- **virtual**: Methods should typically be overridden by the user.  
- **const**: Methods have no side effects.  
- **vararg**: Accepts variable arguments.  
- **static**: Callable directly via class name.  
- **void**: Returns no value.  

---

### **References**  
- [TextEdit](class_TextEdit)  
- [CodeEdit](class_CodeEdit)  
- [EditorSyntaxHighlighter](class_EditorSyntaxHighlighter)  
- [SyntaxHighlighter](class_SyntaxHighlighter)  
- [Resource](class_Resource)