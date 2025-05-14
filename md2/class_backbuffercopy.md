# BackBufferCopy

**Inherits:** Node2D < CanvasItem < Node < Object

A node that copies a region of the screen to a buffer for access in shader code.

## Description
- Copies screen content to a buffer for shader access
- The region is defined by the node's position or the entire screen based on copy mode
- The screen texture can be accessed in shaders via a uniform sampler with `hint_screen_texture`

## Note
- Inheriting from Node2D means anchors/margins don't apply to child Control nodes
- To avoid issues with window resizing, add Control-derived nodes as siblings to this node

## Tutorials
- [Screen-reading shaders](../tutorials/shaders/screen-reading_shaders)

## Properties
- **copy_mode**: CopyMode = 1
- **rect**: Rect2(-100, -100, 200, 200) (only used when copy_mode is RECT)

## Enumerations
### CopyMode
- **COPY_MODE_DISABLED** = 0: Uses screen directly
- **COPY_MODE_RECT** = 1: Buffers rectangular region
- **COPY_MODE_VIEWPORT** = 2: Buffers entire screen

## Property Descriptions
### copy_mode
- **set_copy_mode**(value: CopyMode): Sets buffer mode
- **get_copy_mode**(): Returns current buffer mode

### rect
- **set_rect**(value: Rect2): Sets the region to buffer
- **get_rect**(): Returns current region

## Key Methods
- `set_copy_mode()`: Configures buffer mode
- `get_copy_mode()`: Retrieves buffer mode
- `set_rect()`: Defines buffer region
- `get_rect()`: Gets buffer region

## Usage Notes
- The buffer is accessed as a screen texture in shaders
- The rect property is only relevant when copy_mode is set to RECT