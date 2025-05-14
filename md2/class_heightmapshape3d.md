# HeightMapShape3D

**Inherits:** Shape3D → Resource → RefCounted → Object

A 3D height map shape used for physics collision. Typically used with CollisionShape3D for terrain simulation. Limited to flat surfaces; caves or holes are represented by assigning low values to specific points.

Performance: Faster than ConcavePolygonShape3D but slower than BoxShape3D.

---

## Description

- **Purpose**: Provides a shape for physics collision.
- **Use Case**: Ideal for terrain but lacks support for complex structures like overhangs.
- **Image Integration**: Can be generated from an Image resource.

Example usage:
```gdscript
var heightmap_texture = ResourceLoader.load("res://heightmap_image.exr")
var heightmap_image = heightmap_texture.get_image()
heightmap_image.convert(Image.FORMAT_RF)

var height_min = 0.0
var height_max = 10.0

update_map_data_from_image(heightmap_image, height_min, height_max)
```

---

## Properties

- **map_data**: PackedFloat32Array (default: 0, 0, 0, 0)  
  Height map data. Size must match map_width × map_depth.

- **map_depth**: int (default: 2)  
  Depth of the height map. Changing this resizes map_data.

- **map_width**: int (default: 2)  
  Width of the height map. Changing this resizes map_data.

---

## Methods

- **get_max_height() → float**  
  Returns the highest value in map_data. Recalculates when map_data changes.

- **get_min_height() → float**  
  Returns the lowest value in map_data. Recalculates when map_data changes.

- **update_map_data_from_image(image: Image, height_min: float, height_max: float)**  
  Updates map_data from an image. Automatically adjusts map_width and map_depth to match the image size.  
  **Supported formats**: Image.FORMAT_RF (32-bit), Image.FORMAT_RH (16-bit), Image.FORMAT_R8 (8-bit).  
  **Pixel mapping**: 0.0 (black) → height_min, 1.0 (white) → height_max.

---

## Notes

- The returned map_data array is a copy; changes to it do not affect the original property.
- Image processing requires converting to a supported format before use.