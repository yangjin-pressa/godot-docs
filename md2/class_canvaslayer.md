# CanvasLayer

## Overview
A node used for independent rendering of objects within a 2D scene. Inherits from Node.

## Key Functionality
- **Layer Indexing**: Nodes in CanvasLayer are drawn based on layer index. Lower values draw behind higher values.
- **Viewport Integration**: Can be tied to a specific Viewport. Cannot share between multiple Viewports.
- **Visibility Control**: Can be hidden or shown. Visibility affects drawing order but not underlying layers.
- **Transform Support**: Supports scaling, rotation, and custom transforms for layout.

## Tutorials
- [Basic Canvas Usage](https://godotengine.org/documentation/usage/2d/using_a_canvas.html)
- [CanvasLayer Best Practices](https://godotengine.org/documentation/usage/2d/canvaslayer.html)

## Properties
- **custom_viewport**: Node reference to the associated Viewport
- **follow_viewport_enabled**: boolean (default: false) - Enables Viewport synchronization
- **follow_viewport_scale**: float (default: 1.0) - Scale factor for Viewport
- **layer**: int (default: 1) - Drawing order priority
- **offset**: Vector2 (default: (0,0)) - Base position offset
- **rotation**: float (default: 0.0) - Radial rotation angle
- **scale**: Vector2 (default: (1,1)) - Scaling factor
- **transform**: Transform2D (default: identity) - Custom transformation matrix
- **visible**: boolean (default: true) - Visibility state

## Methods
- **get_canvas()**: Returns RID of the canvas associated with this layer
- **get_final_transform()**: Returns transformation matrix to viewport coordinates
- **hide()**: Hides all CanvasItems under this layer (equivalent to setting visible=false)
- **show()**: Shows all CanvasItems under this layer (equivalent to setting visible=true)

## Signals
- **visibility_changed():** Emitted when visibility state changes

## Important Notes
1. Multiple layers with same index: Children of one layer will draw behind those of another
2. Embedded windows: Viewport changes affect layers but not their internal coordinates
3. Transform priority: Custom transforms override offset/rotation/scale settings
4. Layer order: The lowest index layer is drawn first, highest last

## Usage Examples
```gdscript
# Create a new CanvasLayer
var layer = CanvasLayer.new()

# Set properties
layer.layer = 2
layer.scale = Vector2(2, 2)
layer.rotation = 45.0
layer.visible = false

# Get transformation
var transform = layer.get_final_transform()
```