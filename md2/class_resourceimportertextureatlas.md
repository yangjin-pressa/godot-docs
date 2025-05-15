**Class Name**: ResourceImporterTextureAtlas  
**Inherits**: ResourceImporter → RefCounted → Object  

---

### **Description**  
Imports textures from a PNG image into an AtlasTexture for 2D rendering. Optimizes memory usage for 2D animations. Supports **Region** or **Mesh** import modes. Not supported for 3D.  
- **Region mode**: AtlasTexture resource (fast rendering, but may retain transparent areas).  
- **Mesh mode**: ArrayMesh resource (reduces fill rate but slower rendering).  

**Notes**:  
- Does not handle TileSetAtlasSource (use TileSet editor instead).  

---

### **Properties**  
| Name | Type | Default | Description |  
|------|------|---------|-------------|  
| atlas_file | String | "" | Path to PNG spritesheet. Required for import. |  
| crop_to_region | bool | false | Removes empty areas from atlas. Only effective if import_mode is **Region**. |  
| import_mode | int | 0 | Mode: 0 = Region, 1 = Mesh |  
| trim_alpha_border_from_region | bool | true | Trims transparent pixels to reduce memory. Only effective if import_mode is **Region**. |  

---

### **Key Notes**  
- **atlas_file**: Must be a valid PNG path. Invalid path causes import failure.  
- **import_mode**:  
  - **Region**: AtlasTexture (fast, but may retain transparent areas).  
  - **Mesh**: ArrayMesh (reduces fill rate, but slower rendering).  
- **trim_alpha_border_from_region**: Optimize memory by removing transparent borders.  
- **crop_to_region**: Avoids empty spaces in the atlas but does not alter storage.  

---

### **Related Classes**  
- [ResourceImporterTexture](#)  
- [ResourceImporterLayeredTexture](#)  
- [AtlasTexture](#)  
- [ArrayMesh](#)  
- [TileSetAtlasSource](#) (use TileSet editor for this)