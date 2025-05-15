# ScrollContainer Class Documentation

## Overview
The `ScrollContainer` class provides a scrollable area for content that exceeds the size of its container. It manages horizontal and vertical scrolling through internal scroll bars, and allows customization of scroll behavior and appearance.

## Properties

### Horizontal Scroll Mode
```gdscript
@property var horizontal_scroll_mode: ScrollMode = 1
```
Controls whether the horizontal scrollbar can be used and when it should be visible. See `ScrollMode` for options.

### Scroll Deadzone
```gdscript
@property var scroll_deadzone: int = 0
```
Deadzone for touch scrolling. Lower deadzone makes the scrolling more sensitive.

### Horizontal Scroll Value
```gdscript
@property var scroll_horizontal: int = 0
```
The current horizontal scroll value. **Note:** Setting this early needs to be deferred, just like in `scroll_vertical`.

### Horizontal Custom Scroll Step
```gdscript
@property var scroll_horizontal_custom_step: float = -1.0
```
Overrides the `ScrollBar.custom_step` used when clicking the internal scroll bar's horizontal increment and decrement buttons or when using arrow keys.

### Vertical Scroll Value
```gdscript
@property var scroll_vertical: int = 0
```
The current vertical scroll value. **Note:** Setting this early needs to be deferred, just like in `scroll_horizontal`.

### Vertical Custom Scroll Step
```gdscript
@property var scroll_vertical_custom_step: float = -1.0
```
Overrides the `ScrollBar.custom_step` used when clicking the internal scroll bar's vertical increment and decrement buttons or when using arrow keys.

### Vertical Scroll Mode
```gdscript
@property var vertical_scroll_mode: ScrollMode = 1
```
Controls whether the vertical scrollbar can be used and when it should be visible. See `ScrollMode` for options.

## Methods

### ensure_control_visible(control: Control)
```gdscript
func ensure_control_visible(control: Control)
```
Ensures the given `control` is visible (must be a direct or indirect child of the ScrollContainer). Used by `follow_focus`.

**Note:** This will not work on a node that was just added during the same frame. If you want to scroll to a newly added child, you must wait until the next frame using `SceneTree.process_frame`.

### get_h_scroll_bar()
```gdscript
func get_h_scroll_bar() -> HScrollBar
```
Returns the horizontal scrollbar `HScrollBar` of this `ScrollContainer`.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, use `horizontal_scroll_mode`.

### get_v_scroll_bar()
```gdscript
func get_v_scroll_bar() -> VScrollBar
```
Returns the vertical scrollbar `VScrollBar` of this `ScrollContainer`.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, use `vertical_scroll_mode`.

## Theme Properties

### Focus Border
```gdscript
@property var focus: StyleBox
```
The focus border `StyleBox` of the `ScrollContainer`. Only used if `draw_focus_border` is `true`.

### Panel Background
```gdscript
@property var panel: StyleBox
```
The background `StyleBox` of the `ScrollContainer`.