# Expression

**Inherits:** RefCounted < Object

A class that stores an expression you can execute.

## Description
An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

Example: `sqrt(pow(3, 2) + pow(4, 2))`

## Tutorials
- Evaluating Expressions

## Methods
- `execute(inputs: Array = [], base_instance: Object = null, show_error: bool = true, const_calls_only: bool = false): Variant`
- `get_error_text(): String | const`
- `has_execute_failed(): bool | const`
- `parse(expression: String, input_names: PackedStringArray = PackedStringArray()): Error`

## Method Descriptions
### execute
Executes the parsed expression and returns the result. Use `has_execute_failed()` to check for errors.

**Parameters:**
- inputs: Array of values for variables defined in parse()
- base_instance: Object to use as context for method calls
- show_error: bool to display errors
- const_calls_only: bool to restrict calls to const methods

### get_error_text
Returns error text if parse() or execute() failed.

### has_execute_failed
Returns true if execute() failed.

### parse
Parses the expression and returns an error code. Optionally specify input variable names.

## Example Code
**GDScript:**
```gdscript
var expression = Expression.new()
func _ready():
    $LineEdit.text_submitted.connect(self._on_text_submitted)
func _on_text_submitted(command):
    var error = expression.parse(command)
    if error != OK:
        print(expression.get_error_text())
        return
    var result = expression.execute()
    if not expression.has_execute_failed():
        $LineEdit.text = str(result)
```

**C#:**
```csharp
private Expression _expression = new Expression();
public override void _Ready()
{
    GetNode<LineEdit>("LineEdit").TextSubmitted += OnTextEntered;
}
private void OnTextEntered(string command)
{
    Error error = _expression.Parse(command);
    if (error != Error.Ok)
    {
        GD.Print(_expression.GetErrorText());
        return;
    }
    Variant result = _expression.Execute();
    if (!_expression.HasExecuteFailed())
    {
        GetNode<LineEdit>("LineEdit").Text = result.ToString();
    }
}
```