**Class:** PlaceholderCubemap  
**Inherits:**  
- PlaceholderTextureLayered  
  - TextureLayered  
    - Texture  
      - Resource  
        - RefCounted  
          - Object  

**Description**  
A Cubemap without image data. Used in two scenarios:  
- Dedicated server mode (image data does not affect game logic)  
- When a Cubemap-derived class is missing (e.g., due to engine version differences)  

**Note**  
This class is not for rendering or shader use. UV calculations and other operations may not work reliably.  

**Citations**  
- :ref:`Cubemap<class_Cubemap>`  
- :ref:`TextureLayered<class_TextureLayered>`  
- :ref:`Resource<class_Resource>`  
- :ref:`RefCounted<class_RefCounted>`  
- :ref:`Object<class_Object>`  

**Key Use Cases**  
- Reduce PCK file size in dedicated servers  
- Replace missing Cubemap-derived classes across engine versions