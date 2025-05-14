# Path3D  

**Inherits:** Node3D → Node → Object  

## Description  
- Allows `PathFollow3D` child nodes to follow a `Curve3D`.  
- Path is relative to the moved nodes (children of `PathFollow3D`).  
- Curve should typically start with a zero vector `(0, 0, 0)`.  

## Properties  
- **curve**: `Curve3D` (default: none)  
- **debug_custom_color**: `Color` (default: `Color(0, 0, 0, 1)`)  

## Signals  
- **curve_changed**: Emitted when `curve` changes.  
- **debug_color_changed**: Emitted when `debug_custom_color` changes.  

## Property Descriptions  
### curve  
- **set_curve(value: Curve3D)**: Sets the path curve.  
- **get_curve()**: Returns the current curve.  
- **Description**: Defines the path for `PathFollow3D` nodes.  

### debug_custom_color  
- **set_debug_custom_color(value: Color)**: Sets the editor-drawing color.  
- **get_debug_custom_color()**: Returns the current color.  
- **Description**: Custom color for visualizing the path in the editor.  
- **Note**: Default color (`Color(0.0, 0.0, 0.0)`) uses EditorSettings color.  

## Method Definitions  
- **set_curve(value: Curve3D)**: Overrides the default behavior for curve assignment.  
- **get_curve()**: Returns the current curve without side effects.  
- **set_debug_custom_color(value: Color)**: Overrides the default behavior for color settings.  
- **get_debug_custom_color()**: Returns the current color without side effects.