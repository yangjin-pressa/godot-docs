# VisibleOnScreenNotifier2D

## Class Hierarchy
- **VisibleOnScreenNotifier2D**  
  Inherits from: Node2D → CanvasItem → Node → Object  
  Inherited by: VisibleOnScreenEnabler2D

## Description
A 2D rectangular area that detects visibility on screen. Emits signals when this region enters or exits the screen.  
**Note:** Requires `CanvasItem.visible` to be set to `true` for functionality.

## Tutorials
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

## Properties
- **rect**: `Rect2` (default: `Rect2(-10, -10, 20, 20)`)  
  Bounding rectangle for visibility detection.  
- **show_rect**: `bool` (default: `true`)  
  If `true`, displays the rectangle in the editor for visual debugging.  
  (Does not affect screen culling detection.)

## Methods
- **is_on_screen()** → `bool`  
  Returns `true` if the bounding rectangle is currently on screen.  
  **Note:** Returns `false` initially, as visibility is determined after the first frame.

## Signals
- **screen_entered()**  
  Emitted when the region enters the screen.  
- **screen_exited()**  
  Emitted when the region exits the screen.

## Property Descriptions
- **rect**  
  - `set_rect(value: Rect2)`: Sets the bounding rectangle.  
  - `get_rect()`: Retrieves the current rectangle.  
- **show_rect**  
  - `set_show_rect(value: bool)`: Toggles the visibility of the rectangle in the editor.  
  - `is_showing_rect()`: Returns the current `show_rect` value.

## Key Notes
- The `is_on_screen()` method relies on render culling and may return `false` immediately after instantiation.  
- `show_rect` affects editor visualization, not actual screen culling logic.