**Class Name:** EditorSceneFormatImporterBlend  
**Inherits From:** EditorSceneFormatImporter → RefCounted → Object  

---

### **Description**  
- Imports Blender `.blend` scene files via the glTF 2.0 import pipeline.  
- Requires Blender to be installed.  
- Uses Blender's glTF "Use Original" mode to reference external textures.  
- Only active if `ProjectSettings.filesystem/import/blender/enabled` is enabled.  

---

### **Key Requirements**  
- **Blender Version:** Requires Blender 3.0 or later.  
- **Configuration:**  
  - Blender binary path set via `EditorSettings.filesystem/import/blender/blender_path`.  
  - Enabled in `ProjectSettings.filesystem/import/blender/enabled` to process `.blend` files.  

---

### **Internal Behavior**  
- Uses Blender's glTF "Use Original" mode for texture handling.  
- Expects `.blend` files to be exported as glTF 2.0 before import.  

---

### **Notes**  
- No code blocks or method definitions are present in the source.  
- References to settings are preserved as original property names.  

--- 

**Language:** English (original document language retained).