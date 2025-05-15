# Popup

**Inherits:** Window < Viewport < Node < Object  
**Inherited By:** PopupMenu, PopupPanel  

## Description
Base class for contextual windows and panels with fixed position. It's a modal by default and provides methods for custom popup behavior.

## Properties
- **borderless**: true (overrides Window.borderless)  
- **maximize_disabled**: true (overrides Window.maximize_disabled)  
- **minimize_disabled**: true (overrides Window.minimize_disabled)  
- **popup_window**: true (overrides Window.popup_window)  
- **popup_wm_hint**: true (overrides Window.popup_wm_hint)  
- **transient**: true (overrides Window.transient)  
- **unresizable**: true (overrides Window.unresizable)  
- **visible**: false (overrides Window.visible)  
- **wrap_controls**: true (overrides Window.wrap_controls)  

## Signals
- **popup_hide** (): Emitted when the popup is hidden.  

## Key Features
- Modal by default  
- Overrides Window properties for popup behavior  
- Supports custom popup implementations