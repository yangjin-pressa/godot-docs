# SpinBox Class Documentation

## Properties
### `custom`
- **Type**: `float`
- **Description**: Custom value. This property is a wrapper for the `value` property.
- **Default**: `0.0`
- **Note**: This property is a wrapper for the `value` property.

### `value`
- **Type**: `float`
- **Description**: The current value of the spin box.
- **Default**: `0.0`

### `min`
- **Type**: `float`
- **Description**: Minimum value allowed.
- **Default**: `0.0`

### `max`
- **Type**: `float`
- **Description**: Maximum value allowed.
- **Default**: `0.0`

### `step`
- **Type**: `float`
- **Description**: Step size for incrementing or decrementing the value.
- **Default**: `1.0`

### `is_read_only`
- **Type**: `bool`
- **Description**: Whether the value can be changed.
- **Default**: `false`

### `is_independent`
- **Type**: `bool`
- **Description**: Whether the value is independent of other controls.
- **Default**: `false`

### `is_discrete`
- **Type**: `bool`
- **Description**: Whether the value is discrete (only whole numbers).
- **Default**: `false`

## Methods
### `apply()`
- **Type**: `virtual`
- **Description**: Called when the value is changed. This method should typically be overridden by the user to have any effect.
- **Note**: This method is virtual and is called when the value is changed.

## Theme Properties

### Icons
- **`down`**  
  - **Type**: `Texture2D`  
  - **Description**: Down button icon, displayed in the middle of the down (value-decreasing) button.

- **`down_disabled`**  
  - **Type**: `Texture2D`  
  - **Description**: Down button icon when the button is disabled.

- **`down_hover`**  
  - **Type**: `Texture2D`  
  - **Description**: Down button icon when the button is hovered.

- **`down_pressed`**  
  - **Type**: `Texture2D`  
  - **Description**: Down button icon when the button is being pressed.

- **`up`**  
  - **Type**: `Texture2D`  
  - **Description**: Up button icon, displayed in the middle of the up (value-increasing) button.

- **`up_disabled`**  
  - **Type**: `Texture2D`  
  - **Description**: Up button icon when the button is disabled.

- **`up_hover`**  
  - **Type**: `Texture2D`  
  - **Description**: Up button icon when the button is hovered.

- **`up_pressed`**  
  - **Type**: `Texture2D`  
  - **Description**: Up button icon when the button is being pressed.

- **`updown`**  
  - **Type**: `Texture2D`  
  - **Description**: Single texture representing both the up and down buttons. It is displayed in the middle of the buttons and does not change upon interaction. It is recommended to use individual icons for better usability.

### Background Styles
- **`down_background`**  
  - **Type**: `StyleBox`  
  - **Description**: Background style of the down button.

- **`down_background_disabled`**  
  - **Type**: `StyleBox`  
  - **Description**: Background style of the down button when disabled.

- **`down_background_hovered`**  
  - **Type**: `StyleBox`  
  - **Description**: Background style of the down button when hovered.

- **`down_background_pressed`**  
  - **Type**: `StyleityBox`  
  - **Description**: Background style of the down button when being pressed.

- **`up_background`**  
  - **Type**: `StyleBox`  
  - **Description**: Background style of the up button.

- **`up_background_disabled`**  
  - **Type**: `StyleBox`  
  - **Description**: Background style of the up button when disabled.

- **`up_background_hovered`**  
  - **Type**: `StyleBox`  
  - **Description**: Background style of the up button when hovered.

- **`up_background_pressed`**  
  - **Type**: `StyleBox`  
  - **Description**: Background style of the up button when being pressed.

### Separators
- **`field_and_buttons_separator`**  
  - **Type**: `StyleBox`  
  - **Description**: Style box drawn in the space occupied by the separation between the input field and the buttons.

- **`up_down_buttons_separator`**  
  - **Type**: `StyleBox`  
  - **Description**: Style box drawn in the space occupied by the separation between the up and down buttons.

### Constants
- **`buttons_width`**  
  - **Type**: `int`  
  - **Description**: Width of the up and down buttons. If smaller than any icon set on the buttons, the respective icon may overlap neighboring elements. If smaller than `0`, the width is automatically adjusted from the icon size.
  - **Default**: `16`

- **`field_and_buttons_separation`**  
  - **Type**: `int`  
  - **Description**: Width of the horizontal separation between the text input field and the buttons.
  - **Default**: `2`

- **`set_min_buttons_width_from_icons`**  
  - **Type**: `int`  
  - **Description**: If not `0`, the minimum button width corresponds to the widest of all icons set on those buttons, even if `buttons_width` is smaller.
  - **Default**: `1`

- **`buttons_width`**  
  - **Type**: `int`  
  - **Description**: Width of the up and down buttons. If smaller than any icon set on the buttons, the respective icon may overlap neighboring elements. If smaller than `0`, the width is automatically adjusted from the icon size.
  - **Default**: `16`

- **`buttons_width`**  
  - **Type**: `int`  
  - **Description**: Width of the up and down buttons. If smaller than any icon set on the buttons, the respective icon may overlap neighboring elements. If smaller than `0`, the width is automatically adjusted from the icon size.
  - **Default**: `16`

- **`buttons_width`**  
  - **Type**: `int`  
  - **Description**: Width of the up and down buttons. If smaller than any icon set on the buttons, the respective icon may overlap neighboring elements. If smaller than `0`, the width is automatically adjusted from the icon size.
  - **Default**: `16`