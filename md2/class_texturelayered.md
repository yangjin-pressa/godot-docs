### TextureLayered Class

**Inheritance:**  
- `Texture`

**Inherited By:**  
- `Texture2D`  
- `TextureCube`  
- `Texture2DArray`  

---

#### Description  
The `TextureLayered` class represents a texture composed of multiple layers, each of which is an `Image`. It provides methods to access and manage individual layers, as well as properties like format, width, height, and mipmap status.

---

#### Methods

1. **`get_format()`**  
   - **Return:** `Format`  
   - Returns the current format of the texture.

2. **`get_height()`**  
   - **Return:** `int`  
   - Returns the height of the texture in pixels.

3. **`get_layer_data(layer)`**  
   - **Param:** `layer` (int)  
   - **Return:** `Image`  
   - Returns the `Image` resource from the specified layer.

4. **`get_layered_type()`**  
   - **Return:** `LayeredType`  
   - Returns the type of the texture (e.g., 2D, cubemap, 2D array).

5. **`get_layers()`**  
   - **Return:** `int`  
   - Returns the number of layers (i.e., the number of `Image` resources).

6. **`get_width()`**  
   - **Return:** `int`  
   - Returns the width of the texture in pixels.

7. **`has_mipmaps()`**  
   - **Return:** `bool`  
   - Returns `true` if the texture has generated mipmaps.

---

#### Enumerated Values

- **`LAYERED_TYPE_2D`**  
  - Represents a 2D texture.

- **`LAYERED_TYPE_CUBEMAP`**  
  - Represents a cubemap texture.

- **`LAYERED_TYPE_2D_ARRAY`**  
  - Represents a 2D array texture.

---

#### Notes  
- `get_layer_data(layer)` allows access to individual image layers.  
- The `layered_type` determines how the texture is accessed (e.g., cubemaps have specialized handling).  
- Mipmaps are generated if the texture supports them.  

--- 

**Related Classes:**  
- `Texture2D`  
- `TextureCube`  
- `Texture2DArray`  
- `Format`  
- `LayeredType`