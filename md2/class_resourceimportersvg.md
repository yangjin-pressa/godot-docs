# ResourceImporterSVG

**Inherits:** ResourceImporter → RefCounted → Object

Imports a SVG file as a scalable texture for use in 2D or 3D rendering.

## Description
This importer imports SVGTexture resources. See also ResourceImporterTexture and ResourceImporterImage.

## Properties
- **base_scale**: float = 1.0  
  SVG texture scale. 1.0 is the original SVG size. Higher values result in a larger image.
- **color_map**: Dictionary = {}  
  If set, remaps SVG texture colors according to Color-map.
- **compress**: bool = true  
  If true, uses lossless compression for the SVG source.
- **saturation**: float = 1.0  
  Overrides texture saturation.

## Property Descriptions
- **base_scale**  
  SVG texture scale. 1.0 is the original SVG size. Higher values result in a larger image.
- **color_map**  
  If set, remaps SVG texture colors according to Color-map.
- **compress**  
  If true, uses lossless compression for the SVG source.
- **saturation**  
  Overrides texture saturation.