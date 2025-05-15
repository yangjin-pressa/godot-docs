# SubViewport

**Inherits**: Viewport < Node < Object

## Overview
An interface to a game world that doesn't create a window or draw to the screen directly.

## Description
- Isolates a rectangular region of a scene for independent display
- Used for displaying UI in 3D space
- Requires non-zero size and placement in SubViewportContainer or ViewportTexture
- Input events are not passed to standalone instances by default

## Tutorials
- Using Viewports
- Viewport and canvas transforms
- [GUI in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2807)
- [3D in 2D Viewport Demo](https://godotengine.org/asset-library/asset/2804)
- [2D in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2803)
- [Screen Capture Demo](https://godotengine.org/asset-library/asset/2808)
- [Dynamic Split Screen Demo](https://godotengine.org/asset-library/asset/2806)
- [3D Resolution Scaling Demo](https://godotengine.org/asset-library/asset/2805)

## Properties
- **render_target_clear_mode**: ClearMode (0: ALWAYS, 1: NEVER, 2: ONCE)
- **render_target_update_mode**: UpdateMode (0: DISABLED, 1: ONCE, 2: WHEN_VISIBLE, 3: WHEN_PARENT_VISIBLE, 4: ALWAYS)
- **size**: Vector2i (512, 512)
- **size_2d_override**: Vector2i (0, 0)
- **size_2d_override_stretch**: false

## Enumerations
### ClearMode
- CLEAR_MODE_ALWAYS: Always clear render target
- CLEAR_MODE_NEVER: Never clear render target
- CLEAR_MODE_ONCE: Clear once then switch to NEVER

### UpdateMode
- UPDATE_DISABLED: No update
- UPDATE_ONCE: Update once
- UPDATE_WHEN_VISIBLE: Update when visible
- UPDATE_WHEN_PARENT_VISIBLE: Update when parent is visible
- UPDATE_ALWAYS: Always update

## Property Descriptions
- **render_target_clear_mode**: Sets clear mode for render target (2D use only)
- **render_target_update_mode**: Sets update mode for render target
- **size**: Sets viewport dimensions (minimum 2x2 pixels)
- **size_2d_override**: Overrides 2D size (0 disables override)
- **size_2d_override_stretch**: If true, overrides affect stretch behavior

## Notes
- Size cannot be changed if parent is SubViewportContainer with stretch enabled
- Input events require container placement for propagation
- 2D size override uses screen space coordinates