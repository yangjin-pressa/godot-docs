# Separator

**Inherits:** Control < CanvasItem < Node < Object

**Inherited By:** HSeparator, VSeparator

## Description
Abstract base class for separators, used for separating other controls. Separators are purely visual and typically drawn as a StyleBoxLine.

## Theme Properties
- **separation**: int = 0  
  The size of the area covered by the separator. Functions as a minimum width/height.

- **separator**: StyleBox  
  The style for the separator line. Best used with StyleBoxLine (enable vertical for VSeparator).

## Key Notes
- Separators are visual elements with no functional behavior.
- The "separation" property controls the minimum size of the separator area.
- The "separator" property defines the visual style, requiring a StyleBoxLine for optimal results.