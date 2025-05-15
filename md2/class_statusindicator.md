# StatusIndicator

**Inherits:** Node < Object  
**Note:** Status indicator is implemented on macOS and Windows.

## Properties

- **icon**: Texture2D (default: empty)  
  - Set/Get: `set_icon(Texture2D)`, `get_icon()`  
  - Description: Status indicator icon.

- **menu**: NodePath (default: "")  
  - Set/Get: `set_menu(NodePath)`, `get_menu()`  
  - Description: Native popup menu. If set, the "pressed" signal is not emitted.  
  - Note: Native popup requires NativeMenu to support FEATURE_POPUP_MENU.

- **tooltip**: String (default: "")  
  - Set/Get: `set_tooltip(String)`, `get_tooltip()`  
  - Description: Status indicator tooltip.

- **visible**: bool (default: true)  
  - Set/Get: `set_visible(bool)`, `is_visible()`  
  - Description: If true, the status indicator is visible.

## Methods

- **get_rect()** → Rect2 (const)  
  - Description: Returns the status indicator rectangle in screen coordinates. Returns empty Rect2 if not visible.

## Signals

- **pressed(mouse_button: int, mouse_position: Vector2i)**  
  - Description: Emitted when the status indicator is pressed.

## Key Details

- **Platform Support**: macOS, Windows  
- ** native popup menu**: Only supported if NativeMenu has FEATURE_POPUP_MENU.  
- **visibility**: Controlled by `visible` property.  
- **tooltip**: Can be set via `set_tooltip()`.