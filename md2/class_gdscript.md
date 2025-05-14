# GDScript

**Inherits:** Script < Resource < RefCounted < Object

A script implemented in the GDScript programming language, saved with the `.gd` extension. The script extends the functionality of all objects that instantiate it.

## Description

A script implemented in the GDScript programming language, saved with the `.gd` extension. The script extends the functionality of all objects that instantiate it.

Calling `new()` creates a new instance of the script. `Object.set_script()` extends an existing object, if that object's class matches one of the script's base classes.

## Tutorials

- [GDScript documentation index](../tutorials/scripting/gdscript/index)

## Methods

- **Variant** new(...) |vararg| 

## Method Descriptions

### new()

Returns a new instance of the script.

```gdscript
var MyClass = load("myclass.gd")
var instance = MyClass.new()
print(instance.get_script() == MyClass) # Prints true
```

## References

- [GDScript documentation index](../tutorials/scripting/gdscript/index)