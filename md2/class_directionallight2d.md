# DirectionalLight2D

## Inheritance
- **DirectionalLight2D** < [Light2D](class_Light2D) < [Node2D](class_Node2D) < [CanvasItem](class_CanvasItem) < [Node](class_Node) < [Object](class_Object)

## Description
A directional light simulates infinite parallel rays for 2D scenes, ideal for modeling strong-intensity lights like sunlight or moonlight. 
- **Note:** Does not support light cull masks but supports shadow cull masks. Always lights 2D nodes regardless of their `CanvasItem.light_mask` settings.

## Tutorials
- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows)

## Properties
- **height**: `float` = 0.0  
  - Controls light direction for 2D normal mapping. Ranges from 0 (parallel to plane) to 1 (perpendicular to plane).  
  - Method: `set_height(value: float)`, `get_height()`

- **max_distance**: `float` = 10000.0  
  - Maximum distance for shadow culling. Lower values prevent distant shadows and improve performance.  
  - Method: `set_max_distance(value: float)`, `get_max_distance()`  
  - Note: `Camera2D.zoom` does not affect this value. Shadows fade sooner at higher zoom levels.

## Key Features
- Always illuminates 2D nodes
- Height affects normal mapping orientation
- Max distance controls shadow culling behavior
- Light cull masks are not supported