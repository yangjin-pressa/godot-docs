# ConfirmationDialog

## Inheritance Hierarchy
- Inherits: `AcceptDialog` < `Window` < `Viewport` < `Node` < `Object`

## Inherited By
- EditorCommandPalette
- EditorFileDialog
- FileDialog
- ScriptCreateDialog

## Description
A dialog used for confirmation of actions. Similar to `AcceptDialog`, but Cancel and OK button outcomes differ. Button order varies by OS.

### Code Examples
```gdscript
get_cancel_button().pressed.connect(_on_canceled)
```

```csharp
GetCancelButton().Pressed += OnCanceled;
```

## Properties
- **cancel_button_text**: `String` = "Cancel"
- **min_size**: `Vector2i` = (200, 70) (overrides `Window` min_size)
- **size**: `Vector2i` = (200, 100) (overrides `Window` size)
- **title**: `String` = "Please Confirm..." (overrides `Window` title)

## Methods
- **get_cancel_button()**: Returns the cancel button.  
  **Warning**: Internal node. Modify visibility via `CanvasItem.visible` instead of removing.

## Property Descriptions
- **cancel_button_text**: Text displayed by the cancel button.  
  - `set_cancel_button_text(value: String)`: Sets the text.  
  - `get_cancel_button_text()`: Retrieves the text.

## Method Descriptions
- **get_cancel_button()**: Returns the cancel button.  
  **Warning**: Internal node. Modify visibility via `CanvasItem.visible` instead of removing.