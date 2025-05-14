**Class: CompressedCubemap**  
**Inherits:** `CompressedTextureLayered` → `TextureLayered` → `Texture` → `Resource` → `RefCounted` → `Object`  

---

### **Description**  
A cubemap loaded from a `.ccube` file (internal Godot format). It supports multiple compression methods, affecting memory usage, loading speed, and quality.  

---

### **Compression Methods**  
- **Lossless**: WebP/PNG (uncompressed on GPU)  
- **Lossy**: WebP (uncompressed on GPU)  
- **VRAM Compressed**: Compressed on GPU (reduces GPU memory usage)  
- **VRAM Uncompressed**: Uncompressed on GPU (no memory reduction)  
- **Basis Universal**: Compressed on GPU (lower file size than VRAM Compressed, but slower to compress and lower quality)  

---

### **Key Notes**  
- **VRAM Compressed** reduces GPU memory usage but may introduce artifacts, ideal for 3D rendering.  
- **Lossless/Lossy** reduces disk storage but does not optimize GPU memory.  
- **Basis Universal** offers better file size savings than VRAM Compressed but with trade-offs in speed and quality.  

---

### **Reference**  
See [Cubemap](class_Cubemap) for general cubemap information.