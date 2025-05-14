**Class: CompressedTexture2D**  
*Inherits:* Texture2D < Texture < Resource < RefCounted < Object  

---

### **Description**  
A 2D texture loaded from a `.ctex` file (internal to Godot, created via the import system). Supports 4 compression methods:  
- **Lossless**: WebP/PNG (uncompressed on GPU)  
- **Lossy**: WebP (uncompressed on GPU)  
- **VRAM Compressed**: Compressed on GPU (reduces GPU memory usage)  
- **VRAM Uncompressed**: Uncompressed on GPU  
- **Basis Universal**: Compressed on GPU (lower file size than VRAM Compressed, but slower and lower quality)  

**Note:** VRAM Compressed reduces GPU memory usage but may introduce artifacts, suitable for 3D rendering.  

---

### **Properties**  
- **load_path**: String = ""  
  - The file path to a `.ctex` file.  
  - 🔗 [class_CompressedTexture2D_property_load_path](#class_CompressedTexture2D_property_load_path)  

- **resource_local_to_scene**: bool = false  
  - Overrides Resource's default behavior.  

---

### **Methods**  
- **load(path: String)** → Error  
  - Loads the texture from the specified `path`.  
  - 🔗 [class_CompressedTexture2D_method_load](#class_CompressedTexture2D_method_load)  

---

### **Property Descriptions**  
**load_path**:  
- **Type**: String  
- **Default**: ""  
- **Description**: Path to the `.ctex` file.  

---

### **Method Descriptions**  
**load**:  
- **Parameters**: `path` (String)  
- **Returns**: Error  
- **Description**: Loads the texture from the specified `path`.  

--- 

**Note:** VRAM Compressed textures load faster but may have visible artifacts. Use for 3D rendering; avoid for 2D.