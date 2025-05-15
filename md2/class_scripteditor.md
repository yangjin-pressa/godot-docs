**ScriptEditor**  
- **Inherits**: Node  
- **Description**: The Godot editor's script editor.  
  - **Note**: Should not be instantiated directly.  

---

### **Methods**  
- **`update_docs_from_script(script: Script)`**:  
  - **Description**: Updates documentation for the given script if it's currently open.  
  - **Note**: Call this when a script is modified to keep documentation in sync.  

- **`goto_line(line_number: int)`**:  
  - **Description**: Navigate to the specified line in the current script.  

- **`open_script_create_dialog(base_name: String, base_path: String)`**:  
  - **Description**: Opens a dialog to create a new script extending `base_name`.  
  - **Note**: File extension is automatically added based on the selected language.  

- **`register_syntax_highlighter(highlighter: EditorSyntaxHighlighter)`**:  
  - **Description**: Registers a syntax highlighter for all open scripts.  
  - **Note**: Does not affect scripts already opened.  

- **`unregister_syntax_highlighter(highlighter: EditorSyntaxHighlighter)`**:  
  - **Description**: Removes a syntax highlighter from the editor.  
  - **Note**: Already opened scripts retain the highlighter.  

- **`goto_help(topic: String)`**:  
  - **Description**: Navigates to a specific line in the current script.  
  - **Example Topics**:  
    - `class_ScriptEditor_signal_editor_script_changed`  
    - `class_ScriptEditor_signal_script_close`  

---

### **Signals**  
- **`editor_script_changed`**:  
  - **Description**: Triggered when a script is modified.  

- **`script_close`**:  
  - **Description**: Triggered when a script is closed.  

---

### **Key Notes**  
- **`update_docs_from_script`**: Ensure documentation reflects script changes.  
- **Syntax Highlighters**: Registered highlighters apply to new scripts, not existing ones.  
- **Script Creation**: Base name and path are used to generate a new script file.  

--- 

**Inheritance Chain**:  
`ScriptEditor → Node`