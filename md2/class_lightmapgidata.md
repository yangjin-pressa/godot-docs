### LightmapGIData

**Description**  
A resource that holds baked lightmap data. It inherits from `LightmapGI`.

---

### Properties

| Property             | Description                                      | Default |
|----------------------|--------------------------------------------------|---------|
| LightmapGIData       | A resource that holds baked lightmap data.        | -       |
| users                | A list of baked objects in this LightmapGIData resource. | -       |
| spherical_harmonics  | Whether spherical harmonics are used.             | -       |

---

### Methods

#### `get_user_count()`
**Description:**  
Returns the number of objects that are considered baked within this `LightmapGIData`.

**Parameters:**  
None

**Return value:**  
`int`

---

#### `set_uses_spherical_harmonics(bool)`
**Description:**  
Sets whether spherical harmonics are used in this `LightmapGIData`.

**Parameters:**  
- `bool` - A boolean indicating whether to use spherical harmonics.

**Return value:**  
`void`

---

### Enumerations

**ShadowMapType**
```cpp
enum class ShadowMapType {
    None,
    Basic,
    // ... other values
};
```

---

### Property Descriptions

- **users**: A list of baked objects in this `LightmapGIData` resource.  
- **spherical_harmonics**: Whether spherical harmonics are used.  

---

### Method Descriptions

- **get_user_count**: Returns the number of objects that are considered baked within this `LightmapGIData`.  
- **set_uses_spherical_harmonics**: Sets whether spherical harmonics are used in this `LightmapGIData`.