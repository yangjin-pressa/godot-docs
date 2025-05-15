# ResourceImporter

**Inherits:** RefCounted < Object

**Inherited By:**  
- EditorImportPlugin  
- ResourceImporterBitMap  
- ResourceImporterBMFont  
- ResourceImporterCSVTranslation  
- ResourceImporterDynamicFont  
- ResourceImporterImage  
- ResourceImporterImageFont  
- ResourceImporterLayeredTexture  
- ResourceImporterMP3  
- ResourceImporterOBJ  
- ResourceImporterOggVorbis  
- ResourceImporterScene  
- ResourceImporterShaderFile  
- ResourceImporterSVG  
- ResourceImporterTexture  
- ResourceImporterTextureAtlas  
- ResourceImporterWAV  

Base class for resource importers.

**Description**  
This is the base class for Godot's resource importers. To implement your own resource importers using editor plugins, see [EditorImportPlugin](class_EditorImportPlugin).

**Tutorials**  
- [Import plugins](../tutorials/plugins/editor/import_plugins)

**Enumerations**  
**ImportOrder**  
- `IMPORT_ORDER_DEFAULT` = `0`  
  The default import order.

- `IMPORT_ORDER_SCENE` = `100`  
  The import order for scenes, which ensures scenes are imported after all other core resources such as textures. Custom importers should generally have an import order lower than `100` to avoid issues when importing scenes that rely on custom resources.

**Code Examples**  
```  
enum ImportOrder:  
    IMPORT_ORDER_DEFAULT = 0  
    IMPORT_ORDER_SCENE = 100  
```