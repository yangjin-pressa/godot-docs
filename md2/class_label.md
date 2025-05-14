# Label Class Description

## Overview
The `Label` class in Godot is a versatile UI element used to display text. It supports text styling, layout, and rendering features, making it suitable for a wide range of applications, including information displays, status indicators, and dynamic text content.

---

## Properties

### Main Text Property
- **text** (String): The main text displayed by the Label. This is the core content that the Label is designed to show.

### Text Styling and Appearance
- **font_color** (Color): The default color of the text. This is a theme property, meaning it is part of the Label's visual style and can be customized globally.
- **outline_size** (int): The size of the text outline. This affects how visible the text is against backgrounds. Note that for MSDF fonts, this value must be within a specific range for optimal rendering.
- **shadow_offset_x** (int): The horizontal offset of the text's shadow.
- **shadow_offset_y** (int): The vertical offset of the text's shadow.
- **shadow_outline_size** (int): The size of the shadow outline.

### Text Layout and Spacing
- **line_spacing** (int): Additional vertical spacing between lines (in pixels). This is added to the line descent. Can be a negative value for tighter spacing.
- **paragraph_spacing** (int): Vertical space between paragraphs. This is added on top of the line spacing.
- **font_size** (int): The font size of the text. This is a theme property and defines the size of the text.
- **font** (Font): The font used for the Label's text. This is a theme property and can be customized for different styling needs.

### Text Display Control
- **visible_characters** (int): The number of visible characters in the Label. This is determined by the `visible_ratio` and `visible_characters` properties.
- **visible_ratio** (float): The fraction of characters to display, relative to the total character count. This determines how much of the text is visible at once.

---

## Methods

### Text Analysis
- **get_character_bounds(pos: int)** (Rect2): Returns the bounding rectangle of the character at position `pos` in the Label's local coordinate system. If the character is non-visual or the position is invalid, returns an empty `Rect2`.
- **get_line_count()** (int): Returns the number of lines of text the Label has. This is useful for determining the layout or layout adjustments.
- **get_line_height(line: int = -1)** (int): Returns the height of the specified line. If `line` is -1, returns the height of the tallest line. If there are no lines, returns the font size in pixels.
- **get_total_character_count()** (int): Returns the total number of printable characters in the text (excluding spaces and newlines). This is useful for text processing or length calculations.
- **get_visible_line_count()** (int): Returns the number of lines currently visible. This is useful for scrolling or dynamic content adjustments.

---

## Theme Properties

### Visual Styling
- **font_color**: Default text color. This is part of the Label's visual style and can be customized to fit the UI theme.
- **font_outline_color**: Color of the text outline. This is used when an outline is applied to the text.
- **font_shadow_color**: Color of the text's shadow effect. This is used when a shadow is applied to the text.
- **line_spacing**: Additional vertical spacing between lines (in pixels). This is part of the Label's layout settings and affects spacing between lines.
- **outline_size**: Text outline size. This is part of the Label's visual styling and affects the visibility of the text against backgrounds.
- **paragraph_spacing**: Vertical space between paragraphs. This is part of the Label's layout settings and affects spacing between paragraphs.

### Font and Font Size
- **font**: The font used for the Label's text. This is part of the Label's visual styling and can be customized for different styling needs.
- **font_size**: The font size of the Label's text. This is part of the Label's visual style and defines the size of the text.

### UI Interaction
- **focus**: The `StyleBox` used when the Label is focused (for assistive technologies). This is part of the Label's UI interaction styling and affects the appearance when focused.
- **normal**: The `StyleBox` used as the background for the Label. This is part of the Label's UI style and affects the background appearance.

---

## Notes and Considerations
- **Outline and Shadow Rendering**: The `outline_size` and `shadow_offset` properties affect how the text is rendered. For MSDF fonts, the `outline_size` must be within a specific range for the text to render correctly. Using a value larger than half the font size is not recommended as it may cause rendering issues.
- **Line and Paragraph Spacing**: The `line_spacing` and `paragraph_spacing` properties control the vertical spacing between lines and paragraphs, respectively. This is useful for adjusting text layout in the UI.
- **Visibility Control**: The `visible_ratio` and `visible_characters` properties control how much of the text is visible at once. This is useful for scrolling or dynamic content display.

---

## Use Cases
- **Simple Text Display**: The Label is ideal for displaying static text in a UI, such as status messages or labels.
- **Dynamic Text**: The Label can be used to display text that changes over time, such as countdown timers or progress indicators.
- **Styling and Layout**: The various spacing and text properties allow for a wide range of styling and layout options, making it suitable for complex UI designs.
- **Accessibility**: The `focus` property allows for customization of the appearance when the Label is focused, aiding accessibility for assistive technologies.

The Label class provides a flexible and powerful way to display and manage text in Godot, with a wide range of properties and methods to control text styling, layout, and rendering.