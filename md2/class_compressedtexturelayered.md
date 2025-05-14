**Class Name:** CompressedTextureLayered  
**Inherits:** TextureLayered → Texture → Resource → RefCounted → Object  
**Inherited By:** CompressedCubemap, CompressedCubemapArray, CompressedTexture2DArray  

---

### Description  
Base class for compressed texture arrays (CompressedTexture2DArray, CompressedTexture3D). Not intended for direct use but provides essential functions for derived types. See also TextureLayered.

---

### Properties  
- **load_path**:  
  - **Type**: String  
  - **Default**: ""  
  - **Description**: Path the texture should be loaded from.  

---

### Methods  
- **load(path: String)** → Error  
  - **Description**: Loads the texture at `path`.  
  - **Note**: Virtual method (override in derived classes for custom behavior).  

---

### Property Descriptions  
**load_path**  
- **Type**: String  
- **Default**: ""  
- **Description**: Path the texture should be loaded from.  

---

### Method Descriptions  
**load(path: String)** → Error  
- **Description**: Loads the texture at `path`.  
- **Note**: Virtual method (override in derived classes for custom behavior).  

---

### Related Classes  
- [TextureLayered](class_TextureLayered)  
- [CompressedTexture2DArray](class_CompressedTexture2DArray)  
- [CompressedTexture3D](class_CompressedTexture3D)