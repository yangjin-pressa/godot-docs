# SVGTexture

**Inherits:** Texture2D < Texture < Resource < RefCounted < Object

A scalable Texture2D based on an SVG image. SVGTexture's are automatically re-rasterized to match font oversampling.

## Description
A scalable Texture2D based on an SVG image. SVGTexture's are automatically re-rasterized to match font oversampling.

## Properties
- **base_scale**: float = 1.0  
  SVG texture scale. 1.0 is the original SVG size. Higher values result in a larger image.

- **color_map**: Dictionary = {}  
  If set, remaps SVG texture colors according to Color map.

- **saturation**: float = 1.0  
  Overrides texture saturation.

- **resource_local_to_scene**: bool = false  
  Overrides Resource::resource_local_to_scene.

## Methods
- **create_from_string(source: String, scale: float = 1.0, saturation: float = 1.0, color_map: Dictionary = {})**  
  Creates a new SVGTexture and initializes it by allocating and setting the SVG data from string.

- **get_source()**  
  Returns SVG source code.

- **set_size_override(size: Vector2i)**  
  Resizes the texture to the specified dimensions.

- **set_source(source: String)**  
  Sets SVG source code.

## Property Descriptions
- **base_scale**: float = 1.0  
  SVG texture scale. 1.0 is the original SVG size. Higher values result in a larger image.

- **color_map**: Dictionary = {}  
  If set, remaps SVG texture colors according to Color map.

- **saturation**: float = 1.0  
  Overrides texture saturation.

## Method Descriptions
- **create_from_string(source: String, scale: float = 1.0, saturation: float = 1.0, color_map: Dictionary = {})**  
  Creates a new SVGTexture and initializes it by allocating and setting the SVG data from string.

- **get_source()**  
  Returns SVG source code.

- **set_size_override(size: Vector2i)**  
  Resizes the texture to the specified dimensions.

- **set_source(source: String)**  
  Sets SVG source code.