# ColorPickerButton

**Inherits:** Button → BaseButton → Control → CanvasItem → Node → Object

A button that brings up a ColorPicker when pressed.

## Description
Encapsulates a ColorPicker, making it accessible by pressing a button. Pressing the button will toggle the ColorPicker's visibility.

**Note:** By default, the button may not be wide enough for the color preview swatch to be visible. Set `custom_minimum_size` to a big enough value to give the button enough space.

## Tutorials
- [2D GD Paint Demo](https://godotengine.org/asset-library/asset/2768)
- [GUI Drag And Drop Demo](https://godotengine.org/asset-library/asset/2767)

## Properties
- **color**: Color(0, 0, 0, 1)
- **edit_alpha**: true
- **toggle_mode**: true (overrides BaseButton's toggle_mode)

## Methods
- **get_picker()**: Returns the ColorPicker that this node toggles.
- **get_popup()**: Returns the PopupPanel which allows connecting to popup signals.

## Theme Properties
- **bg**: Background of the color preview rect on the button.

## Signals
- **color_changed(color: Color)**: Emitted when the color changes.
- **picker_created()**: Emitted when the ColorPicker is created.
- **popup_closed()**: Emitted when the ColorPicker is closed.

## Property Descriptions
- **color**: The currently selected color.
- **edit_alpha**: If true, the alpha channel in the ColorPicker is visible.

## Method Descriptions
- **get_picker()**: Returns the ColorPicker that this node toggles.
- **get_popup()**: Returns the PopupPanel which allows connecting to popup signals.

## Theme Property Descriptions
- **bg**: The background of the color preview rect on the button.