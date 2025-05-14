### ImageTexture3D

**Description**  
A 3D texture that inherits from `Texture3D`. It is used to represent images in three dimensions, supporting operations such as rendering, filtering, and manipulation in 3D space. This class provides methods for creating and managing 3D textures, with specific attributes and parameters for control over texture behavior.

---

### **Inherits From**  
- `Texture3D`  
  - A base class for textures that supports 3D spatial data.  

**See Also**:  
- `ImageTextureLayered`  
  - A related class for layered textures.  

---

### **Methods**  

#### **create**  
**Return**: `Error`  
**Description**: Creates a new `ImageTexture3D` instance. This method is *virtual* (should typically be overridden by the user to have any effect).  

**Parameters**:  
- `format` (Format): The format of the texture data (e.g., RGB, RGBA).  
- `width` (int): The width of the texture.  
- `height` (int): The height of the texture.  
- `depth` (int): The depth of the texture.  
- `use_mipmaps` (bool): Whether to use mipmaps for texture filtering.  
- `data` (Array[Image]): The initial data for the texture.  

**Note**: This method is marked as `virtual`, indicating it may be overridden in derived classes for custom behavior.  

---

#### **update**  
**Return**: `Error`  
**Description**: Updates the texture data. This method is *const* (has no side effects, does not modify the instance).  

**Parameters**:  
- `data` (Array[Image]): The new data to set for the texture.  

**Note**: This method is marked as `const`, ensuring it does not alter the state of the object.  

---

### **Other References**  
- `Format`: An enum defining texture data formats.  
- `int`: A data type for integer values.  
- `bool`: A data type for boolean values.  
- `Array[Image]`: A collection of image objects.  

---

### **Usage Example**  
```plaintext
texture = ImageTexture3D.create(
    format=Format.RGBA,
    width=512,
    height=512,
    depth=1,
    use_mipmaps=true,
    data=[...]
)
```  

This example creates a 3D texture with RGBA format, dimensions 512x512, and uses mipmaps. The `data` parameter is an array of image objects containing the initial texture content.  

--- 

**Summary**:  
The `ImageTexture3D` class provides a flexible and powerful way to manage 3D textures in applications that require spatial data representation. It supports creation, updating, and customization of textures through a variety of parameters, with clear documentation for each method.