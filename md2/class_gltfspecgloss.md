# GLTFSpecGloss

**Inherits:** Resource < RefCounted < Object  
**Archived glTF extension for specular/glossy materials**

## Description
KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.

## Tutorials
- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving)
- [KHR_materials_pbrSpecularGlossiness glTF extension spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Archived/KHR_materials_pbrSpecularGlossiness)

## Properties
- **diffuse_factor**: Color = Color(1, 1, 1, 1)  
  Reflects diffuse factor of the material.
- **diffuse_img**: Image  
  Diffuse texture.
- **gloss_factor**: float = 1.0  
  Glossiness or smoothness of the material.
- **spec_gloss_img**: Image  
  Specular-glossiness texture.
- **specular_factor**: Color = Color(1, 1, 1, 1)  
  Specular RGB color of the material. Alpha channel is unused.

## Property Methods
### diffuse_factor
- **set_diffuse_factor(value: Color)**  
  Sets the diffuse factor.
- **get_diffuse_factor()**  
  Gets the diffuse factor.

### diffuse_img
- **set_diffuse_img(value: Image)**  
  Sets the diffuse texture.
- **get_diffuse_img()**  
  Gets the diffuse texture.

### gloss_factor
- **set_gloss_factor(value: float)**  
  Sets the glossiness.
- **get_gloss_factor()**  
  Gets the glossiness.

### spec_gloss_img
- **set_spec_gloss_img(value: Image)**  
  Sets the specular-glossiness texture.
- **get_spec_gloss_img()**  
  Gets the specular-glossiness texture.

### specular_factor
- **set_specular_factor(value: Color)**  
  Sets the specular color.
- **get_specular_factor()**  
  Gets the specular color.