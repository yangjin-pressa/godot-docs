# AspectRatioContainer

**Inherits:** Container → Control → CanvasItem → Node → Object

A container that preserves the proportions of its child controls.

## Description
A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. Useful when a container has a dynamic size and the child nodes must adjust their sizes accordingly without losing their aspect ratios.

## Tutorials
- [Using Containers](../tutorials/ui/gui_containers)

## Properties
- **alignment_horizontal**: AlignmentMode = 1
- **alignment_vertical**: AlignmentMode = 1
- **ratio**: float = 1.0
- **stretch_mode**: StretchMode = 2

## Enumerations

### StretchMode
- **STRETCH_WIDTH_CONTROLS_HEIGHT** = 0
  - The height of child controls is automatically adjusted based on the width of the container.
- **STRETCH_HEIGHT_CONTROLS_WIDTH** = 1
  - The width of child controls is automatically adjusted based on the height of the container.
- **STRETCH_FIT** = 2
  - The bounding rectangle of child controls is automatically adjusted to fit inside the container while keeping the aspect ratio.
- **STRETCH_COVER** = 3
  - The width and height of child controls is automatically adjusted to make their bounding rectangle cover the entire area of the container while keeping the aspect ratio. [Control.clip_contents](class_Control_property_clip_contents) is enabled, this allows to show only the container's area restricted by its own bounding rectangle.

### AlignmentMode
- **ALIGNMENT_BEGIN** = 0
  - Aligns child controls with the beginning (left or top) of the container.
- **ALIGNMENT_MIDDLE** = 1
  - Aligns child controls with the middle (center) of the container.
- **ALIGNMENT_END** = 2
  - Aligns child controls with the end (right or bottom) of the container.

## Property Descriptions

### alignment_horizontal
**Type:** AlignmentMode  
**Default:** 1  
**Setters:** set_alignment_horizontal  
**Getters:** get_alignment_horizontal

### alignment_vertical
**Type:** AlignmentMode  
**Default:** 1  
**Setters:** set_alignment_vertical  
**Getters:** get_alignment_vertical

### ratio
**Type:** float  
**Default:** 1.0  
**Setters:** set_ratio  
**Getters:** get_ratio

### stretch_mode
**Type:** StretchMode  
**Default:** 2  
**Setters:** set_stretch_mode  
**Getters:** get_stretch_mode