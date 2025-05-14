### AtlasTexture

**Inherits from:** `Texture`, `Node`, `Object`

---

### Description

AtlasTexture is a type of texture that can hold multiple smaller textures (sprites) in a single larger texture. This is useful for managing multiple small textures efficiently, especially in games where many sprites are used in the same place.

**Important:** AtlasTexture cannot be used in an `AnimatedTexture`.

---

### Properties

- **atlas**: `Texture2D`  
  The texture that contains the atlas. Can be any type inheriting from `Texture2D`, including another `AtlasTexture`.

- **margin**: `Vector2`  
  The margin around each texture in the atlas. Used to ensure there is space between textures when they are placed.

- **padding**: `Vector2`  
  The padding around each texture in the atlas. This is used to define the spacing between the edges of adjacent textures.

- **split**: `bool`  
  Whether the atlas is split into multiple layers. This is useful for managing different textures in separate layers.

---

### Property Descriptions

- **atlas**:  
  The texture that contains the atlas. Can be any type inheriting from `Texture2D`, including another `AtlasTexture`.

- **margin**:  
  The margin around each texture in the atlas. Used to ensure there is space between textures when they are placed.

- **padding**:  
  The padding around each texture in the atlas. This is used to define the spacing between the edges of adjacent textures.

- **split**:  
  Whether the atlas is split into multiple layers. This is useful for managing different textures in separate layers.

---

### Methods

- **set_atlas(value)**  
  Sets the atlas texture.

- **get_atlas()**  
  Retrieves the atlas texture.

- **set_margin(value)**  
  Sets the margin around each texture in the atlas.

- **get_margin()**  
  Retrieves the margin around each texture in the atlas.

- **set_padding(value)**  
  Sets the padding around each texture in the atlas.

- **get_padding()**  
  Retrieves the padding around each texture in the atlas.

- **set_split(value)**  
  Sets whether the atlas is split into multiple layers.

- **get_split()**  
  Retrieves whether the atlas is split into multiple layers.