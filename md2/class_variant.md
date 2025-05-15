# Variant

## Description

A Variant is a flexible data type in Godot that can store various types. Dynamic languages like GDScript and C# use it to handle variable data. Godot's API uses Variants to track scripting variables, and they are used for communication, serialization, and data movement.

### Key Features
- Stores almost any engine datatype.
- Supports operations between many variants.
- Can be hashed for quick comparisons.
- Enables safe type conversion.
- Abstracts method calls and arguments.
- Supports deferred calls and thread transfers.
- Serializable for disk or network use.
- Supports editable settings and dictionaries.
- Works as exported properties for the editor.

### Examples
**GDScript:**
```gdscript
var foo = 2
match typeof(foo):
    TYPE_NIL:
        print("foo is null")
    TYPE_INT:
        print("foo is an integer")
    TYPE_OBJECT:
        print("foo is a(n) %s" % foo.get_class())
```

**C#:**
```csharp
Variant foo = 2;
switch (foo.VariantType)
{
    case Variant.Type.Nil:
        GD.Print("foo is null");
        break;
    case Variant.Type.Int:
        GD.Print("foo is an integer");
        break;
    case Variant.Type.Object:
        GD.Print($"foo is a(n) {foo.AsGodotObject().GetType().Name}");
        break;
}
```

## Global Function
The global `@GlobalScope.typeof()` function returns the enumerated type of a Variant (see `Variant.Type`).

## Containers
- **Dictionary**: Maps any datatype to any other.
- **Array**: Stores an array of Variants.
- **Nested Structures**: Variants can contain dictionaries/arrays, enhancing flexibility.

## Multi-threading
Modifying containers affects all references. Use `Mutex` for thread-safe access.

## C# Differences
C# uses its own `Variant` type for dynamic values, with implicit casting but explicit conversions required.

## Tutorials
- [Variant class introduction](../contributing/development/core_and_modules/variant_class)