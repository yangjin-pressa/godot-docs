# SubViewportContainer

**Inherits:** Container < Control < CanvasItem < Node < Object

## Description
A container that displays contents of underlying SubViewport child nodes. Uses combined size of SubViewport's as minimum size unless stretch is enabled.

**Note:** Changing scale of SubViewportContainer distorts contents. Use margins to change visual size instead.

**Note:** SubViewportContainer forwards mouse-enter/mouse-exit to sub-viewports.

## Properties
- **focus_mode**: 1 (overrides Control's focus_mode)
- **mouse_target**: false
- **stretch**: false
- **stretch_shrink**: 1

## Methods
- **_propagate_input_event(event: InputEvent)** (virtual, const): 
  Experimental. Returns true to propagate event to SubViewport children.

## Property Descriptions

### mouse_target (bool)
Configures whether SubViewportContainer or its SubViewport Control nodes are mouse targets.

- set_mouse_target(value: bool)
- is_mouse_target_enabled()

If false: SubViewport Control nodes are targets.
If true: SubViewportContainer is target.

### stretch (bool)
If true: sub-viewport resizes to container size.

**Note:** If true, cannot manually change SubViewport.size of children.

### stretch_shrink (int)
Divides sub-viewport's resolution by this value while preserving scale.

**Note:** Requires stretch to be true for this to work.

## Method Descriptions

### _propagate_input_event(event: InputEvent)
Virtual method. Returns true to propagate event to SubViewport children. If not implemented, all events propagate to SubViewports.

**Experimental:** May change or be removed in future versions.