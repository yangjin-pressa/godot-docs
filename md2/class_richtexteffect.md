# RichTextEffect

**Inherits:** Resource < RefCounted < Object

A custom effect for a RichTextLabel.

## Description
A custom effect for a RichTextLabel, which can be loaded in the RichTextLabel inspector or using RichTextLabel.install_effect().

**Note:** For a RichTextEffect to be usable, a BBCode tag must be defined as a member variable called `bbcode` in the script.

**Example:**
```gdscript
# The RichTextEffect will be usable like this: [example]Some text[/example]
var bbcode = "example"
```

```csharp
// The RichTextEffect will be usable like this: [example]Some text[/example]
string bbcode = "example";
```

**Note:** As soon as a RichTextLabel contains at least one RichTextEffect, it will continuously process the effect unless the project is paused. This may impact battery life negatively.

## Tutorials
- [BBCode in RichTextLabel](../tutorials/ui/bbcode_in_richtextlabel)
- [RichTextEffect test project (third-party)](https://github.com/Eoin-ONeill-Yokai/Godot-Rich-Text-Effect-Test-Project)

## Methods
- `_process_custom_fx(char_fx: CharFXTransform)`: Virtual method to modify properties in `char_fx`. Returns `true` if the character could be transformed successfully. Returns `false` to skip transformation.

## Method Descriptions
**_process_custom_fx(char_fx: CharFXTransform)**  
Override this method to modify properties in `char_fx`. The method must return `true` if the character could be transformed successfully. If the method returns `false`, it will skip transformation to avoid displaying broken text.

## Notes
- The `bbcode` variable must define a BBCode tag for the effect to be usable.
- Continuous processing of RichTextEffect may affect battery life.