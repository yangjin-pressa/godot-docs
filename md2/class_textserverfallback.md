**Class:** TextServerFallback  
**Inherits:** TextServerExtension < TextServer < RefCounted < Object  

**Description**  
A fallback implementation of Godot's text server. Faster than TextServerAdvanced for large text processing but lacks BiDi and complex text layout support.  

**Note**  
This text server is not part of official Godot binaries. To use it, compile the engine with `module_text_server_fb_enabled=yes`. Disable TextServerAdvanced with `module_text_server_adv_enabled=no` to reduce binary size.  

**References**  
XML source: https://github.com/godotengine/godot/tree/master/modules/text_server_fb/doc_classes/TextServerFallback.xml  

**Key Concepts**  
- Fallback text server for performance-critical scenarios  
- No support for BiDi or complex text layout  
- Requires explicit compilation configuration  
- Alternative to TextServerAdvanced for binary size optimization