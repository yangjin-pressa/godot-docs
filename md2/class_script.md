### Script Class Documentation

#### Description
The `Script` class represents a script in a game engine or development environment. It provides methods to manage the source code of a script, check its validity, and interact with the environment. Key features include methods to determine if a script contains source code, check its status, and reload it.

#### Tutorials
[View tutorials](#) for more information on using the Script class.

---

### Properties
- **source_code**: String  
  The source code of the script.

---

### Methods

#### `has_source_code() -> bool`
Returns `true` if the script contains non-empty source code.  
**Note**: If a script has no source code, it is not necessarily invalid. For example, a `GDScript` exported with binary tokenization may have no source code but still function correctly. This can be checked with `can_instantiate()`.

```gdscript
// GDScript example
func example() -> void:
    pass

// C# example
public void Example()
{
    // code
}
```

#### `instance_has() -> bool`
Checks if the script instance is valid.

#### `is_abstract() -> bool`
Determines if the script is abstract (i.e., not a concrete implementation).

#### `is_tool() -> bool`
Checks if the script is a tool (e.g., for development purposes).

#### `reload() -> Error`
Reloading the script may be necessary if changes are made to the source code. Returns an error if reloading fails.

---

### Notes
- `source_code` can be empty but does not imply the script is invalid.
- `can_instantiate()` can be used to verify if a script is usable even if it lacks source code.