# ScrollBar

## Inheritance
- **Inherits**: Range < Control < CanvasItem < Node < Object
- **Inherited By**: HScrollBar, VScrollBar

## Description
Abstract base class for scrollbars, typically used to navigate through content that extends beyond the visible area of a control. Scrollbars are Range-based controls.

## Properties
- **custom_step**: float = -1.0  
  Overrides the step used when clicking increment/decrement buttons or using arrow keys when the ScrollBar is focused.
- **focus_mode**: FocusMode = 3  
  Overrides the focus mode of the parent Control.
- **step**: float = 0.0  
  Overrides the step of the parent Range.

## Theme Properties
- **decrement**: Texture2D  
  Icon for scrolling left/up. Supports custom_step.
- **decrement_highlight**: Texture2D  
  Displayed when mouse hovers over decrement button.
- **decrement_pressed**: Texture2D  
  Displayed when decrement button is pressed.
- **increment**: Texture2D  
  Icon for scrolling right/down. Supports custom_step.
- **increment_highlight**: Texture2D  
  Displayed when mouse hovers over increment button.
- **increment_pressed**: Texture2D  
  Displayed when increment button is pressed.
- **grabber**: StyleBox  
  Texture for the draggable scroll grabber.
- **grabber_highlight**: StyleBox  
  Used when mouse hovers over grabber.
- **grabber_pressed**: StyleBox  
  Used when grabber is dragged.
- **scroll**: StyleBox  
  Background of the ScrollBar.
- **scroll_focus**: StyleBox  
  Background when ScrollBar has GUI focus.

## Signals
- **scrolling**: Emits when the ScrollBar is being scrolled.

## Property Descriptions
- **custom_step**:  
  - `set_custom_step(value: float)`: Overrides step for buttons/arrow keys.  
  - `get_custom_step()`: Returns current custom step value.