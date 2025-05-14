# EditorCommandPalette

**Inherits:** ConfirmationDialog < AcceptDialog < Window < Viewport < Node < Object

Godot editor's command palette.

## Description
Object that holds all the available Commands and their shortcuts text. These Commands can be accessed through **Editor > Command Palette** menu.

Command key names use slash delimiters to distinguish sections, for example: ``"example/command1"`` then ``example`` will be the section name.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_command_palette](class_EditorInterface_method_get_command_palette).

## Properties
- **dialog_hide_on_ok**: bool (false) - overrides AcceptDialog property

## Methods
- **add_command**(command_name: String, key_name: String, binded_callable: Callable, shortcut_text: String = "None")  
  Adds a custom command to EditorCommandPalette.

- **remove_command**(key_name: String)  
  Removes the custom command from EditorCommandPalette.

## Method Descriptions

### add_command
- **command_name**: String (Name of the Command. This is displayed to the user.)
- **key_name**: String (Name of the key for a particular Command. This is used to uniquely identify the Command.)
- **binded_callable**: Callable (Callable of the Command. This will be executed when the Command is selected.)
- **shortcut_text**: String (Shortcut text of the Command if available.)

### remove_command
- **key_name**: String (Name of the key for a particular Command.)

## Code Examples

**GDScript**:
```gdscript
var command_palette = EditorInterface.get_command_palette()
var command_callable = Callable(self, "external_command").bind(arguments)
command_palette.add_command("command", "test/command", command_callable)
```

**CSharp**:
```csharp
EditorCommandPalette commandPalette = EditorInterface.Singleton.GetCommandPalette();
Callable commandCallable = new Callable(this, MethodName.ExternalCommand);
commandPalette.AddCommand("command", "test/command", commandCallable);
```