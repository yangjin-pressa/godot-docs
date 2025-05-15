**Class: RDTextureFormat**  
**Inherits:** RefCounted < Object  

---

### **Description**  
Used by RenderingDevice for texture format configuration.  

---

### **Properties**  
- **array_layers**: int = 1  
  - Number of layers in a 2D texture array.  
- **depth**: int = 1  
  - Texture depth (always 1 for 2D).  
- **format**: DataFormat = 8  
  - Pixel data format (e.g., R8, RGBA8).  
- **height**: int = 1  
  - Texture height (in pixels).  
- **is_discardable**: bool = false  
  - Whether texture contents can be discarded between frames.  
- **is_resolve_buffer**: bool = false  
  - Used as destination for resolve operations.  
- **mipmaps**: int = 1  
  - Number of mipmaps in the texture.  
- **samples**: TextureSamples = 0  
  - Number of samples for multisampling.  
- **texture_type**: TextureType = 1  
  - Texture type (e.g., 2D, 3D).  
- **usage_bits**: bitfield<TextureUsageBits> = 0  
  - Bitmask defining texture usage (e.g., render target, shader resource).  
- **width**: int = 1  
  - Texture width (in pixels).  

---

### **Methods**  
- **add_shareable_format(format: DataFormat)**  
  - Adds a format to the list of valid formats for RDTextureView.  
- **remove_shareable_format(format: DataFormat)**  
  - Removes a format from the list of valid formats for RDTextureView.  

---

### **Key Notes**  
- **Usage Bits**: Bitmask for texture usage (e.g., rendering, storage).  
- **Shareable Formats**: Formats allowed for RDTextureView.format_override.  
- **Discardable Textures**: Optimized for performance by avoiding content preservation.  
- **Resolve Buffer**: Destination for texture resolution operations (e.g., MSAA).