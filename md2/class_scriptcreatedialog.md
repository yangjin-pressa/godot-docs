# ScriptCreateDialog

## Description
The ScriptCreateDialog creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the Window.popup() methods.

**Example Usage:**

**GDScript:**
```gdscript
func _ready():
    var dialog = ScriptCreateDialog.new()
    dialog.config("Node", "res://new_node.gd") # For in-engine types.
    dialog.config("\"res://base_node.gd\"", "res://derived_node.gd") # For script types.
    dialog.popup_centered()
```

**C#:**
```csharp
public override void _Ready()
{
    var dialog = new ScriptCreateDialog();
    dialog.Config("Node", "res://NewNode.cs"); // For in-engine types.
    dialog.Config("\"res://BaseNode.cs\"", "res://DerivedNode.cs"); // For script types.
    dialog.PopupCentered();
}
```

## Properties
- **dialog_hide_on_ok**: bool, false (overrides AcceptDialog property)
- **ok_button_text**: String, "Create" (overrides AcceptDialog property)
- **title**: String, "Attach Node Script" (overrides Window property)

## Methods
- **config** (inherits: String, path: String, built_in_enabled: bool = true, load_enabled: bool = true)  
  Prefills required fields to configure the ScriptCreateDialog for use.

## Signals
- **script_created** (script: Script)  
  Emitted when the user clicks the OK button.

## Key Details
- Inherits from: ConfirmationDialog → AcceptDialog → Window → Viewport → Node → Object
- Used for creating new Script files with specified templates
- Supports configuration for both in-engine types and script types
- Emits signal when OK button is clicked